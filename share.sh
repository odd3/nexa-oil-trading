#!/usr/bin/env bash
# Deelt de Nexa Oil Trading website via een tijdelijke publieke link (Cloudflare).
# Gebruik:  ./share.sh         (dubbelklik werkt niet altijd; open Terminal en run dit)
# Stoppen:  Ctrl+C  of  ./share.sh stop
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
PORT=8787

if [ "$1" = "stop" ]; then
  pkill -f "cloudflared" 2>/dev/null && echo "Tunnel gestopt." || echo "Geen tunnel actief."
  pkill -f "http.server $PORT" 2>/dev/null && echo "Server gestopt." || echo "Geen server actief."
  exit 0
fi

# 1) lokale server starten (indien nog niet actief)
if ! pgrep -f "http.server $PORT" >/dev/null; then
  ( cd "$DIR" && python3 -m http.server $PORT >/tmp/dpt_pub_server.log 2>&1 & )
  echo "Lokale server gestart op poort $PORT."
else
  echo "Lokale server draait al."
fi

# 2) oude tunnel opruimen + nieuwe starten
pkill -f "cloudflared" 2>/dev/null || true
sleep 1
rm -f /tmp/dpt_cf.log
cloudflared tunnel --protocol http2 --url "http://localhost:$PORT" >/tmp/dpt_cf.log 2>&1 &

echo "Tunnel wordt opgezet, even geduld..."
URL=""
for i in $(seq 1 30); do
  URL=$(grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' /tmp/dpt_cf.log 2>/dev/null | head -1)
  [ -n "$URL" ] && break
  sleep 2
done

if [ -n "$URL" ]; then
  echo ""
  echo "==================================================================="
  echo "  PUBLIEKE LINK:  $URL"
  echo "  Duitse versie:  $URL/de/index.html"
  echo "==================================================================="
  echo "  Laat dit venster open staan. Sluiten = link offline."
  echo "  Stoppen: druk Ctrl+C, of run:  ./share.sh stop"
  echo ""
  # blijf draaien zodat de tunnel actief blijft
  wait
else
  echo "Kon geen tunnel-URL ophalen. Probeer opnieuw of check je internet."
  exit 1
fi
