# -*- coding: utf-8 -*-
"""Static site generator for Nexa Oil (EN + DE)."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ images
# --- verified-correct base images (content visually confirmed) ---
_DUBAI  = "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1600&q=80"  # Dubai skyline
_PORT   = "https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3?auto=format&fit=crop&w=1600&q=80"  # aerial cargo/oil port
_ENGINE = "https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?auto=format&fit=crop&w=1200&q=80"  # engine block
_INDUS  = "https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?auto=format&fit=crop&w=1600&q=80"  # heavy industry / welding
_MARINE = "https://images.unsplash.com/photo-1605281317010-fe5ffe798166?auto=format&fit=crop&w=1200&q=80"  # vessel at sea
_GREASE = "https://images.unsplash.com/photo-1530124566582-a618bc2615dc?auto=format&fit=crop&w=1200&q=80"  # workshop tools
_TEAM   = "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1200&q=80"  # office team
_LAB    = "https://images.unsplash.com/photo-1581093588401-fbb62a02f120?auto=format&fit=crop&w=1200&q=80"  # lab / safety
IMG = {
    "hero":      _DUBAI,
    "dubai":     _DUBAI,
    "refinery":  _PORT,
    "tanker":    _PORT,
    "rig":       _INDUS,
    "barrels":   _DUBAI,
    "crude":     _PORT,
    "pipes":     _INDUS,
    "engine":    _ENGINE,
    "hydraulic": _INDUS,
    "gear":      _ENGINE,
    "compressor":_INDUS,
    "marine":    _MARINE,
    "grease":    _GREASE,
    "port":      _PORT,
    "team":      _TEAM,
    "lab":       _LAB,
    "industry":  _PORT,
    "news1":     "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?auto=format&fit=crop&w=1000&q=80",
    "news2":     "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?auto=format&fit=crop&w=1000&q=80",
    "news3":     "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=1000&q=80",
}

# ------------------------------------------------------------------ svg icons
def ic(name):
    P = {
        "supply":   '<path d="M3 7h13v10H3z"/><path d="M16 10h3l2 3v4h-5z"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
        "globe":    '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"/>',
        "logistics":'<path d="M2 7l10-4 10 4-10 4z"/><path d="M2 7v10l10 4 10-4V7"/><path d="M12 11v10"/>',
        "handshake":'<path d="M8 11l3 3 5-5 4 4M2 12l4-4 4 2"/><path d="M16 14l2 2"/>',
        "shield":   '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
        "drop":     '<path d="M12 3c4 5 6 8 6 11a6 6 0 0 1-12 0c0-3 2-6 6-11z"/>',
        "barrel":   '<rect x="6" y="3" width="12" height="18" rx="2"/><path d="M6 9h12M6 15h12"/>',
        "gear":     '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
        "ship":     '<path d="M3 14l9-3 9 3-2 6H5z"/><path d="M12 11V4M8 7h8"/>',
        "factory":  '<path d="M3 21V10l6 4V10l6 4V6l6 4v11z"/><path d="M7 17h2M13 17h2"/>',
        "doc":      '<path d="M6 2h8l4 4v16H6z"/><path d="M14 2v4h4M9 13h6M9 17h6"/>',
        "phone":    '<path d="M5 3h4l2 5-3 2a12 12 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
        "mail":     '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
        "pin":      '<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
        "clock":    '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        "check":    '<path d="M20 6L9 17l-5-5"/>',
        "wrench":   '<path d="M14 7a4 4 0 0 1-5 5l-6 6 2 2 6-6a4 4 0 0 0 5-5z"/>',
        "leaf":     '<path d="M5 21c0-9 5-14 14-14 0 9-5 14-14 14z"/><path d="M5 21C9 13 13 11 17 10"/>',
        "scale":    '<path d="M12 3v18M5 7h14M5 7l-2 6h4zM19 7l-2 6h4z"/><path d="M3 13a2 2 0 0 0 4 0M17 13a2 2 0 0 0 4 0"/>',
        "truck":    '<rect x="2" y="7" width="12" height="9"/><path d="M14 10h4l3 3v3h-7z"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
        "anchor":   '<circle cx="12" cy="5" r="2"/><path d="M12 7v13M5 13a7 7 0 0 0 14 0M5 13H3M19 13h2"/>',
        "pickaxe":  '<path d="M4 20l8-8M14 4a8 8 0 0 1 6 6M10 4a8 8 0 0 0-6 6"/>',
        "building": '<path d="M4 21V5l8-3 8 3v16"/><path d="M9 9h2M13 9h2M9 13h2M13 13h2M9 17h6"/>',
        "bolt":     '<path d="M13 2L4 14h6l-1 8 9-12h-6z"/>',
        "arrow":    '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "download": '<path d="M12 3v12M7 11l5 4 5-4M5 21h14"/>',
        "search":   '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/>',
        "users":    '<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 6a3 3 0 0 1 0 6M15 14a6 6 0 0 1 6 6"/>',
    }
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % P[name]

# ------------------------------------------------------------------ translations (shell)
NAV_ITEMS = ["index.html","about.html","__PRODUCTS__","global-network.html",
             "industries.html","quality.html","catalog.html","news.html","contact.html"]
PROD_ITEMS = ["__label__","products.html","crude-oil.html","lubricants.html"]

T = {
  "en": {
    "nav": {"index.html":"Home","about.html":"About","__PRODUCTS__":"Products",
            "global-network.html":"Global Network","industries.html":"Industries",
            "quality.html":"Quality","catalog.html":"Catalog","news.html":"News","contact.html":"Contact"},
    "prod": {"__label__":"Browse","products.html":"All Products","crude-oil.html":"Crude Oil",
             "lubricants.html":"Industrial Lubricants"},
    "products_word":"Products",
    "quote_btn":"Request a Quote",
    "home_link":"Home",
    "menu":"Menu",
    "f_company":"Company","f_products":"Products","f_touch":"Get in touch",
    "f_company_links":[("about.html","About Us"),("global-network.html","Global Supply Network"),
                       ("quality.html","Quality & Compliance"),("news.html","News & Market Updates")],
    "f_product_links":[("crude-oil.html","Crude Oil"),("lubricants.html","Industrial Lubricants"),
                       ("catalog.html","Catalog"),("industries.html","Industries We Serve")],
    "f_addr":"Nexa Oil<br>Dubai, United Arab Emirates",
    "f_hours":"Sun &ndash; Fri, 09:00 &ndash; 18:00 GST",
    "f_about":"A Dubai-based international energy trading company specialising in the supply of premium "
              "crude oil and high-performance industrial lubricants to markets across five continents.",
    "f_rights":"All rights reserved.",
    "f_bottom_loc":"Dubai, United Arab Emirates",
    "f_quote":"Request a Quote","f_contact":"Contact",
    "cta_eyebrow":"Let's do business",
    "cta_title":"Ready to source with confidence?",
    "cta_text":"Request a tailored quotation for crude oil or industrial lubricants and our trading desk "
               "will respond within one business day with pricing, availability and delivery terms.",
    "cta_btn1":"Request a Quote","cta_btn2":"Contact Our Desk",
  },
  "de": {
    "nav": {"index.html":"Start","about.html":"Über uns","__PRODUCTS__":"Produkte",
            "global-network.html":"Globales Netzwerk","industries.html":"Branchen",
            "quality.html":"Qualität","catalog.html":"Katalog","news.html":"Aktuelles","contact.html":"Kontakt"},
    "prod": {"__label__":"Übersicht","products.html":"Alle Produkte","crude-oil.html":"Rohöl",
             "lubricants.html":"Industrieschmierstoffe"},
    "products_word":"Produkte",
    "quote_btn":"Angebot anfordern",
    "home_link":"Start",
    "menu":"Menü",
    "f_company":"Unternehmen","f_products":"Produkte","f_touch":"Kontakt aufnehmen",
    "f_company_links":[("about.html","Über uns"),("global-network.html","Globales Liefernetzwerk"),
                       ("quality.html","Qualität & Compliance"),("news.html","Aktuelles & Marktberichte")],
    "f_product_links":[("crude-oil.html","Rohöl"),("lubricants.html","Industrieschmierstoffe"),
                       ("catalog.html","Katalog"),("industries.html","Branchen, die wir beliefern")],
    "f_addr":"Nexa Oil<br>Dubai, Vereinigte Arabische Emirate",
    "f_hours":"So &ndash; Fr, 09:00 &ndash; 18:00 GST",
    "f_about":"Ein in Dubai ansässiges internationales Energiehandelsunternehmen, spezialisiert auf die "
              "Lieferung von hochwertigem Rohöl und leistungsstarken Industrieschmierstoffen an Märkte "
              "auf fünf Kontinenten.",
    "f_rights":"Alle Rechte vorbehalten.",
    "f_bottom_loc":"Dubai, Vereinigte Arabische Emirate",
    "f_quote":"Angebot anfordern","f_contact":"Kontakt",
    "cta_eyebrow":"Lassen Sie uns zusammenarbeiten",
    "cta_title":"Bereit, mit Vertrauen zu beschaffen?",
    "cta_text":"Fordern Sie ein massgeschneidertes Angebot für Rohöl oder Industrieschmierstoffe an – "
               "unser Handelsteam antwortet innerhalb eines Werktags mit Preisen, Verfügbarkeit und Lieferbedingungen.",
    "cta_btn1":"Angebot anfordern","cta_btn2":"Kontakt aufnehmen",
  },
}

def brand():
    return (
      '<a href="index.html" class="brand">' +
      '<span class="brand__mark"><svg viewBox="0 0 24 24" fill="none" stroke="#0b0b0d" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3c4 5 6 8 6 11a6 6 0 0 1-12 0c0-3 2-6 6-11z"/></svg></span>' +
      '<span class="brand__txt"><span class="brand__name">Nexa</span>' +
      '<span class="brand__sub">Oil</span></span></a>'
    )

def lang_switch(lang, filename, mobile=False):
    # counterpart link to the other language
    de_href = ("" if lang == "en" else "../") if False else None
    if lang == "en":
        en_href, de_link = "index.html" if filename == "index.html" else filename, "de/" + filename
        en_active, de_active = "active", ""
        en_target, de_target = "#", "de/" + filename
    else:
        en_target, de_target = "../" + filename, "#"
        en_active, de_active = "", "active"
    cls = "m-lang" if mobile else "lang-switch"
    return ('<div class="%s"><a href="%s" class="%s" hreflang="en">EN</a>'
            '<a href="%s" class="%s" hreflang="de">DE</a></div>'
            % (cls, en_target, en_active, de_target, de_active))

def nav_html(active, lang):
    t = T[lang]; items = ""
    for href in NAV_ITEMS:
        if href == "__PRODUCTS__":
            sub = ""
            for h in PROD_ITEMS:
                if h == "__label__":
                    sub += '<span class="dropdown__label">%s</span>' % t["prod"]["__label__"]
                else:
                    sub += '<a href="%s">%s</a>' % (h, t["prod"][h])
            act = " active" if active in ("products.html","crude-oil.html","lubricants.html") else ""
            items += ('<div class="has-dropdown"><a class="has-drop%s">%s'
                      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></a>'
                      '<div class="dropdown">%s</div></div>') % (act, t["products_word"], sub)
        else:
            act = " active" if href == active else ""
            items += '<a href="%s" class="%s">%s</a>' % (href, act.strip(), t["nav"][href])
    return items

def mobile_html(active, lang, filename):
    t = T[lang]; out = ""
    for href in NAV_ITEMS:
        if href == "__PRODUCTS__":
            out += '<span class="m-label">%s</span>' % t["products_word"]
            for h in PROD_ITEMS:
                if h != "__label__":
                    out += '<a href="%s">%s</a>' % (h, t["prod"][h])
        else:
            out += '<a href="%s">%s</a>' % (href, t["nav"][href])
    out += lang_switch(lang, filename, mobile=True)
    out += '<a class="btn btn--gold" href="quote.html">%s %s</a>' % (t["quote_btn"], ic("arrow"))
    return out

def header(active, lang, filename):
    t = T[lang]
    return (
      '<header class="header"><div class="container"><nav class="nav">' +
      brand() +
      '<div class="nav-menu">' + nav_html(active, lang) + '</div>' +
      '<div style="display:flex;align-items:center">' + lang_switch(lang, filename) +
      '<div class="nav-cta"><a class="btn btn--gold" href="quote.html">%s</a></div></div>' % t["quote_btn"] +
      '<button class="burger" aria-label="%s"><span></span><span></span><span></span></button>' % t["menu"] +
      '</nav></div></header>' +
      '<div class="mobile-nav">' + mobile_html(active, lang, filename) + '</div>' +
      '<div class="overlay"></div>'
    )

def footer(lang):
    t = T[lang]
    cols = ""
    for title, links in [(t["f_company"], t["f_company_links"]), (t["f_products"], t["f_product_links"])]:
        ls = "".join('<li><a href="%s">%s</a></li>' % (h, l) for h, l in links)
        cols += '<div><h5>%s</h5><ul>%s</ul></div>' % (title, ls)
    contact = (
      '<div class="footer__contact"><h5>%s</h5><ul>' % t["f_touch"] +
      '<li>' + ic("pin") + '<span>%s</span></li>' % t["f_addr"] +
      '<li>' + ic("mail") + '<a href="mailto:sales@nexaoiltrading.com">sales@nexaoiltrading.com</a></li>'
      '<li>' + ic("clock") + '<span>%s</span></li>' % t["f_hours"] +
      '</ul>'
      '<div class="socials">'
      '<a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM10 9h3.8v1.7h.05c.53-1 1.8-2 3.7-2 4 0 4.7 2.6 4.7 6V21h-4v-5.3c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9V21h-4z"/></svg></a>'
      '<a href="#" aria-label="X"><svg viewBox="0 0 24 24"><path d="M17 3h3l-7 8 8 10h-6l-5-6-5 6H2l7-9L1 3h6l4 5z"/></svg></a>'
      '<a href="#" aria-label="Email"><svg viewBox="0 0 24 24"><path d="M3 5h18v14H3z" fill="none" stroke="#fff" stroke-width="1.5"/><path d="M3 6l9 7 9-7" fill="none" stroke="#fff" stroke-width="1.5"/></svg></a>'
      '</div></div>'
    )
    about = ('<div class="footer__about">' + brand() + '<p>%s</p></div>' % t["f_about"])
    return (
      '<footer class="footer"><div class="container">'
      '<div class="footer__top">' + about + cols + contact + '</div>'
      '<div class="footer__bottom">'
      '<span>&copy; <span id="year">2026</span> Nexa Oil. %s</span>' % t["f_rights"] +
      '<span>%s &nbsp;·&nbsp; <a href="quote.html">%s</a> &nbsp;·&nbsp; <a href="contact.html">%s</a></span>'
      % (t["f_bottom_loc"], t["f_quote"], t["f_contact"]) +
      '</div></div></footer>'
    )

# ------------------------------------------------------------------ page shell
def page(filename, title, desc, body, active, solid=True, lang="en", asset_prefix=""):
    body_cls = "solid-header" if solid else ""
    alt_de = ("de/" + filename) if lang == "en" else filename
    alt_en = filename if lang == "en" else ("../" + filename)
    html = (
'<!DOCTYPE html>\n<html lang="%s">\n<head>\n'
'<meta charset="UTF-8">\n'
'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
'<title>%s | Nexa Oil</title>\n'
'<meta name="description" content="%s">\n'
'<meta name="keywords" content="oil trading Dubai, crude oil supplier UAE, industrial lubricants, energy trading company, FOB CIF CFR, Rohöl Händler, Industrieschmierstoffe, Energiehandel">\n'
'<meta name="author" content="Nexa Oil">\n'
'<meta property="og:type" content="website">\n'
'<meta property="og:title" content="%s | Nexa Oil">\n'
'<meta property="og:description" content="%s">\n'
'<meta property="og:site_name" content="Nexa Oil">\n'
'<meta property="og:locale" content="%s">\n'
'<link rel="alternate" hreflang="en" href="%s">\n'
'<link rel="alternate" hreflang="de" href="%s">\n'
'<meta name="theme-color" content="#0b0b0d">\n'
'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
'<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">\n'
'<link rel="stylesheet" href="%sassets/css/style.css">\n'
'<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns=%%27http://www.w3.org/2000/svg%%27 viewBox=%%270 0 24 24%%27%%3E%%3Cpath d=%%27M12 3c4 5 6 8 6 11a6 6 0 0 1-12 0c0-3 2-6 6-11z%%27 fill=%%27%%23FF6A00%%27/%%3E%%3C/svg%%3E">\n'
'</head>\n<body class="%s">\n%s\n<main>\n%s\n</main>\n%s\n'
'<script src="%sassets/js/main.js"></script>\n</body>\n</html>\n'
    ) % ("de" if lang=="de" else "en", title, desc, title, desc,
         "de_DE" if lang=="de" else "en_US", alt_en, alt_de,
         asset_prefix, body_cls, header(active, lang, filename), body, footer(lang),
         asset_prefix)
    outdir = OUT if lang == "en" else os.path.join(OUT, "de")
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    with open(os.path.join(outdir, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", ("de/" if lang=="de" else "") + filename)

# ------------------------------------------------------------------ reusable blocks
def page_hero(eyebrow, title, lead, img, crumb, lang="en"):
    home = T[lang]["home_link"]
    cb = '<div class="breadcrumb"><a href="index.html">%s</a> <span>/</span> %s</div>' % (home, crumb)
    return (
      '<section class="page-hero" style="background-image:linear-gradient(120deg,rgba(10,10,12,.93),rgba(22,22,26,.78)),url(%s)">'
      '<div class="container"><span class="eyebrow eyebrow--center reveal">%s</span>'
      '<h1 class="reveal d1">%s</h1><p class="lead reveal d2">%s</p>%s</div></section>'
    ) % (img, eyebrow, title, lead, cb)

def cta_band(lang="en"):
    t = T[lang]
    return (
      '<section class="cta-band"><div class="cta-band__bg" style="background-image:url(%s)"></div>'
      '<div class="container reveal"><span class="eyebrow eyebrow--center">%s</span>'
      '<h2>%s</h2><p class="lead">%s</p>'
      '<div class="btn-row" style="justify-content:center">'
      '<a class="btn btn--gold" href="quote.html">%s %s</a>'
      '<a class="btn btn--ghost" href="contact.html">%s</a></div></div></section>'
    ) % (IMG["port"], t["cta_eyebrow"], t["cta_title"], t["cta_text"],
         t["cta_btn1"], ic("arrow"), t["cta_btn2"])

def world_map():
    dubai = (560, 250)
    nodes = [("Rotterdam",470,150),("New York",250,180),("Houston",200,230),
             ("Santos",330,360),("Singapore",760,290),("Shanghai",800,210),
             ("Mumbai",640,265),("Lagos",480,300),("Durban",540,390),("Tokyo",850,195)]
    routes = ""
    dots = '<circle class="map-dot" cx="%d" cy="%d" r="7" fill="#ff6a00"/>' % dubai
    dots += '<circle cx="%d" cy="%d" r="13" fill="none" stroke="#ff6a00" stroke-width="1.2" opacity=".5"/>' % dubai
    labels = '<text x="%d" y="%d" fill="#fff" font-size="13" font-family="Inter" font-weight="600">Dubai HQ</text>' % (dubai[0]+14, dubai[1]+4)
    for name, x, y in nodes:
        mx = (dubai[0]+x)/2
        my = min(dubai[1], y) - 50
        routes += '<path class="map-route" d="M%d %d Q %d %d %d %d" fill="none" stroke="#ff6a00" stroke-width="1.3" opacity=".55"/>' % (dubai[0],dubai[1],mx,my,x,y)
        dots += '<circle class="map-dot" cx="%d" cy="%d" r="4.5" fill="#ffb27a"/>' % (x,y)
        labels += '<text x="%d" y="%d" fill="#AAB4C0" font-size="11" font-family="Inter">%s</text>' % (x+7,y+3,name)
    return (
      '<div class="map-wrap reveal"><svg viewBox="0 0 1000 500" role="img" aria-label="Global trading routes from Dubai">'
      '<rect width="1000" height="500" fill="#161619"/>'
      '<g fill="#26262c" stroke="#38383f" stroke-width="1">'
      '<path d="M120 140 q60 -40 150 -20 q60 10 70 60 q-20 60 -80 80 q-90 30 -130 -20 q-30 -60 -10 -100z"/>'
      '<path d="M300 300 q40 -20 70 10 q20 60 -10 110 q-40 40 -70 0 q-20 -70 10 -120z"/>'
      '<path d="M440 110 q70 -30 140 -10 q40 20 30 70 q-30 40 -90 40 q-70 0 -90 -50 q-10 -30 10 -50z"/>'
      '<path d="M470 270 q60 -20 110 20 q30 70 -10 130 q-50 40 -90 -10 q-40 -90 -10 -160z"/>'
      '<path d="M620 150 q90 -30 200 -10 q90 30 100 90 q-20 70 -130 90 q-160 20 -190 -60 q-20 -70 20 -100z"/>'
      '<path d="M780 330 q40 -10 70 20 q10 40 -30 60 q-50 10 -60 -30 q-5 -30 20 -50z"/>'
      '</g>'
      + routes + dots + labels +
      '</svg></div>'
    )

def oil_barrel():
    """Premium SVG oil drum for the hero: black steel body with an orange NEXA band."""
    drop = 'M12 3c4 5 6 8 6 11a6 6 0 0 1-12 0c0-3 2-6 6-11z'
    return (
      '<div class="hero-barrel" aria-hidden="true">'
      '<svg viewBox="0 0 380 500" xmlns="http://www.w3.org/2000/svg">'
      '<defs>'
        '<linearGradient id="nxBody" x1="0" y1="0" x2="1" y2="0">'
          '<stop offset="0" stop-color="#151517"/><stop offset="0.15" stop-color="#4a4a52"/>'
          '<stop offset="0.45" stop-color="#2b2b30"/><stop offset="0.8" stop-color="#161618"/>'
          '<stop offset="1" stop-color="#0b0b0d"/></linearGradient>'
        '<linearGradient id="nxLid" x1="0" y1="0" x2="1" y2="0">'
          '<stop offset="0" stop-color="#3a3a41"/><stop offset="0.5" stop-color="#5a5a63"/>'
          '<stop offset="1" stop-color="#1a1a1d"/></linearGradient>'
        '<linearGradient id="nxRib" x1="0" y1="0" x2="1" y2="0">'
          '<stop offset="0" stop-color="#0c0c0e"/><stop offset="0.5" stop-color="#3c3c43"/>'
          '<stop offset="1" stop-color="#0a0a0c"/></linearGradient>'
        '<linearGradient id="nxBand" x1="0" y1="0" x2="0" y2="1">'
          '<stop offset="0" stop-color="#ff8a3d"/><stop offset="0.5" stop-color="#ff6a00"/>'
          '<stop offset="1" stop-color="#e85d00"/></linearGradient>'
        '<radialGradient id="nxGlow" cx="0.5" cy="0.5" r="0.5">'
          '<stop offset="0" stop-color="#ff6a00" stop-opacity="0.45"/>'
          '<stop offset="0.6" stop-color="#ff6a00" stop-opacity="0.12"/>'
          '<stop offset="1" stop-color="#ff6a00" stop-opacity="0"/></radialGradient>'
      '</defs>'
      # ambient glow + contact shadow
      '<ellipse cx="190" cy="255" rx="185" ry="205" fill="url(#nxGlow)"/>'
      '<ellipse cx="190" cy="436" rx="126" ry="20" fill="#050506" opacity="0.5"/>'
      '<g class="barrel-body">'
        # black steel body
        '<path d="M70 120 L70 412 A120 30 0 0 0 310 412 L310 120 Z" fill="url(#nxBody)"/>'
        # metallic sheen
        '<ellipse cx="120" cy="266" rx="17" ry="128" fill="#ffffff" opacity="0.11"/>'
        '<ellipse cx="120" cy="266" rx="6" ry="128" fill="#ffffff" opacity="0.15"/>'
        # top rib
        '<path d="M70 172 A120 26 0 0 0 310 172 L310 192 A120 26 0 0 1 70 192 Z" fill="url(#nxRib)"/>'
        '<path d="M72 173 A118 25 0 0 0 308 173" fill="none" stroke="#5a5a63" stroke-width="1.2" opacity="0.5"/>'
        # bottom rib
        '<path d="M70 345 A120 26 0 0 0 310 345 L310 365 A120 26 0 0 1 70 365 Z" fill="url(#nxRib)"/>'
        '<path d="M72 346 A118 25 0 0 0 308 346" fill="none" stroke="#5a5a63" stroke-width="1.2" opacity="0.5"/>'
        # centre ORANGE label band
        '<path d="M70 240 A120 27 0 0 0 310 240 L310 304 A120 27 0 0 1 70 304 Z" '
        'fill="url(#nxBand)" stroke="#c24e00" stroke-width="1.5"/>'
        '<g transform="translate(178,244) scale(1.0)"><path d="' + drop + '" fill="#0b0b0d"/></g>'
        '<text x="190" y="296" text-anchor="middle" fill="#0b0b0d" '
        'font-family="Space Grotesk, Inter, sans-serif" font-size="27" font-weight="700" '
        'letter-spacing="4">NEXA</text>'
        # top lid (dark)
        '<ellipse cx="190" cy="120" rx="120" ry="30" fill="url(#nxLid)" stroke="#0a0a0c" stroke-width="2"/>'
        '<ellipse cx="190" cy="120" rx="94" ry="22" fill="none" stroke="#4a4a52" stroke-width="1.5"/>'
        '<ellipse cx="150" cy="116" rx="13" ry="5.5" fill="#0c0c0e"/>'
        '<ellipse cx="150" cy="115" rx="13" ry="5.5" fill="none" stroke="#5a5a63" stroke-width="1" opacity="0.6"/>'
      '</g>'
      # animated drip from the bung
      '<g class="barrel-drip"><path transform="translate(143,124) scale(0.6)" d="' + drop + '" fill="#ff8a3d"/></g>'
      '</svg></div>'
    )

import build_pages      # English content
import build_pages_de   # German content
build_pages.run(globals())
build_pages_de.run(globals())
