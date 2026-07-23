# -*- coding: utf-8 -*-
"""Deutsche Seiteninhalte für Nexa Oil."""

L = "de"
AP = "../"   # asset prefix für /de/

def acc(q, a):
    return ('<div class="acc-item"><button class="acc-head">%s<span class="pm">+</span></button>'
            '<div class="acc-body"><p>%s</p></div></div>' % (q, a))


def run(g):
    page = g["page"]; ic = g["ic"]; IMG = g["IMG"]
    page_hero = g["page_hero"]; cta_band = g["cta_band"]; world_map = g["world_map"]

    def P(filename, title, desc, body, active, solid=True):
        page(filename, title, desc, body, active, solid=solid, lang=L, asset_prefix=AP)

    def ph(eyebrow, title, lead, img, crumb):
        return page_hero(eyebrow, title, lead, img, crumb, lang=L)

    def cta():
        return cta_band(L)

    def card(icon, title, text):
        return ('<div class="card reveal"><div class="ico">%s</div><h3>%s</h3><p>%s</p></div>'
                % (ic(icon), title, text))

    def feat(icon, title, text):
        return ('<div class="feat reveal"><div class="feat__ico">%s</div><div><h4>%s</h4><p>%s</p></div></div>'
                % (ic(icon), title, text))

    def prod(img, tag, title, text, link="products.html"):
        return ('<div class="prod reveal"><div class="prod__img" style="background-image:url(%s)">'
                '<span class="prod__tag">%s</span></div><div class="prod__body"><h3>%s</h3><p>%s</p>'
                '<a class="prod__link" href="%s">Mehr erfahren %s</a></div></div>'
                % (img, tag, title, text, link, ic("arrow")))

    # ============================================================= START
    hero = (
      '<section class="hero">'
      '<div class="hero__bg" style="background-image:url(%s)"></div><div class="hero__veil"></div>'
      '<div class="container">'
      '<span class="eyebrow reveal">Dubai · Internationaler Energiehandel</span>'
      '<h1 class="reveal d1">Antrieb für den globalen Energiehandel</h1>'
      '<p class="lead reveal d2">Nexa Oil ist ein in Dubai ansässiges internationales '
      'Energiehandelsunternehmen, spezialisiert auf die Lieferung von hochwertigem Rohöl und '
      'Industrieschmierstoffen von vertrauenswürdigen Produzenten aus dem Nahen Osten.</p>'
      '<div class="btn-row reveal d3">'
      '<a class="btn btn--gold" href="quote.html">Angebot anfordern %s</a>'
      '<a class="btn btn--ghost" href="products.html">Produkte ansehen</a></div>'
      '<div class="hero-stats reveal d4">'
      '<div class="hero-stat"><div class="num"><span data-count="40" data-suffix="+">40+</span></div><div class="lbl">Belieferte Länder</div></div>'
      '<div class="hero-stat"><div class="num"><span data-count="5">5</span></div><div class="lbl">Kontinente</div></div>'
      '<div class="hero-stat"><div class="num"><span data-count="24" data-suffix="/7">24/7</span></div><div class="lbl">Handelsabteilung</div></div>'
      '<div class="hero-stat"><div class="num">VAE</div><div class="lbl">Strategische Häfen</div></div>'
      '</div></div>'
      '<div class="scroll-cue"><span>Scrollen</span><span class="mouse"></span></div>'
      '</section>'
    ) % (IMG["hero"], ic("arrow"))
    hero = hero.replace('<div class="scroll-cue">', g["oil_barrel"]() + '<div class="scroll-cue">')

    why = (
      '<section class="section"><div class="container">'
      '<div class="section-head text-center mw-720 mx-auto reveal">'
      '<span class="eyebrow eyebrow--center">Warum wir</span>'
      '<h2>Ein Handelspartner, gebaut auf Vertrauen und Zuverlässigkeit</h2>'
      '<p class="lead">Wir verbinden enge Produzentenbeziehungen am Golf mit disziplinierter Logistik, um '
      'Energieprodukte pünktlich, spezifikationsgerecht und zu Konditionen zu liefern, die für Ihr Geschäft funktionieren.</p></div>'
      '<div class="grid g-3">'
      + card("supply","Zuverlässige Lieferkette","Langjährige Vereinbarungen mit etablierten Produzenten aus dem Nahen Osten sichern konstante Mengen und Qualität – auch in angespannten Märkten.")
      + card("globe","Globale Reichweite","Aktive Handelsströme nach Europa, Asien, Afrika, Nord- und Südamerika von einem einzigen, gut vernetzten Drehkreuz aus.")
      + card("logistics","Effiziente Logistik","Direkter Zugang zu den Tiefwasserhäfen der VAE hält Lieferzeiten kurz und Frachtkosten auf jeder wichtigen Route wettbewerbsfähig.")
      + card("handshake","Vertrauensvolle Partnerschaften","Wir investieren in langfristige Beziehungen zu Lieferanten und Käufern und stellen Folgegeschäft über Einzeltransaktionen.")
      + card("shield","Transparente Abläufe","Klare Preise, anerkannte Incoterms und vollständige Dokumentation geben Geschäftspartnern in jeder Phase Sicherheit.")
      + card("clock","Reaktionsschnelle Abteilung","Eine engagierte Handelsabteilung antwortet auf Anfragen innerhalb eines Werktags – mit Preisen und Verfügbarkeit, auf die Sie reagieren können.")
      + '</div></div></section>'
    )

    stat_strip = (
      '<section class="section--tight bg-navy"><div class="container">'
      '<div class="stat-strip">'
      '<div class="reveal"><div class="num"><span data-count="40" data-suffix="+">40+</span></div><div class="lbl">Weltweit belieferte Länder</div></div>'
      '<div class="reveal d1"><div class="num"><span data-count="6">6</span></div><div class="lbl">Schmierstoff-Produktfamilien</div></div>'
      '<div class="reveal d2"><div class="num"><span data-count="3">3</span></div><div class="lbl">Gehandelte Rohölsorten</div></div>'
      '<div class="reveal d3"><div class="num"><span data-count="100" data-suffix="%">100%</span></div><div class="lbl">Dokumentierte, konforme Geschäfte</div></div>'
      '</div></div></section>'
    )

    products_overview = (
      '<section class="section bg-soft"><div class="container">'
      '<div class="section-head text-center mw-720 mx-auto reveal">'
      '<span class="eyebrow eyebrow--center">Unser Portfolio</span>'
      '<h2>Rohöl & Industrieschmierstoffe</h2>'
      '<p class="lead">Von Rohöl in Bohrlochqualität bis zu präzise entwickelten Schmierstoffen liefern wir '
      'die Energieprodukte, die Raffinerien, Flotten und Schwerindustrie am Laufen halten.</p></div>'
      '<div class="grid g-3">'
      + prod(IMG["crude"],"Rohöl","Leicht · Mittel · Schwer","Hochwertiges Rohöl aus dem Nahen Osten, geliefert zu FOB-, CIF- und CFR-Bedingungen für Raffinerien und die petrochemische Industrie.","crude-oil.html")
      + prod(IMG["engine"],"Schmierstoffe","Motoren- & Hydrauliköle","Leistungsstarke Motoren- und Hydrauliköle für Automobil-, Industrie- und Maschinenanwendungen.","lubricants.html")
      + prod(IMG["marine"],"Schmierstoffe","Schiffsschmierstoffe & Fette","Schiffsschmierstoffe, Getriebe- und Kompressoröle sowie Hochleistungsfette für Schifffahrt, Offshore und Industrie.","lubricants.html")
      + '</div>'
      '<div class="text-center" style="margin-top:46px"><a class="btn btn--dark" href="products.html">Alle Produkte entdecken %s</a></div>'
      '</div></section>'
    ) % ic("arrow")

    network = (
      '<section class="section bg-navy"><div class="container">'
      '<div class="section-head text-center mw-720 mx-auto reveal">'
      '<span class="eyebrow eyebrow--center">Globales Liefernetzwerk</span>'
      '<h2>Von Dubai in die Welt</h2>'
      '<p class="lead">Strategisch zwischen Ost und West gelegen, verschaffen uns die VAE schnellen, flexiblen '
      'Zugang zu jeder wichtigen Schifffahrtsroute und jedem Absatzmarkt.</p></div>'
      + world_map() +
      '<div class="region-grid">'
      '<div class="region reveal"><div class="r-ico">🇪🇺</div><h4>Europa</h4><p>Rotterdam · Mittelmeer</p></div>'
      '<div class="region reveal d1"><div class="r-ico">🌏</div><h4>Asien</h4><p>Singapur · China · Indien</p></div>'
      '<div class="region reveal d2"><div class="r-ico">🌍</div><h4>Afrika</h4><p>West- & Ostküste</p></div>'
      '<div class="region reveal d3"><div class="r-ico">🌎</div><h4>Nordamerika</h4><p>US-Golf · Atlantik</p></div>'
      '<div class="region reveal d4"><div class="r-ico">🌴</div><h4>Südamerika</h4><p>Brasilien · Andenregion</p></div>'
      '</div>'
      '<div class="text-center" style="margin-top:46px"><a class="btn btn--gold" href="global-network.html">Unser Netzwerk ansehen %s</a></div>'
      '</div></section>'
    ) % ic("arrow")

    trust = (
      '<section class="section--tight"><div class="container">'
      '<p class="text-center reveal" style="color:#8a96a4;letter-spacing:.16em;text-transform:uppercase;font-size:.78rem;margin-bottom:30px">'
      'Partner entlang der gesamten globalen Energiewertschöpfungskette</p>'
      '<div class="trust reveal d1">'
      '<span>RAFFINERIEN</span><span>REEDEREIEN</span><span>OEM-FLOTTEN</span>'
      '<span>DISTRIBUTOREN</span><span>PETROCHEMIE</span><span>INDUSTRIE-OEMs</span>'
      '</div></div></section>'
    )

    P("index.html",
      "Internationaler Energiehandel aus Dubai",
      "Nexa Oil ist ein in Dubai ansässiges internationales Energiehandelsunternehmen, das weltweit hochwertiges Rohöl und Industrieschmierstoffe zu FOB-, CIF- und CFR-Bedingungen liefert.",
      hero + why + stat_strip + products_overview + network + trust + cta(),
      "index.html", solid=False)

    # ============================================================= ÜBER UNS
    about_body = (
      ph("Über Nexa Oil","Energie, auf die sich die Welt verlässt",
        "Ein in Dubai ansässiger Händler, Broker und Distributor, der vertrauenswürdige Produzenten aus dem Nahen Osten mit Käufern auf fünf Kontinenten verbindet.",
        IMG["dubai"], "<span>Über uns</span>")
      + '<section class="section"><div class="container"><div class="split">'
        '<div class="reveal"><span class="eyebrow">Wer wir sind</span>'
        '<h2>Verwurzelt am Golf, weltweit aktiv</h2>'
        '<p>Nexa Oil ist ein internationales Energiehandelsunternehmen mit Sitz in Dubai, '
        'Vereinigte Arabische Emirate. Als Händler, Broker und Distributor sind wir auf die weltweite Lieferung '
        'von hochwertigem Rohöl und einem umfassenden Sortiment leistungsstarker Industrieschmierstoffe spezialisiert.</p>'
        '<p>Unsere Position in den VAE – an der Schnittstelle des europäischen, asiatischen und afrikanischen '
        'Handels – ermöglicht es uns, Produkte effizient von den zuverlässigsten Produzenten der Region zu Kunden '
        'weltweit zu bewegen. Diesen geografischen Vorteil verbinden wir mit disziplinierter Handelspraxis, '
        'transparenter Dokumentation und einem beziehungsorientierten Ansatz, der uns zu einem verlässlichen Partner gemacht hat.</p>'
        '<div class="btn-row" style="margin-top:24px"><a class="btn btn--dark" href="quote.html">Mit uns arbeiten %s</a></div></div>'
        '<div class="split__media reveal d1" style="background-image:url(%s)">'
        '<div class="badge-float"><div class="num">Dubai, VAE</div><div class="lbl">Globaler Handelssitz</div></div></div>'
        '</div></div></section>' % (ic("arrow"), IMG["refinery"])
      + '<section class="section bg-soft"><div class="container">'
        '<div class="grid g-2" style="align-items:start">'
        '<div class="card reveal"><div class="ico">%s</div><h3>Unsere Mission</h3>'
        '<p>Zuverlässige, transparente und wettbewerbsfähig bepreiste Energieprodukte an Industrien weltweit zu '
        'liefern – und durch Vertrauen, Konstanz und operative Exzellenz langfristigen Wert für Lieferanten und Kunden zu schaffen.</p></div>'
        '<div class="card reveal d1"><div class="ico">%s</div><h3>Unsere Vision</h3>'
        '<p>Als führendes unabhängiges Energiehandelshaus aus den VAE anerkannt zu werden – bekannt für Integrität, '
        'globale Reichweite und die Verlässlichkeit jedes Barrels und jedes Fasses, das wir bewegen.</p></div>'
        '</div></div></section>' % (ic("bolt"), ic("globe"))
      + '<section class="section"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Unsere Werte</span>'
        '<h2>Die Prinzipien hinter jedem Geschäft</h2></div>'
        '<div class="feat-list grid g-2">'
        + feat("handshake","Integrität zuerst","Wir halten unsere Zusagen ein. Klare Bedingungen, korrekte Dokumentation und faires Handeln liegen jeder Transaktion zugrunde.")
        + feat("shield","Zuverlässigkeit","Kunden planen mit unserer Lieferung. Wir schützen ihre Kontinuität durch gesicherte Mengen und bewährte Logistik.")
        + feat("globe","Globale Perspektive","Wir denken in Handelsrouten, nicht in Grenzen – und bringen das richtige Produkt zum richtigen Preis in den richtigen Markt.")
        + feat("scale","Compliance","Geschäfte werden so strukturiert, dass sie internationale Standards, Sanktionsprüfungen und anerkannte Qualitätsmassstäbe erfüllen.")
        + '</div></div></section>'
      + '<section class="section--tight bg-navy"><div class="container"><div class="stat-strip">'
        '<div class="reveal"><div class="num"><span data-count="40" data-suffix="+">40+</span></div><div class="lbl">Zielmärkte</div></div>'
        '<div class="reveal d1"><div class="num"><span data-count="5">5</span></div><div class="lbl">Kontinente</div></div>'
        '<div class="reveal d2"><div class="num"><span data-count="9">9</span></div><div class="lbl">Produktkategorien</div></div>'
        '<div class="reveal d3"><div class="num"><span data-count="24" data-suffix="/7">24/7</span></div><div class="lbl">Handelsverfügbarkeit</div></div>'
        '</div></div></section>'
      + cta()
    )
    P("about.html","Über uns",
      "Erfahren Sie mehr über Nexa Oil – ein in Dubai ansässiges internationales Energiehandelsunternehmen, das vertrauenswürdige Produzenten aus dem Nahen Osten mit Käufern auf fünf Kontinenten verbindet.",
      about_body, "about.html")

    # ============================================================= PRODUKTE
    products_body = (
      ph("Unsere Produkte","Rohöl & Industrieschmierstoffe",
        "Ein fokussiertes Portfolio hochwertiger Energieprodukte, gehandelt zu anerkannten internationalen Bedingungen und gestützt auf zuverlässige Lieferungen vom Golf.",
        IMG["barrels"], "<span>Produkte</span>")
      + '<section class="section"><div class="container"><div class="split">'
        '<div class="split__media reveal" style="background-image:url(%s)">'
        '<div class="badge-float"><div class="num">FOB · CIF · CFR</div><div class="lbl">Flexible Handelsbedingungen</div></div></div>'
        '<div class="reveal d1"><span class="eyebrow">Rohöl</span><h2>Hochwertiges Rohöl aus dem Nahen Osten</h2>'
        '<p>Wir handeln leichtes, mittleres und schweres Rohöl von etablierten Produzenten am gesamten Golf. '
        'Ladungen werden zu FOB-, CIF- und CFR-Bedingungen an Raffinerien und die petrochemische Industrie weltweit geliefert.</p>'
        '<div class="terms"><div class="term"><div class="t">FOB</div><div class="d">Frei an Bord</div></div>'
        '<div class="term"><div class="t">CIF</div><div class="d">Kosten, Versicherung & Fracht</div></div>'
        '<div class="term"><div class="t">CFR</div><div class="d">Kosten & Fracht</div></div></div>'
        '<div class="btn-row" style="margin-top:26px"><a class="btn btn--dark" href="crude-oil.html">Details zu Rohöl %s</a></div></div>'
        '</div></div></section>' % (IMG["crude"], ic("arrow"))
      + '<section class="section bg-soft"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Industrieschmierstoffe</span>'
        '<h2>Leistungsstarke Industrielösungen</h2>'
        '<p class="lead">Ein komplettes Schmierstoffsortiment für Automobil-, Schifffahrts-, Fertigungs- und '
        'Schwerindustrieanwendungen – erhältlich als Massenware und in Gebinden.</p></div>'
        '<div class="grid g-3">'
        + prod(IMG["engine"],"Motorenöle","Motorenöle","Motorenöle für Automobil- und Industriemotoren, entwickelt für Schutz, Effizienz und verlängerte Ölwechselintervalle.","lubricants.html")
        + prod(IMG["hydraulic"],"Hydraulik","Hydrauliköle","Verschleissschutz-Hydraulikflüssigkeiten für anspruchsvolle Maschinen und präzise Hydrauliksysteme.","lubricants.html")
        + prod(IMG["gear"],"Getriebeöle","Getriebeöle","Hochdruck-Getriebeöle für strapazierfähige industrielle und mobile Getriebesysteme.","lubricants.html")
        + prod(IMG["compressor"],"Kompressor","Kompressoröle","Thermisch stabile Öle für Rotations-, Hub- und Schraubenkompressoren.","lubricants.html")
        + prod(IMG["marine"],"Schifffahrt","Schiffsschmierstoffe","Zylinder-, System- und Trunk-Piston-Öle für Schifffahrt und Offshore-Flotten.","lubricants.html")
        + prod(IMG["grease"],"Fette","Fette","Lithium-, Kalzium- und Spezialfette für schwere Industrieanlagen.","lubricants.html")
        + '</div></div></section>'
      + '<section class="section"><div class="container"><div class="section-head text-center mw-720 mx-auto reveal">'
        '<span class="eyebrow eyebrow--center">Lieferformate</span><h2>Massenware und Gebinde, ganz nach Wunsch</h2></div>'
        '<div class="grid g-4">'
        + card("ship","Massengut & Schiff","Komplette Schiffsladungen und Teilpartien, koordiniert auf Ihren Ladehafen und Zeitplan.")
        + card("barrel","Fässer","Standard-Stahlfässer 200/208 Liter für Distributoren und Industriekunden.")
        + card("truck","IBC & Container","1.000-Liter-IBC für effiziente Handhabung und Lagerung.")
        + card("doc","Individuelle Gebinde","Eigenmarken und massgeschneiderte Gebindegrössen ab vereinbarten Mengen verfügbar.")
        + '</div></div></section>'
      + cta()
    )
    P("products.html","Produkte",
      "Entdecken Sie das Portfolio von Nexa Oil – hochwertiges Rohöl und Industrieschmierstoffe: Motoren-, Hydraulik-, Getriebe-, Kompressor- und Schiffsöle sowie Fette, gehandelt zu FOB, CIF und CFR.",
      products_body, "products.html")

    # ============================================================= ROHÖL
    crude_body = (
      ph("Rohöl","Hochwertiges Rohöl aus dem Nahen Osten",
        "Leichte, mittlere und schwere Sorten für Raffinerien und die petrochemische Industrie – geliefert zu FOB-, CIF- und CFR-Bedingungen.",
        IMG["rig"], '<a href="products.html">Produkte</a> <span>/</span> Rohöl')
      + '<section class="section"><div class="container"><div class="split">'
        '<div class="reveal"><span class="eyebrow">Überblick</span><h2>Zuverlässige Rohöllieferung vom Golf</h2>'
        '<p>Nexa Oil handelt hochwertiges Rohöl aus dem Nahen Osten von etablierten regionalen Produzenten. '
        'Unsere Ladungen versorgen Raffinerien und petrochemische Komplexe, die konstante Qualität, sichere Mengen '
        'und zuverlässige Lieferung verlangen.</p>'
        '<p>Wir strukturieren jede Transaktion rund um den bevorzugten Incoterm des Käufers – ob Verladung am '
        'Ursprung (FOB) oder Lieferung inklusive Fracht und Versicherung (CIF / CFR) – und stellen den vollständigen '
        'Dokumentensatz für einen reibungslosen, konformen Handel bereit.</p>'
        '<div class="chips" style="margin-top:8px"><span class="chip">Raffinerie-Einsatzstoff</span>'
        '<span class="chip">Petrochemische Industrie</span><span class="chip">Langfristverträge</span>'
        '<span class="chip">Spot-Ladungen</span></div></div>'
        '<div class="split__media reveal d1" style="background-image:url(%s)"></div>'
        '</div></div></section>' % IMG["refinery"]
      + '<section class="section bg-soft"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Sorten</span>'
        '<h2>Von uns gehandelte Sorten</h2></div><div class="grid g-3">'
        + card("drop","Leichtes Rohöl","Geringe Dichte und niedriger Schwefelgehalt. Hohe Ausbeute an Benzin und Naphtha – ideal für auf Kraftstoffe optimierte Raffinerien.")
        + card("drop","Mittleres Rohöl","Ausgewogene Dichte und Schwefelgehalt, mit einem vielseitigen Ausbeuteprofil über Destillate und Mittelprodukte hinweg.")
        + card("drop","Schweres Rohöl","Sorten höherer Dichte für komplexe Raffinerien und petrochemische Einsatzstoffe, mit starkem Mitteldestillat-Potenzial.")
        + '</div></div></section>'
      + '<section class="section"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Richtwerte zur Spezifikation</span>'
        '<h2>Typische Qualitätsparameter</h2><p class="lead">Repräsentative Werte – die endgültigen Spezifikationen werden je Ladung und Qualitätszertifikat bestätigt.</p></div>'
        '<div class="reveal d1"><table class="spec-table"><thead><tr><th>Parameter</th><th>Leicht</th><th>Mittel</th><th>Schwer</th></tr></thead>'
        '<tbody>'
        '<tr><td>API-Dichte</td><td>&gt; 34&deg;</td><td>26&ndash;34&deg;</td><td>&lt; 26&deg;</td></tr>'
        '<tr><td>Schwefelgehalt</td><td>&lt; 0,5%</td><td>0,5&ndash;1,5%</td><td>&gt; 1,5%</td></tr>'
        '<tr><td>Dichte @ 15&deg;C</td><td>~0,85 g/cm&sup3;</td><td>~0,89 g/cm&sup3;</td><td>~0,93 g/cm&sup3;</td></tr>'
        '<tr><td>Hauptverwendung</td><td>Kraftstoffe</td><td>Gemischte Raffination</td><td>Petrochemie / Heizöl</td></tr>'
        '<tr><td>Incoterms</td><td>FOB / CIF / CFR</td><td>FOB / CIF / CFR</td><td>FOB / CIF / CFR</td></tr>'
        '</tbody></table></div></div></section>'
      + '<section class="section bg-navy"><div class="container"><div class="section-head text-center mw-720 mx-auto reveal">'
        '<span class="eyebrow eyebrow--center">Handelsbedingungen</span><h2>Wie wir kontrahieren</h2></div>'
        '<div class="grid g-3">'
        + feat("ship","FOB — Frei an Bord","Der Käufer nominiert das Schiff; wir liefern die Ladung an Bord im Ladehafen, der Eigentumsübergang erfolgt an der Schiffsreling.")
        + feat("anchor","CIF — Kosten, Versicherung & Fracht","Wir organisieren und bezahlen Transport und Seeversicherung bis zum genannten Bestimmungshafen.")
        + feat("logistics","CFR — Kosten & Fracht","Wir organisieren und bezahlen die Fracht bis zum Bestimmungshafen; die Versicherung übernimmt der Käufer.")
        + '</div></div></section>'
      + cta()
    )
    P("crude-oil.html","Rohöl",
      "Hochwertiges Rohöl aus dem Nahen Osten – leichte, mittlere und schwere Sorten – geliefert von Nexa Oil zu FOB-, CIF- und CFR-Bedingungen für Raffinerien und Petrochemie.",
      crude_body, "crude-oil.html")

    # ============================================================= SCHMIERSTOFFE
    def lube(anchor, icon, title, text, img, points, rev=False):
        pts = "".join('<span class="chip">%s</span>' % p for p in points)
        media = '<div class="split__media reveal d1" style="background-image:url(%s)"></div>' % img
        txt = ('<div class="reveal"><span class="eyebrow">Industrieschmierstoffe</span><h2>%s</h2><p>%s</p>'
               '<div class="chips" style="margin-top:8px">%s</div></div>' % (title, text, pts))
        inner = (txt + media) if not rev else (media + txt)
        cls = "split split--rev" if rev else "split"
        return ('<section class="section%s" id="%s"><div class="container"><div class="%s">%s</div></div></section>'
                % (" bg-soft" if rev else "", anchor, cls, inner))

    lub_body = (
      ph("Industrieschmierstoffe","Hochleistungsschmierung für die Industrie",
        "Motoren-, Hydraulik-, Getriebe-, Kompressor- und Schiffsöle sowie strapazierfähige Fette – entwickelt für Zuverlässigkeit unter Last.",
        IMG["pipes"], '<a href="products.html">Produkte</a> <span>/</span> Industrieschmierstoffe')
      + '<section class="section--tight"><div class="container"><div class="chips reveal" style="justify-content:center">'
        '<a class="chip" href="#engine-oils">Motorenöle</a><a class="chip" href="#hydraulic-oils">Hydrauliköle</a>'
        '<a class="chip" href="#gear-oils">Getriebeöle</a><a class="chip" href="#compressor-oils">Kompressoröle</a>'
        '<a class="chip" href="#marine-lubricants">Schiffsschmierstoffe</a><a class="chip" href="#greases">Fette</a>'
        '</div></div></section>'
      + lube("engine-oils","bolt","Motorenöle",
          "Hochwertige Motorenöle für Automobil- und Industriemotoren, formuliert zum Schutz vor Verschleiss, Ablagerungen und thermischem Abbau bei gleichzeitiger Förderung der Kraftstoffeffizienz und verlängerter Ölwechselintervalle. Mineralische, teilsynthetische und vollsynthetische Sorten verfügbar.",
          IMG["engine"], ["Automobilmotoren","Industriemotoren","Synthetisch & mineralisch","Lange Intervalle"])
      + lube("hydraulic-oils","wrench","Hydrauliköle",
          "Verschleissschutz-Hydraulikflüssigkeiten für Hydrauliksysteme unter hohem Druck und wechselnden Temperaturen. Hervorragende Oxidationsstabilität, Wasserabscheidung und Filtrierbarkeit halten Präzisionssysteme sauber.",
          IMG["hydraulic"], ["Verschleissschutz (AW)","Hoher VI","Maschinensysteme","Lange Lebensdauer"], rev=True)
      + lube("gear-oils","gear","Getriebeöle",
          "Hochdruck-Getriebeöle für strapazierfähige Getriebesysteme in industriellen und mobilen Anlagen. Überlegene Tragfähigkeit und thermische Stabilität schützen Zahnräder und Lager vor Fressen, Grübchen- und Mikropitting.",
          IMG["gear"], ["EP-Additive","Industriegetriebe","Strapazierfähig","Hohes Drehmoment"])
      + lube("compressor-oils","factory","Kompressoröle",
          "Thermisch stabile Kompressoröle für Rotations-, Hub- und Schraubenkompressoren. Geringe Verkokungsneigung und starke Oxidationsbeständigkeit verlängern die Lebensdauer und schützen vor Ablagerungen im anspruchsvollen Verdichtungsbetrieb.",
          IMG["compressor"], ["Rotation & Schraube","Hubkolben","Geringe Ablagerungen","Luft & Gas"], rev=True)
      + lube("marine-lubricants","anchor","Schiffsschmierstoffe",
          "Ein komplettes Schiffssortiment – Zylinderöle, Systemöle und Trunk-Piston-Motorenöle – für Schifffahrt und Offshore-Flotten. Entwickelt für hohen BN-Schutz, Ablagerungskontrolle und zuverlässige Leistung mit verschiedenen Schiffskraftstoffen.",
          IMG["marine"], ["Zylinderöle","Systemöle","Trunk-Piston","Offshore"])
      + lube("greases","barrel","Fette",
          "Lithium-, Kalziumkomplex- und Spezialfette für schwere Industrieanlagen. Hervorragende mechanische Stabilität, Wasserbeständigkeit und EP-Leistung schützen Lager und Bauteile über weite Temperaturbereiche.",
          IMG["grease"], ["Lithiumkomplex","Kalziumkomplex","EP / Hochtemperatur","Wasserbeständig"], rev=True)
      + cta()
    )
    P("lubricants.html","Industrieschmierstoffe",
      "Nexa Oil liefert leistungsstarke Industrieschmierstoffe – Motoren-, Hydraulik-, Getriebe-, Kompressor- und Schiffsöle sowie Fette – für Industrie, Schifffahrt und schwere Anlagen weltweit.",
      lub_body, "lubricants.html")

    # ============================================================= NETZWERK
    gn_body = (
      ph("Globales Liefernetzwerk","Ein Drehkreuz. Jeder Markt.",
        "Mit Sitz in Dubai und Anbindung an die meistbefahrenen Handelsrouten der Welt bewegen wir Energieprodukte effizient vom Lieferanten zum Kunden.",
        IMG["port"], "<span>Globales Liefernetzwerk</span>")
      + '<section class="section bg-navy"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Weltweite Distribution</span>'
        '<h2>Dubai im Zentrum des globalen Handels</h2>'
        '<p class="lead">Unser Standort in den VAE liegt in unmittelbarer Reichweite von Europa, Asien, Afrika und '
        'Amerika – das verkürzt Lieferzeiten und erweitert Ihre Optionen.</p></div>'
        + world_map() +
        '<div class="region-grid">'
        '<div class="region reveal"><div class="r-ico">🇪🇺</div><h4>Europa</h4><p>Rotterdam · ARA · Mittelmeer</p></div>'
        '<div class="region reveal d1"><div class="r-ico">🌏</div><h4>Asien</h4><p>Singapur · China · Indien</p></div>'
        '<div class="region reveal d2"><div class="r-ico">🌍</div><h4>Afrika</h4><p>West- & Ostafrika</p></div>'
        '<div class="region reveal d3"><div class="r-ico">🌎</div><h4>Nordamerika</h4><p>US-Golf · Atlantik</p></div>'
        '<div class="region reveal d4"><div class="r-ico">🌴</div><h4>Südamerika</h4><p>Brasilien · Anden</p></div>'
        '</div></div></section>'
      + '<section class="section"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">So funktioniert es</span>'
        '<h2>Vom Lieferanten zum Kunden</h2><p class="lead">Eine koordinierte Kette, die das Produkt in Bewegung hält und Geschäftspartner in jedem Schritt informiert.</p></div>'
        '<div class="steps">'
        '<div class="step reveal"><h4>Beschaffung</h4><p>Wir sichern Produkte von vertrauenswürdigen Produzenten aus dem Nahen Osten über feste Lieferverträge.</p></div>'
        '<div class="step reveal d1"><h4>Vertrag</h4><p>Bedingungen, Incoterms, Qualität und Menge werden mit dem Käufer vereinbart und dokumentiert.</p></div>'
        '<div class="step reveal d2"><h4>Logistik</h4><p>Schiffsnominierung, Inspektion, Versicherung und Hafenkoordination werden über VAE-Drehkreuze organisiert.</p></div>'
        '<div class="step reveal d3"><h4>Lieferung</h4><p>Die Ladung wird verschifft, Dokumente freigegeben und das Produkt zu den vereinbarten Bedingungen geliefert.</p></div>'
        '</div></div></section>'
      + '<section class="section bg-soft"><div class="container"><div class="grid g-3">'
        + card("logistics","Effiziente Logistikkette","Direkter Zugang zu Tiefwasserhäfen der VAE und grossen Carriern hält Frachtkosten wettbewerbsfähig und Zeitpläne knapp.")
        + card("ship","Internationale Verschiffung","Wir koordinieren Schiffsnominierung, Begutachtung und Seeversicherung über globale Routen.")
        + card("globe","Globale Handelsrouten","Etablierte Ströme auf fünf Kontinenten geben Käufern Flexibilität bei Ursprung, Timing und Lieferung.")
        + '</div></div></section>'
      + cta()
    )
    P("global-network.html","Globales Liefernetzwerk",
      "Entdecken Sie das globale Liefernetzwerk von Nexa Oil – mit Sitz in Dubai, effizienter Logistik und internationaler Verschiffungskoordination nach Europa, Asien, Afrika und Amerika.",
      gn_body, "global-network.html")

    # ============================================================= BRANCHEN
    branchen = [
        ("factory","Öl & Gas","Einsatzstoffe, Schmierstoffe und Fluide für Upstream-, Midstream- und Downstream-Betriebe."),
        ("anchor","Schifffahrt & Marine","Zylinder-, System- und Trunk-Piston-Öle sowie Fette für Handelsflotten und Offshore."),
        ("gear","Fertigung","Hydraulik-, Getriebe- und Kompressoröle, die Produktionslinien zuverlässig und effizient halten."),
        ("building","Bauwesen","Robuste Schmierstoffe und Kraftstoffe für schwere Geräte, Erdbau- und Baustellenmaschinen."),
        ("pickaxe","Bergbau","EP-Getriebeöle und Fette, entwickelt für extreme Lasten, Staub und raue Umgebungen."),
        ("truck","Logistik & Transport","Motoren- und Antriebsschmierstoffe für Flotten, Häfen und Distribution."),
        ("bolt","Energiesektor","Rohöl-Einsatzstoffe und Industriefluide für Stromerzeugung und Energieinfrastruktur."),
        ("wrench","Schwerindustrie","Hochleistungsschmierung für Stahl, Zement, Verarbeitung und grosse rotierende Anlagen."),
    ]
    ind_cards = "".join(
        '<div class="card reveal%s"><div class="ico">%s</div><h3>%s</h3><p>%s</p></div>'
        % (" d"+str(i%4) if i%4 else "", ic(icon), t, d) for i,(icon,t,d) in enumerate(branchen))
    ind_body = (
      ph("Branchen, die wir beliefern","Energieprodukte für jeden anspruchsvollen Sektor",
        "Von Raffinerien bis zum Bergbau halten unser Rohöl und unsere Schmierstoffe kritische Abläufe in der gesamten Weltwirtschaft am Laufen.",
        IMG["industry"], "<span>Branchen</span>")
      + '<section class="section"><div class="container"><div class="grid g-4">' + ind_cards + '</div></div></section>'
      + '<section class="section bg-navy"><div class="container"><div class="split">'
        '<div class="reveal"><span class="eyebrow">Branchenkompetenz</span><h2>Produkt und Anwendung passgenau verbinden</h2>'
        '<p>Jede Branche stellt andere Anforderungen an einen Schmierstoff oder Einsatzstoff. Unser Team hilft Ihnen, '
        'die richtige Sorte, Spezifikation und das richtige Lieferformat für Ihre Betriebsbedingungen zu wählen – und hält die Versorgung zuverlässig aufrecht.</p>'
        '<div class="feat-list" style="margin-top:24px">'
        + feat("check","Anwendungsberatung","Sorten- und Spezifikationsberatung, abgestimmt auf Ihre Anlagen und Betriebszyklen.")
        + feat("check","Konstante Versorgung","Gesicherte Mengen, damit Produktion und Flotten nie warten müssen.")
        + feat("check","Globale Lieferung","Massenware oder Gebinde, geliefert an Ihren nächstgelegenen Hafen.")
        + '</div></div>'
        '<div class="split__media reveal d1" style="background-image:url(%s)"></div>'
        '</div></div></section>' % IMG["pipes"]
      + cta()
    )
    P("industries.html","Branchen, die wir beliefern",
      "Nexa Oil beliefert Öl & Gas, Schifffahrt, Fertigung, Bauwesen, Bergbau, Logistik, Energie und Schwerindustrie weltweit mit Rohöl und Industrieschmierstoffen.",
      ind_body, "industries.html")

    # ============================================================= QUALITÄT
    q_body = (
      ph("Qualität & Compliance","Standards, auf die Sie handeln können",
        "Dokumentierte Qualität, anerkannte Spezifikationen und disziplinierte Compliance liegen jeder Ladung und jedem Fass zugrunde, das wir liefern.",
        IMG["lab"], "<span>Qualität & Compliance</span>")
      + '<section class="section"><div class="container"><div class="grid g-3">'
        + card("shield","Qualitätssicherung","Produkte werden gemäss anerkannten internationalen Spezifikationen geliefert, mit Qualitäts- und Analysezertifikaten je Ladung.")
        + card("scale","Regulatorische Compliance","Geschäfte werden so strukturiert, dass sie internationale Handelsvorschriften, Sanktionsprüfungen und KYC-Anforderungen erfüllen.")
        + card("doc","Vollständige Dokumentation","Komplette Dokumentensätze – Q&Q-Zertifikate, Konnossemente, Versicherung und Ursprungspapiere – stützen jede Transaktion.")
        + card("leaf","Verantwortungsvoller Handel","Wir fördern sichere Handhabung, korrekte Lagerung und eine umweltbewusste Produktverantwortung.")
        + card("check","Unabhängige Inspektion","Ladungen können von anerkannten Drittinspektoren bei Verladung und Löschung begutachtet werden – für zusätzliche Sicherheit.")
        + card("globe","Internationale Standards","Schmierstoffe orientieren sich an weithin anerkannten Industrie- und OEM-Leistungsmassstäben.")
        + '</div></div></section>'
      + '<section class="section bg-soft"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">FAQ</span>'
        '<h2>Compliance, beantwortet</h2></div>'
        '<div class="mw-820 mx-auto reveal d1">'
        + acc("Welche Spezifikationen erfüllen Ihre Produkte?",
              "Rohölsorten werden gemäss vereinbarten Qualitätszertifikaten geliefert, die API-Dichte, Schwefelgehalt und Dichte abbilden. Schmierstoffe orientieren sich an anerkannten internationalen und OEM-Leistungsstandards; technische Datenblätter sind je Produkt verfügbar.")
        + acc("Zu welchen Incoterms handeln Sie?",
              "Wir kontrahieren regelmässig zu FOB, CIF und CFR. Der passende Begriff wird mit jedem Käufer vereinbart – je nachdem, wer Fracht und Versicherung organisiert und bezahlt.")
        + acc("Bieten Sie unabhängige Inspektionen an?",
              "Ja. Ladungen können von anerkannten Inspektionsgesellschaften bei Verladung und Löschung unabhängig begutachtet werden; entsprechende Mengen- und Qualitätszertifikate werden ausgestellt.")
        + acc("Wie handhaben Sie Sanktionen und KYC?",
              "Jeder Geschäftspartner wird im Rahmen unseres Onboardings geprüft. Wir strukturieren Geschäfte so, dass sie geltende internationale Sanktions- und Handelskontrollregime einhalten.")
        + acc("Welche Dokumente gehören zu einem Geschäft?",
              "Standard-Dokumentensätze umfassen Handelsrechnung, Konnossement, Ursprungszeugnis, Qualitäts- und Mengenzertifikate sowie ggf. Versicherungsdokumente.")
        + '</div></div></section>'
      + cta()
    )
    P("quality.html","Qualität & Compliance",
      "Nexa Oil steht für strenge Qualität und Compliance – anerkannte Spezifikationen, vollständige Dokumentation, unabhängige Inspektion, Sanktionsprüfung und verantwortungsvollen Handel.",
      q_body, "quality.html")

    # ============================================================= KATALOG
    cat_items = [
        ("doc","Rohöl-Programm","Sorten, Richtwerte zur Spezifikation und Handelsbedingungen für leichtes, mittleres und schweres Rohöl."),
        ("bolt","Sortiment Motorenöle","Motorenöle für Automobil und Industrie mit Viskositätsklassen und Leistungsstufen."),
        ("wrench","Sortiment Hydrauliköle","Verschleissschutz- und Hoch-VI-Hydraulikflüssigkeiten mit technischen Parametern."),
        ("gear","Sortiment Getriebeöle","Hochdruck-Getriebeöl-Spezifikationen für Industrie und Mobilbereich."),
        ("factory","Sortiment Kompressoröle","Öle für Rotations-, Schrauben- und Hubkolbenkompressoren."),
        ("anchor","Sortiment Schiffsschmierstoffe","Zylinder-, System- und Trunk-Piston-Öl-Portfolio für die Schifffahrt."),
        ("barrel","Sortiment Fette","Lithium-, Kalziumkomplex- und Spezialfette mit NLGI-Klassen."),
        ("ship","Gebinde & Handelsbedingungen","Massen-, Fass- und IBC-Formate mit Incoterms und Logistikhinweisen."),
    ]
    cat_list = "".join(
        '<div class="cat-item reveal"><div class="cat-item__ico">%s</div>'
        '<div><h4>%s</h4><p>%s</p></div>'
        '<a class="btn btn--outline" href="quote.html">Ansehen %s</a></div>'
        % (ic(icon), t, d, ic("arrow")) for icon,t,d in cat_items)
    cat_body = (
      ph("Katalog","Produktkatalog & technische Datenblätter",
        "Stöbern Sie online in unserem Sortiment oder laden Sie den vollständigen PDF-Katalog mit Spezifikationen, Gebinden und Handelsbedingungen herunter.",
        IMG["barrels"], "<span>Katalog</span>")
      + '<section class="section"><div class="container"><div class="split">'
        '<div class="reveal"><span class="eyebrow">Download</span><h2>Der komplette Nexa-Oil-Trading-Katalog</h2>'
        '<p>Unser PDF-Katalog vereint Produktbeschreibungen, technische Spezifikationen, Gebindeinformationen und '
        'Handelsbedingungen für unser gesamtes Rohöl- und Schmierstoffsortiment – alles, was Ihr Einkaufsteam an einem Ort benötigt.</p>'
        '<ul class="feat-list" style="margin:24px 0">'
        + feat("check","Technische Spezifikationen","Wichtige Parameter und Leistungsstufen für jede Produktlinie.")
        + feat("check","Gebindeinformationen","Massen-, Fass- und IBC-Formate sowie Gebindegrössen.")
        + feat("check","Handelsbedingungen","Incoterms, Lieferzeiten und Lieferbedingungen auf einen Blick.")
        + '</ul>'
        '<div class="btn-row"><a class="btn btn--gold" href="#sheets">PDF-Katalog herunterladen %s</a>'
        '<a class="btn btn--outline" href="quote.html">Preise anfragen</a></div>'
        '<p class="form-note">PDF-Download und einzelne Produktdatenblätter werden auf Anfrage an geprüfte Geschäftsanfragen ausgegeben.</p></div>'
        '<div class="split__media reveal d1" style="background-image:url(%s)">'
        '<div class="badge-float"><div class="num">9 Linien</div><div class="lbl">Rohöl + Schmierstoffportfolio</div></div></div>'
        '</div></div></section>' % (ic("download"), IMG["lab"])
      + '<section class="section bg-soft" id="sheets"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Online-Datenblätter</span>'
        '<h2>Nach Produktlinie stöbern</h2></div>'
        '<div class="grid" style="gap:18px">' + cat_list + '</div></div></section>'
      + cta()
    )
    P("catalog.html","Katalog",
      "Laden Sie den PDF-Katalog von Nexa Oil herunter oder stöbern Sie online in den Datenblättern – technische Spezifikationen, Gebindeinformationen und Handelsbedingungen für Rohöl und Schmierstoffe.",
      cat_body, "catalog.html")

    # ============================================================= AKTUELLES
    news = [
        (IMG["news1"],"Marktbericht","Golf-Rohöl-Differenziale ziehen an, da die asiatische Nachfrage anzieht",
         "Die Raffineriemargen in Asien festigten sich im Quartalsverlauf, was die Nachfrage nach mittleren und schweren Sorten aus dem Nahen Osten steigerte und die kurzfristige Verfügbarkeit verknappte."),
        (IMG["news2"],"Unternehmen","Nexa Oil weitet Schmierstoff-Distribution nach Westafrika aus",
         "Neue Distributorenvereinbarungen erweitern die Reichweite unserer Schiffs- und Industrieschmierstoffe in wichtigen westafrikanischen Häfen und verkürzen die Lieferzeiten für regionale Käufer."),
        (IMG["news3"],"Logistik","VAE-Hafenumschlag unterstützt schnellere Abfertigung von Teilpartien",
         "Anhaltende Investitionen in die Terminalkapazität der VAE helfen Händlern, Ladefenster zu verkürzen und die Planungssicherheit bei kleineren Partien zu verbessern."),
    ]
    news_cards = "".join(
        '<article class="news-card reveal%s"><div class="news-card__img" style="background-image:url(%s)"></div>'
        '<div class="news-card__body"><div class="news-meta"><span class="cat">%s</span><span>Juni 2026</span></div>'
        '<h3>%s</h3><p>%s</p><a class="prod__link" href="#">Weiterlesen %s</a></div></article>'
        % (" d"+str(i+1) if i else "", img, cat, t, d, ic("arrow")) for i,(img,cat,t,d) in enumerate(news))
    news_body = (
      ph("Aktuelles & Marktberichte","Einblicke aus der Handelsabteilung",
        "Marktkommentare, Unternehmensnachrichten und Logistik-Updates aus unserem weltweiten Energiehandel.",
        IMG["refinery"], "<span>Aktuelles & Marktberichte</span>")
      + '<section class="section"><div class="container"><div class="grid g-3">' + news_cards + '</div></div></section>'
      + '<section class="section bg-navy"><div class="container"><div class="split">'
        '<div class="reveal"><span class="eyebrow">Bleiben Sie informiert</span><h2>Marktberichte in Ihrem Postfach</h2>'
        '<p class="lead">Abonnieren Sie regelmässige Markt­kommentare zu Rohöl und Schmierstoffen sowie Nexa-Oil-Trading-Mitteilungen.</p>'
        '<form class="btn-row" data-mock style="margin-top:10px;gap:12px;max-width:520px">'
        '<input type="email" required placeholder="Ihre geschäftliche E-Mail" '
        'style="flex:1;min-width:220px;padding:14px 16px;border-radius:8px;border:1.5px solid rgba(255,255,255,.2);background:rgba(255,255,255,.06);color:#fff">'
        '<button class="btn btn--gold" type="submit">Abonnieren</button>'
        '<div class="form-success">Vielen Dank – Sie haben die Nexa-Oil-Trading-Marktberichte abonniert.</div></form></div>'
        '<div class="split__media reveal d1" style="background-image:url(%s)"></div>'
        '</div></div></section>'
    ) % IMG["barrels"]
    news_body += cta()
    P("news.html","Aktuelles & Marktberichte",
      "Aktuelles und Marktberichte von Nexa Oil – Markt­kommentare zu Rohöl und Schmierstoffen, Unternehmensmitteilungen und Logistikeinblicke aus unserer Handelsabteilung in Dubai.",
      news_body, "news.html")

    # ============================================================= ANGEBOT
    products_opts = ["Leichtes Rohöl","Mittleres Rohöl","Schweres Rohöl","Motorenöle","Hydrauliköle",
                     "Getriebeöle","Kompressoröle","Schiffsschmierstoffe","Fette","Sonstiges / Gemischt"]
    opts = "".join('<option>%s</option>' % o for o in products_opts)
    quote_body = (
      ph("Angebot anfordern","Sagen Sie uns, was Sie benötigen",
        "Teilen Sie uns Ihren Bedarf mit – unsere Handelsabteilung antwortet innerhalb eines Werktags mit Preisen, Verfügbarkeit und Lieferbedingungen.",
        IMG["port"], "<span>Angebot anfordern</span>")
      + '<section class="section"><div class="container"><div class="split" style="gap:48px;align-items:start">'
        '<div class="reveal" style="position:sticky;top:100px">'
        '<span class="eyebrow">Warum bei uns anfragen</span><h2>Ein klares, schnelles Angebot</h2>'
        '<ul class="feat-list" style="margin-top:22px">'
        + feat("clock","Antwort am selben Tag","Unsere Abteilung antwortet auf qualifizierte Anfragen innerhalb eines Werktags.")
        + feat("scale","Anerkannte Bedingungen","Preise zu FOB, CIF oder CFR mit transparenten, dokumentierten Konditionen.")
        + feat("ship","Flexible Logistik","Massenware oder Gebinde, geliefert an Ihren bevorzugten Hafen.")
        + feat("shield","Vertraulich","Ihre Anfrage wird diskret von unserem Handelsteam bearbeitet.")
        + '</ul>'
        '<div class="info-card" style="margin-top:30px"><div class="ico">%s</div><div><h4>Lieber per E-Mail?</h4>'
        '<p><a href="mailto:sales@nexaoiltrading.com">sales@nexaoiltrading.com</a></p></div></div></div>'
        '<div class="form-card reveal d1">'
        '<div class="form-success">Vielen Dank – Ihre Angebotsanfrage ist eingegangen. Unsere Handelsabteilung kontaktiert Sie innerhalb eines Werktags.</div>'
        '<form data-mock><div class="form-grid">'
        '<div class="field"><label>Firmenname <span class="req">*</span></label><input required placeholder="Ihr Unternehmen"></div>'
        '<div class="field"><label>Ansprechpartner <span class="req">*</span></label><input required placeholder="Vollständiger Name"></div>'
        '<div class="field"><label>E-Mail <span class="req">*</span></label><input type="email" required placeholder="sie@unternehmen.com"></div>'
        '<div class="field"><label>Telefon</label><input type="tel" placeholder="+971 ..."></div>'
        '<div class="field"><label>Land <span class="req">*</span></label><input required placeholder="Bestimmungsland"></div>'
        '<div class="field"><label>Produktauswahl <span class="req">*</span></label><select required>%s</select></div>'
        '<div class="field"><label>Benötigte Menge</label><input placeholder="z. B. 50.000 t / 200 Fässer"></div>'
        '<div class="field"><label>Lieferhafen</label><input placeholder="Lösch- / Ladehafen"></div>'
        '<div class="field full"><label>Bevorzugter Incoterm</label><select><option>FOB — Frei an Bord</option>'
        '<option>CIF — Kosten, Versicherung & Fracht</option><option>CFR — Kosten & Fracht</option><option>Wird mitgeteilt</option></select></div>'
        '<div class="field full"><label>Nachricht</label><textarea placeholder="Spezifikationen, Zeitpläne oder weitere Angaben..."></textarea></div>'
        '</div><div style="margin-top:24px"><button class="btn btn--gold" type="submit">Anfrage senden %s</button></div>'
        '<p class="form-note">Mit dem Absenden erklären Sie sich damit einverstanden, von Nexa Oil zu Ihrer Anfrage kontaktiert zu werden. '
        'Dies ist ein Demonstrationsformular – es wird keine Live-Übermittlung gesendet.</p>'
        '</form></div></div></div></section>'
    ) % (ic("mail"), opts, ic("arrow"))
    P("quote.html","Angebot anfordern",
      "Fordern Sie bei Nexa Oil ein Angebot für Rohöl oder Industrieschmierstoffe an. Geben Sie Produkt, Menge, Lieferhafen und bevorzugten Incoterm an – Antwort innerhalb eines Werktags.",
      quote_body, "quote.html")

    # ============================================================= KONTAKT
    contact_body = (
      ph("Kontakt","Lassen Sie uns ins Gespräch kommen",
        "Erreichen Sie unsere Handelsabteilung in Dubai für Preise, Partnerschaften oder allgemeine Anfragen – wir antworten zügig auf jede qualifizierte Nachricht.",
        IMG["dubai"], "<span>Kontakt</span>")
      + '<section class="section"><div class="container"><div class="grid g-3" style="margin-bottom:48px">'
        '<div class="info-card reveal"><div class="ico">%s</div><div><h4>Hauptsitz</h4>'
        '<p>Nexa Oil<br>Dubai, Vereinigte Arabische Emirate</p></div></div>'
        '<div class="info-card reveal d1"><div class="ico">%s</div><div><h4>E-Mail</h4>'
        '<p><a href="mailto:sales@nexaoiltrading.com">sales@nexaoiltrading.com</a></p></div></div>'
        '<div class="info-card reveal d2"><div class="ico">%s</div><div><h4>Handelszeiten</h4>'
        '<p>Sonntag – Freitag<br>09:00 – 18:00 GST</p></div></div>'
        '</div>'
        '<div class="split" style="gap:48px;align-items:start">'
        '<div class="form-card reveal">'
        '<div class="form-success">Vielen Dank für Ihre Nachricht – ein Mitglied unseres Teams meldet sich in Kürze.</div>'
        '<h3 style="margin-bottom:6px">Senden Sie uns eine Nachricht</h3>'
        '<p style="color:#5c6775;margin-bottom:24px;font-size:.95rem">Mit <span style="color:#c0392b">*</span> markierte Felder sind Pflichtfelder.</p>'
        '<form data-mock><div class="form-grid">'
        '<div class="field"><label>Name <span class="req">*</span></label><input required placeholder="Ihr Name"></div>'
        '<div class="field"><label>Unternehmen</label><input placeholder="Firmenname"></div>'
        '<div class="field"><label>E-Mail <span class="req">*</span></label><input type="email" required placeholder="sie@unternehmen.com"></div>'
        '<div class="field"><label>Telefon</label><input type="tel" placeholder="+971 ..."></div>'
        '<div class="field full"><label>Nachricht <span class="req">*</span></label><textarea required placeholder="Wie können wir helfen?"></textarea></div>'
        '</div><div style="margin-top:22px"><button class="btn btn--gold" type="submit">Nachricht senden %s</button></div></form></div>'
        '<div class="reveal d1"><span class="eyebrow">Dubai, VAE</span><h2>Strategisch günstig für den Welthandel</h2>'
        '<p>Unsere Lage in Dubai bringt uns in Reichweite der wichtigsten Schifffahrtsrouten und Absatzmärkte der Welt. '
        'Ob Raffinerie, Distributor, Reederei oder Industriekunde – unser Team steht für Sie bereit.</p>'
        '<div class="map-wrap" style="padding:0;margin-top:24px;min-height:300px;background-image:linear-gradient(120deg,rgba(10,10,12,.4),rgba(10,10,12,.15)),url(%s);background-size:cover;background-position:center;border-radius:14px"></div>'
        '<div class="grid g-2" style="margin-top:24px;gap:16px">'
        + feat("mail","Allgemein & Vertrieb","sales@nexaoiltrading.com")
        + feat("pin","Besuch","Dubai, Vereinigte Arabische Emirate")
        + '</div></div>'
        '</div></div></section>'
    ) % (ic("pin"), ic("mail"), ic("clock"), ic("arrow"), IMG["dubai"])
    P("contact.html","Kontakt",
      "Kontaktieren Sie Nexa Oil in Dubai, Vereinigte Arabische Emirate. E-Mail sales@nexaoiltrading.com für Anfragen zu Rohöl und Industrieschmierstoffen, Angebote und Partnerschaften.",
      contact_body, "contact.html")
