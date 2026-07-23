#!/usr/bin/env bash
# Houdt de Nexa Oil Trading website continu online (lokale server + Cloudflare tunnel).
# De bewaker herstart automatisch wat uitvalt. De actuele link staat altijd in LIVE_URL.txt.
# Starten:  nohup ./keepalive.sh >/tmp/dpt_keepalive.log 2>&1 &
# Stoppen:  ./keepalive.sh stop
DIR="$(cd "$(dirname "$0")" && pwd)"
PORT=8787
URLFILE="$DIR/LIVE_URL.txt"
LOG=/tmp/dpt_cf.log

if [ "$1" = "stop" ]; then
  pkill -f "keepalive.sh" 2>/dev/null
  pkill -f "cloudflared" 2>/dev/null && echo "Tunnel gestopt."
  pkill -f "http.server $PORT" 2>/dev/null && echo "Server gestopt."
  exit 0
fi

start_server(){
  pgrep -f "http.server $PORT" >/dev/null || \
    ( cd "$DIR" && nohup python3 -m http.server $PORT >/tmp/dpt_pub_server.log 2>&1 & )
}

start_tunnel(){
  rm -f "$LOG"
  nohup cloudflared tunnel --protocol http2 --url "http://localhost:$PORT" >"$LOG" 2>&1 &
  for i in $(seq 1 30); do
    U=$(grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' "$LOG" 2>/dev/null | head -1)
    [ -n "$U" ] && { echo "$U" > "$URLFILE"; break; }
    sleep 2
  done
}

start_server
# behoud bestaande tunnel-URL als er al een tunnel draait
if pgrep -f "cloudflared tunnel" >/dev/null; then
  U=$(grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' "$LOG" 2>/dev/null | head -1)
  [ -n "$U" ] && echo "$U" > "$URLFILE"
else
  start_tunnel
fi

# bewaker: herstart alleen bij procesverlies (transiente netwerk-blips lost cloudflared zelf op)
while true; do
  start_server
  pgrep -f "cloudflared tunnel" >/dev/null || start_tunnel
  sleep 30
done
