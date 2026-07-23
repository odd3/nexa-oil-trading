# -*- coding: utf-8 -*-
"""Page content for Nexa Oil."""

def run(g):
    page = g["page"]; ic = g["ic"]; IMG = g["IMG"]
    page_hero = g["page_hero"]; cta_band = g["cta_band"]; world_map = g["world_map"]

    def card(icon, title, text):
        return ('<div class="card reveal"><div class="ico">%s</div><h3>%s</h3><p>%s</p></div>'
                % (ic(icon), title, text))

    def feat(icon, title, text):
        return ('<div class="feat reveal"><div class="feat__ico">%s</div><div><h4>%s</h4><p>%s</p></div></div>'
                % (ic(icon), title, text))

    def prod(img, tag, title, text, link="products.html"):
        return ('<div class="prod reveal"><div class="prod__img" style="background-image:url(%s)">'
                '<span class="prod__tag">%s</span></div><div class="prod__body"><h3>%s</h3><p>%s</p>'
                '<a class="prod__link" href="%s">Learn more %s</a></div></div>'
                % (img, tag, title, text, link, ic("arrow")))

    # ============================================================= HOME
    hero = (
      '<section class="hero">'
      '<div class="hero__bg" style="background-image:url(%s)"></div><div class="hero__veil"></div>'
      '<div class="container">'
      '<span class="eyebrow reveal">Dubai · International Energy Trading</span>'
      '<h1 class="reveal d1">Powering Global Energy Trade</h1>'
      '<p class="lead reveal d2">Nexa Oil is a Dubai-based international energy trading company '
      'specializing in the supply of premium crude oil and industrial lubricants sourced from trusted '
      'Middle Eastern producers.</p>'
      '<div class="btn-row reveal d3">'
      '<a class="btn btn--gold" href="quote.html">Request a Quote %s</a>'
      '<a class="btn btn--ghost" href="products.html">View Products</a></div>'
      '<div class="hero-stats reveal d4">'
      '<div class="hero-stat"><div class="num"><span data-count="40" data-suffix="+">40+</span></div><div class="lbl">Countries Served</div></div>'
      '<div class="hero-stat"><div class="num"><span data-count="5">5</span></div><div class="lbl">Continents Reached</div></div>'
      '<div class="hero-stat"><div class="num"><span data-count="24" data-suffix="/7">24/7</span></div><div class="lbl">Trading Desk</div></div>'
      '<div class="hero-stat"><div class="num">UAE</div><div class="lbl">Strategic Ports</div></div>'
      '</div></div>'
      '<div class="scroll-cue"><span>Scroll</span><span class="mouse"></span></div>'
      '</section>'
    ) % (IMG["hero"], ic("arrow"))
    hero = hero.replace('<div class="scroll-cue">', g["oil_barrel"]() + '<div class="scroll-cue">')

    why = (
      '<section class="section"><div class="container">'
      '<div class="section-head text-center mw-720 mx-auto reveal">'
      '<span class="eyebrow eyebrow--center">Why Choose Us</span>'
      '<h2>A trading partner built on trust and reliability</h2>'
      '<p class="lead">We combine deep producer relationships in the Gulf with disciplined logistics to deliver '
      'energy products on time, on spec and on terms that work for your business.</p></div>'
      '<div class="grid g-3">'
      + card("supply","Reliable Supply Chain","Long-standing agreements with established Middle Eastern producers ensure consistent volume and quality, even in tight markets.")
      + card("globe","Global Reach","Active trading flows into Europe, Asia, Africa, North America and South America from a single, well-connected hub.")
      + card("logistics","Efficient Logistics","Direct access to UAE deep-water ports keeps lead times short and freight competitive across every major route.")
      + card("handshake","Trusted Partnerships","We invest in long-term relationships with suppliers and buyers, prioritising repeat business over one-off transactions.")
      + card("shield","Transparent Operations","Clear pricing, recognised Incoterms and full documentation give counterparties confidence at every stage of the trade.")
      + card("clock","Responsive Desk","A dedicated trading desk responds to enquiries within one business day, with pricing and availability you can act on.")
      + '</div></div></section>'
    )

    stat_strip = (
      '<section class="section--tight bg-navy"><div class="container">'
      '<div class="stat-strip">'
      '<div class="reveal"><div class="num"><span data-count="40" data-suffix="+">40+</span></div><div class="lbl">Countries served worldwide</div></div>'
      '<div class="reveal d1"><div class="num"><span data-count="6">6</span></div><div class="lbl">Lubricant product families</div></div>'
      '<div class="reveal d2"><div class="num"><span data-count="3">3</span></div><div class="lbl">Crude grades traded</div></div>'
      '<div class="reveal d3"><div class="num"><span data-count="100" data-suffix="%">100%</span></div><div class="lbl">Documented, compliant trades</div></div>'
      '</div></div></section>'
    )

    products_overview = (
      '<section class="section bg-soft"><div class="container">'
      '<div class="section-head text-center mw-720 mx-auto reveal">'
      '<span class="eyebrow eyebrow--center">Our Portfolio</span>'
      '<h2>Crude oil & industrial lubricants</h2>'
      '<p class="lead">From wellhead-grade crude to precision-engineered lubricants, we supply the energy products '
      'that keep refineries, fleets and heavy industry running.</p></div>'
      '<div class="grid g-3">'
      + prod(IMG["crude"],"Crude Oil","Light · Medium · Heavy Crude","Premium Middle Eastern crude oil supplied under FOB, CIF and CFR terms for refineries and the petrochemical industry.","crude-oil.html")
      + prod(IMG["engine"],"Lubricants","Engine & Hydraulic Oils","High-performance engine and hydraulic oils for automotive, industrial and machinery applications.","lubricants.html")
      + prod(IMG["marine"],"Lubricants","Marine Lubricants & Greases","Marine lubricants, gear and compressor oils and heavy-duty greases for shipping, offshore and industry.","lubricants.html")
      + '</div>'
      '<div class="text-center" style="margin-top:46px"><a class="btn btn--dark" href="products.html">Explore All Products %s</a></div>'
      '</div></section>'
    ) % ic("arrow")

    network = (
      '<section class="section bg-navy"><div class="container">'
      '<div class="section-head text-center mw-720 mx-auto reveal">'
      '<span class="eyebrow eyebrow--center">Global Supply Network</span>'
      '<h2>From Dubai to the world</h2>'
      '<p class="lead">Strategically positioned between East and West, the UAE gives us fast, flexible access to '
      'every major shipping lane and consuming market.</p></div>'
      + world_map() +
      '<div class="region-grid">'
      '<div class="region reveal"><div class="r-ico">🇪🇺</div><h4>Europe</h4><p>Rotterdam · Med ports</p></div>'
      '<div class="region reveal d1"><div class="r-ico">🌏</div><h4>Asia</h4><p>Singapore · China · India</p></div>'
      '<div class="region reveal d2"><div class="r-ico">🌍</div><h4>Africa</h4><p>West & East coasts</p></div>'
      '<div class="region reveal d3"><div class="r-ico">🌎</div><h4>North America</h4><p>US Gulf · Atlantic</p></div>'
      '<div class="region reveal d4"><div class="r-ico">🌴</div><h4>South America</h4><p>Brazil · Andean region</p></div>'
      '</div>'
      '<div class="text-center" style="margin-top:46px"><a class="btn btn--gold" href="global-network.html">See Our Network %s</a></div>'
      '</div></section>'
    ) % ic("arrow")

    trust = (
      '<section class="section--tight"><div class="container">'
      '<p class="text-center reveal" style="color:#8a96a4;letter-spacing:.16em;text-transform:uppercase;font-size:.78rem;margin-bottom:30px">'
      'Serving partners across the global energy value chain</p>'
      '<div class="trust reveal d1">'
      '<span>REFINERIES</span><span>SHIPPING LINES</span><span>OEM FLEETS</span>'
      '<span>DISTRIBUTORS</span><span>PETROCHEMICALS</span><span>INDUSTRIAL OEMs</span>'
      '</div></div></section>'
    )

    home_body = hero + why + stat_strip + products_overview + network + trust + cta_band()
    page("index.html",
         "International Energy Trading from Dubai",
         "Nexa Oil is a Dubai-based international energy trading company supplying premium crude oil and industrial lubricants worldwide under FOB, CIF and CFR terms.",
         home_body, "index.html", solid=False)

    # ============================================================= ABOUT
    about_body = (
      page_hero("About Nexa Oil","Trading energy the world relies on",
        "A Dubai-headquartered trader, broker and distributor connecting trusted Middle Eastern producers with buyers across five continents.",
        IMG["dubai"], "<span>About Us</span>")
      + '<section class="section"><div class="container"><div class="split">'
        '<div class="reveal"><span class="eyebrow">Who We Are</span>'
        '<h2>Rooted in the Gulf, active across the globe</h2>'
        '<p>Nexa Oil is an international energy trading company based in Dubai, United Arab Emirates. '
        'Operating as a trader, broker and distributor, we specialise in the worldwide supply of premium crude oil and '
        'a full range of high-performance industrial lubricants.</p>'
        '<p>Our position in the UAE — at the crossroads of European, Asian and African trade — allows us to move product '
        'efficiently from the region\'s most reliable producers to customers wherever they operate. We pair that '
        'geographic advantage with disciplined commercial practice, transparent documentation and a relationship-first '
        'approach that has made us a dependable partner in global markets.</p>'
        '<div class="btn-row" style="margin-top:24px"><a class="btn btn--dark" href="quote.html">Work With Us %s</a></div></div>'
        '<div class="split__media reveal d1" style="background-image:url(%s)">'
        '<div class="badge-float"><div class="num">Dubai, UAE</div><div class="lbl">Global trading headquarters</div></div></div>'
        '</div></div></section>' % (ic("arrow"), IMG["refinery"])
      + '<section class="section bg-soft"><div class="container">'
        '<div class="grid g-2" style="align-items:start">'
        '<div class="card reveal"><div class="ico">%s</div><h3>Our Mission</h3>'
        '<p>To deliver reliable, transparent and competitively-priced energy products to industries worldwide — '
        'building long-term value for suppliers and customers through trust, consistency and operational excellence.</p></div>'
        '<div class="card reveal d1"><div class="ico">%s</div><h3>Our Vision</h3>'
        '<p>To be recognised as a leading independent energy trading house out of the UAE, known for integrity, '
        'global reach and the dependability of every barrel and drum we move.</p></div>'
        '</div></div></section>' % (ic("bolt"), ic("globe"))
      + '<section class="section"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Our Values</span>'
        '<h2>The principles behind every trade</h2></div>'
        '<div class="feat-list grid g-2">'
        + feat("handshake","Integrity First","We honour our commitments. Clear terms, accurate documentation and straight dealing underpin every transaction.")
        + feat("shield","Reliability","Customers plan around our supply. We protect their continuity with secured volumes and proven logistics.")
        + feat("globe","Global Perspective","We think in trade lanes, not borders, matching the right product and price to the right market.")
        + feat("scale","Compliance","Trades are structured to meet international standards, sanctions screening and recognised quality benchmarks.")
        + '</div></div></section>'
      + '<section class="section--tight bg-navy"><div class="container"><div class="stat-strip">'
        '<div class="reveal"><div class="num"><span data-count="40" data-suffix="+">40+</span></div><div class="lbl">Destination markets</div></div>'
        '<div class="reveal d1"><div class="num"><span data-count="5">5</span></div><div class="lbl">Continents</div></div>'
        '<div class="reveal d2"><div class="num"><span data-count="9">9</span></div><div class="lbl">Product categories</div></div>'
        '<div class="reveal d3"><div class="num"><span data-count="24" data-suffix="/7">24/7</span></div><div class="lbl">Trading availability</div></div>'
        '</div></div></section>'
      + cta_band()
    )
    page("about.html","About Us",
         "Learn about Nexa Oil — a Dubai-based international energy trading company connecting trusted Middle Eastern producers with buyers across five continents.",
         about_body, "about.html")

    # ============================================================= PRODUCTS
    products_body = (
      page_hero("Our Products","Crude oil & industrial lubricants",
        "A focused portfolio of premium energy products, traded under recognised international terms and backed by reliable Gulf supply.",
        IMG["barrels"], "<span>Products</span>")
      + '<section class="section"><div class="container"><div class="split">'
        '<div class="split__media reveal" style="background-image:url(%s)">'
        '<div class="badge-float"><div class="num">FOB · CIF · CFR</div><div class="lbl">Flexible trade terms</div></div></div>'
        '<div class="reveal d1"><span class="eyebrow">Crude Oil</span><h2>Premium Middle Eastern crude</h2>'
        '<p>We trade light, medium and heavy crude oil sourced from established producers across the Gulf. '
        'Cargoes are supplied under FOB, CIF and CFR terms to refiners and the petrochemical industry worldwide.</p>'
        '<div class="terms"><div class="term"><div class="t">FOB</div><div class="d">Free On Board</div></div>'
        '<div class="term"><div class="t">CIF</div><div class="d">Cost, Insurance & Freight</div></div>'
        '<div class="term"><div class="t">CFR</div><div class="d">Cost & Freight</div></div></div>'
        '<div class="btn-row" style="margin-top:26px"><a class="btn btn--dark" href="crude-oil.html">Crude Oil Details %s</a></div></div>'
        '</div></div></section>' % (IMG["crude"], ic("arrow"))
      + '<section class="section bg-soft"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Industrial Lubricants</span>'
        '<h2>High-performance industrial solutions</h2>'
        '<p class="lead">A complete lubricants range engineered for automotive, marine, manufacturing and heavy-industry '
        'applications — available in bulk and packaged formats.</p></div>'
        '<div class="grid g-3">'
        + prod(IMG["engine"],"Engine Oils","Engine Oils","Automotive and industrial engine oils formulated for protection, efficiency and extended drain intervals.","lubricants.html")
        + prod(IMG["hydraulic"],"Hydraulic","Hydraulic Oils","Anti-wear hydraulic fluids for demanding machinery and precision hydraulic systems.","lubricants.html")
        + prod(IMG["gear"],"Gear Oils","Gear Oils","Extreme-pressure gear oils for heavy-duty industrial and mobile gear systems.","lubricants.html")
        + prod(IMG["compressor"],"Compressor","Compressor Oils","Thermally stable oils for rotary, reciprocating and screw compressors.","lubricants.html")
        + prod(IMG["marine"],"Marine","Marine Lubricants","Cylinder, system and trunk-piston oils for shipping and offshore fleets.","lubricants.html")
        + prod(IMG["grease"],"Greases","Greases","Lithium, calcium and specialty greases for heavy industrial equipment.","lubricants.html")
        + '</div></div></section>'
      + '<section class="section"><div class="container"><div class="section-head text-center mw-720 mx-auto reveal">'
        '<span class="eyebrow eyebrow--center">Supply Formats</span><h2>Bulk and packaged, your way</h2></div>'
        '<div class="grid g-4">'
        + card("ship","Bulk & Vessel","Full cargo lots and parcel shipments coordinated to your loading port and schedule.")
        + card("barrel","Drums","Standard 200/208-litre steel drums for distributors and industrial buyers.")
        + card("truck","IBCs & Totes","1,000-litre intermediate bulk containers for efficient handling and storage.")
        + card("doc","Custom Packaging","Private-label and bespoke pack sizes available on agreed volumes.")
        + '</div></div></section>'
      + cta_band()
    )
    page("products.html","Products",
         "Explore Nexa Oil's portfolio of premium crude oil and industrial lubricants — engine, hydraulic, gear, compressor and marine oils, plus greases — traded under FOB, CIF and CFR.",
         products_body, "products.html")

    # ============================================================= CRUDE OIL
    crude_body = (
      page_hero("Crude Oil","Premium Middle Eastern crude oil",
        "Light, medium and heavy grades supplied to refineries and the petrochemical industry under FOB, CIF and CFR terms.",
        IMG["rig"], '<a href="products.html">Products</a> <span>/</span> Crude Oil')
      + '<section class="section"><div class="container"><div class="split">'
        '<div class="reveal"><span class="eyebrow">Overview</span><h2>Reliable crude supply from the Gulf</h2>'
        '<p>Nexa Oil trades premium Middle Eastern crude oil drawn from established regional producers. '
        'Our cargoes feed refineries and petrochemical complexes that demand consistent quality, secure volume '
        'and dependable delivery.</p>'
        '<p>We structure every transaction around the buyer\'s preferred Incoterm — whether you load at origin (FOB) '
        'or require delivered freight and insurance (CIF / CFR) — and provide the full documentary set to support '
        'a smooth, compliant trade.</p>'
        '<div class="chips" style="margin-top:8px"><span class="chip">Refinery feedstock</span>'
        '<span class="chip">Petrochemical industry</span><span class="chip">Long-term contracts</span>'
        '<span class="chip">Spot cargoes</span></div></div>'
        '<div class="split__media reveal d1" style="background-image:url(%s)"></div>'
        '</div></div></section>' % IMG["refinery"]
      + '<section class="section bg-soft"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Grades</span>'
        '<h2>Grades we trade</h2></div><div class="grid g-3">'
        + card("drop","Light Crude","Low density and low sulphur. High yields of gasoline and naphtha — ideal for refineries optimised for transport fuels.")
        + card("drop","Medium Crude","Balanced density and sulphur content, offering a versatile yield profile across distillates and middle products.")
        + card("drop","Heavy Crude","Higher density grades suited to complex refineries and petrochemical feedstock, with strong middle-distillate potential.")
        + '</div></div></section>'
      + '<section class="section"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Indicative Specifications</span>'
        '<h2>Typical quality parameters</h2><p class="lead">Representative values — final specifications are confirmed per cargo and certificate of quality.</p></div>'
        '<div class="reveal d1"><table class="spec-table"><thead><tr><th>Parameter</th><th>Light</th><th>Medium</th><th>Heavy</th></tr></thead>'
        '<tbody>'
        '<tr><td>API Gravity</td><td>&gt; 34&deg;</td><td>26&ndash;34&deg;</td><td>&lt; 26&deg;</td></tr>'
        '<tr><td>Sulphur Content</td><td>&lt; 0.5%</td><td>0.5&ndash;1.5%</td><td>&gt; 1.5%</td></tr>'
        '<tr><td>Density @ 15&deg;C</td><td>~0.85 g/cm&sup3;</td><td>~0.89 g/cm&sup3;</td><td>~0.93 g/cm&sup3;</td></tr>'
        '<tr><td>Primary Use</td><td>Transport fuels</td><td>Mixed refining</td><td>Petrochemicals / fuel oil</td></tr>'
        '<tr><td>Incoterms</td><td>FOB / CIF / CFR</td><td>FOB / CIF / CFR</td><td>FOB / CIF / CFR</td></tr>'
        '</tbody></table></div></div></section>'
      + '<section class="section bg-navy"><div class="container"><div class="section-head text-center mw-720 mx-auto reveal">'
        '<span class="eyebrow eyebrow--center">Trade Terms</span><h2>How we contract</h2></div>'
        '<div class="grid g-3">'
        + feat("ship","FOB — Free On Board","Buyer nominates the vessel; we deliver cargo onboard at the loading port with title transferring at the ship\'s rail.")
        + feat("anchor","CIF — Cost, Insurance & Freight","We arrange and pay for carriage and marine insurance to the named destination port.")
        + feat("logistics","CFR — Cost & Freight","We arrange and pay for freight to the destination port; buyer covers insurance.")
        + '</div></div></section>'
      + cta_band()
    )
    page("crude-oil.html","Crude Oil",
         "Premium Middle Eastern crude oil — light, medium and heavy grades — supplied by Nexa Oil under FOB, CIF and CFR terms for refineries and petrochemicals.",
         crude_body, "crude-oil.html")

    # ============================================================= LUBRICANTS
    def lube_section(anchor, icon, title, text, img, points, rev=False):
        pts = "".join('<span class="chip">%s</span>' % p for p in points)
        media = '<div class="split__media reveal d1" style="background-image:url(%s)"></div>' % img
        txt = ('<div class="reveal"><span class="eyebrow">Industrial Lubricants</span><h2>%s</h2><p>%s</p>'
               '<div class="chips" style="margin-top:8px">%s</div></div>' % (title, text, pts))
        inner = (txt + media) if not rev else (media + txt)
        cls = "split split--rev" if rev else "split"
        return ('<section class="section%s" id="%s"><div class="container"><div class="%s">%s</div></div></section>'
                % (" bg-soft" if rev else "", anchor, cls, inner))

    lub_body = (
      page_hero("Industrial Lubricants","High-performance lubrication for industry",
        "Engine, hydraulic, gear, compressor and marine oils plus heavy-duty greases — engineered for reliability under load.",
        IMG["pipes"], '<a href="products.html">Products</a> <span>/</span> Industrial Lubricants')
      + '<section class="section--tight"><div class="container"><div class="chips reveal" style="justify-content:center">'
        '<a class="chip" href="#engine-oils">Engine Oils</a><a class="chip" href="#hydraulic-oils">Hydraulic Oils</a>'
        '<a class="chip" href="#gear-oils">Gear Oils</a><a class="chip" href="#compressor-oils">Compressor Oils</a>'
        '<a class="chip" href="#marine-lubricants">Marine Lubricants</a><a class="chip" href="#greases">Greases</a>'
        '</div></div></section>'
      + lube_section("engine-oils","engine","Engine Oils",
          "Premium engine oils for automotive and industrial engines, formulated to protect against wear, deposits and thermal breakdown while supporting fuel efficiency and extended drain intervals. Mineral, semi-synthetic and fully synthetic grades available.",
          IMG["engine"], ["Automotive engines","Industrial engines","Synthetic & mineral","Extended drain"])
      + lube_section("hydraulic-oils","wrench","Hydraulic Oils",
          "Anti-wear hydraulic fluids engineered for hydraulic machinery systems operating under high pressure and variable temperature. Excellent oxidation stability, water separation and filterability keep precision systems running cleanly.",
          IMG["hydraulic"], ["Anti-wear (AW)","High VI grades","Machinery systems","Long oil life"], rev=True)
      + lube_section("gear-oils","gear","Gear Oils",
          "Extreme-pressure gear oils for heavy-duty gear systems in industrial and mobile equipment. Superior load-carrying capacity and thermal stability protect gears and bearings against scuffing, pitting and micro-pitting.",
          IMG["gear"], ["EP additives","Industrial gearboxes","Heavy-duty","High torque"])
      + lube_section("compressor-oils","factory","Compressor Oils",
          "Thermally stable compressor oils for rotary, reciprocating and screw compressors. Low carbon-forming tendency and strong oxidation resistance extend service life and protect against deposits in demanding industrial compression duty.",
          IMG["compressor"], ["Rotary & screw","Reciprocating","Low deposits","Air & gas"], rev=True)
      + lube_section("marine-lubricants","anchor","Marine Lubricants",
          "A complete marine portfolio — cylinder oils, system oils and trunk-piston engine oils — for shipping and offshore fleets. Engineered for high-BN protection, deposit control and reliable performance on a range of marine fuels.",
          IMG["marine"], ["Cylinder oils","System oils","Trunk-piston","Offshore"])
      + lube_section("greases","barrel","Greases",
          "Lithium, calcium-complex and specialty greases for heavy industrial equipment. Excellent mechanical stability, water resistance and EP performance protect bearings and components across wide temperature ranges.",
          IMG["grease"], ["Lithium complex","Calcium complex","EP / high-temp","Water resistant"], rev=True)
      + cta_band()
    )
    page("lubricants.html","Industrial Lubricants",
         "Nexa Oil supplies high-performance industrial lubricants — engine, hydraulic, gear, compressor and marine oils, plus greases — for industry, marine and heavy equipment worldwide.",
         lub_body, "lubricants.html")

    # ============================================================= GLOBAL NETWORK
    gn_body = (
      page_hero("Global Supply Network","One hub. Every market.",
        "Based in Dubai and connected to the world's busiest trade lanes, we move energy products efficiently from supplier to customer.",
        IMG["port"], "<span>Global Supply Network</span>")
      + '<section class="section bg-navy"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Worldwide Distribution</span>'
        '<h2>Dubai at the centre of global trade</h2>'
        '<p class="lead">Our UAE base sits within easy reach of Europe, Asia, Africa and the Americas — '
        'shortening lead times and widening your options.</p></div>'
        + world_map() +
        '<div class="region-grid">'
        '<div class="region reveal"><div class="r-ico">🇪🇺</div><h4>Europe</h4><p>Rotterdam · ARA · Med</p></div>'
        '<div class="region reveal d1"><div class="r-ico">🌏</div><h4>Asia</h4><p>Singapore · China · India</p></div>'
        '<div class="region reveal d2"><div class="r-ico">🌍</div><h4>Africa</h4><p>West & East Africa</p></div>'
        '<div class="region reveal d3"><div class="r-ico">🌎</div><h4>North America</h4><p>US Gulf · Atlantic</p></div>'
        '<div class="region reveal d4"><div class="r-ico">🌴</div><h4>South America</h4><p>Brazil · Andean</p></div>'
        '</div></div></section>'
      + '<section class="section"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">How It Works</span>'
        '<h2>Supplier-to-customer flow</h2><p class="lead">A coordinated chain that keeps product moving and counterparties informed at every step.</p></div>'
        '<div class="steps">'
        '<div class="step reveal"><h4>Sourcing</h4><p>We secure product from trusted Middle Eastern producers under firm supply agreements.</p></div>'
        '<div class="step reveal d1"><h4>Contracting</h4><p>Terms, Incoterms, quality and quantity are agreed and documented with the buyer.</p></div>'
        '<div class="step reveal d2"><h4>Logistics</h4><p>Vessel nomination, inspection, insurance and port coordination are arranged through UAE hubs.</p></div>'
        '<div class="step reveal d3"><h4>Delivery</h4><p>Cargo is shipped, documents released, and product delivered on the agreed terms.</p></div>'
        '</div></div></section>'
      + '<section class="section bg-soft"><div class="container"><div class="grid g-3">'
        + card("logistics","Efficient Logistics Chain","Direct access to deep-water UAE ports and major carriers keeps freight competitive and schedules tight.")
        + card("ship","International Shipping","We coordinate vessel nomination, surveying and marine insurance across global routes.")
        + card("globe","Global Trading Routes","Established flows into five continents give buyers flexibility on origin, timing and delivery.")
        + '</div></div></section>'
      + cta_band()
    )
    page("global-network.html","Global Supply Network",
         "Discover Nexa Oil's global supply network — based in Dubai with efficient logistics and international shipping coordination to Europe, Asia, Africa and the Americas.",
         gn_body, "global-network.html")

    # ============================================================= INDUSTRIES
    industries = [
        ("factory","Oil & Gas","Feedstock, lubricants and fluids for upstream, midstream and downstream operations."),
        ("anchor","Marine & Shipping","Cylinder, system and trunk-piston oils plus greases for commercial fleets and offshore."),
        ("gear","Manufacturing","Hydraulic, gear and compressor oils that keep production lines reliable and efficient."),
        ("building","Construction","Robust lubricants and fuels for heavy plant, earthmoving and site machinery."),
        ("pickaxe","Mining","EP gear oils and greases engineered for extreme loads, dust and harsh environments."),
        ("truck","Logistics & Transport","Engine and driveline lubricants for fleets, ports and distribution operations."),
        ("bolt","Energy Sector","Crude feedstock and industrial fluids for power generation and energy infrastructure."),
        ("wrench","Heavy Industry","High-performance lubrication for steel, cement, processing and large rotating equipment."),
    ]
    ind_cards = "".join(
        '<div class="card reveal%s"><div class="ico">%s</div><h3>%s</h3><p>%s</p></div>'
        % (" d"+str(i%4) if i%4 else "", ic(icon), t, d) for i,(icon,t,d) in enumerate(industries))
    ind_body = (
      page_hero("Industries We Serve","Energy products for every demanding sector",
        "From refineries to mines, our crude and lubricants keep critical operations running across the global economy.",
        IMG["industry"], "<span>Industries</span>")
      + '<section class="section"><div class="container"><div class="grid g-4">' + ind_cards + '</div></div></section>'
      + '<section class="section bg-navy"><div class="container"><div class="split">'
        '<div class="reveal"><span class="eyebrow">Sector Expertise</span><h2>Matching product to application</h2>'
        '<p>Every industry places different demands on a lubricant or feedstock. Our team helps you select the right '
        'grade, specification and supply format for your operating conditions — then keeps it flowing reliably.</p>'
        '<div class="feat-list" style="margin-top:24px">'
        + feat("check","Application guidance","Grade and specification advice matched to your equipment and duty cycle.")
        + feat("check","Consistent supply","Secured volumes so production and fleets are never left waiting.")
        + feat("check","Global delivery","Bulk or packaged product delivered to your nearest convenient port.")
        + '</div></div>'
        '<div class="split__media reveal d1" style="background-image:url(%s)"></div>'
        '</div></div></section>' % IMG["pipes"]
      + cta_band()
    )
    page("industries.html","Industries We Serve",
         "Nexa Oil serves oil & gas, marine, manufacturing, construction, mining, logistics, energy and heavy industry with crude oil and industrial lubricants worldwide.",
         ind_body, "industries.html")

    # ============================================================= QUALITY
    q_body = (
      page_hero("Quality & Compliance","Standards you can trade on",
        "Documented quality, recognised specifications and disciplined compliance underpin every cargo and drum we supply.",
        IMG["lab"], "<span>Quality & Compliance</span>")
      + '<section class="section"><div class="container"><div class="grid g-3">'
        + card("shield","Quality Assurance","Products are supplied against recognised international specifications, with certificates of quality and analysis per cargo.")
        + card("scale","Regulatory Compliance","Trades are structured to meet international trade regulations, sanctions screening and KYC requirements.")
        + card("doc","Full Documentation","Complete documentary sets — Q&Q certificates, bills of lading, insurance and origin papers — support every transaction.")
        + card("leaf","Responsible Trading","We promote safe handling, correct storage guidance and environmentally responsible product stewardship.")
        + card("check","Independent Inspection","Cargoes can be surveyed by recognised third-party inspectors at load and discharge for added assurance.")
        + card("globe","International Standards","Lubricants are referenced to widely-recognised industry and OEM performance benchmarks.")
        + '</div></div></section>'
      + '<section class="section bg-soft"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">FAQ</span>'
        '<h2>Compliance, answered</h2></div>'
        '<div class="mw-820 mx-auto reveal d1">'
        + acc("What specifications do your products meet?",
              "Crude grades are supplied against agreed certificates of quality reflecting API gravity, sulphur and density parameters. Lubricants are referenced to recognised international and OEM performance standards, with technical data sheets available per product.")
        + acc("Which Incoterms do you trade under?",
              "We routinely contract under FOB, CIF and CFR. The appropriate term is agreed with each buyer depending on who arranges and pays for freight and insurance.")
        + acc("Do you provide independent inspection?",
              "Yes. Cargoes can be independently surveyed by recognised inspection companies at loading and discharge, with quantity and quality certificates issued accordingly.")
        + acc("How do you handle sanctions and KYC?",
              "Every counterparty is screened as part of our onboarding. We structure trades to comply with applicable international sanctions and trade-control regimes.")
        + acc("What documentation is included with a trade?",
              "Standard documentary sets include the commercial invoice, bill of lading, certificate of origin, certificates of quality and quantity, and insurance documents where applicable.")
        + '</div></div></section>'
      + cta_band()
    )
    page("quality.html","Quality & Compliance",
         "Nexa Oil upholds rigorous quality and compliance — recognised specifications, full documentation, independent inspection, sanctions screening and responsible trading.",
         q_body, "quality.html")

    # ============================================================= CATALOG
    cat_items = [
        ("doc","Crude Oil Programme","Grades, indicative specifications and trade terms for light, medium and heavy crude."),
        ("bolt","Engine Oils Range","Automotive and industrial engine oils with viscosity grades and performance levels."),
        ("wrench","Hydraulic Oils Range","Anti-wear and high-VI hydraulic fluids with technical parameters."),
        ("gear","Gear Oils Range","Extreme-pressure industrial and mobile gear oil specifications."),
        ("factory","Compressor Oils Range","Oils for rotary, screw and reciprocating compressors."),
        ("anchor","Marine Lubricants Range","Cylinder, system and trunk-piston oil portfolio for shipping."),
        ("barrel","Greases Range","Lithium, calcium-complex and specialty greases with NLGI grades."),
        ("ship","Packaging & Trade Terms","Bulk, drum and IBC formats with Incoterms and logistics notes."),
    ]
    cat_list = "".join(
        '<div class="cat-item reveal"><div class="cat-item__ico">%s</div>'
        '<div><h4>%s</h4><p>%s</p></div>'
        '<a class="btn btn--outline" href="quote.html">View %s</a></div>'
        % (ic(icon), t, d, ic("arrow")) for icon,t,d in cat_items)
    cat_body = (
      page_hero("Catalog","Product catalog & technical sheets",
        "Browse our product range online or download the full PDF catalog with specifications, packaging and trade conditions.",
        IMG["barrels"], "<span>Catalog</span>")
      + '<section class="section"><div class="container"><div class="split">'
        '<div class="reveal"><span class="eyebrow">Download</span><h2>The complete Nexa Oil catalog</h2>'
        '<p>Our PDF catalog brings together product descriptions, technical specifications, packaging information and '
        'trade conditions for our full crude oil and lubricants range — everything your procurement team needs in one place.</p>'
        '<ul class="feat-list" style="margin:24px 0">'
        + feat("check","Technical specifications","Key parameters and performance levels for each product line.")
        + feat("check","Packaging information","Bulk, drum and IBC formats and pack sizes.")
        + feat("check","Trade conditions","Incoterms, lead times and supply terms at a glance.")
        + '</ul>'
        '<div class="btn-row"><a class="btn btn--gold" href="#sheets">Download PDF Catalog %s</a>'
        '<a class="btn btn--outline" href="quote.html">Request Pricing</a></div>'
        '<p class="form-note">PDF download and individual product data sheets are issued on request to verified business enquiries.</p></div>'
        '<div class="split__media reveal d1" style="background-image:url(%s)">'
        '<div class="badge-float"><div class="num">9 Lines</div><div class="lbl">Crude + lubricants portfolio</div></div></div>'
        '</div></div></section>' % (ic("download"), IMG["lab"])
      + '<section class="section bg-soft" id="sheets"><div class="container">'
        '<div class="section-head text-center mw-720 mx-auto reveal"><span class="eyebrow eyebrow--center">Online Product Sheets</span>'
        '<h2>Browse by product line</h2></div>'
        '<div class="grid" style="gap:18px">' + cat_list + '</div></div></section>'
      + cta_band()
    )
    page("catalog.html","Catalog",
         "Download the Nexa Oil PDF catalog or browse online product sheets — technical specifications, packaging information and trade conditions for crude oil and lubricants.",
         cat_body, "catalog.html")

    # ============================================================= NEWS
    news = [
        (IMG["news1"],"Market Update","Gulf crude differentials firm as Asian demand recovers",
         "Refining margins in Asia strengthened through the quarter, lifting demand for Middle Eastern medium and heavy grades and tightening prompt availability."),
        (IMG["news2"],"Company News","Nexa Oil expands lubricants distribution into West Africa",
         "New distributor agreements extend our marine and industrial lubricants reach across key West African ports, shortening lead times for regional buyers."),
        (IMG["news3"],"Logistics","UAE port throughput supports faster turnaround on parcel cargoes",
         "Continued investment in UAE terminal capacity is helping traders compress loading windows and improve schedule reliability on smaller parcels."),
    ]
    news_cards = "".join(
        '<article class="news-card reveal%s"><div class="news-card__img" style="background-image:url(%s)"></div>'
        '<div class="news-card__body"><div class="news-meta"><span class="cat">%s</span><span>Jun 2026</span></div>'
        '<h3>%s</h3><p>%s</p><a class="prod__link" href="#">Read more %s</a></div></article>'
        % (" d"+str(i+1) if i else "", img, cat, t, d, ic("arrow")) for i,(img,cat,t,d) in enumerate(news))
    news_body = (
      page_hero("News & Market Updates","Insight from the trading desk",
        "Market commentary, company news and logistics updates from across our global energy trading operations.",
        IMG["refinery"], "<span>News & Market Updates</span>")
      + '<section class="section"><div class="container"><div class="grid g-3">' + news_cards + '</div></div></section>'
      + '<section class="section bg-navy"><div class="container"><div class="split">'
        '<div class="reveal"><span class="eyebrow">Stay Informed</span><h2>Market updates in your inbox</h2>'
        '<p class="lead">Subscribe for periodic crude and lubricants market commentary and Nexa Oil announcements.</p>'
        '<form class="btn-row" data-mock style="margin-top:10px;gap:12px;max-width:520px">'
        '<input type="email" required placeholder="Your business email" '
        'style="flex:1;min-width:220px;padding:14px 16px;border-radius:8px;border:1.5px solid rgba(255,255,255,.2);background:rgba(255,255,255,.06);color:#fff">'
        '<button class="btn btn--gold" type="submit">Subscribe</button>'
        '<div class="form-success">Thank you — you\'re subscribed to Nexa Oil market updates.</div></form></div>'
        '<div class="split__media reveal d1" style="background-image:url(%s)"></div>'
        '</div></div></section>'
    ) % IMG["barrels"]
    news_body += cta_band()
    page("news.html","News & Market Updates",
         "Nexa Oil news and market updates — crude oil and lubricants market commentary, company announcements and logistics insight from our Dubai trading desk.",
         news_body, "news.html")

    # ============================================================= QUOTE
    products_opts = ["Light Crude Oil","Medium Crude Oil","Heavy Crude Oil","Engine Oils","Hydraulic Oils",
                     "Gear Oils","Compressor Oils","Marine Lubricants","Greases","Other / Mixed"]
    opts = "".join('<option>%s</option>' % o for o in products_opts)
    quote_body = (
      page_hero("Request a Quote","Tell us what you need",
        "Share your requirement and our trading desk will respond within one business day with pricing, availability and delivery terms.",
        IMG["port"], "<span>Request a Quote</span>")
      + '<section class="section"><div class="container"><div class="split" style="gap:48px;align-items:start">'
        '<div class="reveal" style="position:sticky;top:100px">'
        '<span class="eyebrow">Why request from us</span><h2>A clear, fast quotation</h2>'
        '<ul class="feat-list" style="margin-top:22px">'
        + feat("clock","One-day response","Our desk replies to qualified enquiries within one business day.")
        + feat("scale","Recognised terms","Pricing on FOB, CIF or CFR with transparent, documented conditions.")
        + feat("ship","Flexible logistics","Bulk or packaged supply delivered to your preferred port.")
        + feat("shield","Confidential","Your enquiry is handled discreetly by our commercial team.")
        + '</ul>'
        '<div class="info-card" style="margin-top:30px"><div class="ico">%s</div><div><h4>Prefer to email?</h4>'
        '<p><a href="mailto:sales@nexaoiltrading.com">sales@nexaoiltrading.com</a></p></div></div></div>'
        '<div class="form-card reveal d1">'
        '<div class="form-success">Thank you — your quotation request has been received. Our trading desk will contact you within one business day.</div>'
        '<form data-mock><div class="form-grid">'
        '<div class="field"><label>Company Name <span class="req">*</span></label><input required placeholder="Your company"></div>'
        '<div class="field"><label>Contact Person <span class="req">*</span></label><input required placeholder="Full name"></div>'
        '<div class="field"><label>Email <span class="req">*</span></label><input type="email" required placeholder="you@company.com"></div>'
        '<div class="field"><label>Phone</label><input type="tel" placeholder="+971 ..."></div>'
        '<div class="field"><label>Country <span class="req">*</span></label><input required placeholder="Destination country"></div>'
        '<div class="field"><label>Product Selection <span class="req">*</span></label><select required>%s</select></div>'
        '<div class="field"><label>Required Quantity</label><input placeholder="e.g. 50,000 MT / 200 drums"></div>'
        '<div class="field"><label>Delivery Port</label><input placeholder="Discharge / loading port"></div>'
        '<div class="field full"><label>Preferred Incoterm</label><select><option>FOB — Free On Board</option>'
        '<option>CIF — Cost, Insurance & Freight</option><option>CFR — Cost & Freight</option><option>To be advised</option></select></div>'
        '<div class="field full"><label>Message</label><textarea placeholder="Specifications, timelines or any other details..."></textarea></div>'
        '</div><div style="margin-top:24px"><button class="btn btn--gold" type="submit">Submit Request %s</button></div>'
        '<p class="form-note">By submitting you agree to be contacted by Nexa Oil regarding your enquiry. '
        'This is a demonstration form — no live submission is sent.</p>'
        '</form></div></div></div></section>'
    ) % (ic("mail"), opts, ic("arrow"))
    page("quote.html","Request a Quote",
         "Request a quotation from Nexa Oil for crude oil or industrial lubricants. Provide your product, quantity, delivery port and preferred Incoterm — reply within one business day.",
         quote_body, "quote.html")

    # ============================================================= CONTACT
    contact_body = (
      page_hero("Contact","Let's start a conversation",
        "Reach our Dubai trading desk for pricing, partnerships or general enquiries — we respond promptly to every qualified message.",
        IMG["dubai"], "<span>Contact</span>")
      + '<section class="section"><div class="container"><div class="grid g-3" style="margin-bottom:48px">'
        '<div class="info-card reveal"><div class="ico">%s</div><div><h4>Head Office</h4>'
        '<p>Nexa Oil<br>Dubai, United Arab Emirates</p></div></div>'
        '<div class="info-card reveal d1"><div class="ico">%s</div><div><h4>Email</h4>'
        '<p><a href="mailto:sales@nexaoiltrading.com">sales@nexaoiltrading.com</a></p></div></div>'
        '<div class="info-card reveal d2"><div class="ico">%s</div><div><h4>Trading Hours</h4>'
        '<p>Sunday – Friday<br>09:00 – 18:00 GST</p></div></div>'
        '</div>'
        '<div class="split" style="gap:48px;align-items:start">'
        '<div class="form-card reveal">'
        '<div class="form-success">Thank you for reaching out — a member of our team will reply shortly.</div>'
        '<h3 style="margin-bottom:6px">Send us a message</h3>'
        '<p style="color:#5c6775;margin-bottom:24px;font-size:.95rem">Fields marked <span style="color:#c0392b">*</span> are required.</p>'
        '<form data-mock><div class="form-grid">'
        '<div class="field"><label>Name <span class="req">*</span></label><input required placeholder="Your name"></div>'
        '<div class="field"><label>Company</label><input placeholder="Company name"></div>'
        '<div class="field"><label>Email <span class="req">*</span></label><input type="email" required placeholder="you@company.com"></div>'
        '<div class="field"><label>Phone</label><input type="tel" placeholder="+971 ..."></div>'
        '<div class="field full"><label>Message <span class="req">*</span></label><textarea required placeholder="How can we help?"></textarea></div>'
        '</div><div style="margin-top:22px"><button class="btn btn--gold" type="submit">Send Message %s</button></div></form></div>'
        '<div class="reveal d1"><span class="eyebrow">Dubai, UAE</span><h2>Strategically located for global trade</h2>'
        '<p>Our position in Dubai places us within reach of the world\'s most important shipping lanes and consuming '
        'markets. Whether you are a refiner, distributor, shipping line or industrial buyer, our desk is ready to help.</p>'
        '<div class="map-wrap" style="padding:0;margin-top:24px;min-height:300px;background-image:linear-gradient(120deg,rgba(10,10,12,.4),rgba(10,10,12,.15)),url(%s);background-size:cover;background-position:center;border-radius:14px"></div>'
        '<div class="grid g-2" style="margin-top:24px;gap:16px">'
        + feat("mail","General & Sales","sales@nexaoiltrading.com")
        + feat("pin","Visit","Dubai, United Arab Emirates")
        + '</div></div>'
        '</div></div></section>'
    ) % (ic("pin"), ic("mail"), ic("clock"), ic("arrow"), IMG["dubai"])
    page("contact.html","Contact",
         "Contact Nexa Oil in Dubai, United Arab Emirates. Email sales@nexaoiltrading.com for crude oil and industrial lubricant enquiries, quotes and partnerships.",
         contact_body, "contact.html")

# accordion helper (module-level so closures above can use via name)
def acc(q, a):
    return ('<div class="acc-item"><button class="acc-head">%s<span class="pm">+</span></button>'
            '<div class="acc-body"><p>%s</p></div></div>' % (q, a))
