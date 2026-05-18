from pathlib import Path

# Use relative path so it runs flawlessly on any platform (Windows, macOS, Linux)
root = Path('.')

products = [
    {
        'name': 'Burberry Hero',
        'brand': 'Burberry',
        'cat': 'Men',
        'img1': 'images-new/burberry-hero-main.png',
        'img2': 'images-new/burberry-hero-alt.png',
        'price': 'QAR 299',
        'desc': 'Woody aromatic fragrance with a premium modern mood.',
        'badge': 'Best Seller'
    },
    {
        'name': 'Lancôme La Vie Est Belle',
        'brand': 'Lancôme',
        'cat': 'Women',
        'img1': 'images-new/lancome-main.png',
        'img2': 'images-new/lancome-alt.png',
        'price': 'QAR 349',
        'desc': 'Elegant floral sweet fragrance made for signature occasions.',
        'badge': 'New Arrival'
    },
    {
        'name': 'Lattafa Asad',
        'brand': 'Lattafa',
        'cat': 'Arabic',
        'img1': 'images-new/lataffa-asad-main.png',
        'img2': 'images-new/lataffa-asad-alt.png',
        'price': 'QAR 129',
        'desc': 'Bold oriental fragrance with warm spice and long-lasting depth.',
        'badge': 'Arabic Oud'
    },
    {
        'name': 'Armaf Club de Nuit Intense',
        'brand': 'Armaf',
        'cat': 'Men',
        'img1': 'assets/images/armaf-club.webp',
        'img2': 'assets/images/mens-collection.webp',
        'price': 'QAR 189',
        'desc': 'Strong, classy and confident scent for daily and evening wear.',
        'badge': 'Best Seller'
    },
    {
        'name': 'Afnan 9PM',
        'brand': 'Afnan',
        'cat': 'Men',
        'img1': 'assets/images/afnan-9pm.webp',
        'img2': 'images-new/men-category-banner.png',
        'price': 'QAR 159',
        'desc': 'Modern evening fragrance with a sweet, powerful trail.',
        'badge': 'New Arrival'
    },
    {
        'name': 'Guerlain Inspired Selection',
        'brand': 'Guerlain',
        'cat': 'Women',
        'img1': 'assets/images/gift-sets.webp',
        'img2': 'images-new/giftset-category-banner.png',
        'price': 'QAR 399',
        'desc': 'Luxury floral-amber profile with premium bottle presentation.',
        'badge': 'Gift Pick'
    },
    {
        'name': 'French Avenue Oud',
        'brand': 'French Avenue',
        'cat': 'Arabic',
        'img1': 'assets/images/arabic-collection.webp',
        'img2': 'images-new/arabic-category-banner.png',
        'price': 'QAR 169',
        'desc': 'Rich oud, musk and amber notes for a strong Arabic identity.',
        'badge': 'Arabic Oud'
    },
    {
        'name': 'Paris Corner Emirene',
        'brand': 'Paris Corner',
        'cat': 'Women',
        'img1': 'assets/images/womens-collection.webp',
        'img2': 'images-new/women-category-banner.png',
        'price': 'QAR 149',
        'desc': 'Soft elegant scent with a feminine premium finish.',
        'badge': 'New Arrival'
    }
]

nav = '''<div class="topbar"><div class="container"><span>Qatar online perfume store • Premium brands • WhatsApp ordering</span><span>Call / WhatsApp: +974 7776 3375</span></div></div>
<header class="nav"><div class="container"><a class="brand" href="index.html"><span class="mark">D</span><span><b>DEN TIMES</b><small>ONLINE STORE</small></span></a><nav class="links"><a href="index.html">Home</a><a href="shop.html">Shop</a><a href="brands.html">Brands</a><a href="offers.html">Offers</a><a href="about.html">About</a><a href="contact.html">Contact</a><a class="btn" href="https://wa.me/97477763375?text=Hi%20DEN%20TIMES%2C%20I%20want%20to%20order%20perfume">Order on WhatsApp</a></nav><button class="icon-btn menu" aria-label="Open menu">☰</button></div></header>'''

drawer = '''<div class="drawer"><div class="drawer-panel"><button class="icon-btn close-drawer" aria-label="Close">×</button><a href="index.html">Home</a><a href="shop.html">Shop</a><a href="brands.html">Brands</a><a href="offers.html">Offers</a><a href="about.html">About</a><a href="contact.html">Contact</a><a class="btn" href="https://wa.me/97477763375?text=Hi%20DEN%20TIMES%2C%20I%20want%20to%20order%20perfume">WhatsApp Order</a></div></div>
<nav class="bottom-nav"><a href="index.html">Home</a><a href="shop.html">Shop</a><a href="brands.html">Brands</a><a href="offers.html">Offers</a></nav><a class="wa-float" href="https://wa.me/97477763375?text=Hi%20DEN%20TIMES%2C%20I%20want%20to%20order%20perfume">WhatsApp</a>'''

footer = '''<footer class="footer"><div class="container footer-grid"><div class="reveal reveal-slide-up"><h4>DEN TIMES</h4><a class="brand" href="index.html"><span class="mark" style="margin-bottom: 12px">D</span><span><b>DEN TIMES</b><small>ONLINE STORE</small></span></a><p style="color:var(--muted);line-height:1.7;margin-top:10px;">Premium perfumes, designer fragrances, Arabic perfumes, gift sets and WhatsApp ordering in Qatar.</p></div><div class="reveal reveal-slide-up delay-100"><h4>Shop Categories</h4><a href="shop.html">All Perfumes</a><a href="shop.html#men">Men's Perfumes</a><a href="shop.html#women">Women's Perfumes</a><a href="offers.html">Gift Sets</a></div><div class="reveal reveal-slide-up delay-200"><h4>Top Brands</h4><a href="brands.html">Lacoste</a><a href="brands.html">Burberry</a><a href="brands.html">Lattafa</a><a href="brands.html">Afnan</a></div><div class="reveal reveal-slide-up delay-300"><h4>Customer Support</h4><a href="tel:+97477763375">+974 7776 3375</a><a href="https://wa.me/97477763375">WhatsApp Chat</a><a href="contact.html">Enquiry Form</a></div></div></footer>'''

head = lambda title: f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | DEN TIMES Online Store</title><meta name="description" content="DEN TIMES Online Store Qatar - premium perfumes, luxury fragrance brands and Arabic perfumes."><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&display=swap" rel="stylesheet"><link rel="stylesheet" href="assets/css/style.css"></head><body>{nav}'''

end = f'''{footer}{drawer}<script type="module" src="assets/js/main.js"></script></body></html>'''


def product_cards(limit=None):
    items = products[:limit] if limit else products
    s = ''
    for p in items:
        s += f'''<article class="product reveal reveal-slide-up" data-cat="{p['cat'].lower()}" data-brand="{p['brand'].lower()}">
      <a class="img" href="#">
        <span class="card-badge">{p['badge']}</span>
        <img class="product-img-main" loading="lazy" src="{p['img1']}" alt="{p['name']}">
        <img class="product-img-hover" loading="lazy" src="{p['img2']}" alt="{p['name']}">
      </a>
      <div class="product-body">
        <span class="tag">{p['brand']} • {p['cat']}</span>
        <h3 class="serif">{p['name']}</h3>
        <p>{p['desc']}</p>
        <div class="price">
          <b>{p['price']}</b>
          <a class="small-btn" data-wa="{p['name']}" href="#">Enquire</a>
        </div>
      </div>
    </article>'''
    return s


# index.html
index = head('Home') + f'''
<main>
  <section class="hero">
    <div class="container hero-grid">
      <div class="hero-content reveal reveal-slide-up">
        <span class="eyebrow">Premium Perfumes in Qatar</span>
        <h1 class="serif">Luxury scents,<br><span style="color: var(--gold-light); font-style: italic;">delivered with style.</span></h1>
        <p>DEN TIMES Online Store brings designer-inspired, Arabic, men’s, women’s and gift-set perfumes together in a polished online shopping experience with fast WhatsApp ordering.</p>
        <div class="hero-actions">
          <a class="btn" href="shop.html">Explore Collection</a>
          <a class="btn secondary" href="https://wa.me/97477763375?text=Hi%20DEN%20TIMES%2C%20show%20me%20your%20latest%20perfumes">Ask on WhatsApp</a>
        </div>
        <div class="hero-pills">
          <span class="pill">Lacoste</span>
          <span class="pill">Burberry</span>
          <span class="pill">Guerlain</span>
          <span class="pill">Lancôme</span>
          <span class="pill">Lattafa</span>
          <span class="pill">Armaf</span>
          <span class="pill">Afnan</span>
        </div>
      </div>
      <aside class="floating-card reveal reveal-slide-left delay-200">
        <span class="eyebrow">Store Highlights</span>
        <b>Authentic feel. Premium presentation. Simple ordering.</b>
        <div class="stats">
          <div class="stat"><strong>10+</strong><small>Brands</small></div>
          <div class="stat"><strong>24/7</strong><small>WhatsApp</small></div>
          <div class="stat"><strong>Qatar</strong><small>Orders</small></div>
        </div>
      </aside>
    </div>
  </section>

  <div class="marquee">
    <div class="marquee-track">
      <span>Lacoste • Burberry • Guerlain • Lancôme • Lattafa • Armaf • Afnan • French Avenue • Paris Corner • Assaf • </span>
      <span>Lacoste • Burberry • Guerlain • Lancôme • Lattafa • Armaf • Afnan • French Avenue • Paris Corner • Assaf • </span>
    </div>
  </div>

  <section class="section">
    <div class="container">
      <div class="section-head reveal reveal-slide-up">
        <h2 class="serif">Shop by collection</h2>
        <p>Use strong lifestyle visuals for each category so customers understand the product range immediately on mobile.</p>
      </div>
      <div class="grid category-grid">
        <a class="cat reveal reveal-slide-up" href="shop.html">
          <img src="images-new/men-category-banner.png" alt="Men's Perfumes">
          <div>
            <h3>Men's Perfumes</h3>
            <p>Fresh • Woody • Signature</p>
          </div>
        </a>
        <a class="cat reveal reveal-slide-up" href="shop.html">
          <img src="images-new/women-category-banner.png" alt="Women's Perfumes">
          <div>
            <h3>Women's Perfumes</h3>
            <p>Floral • Sweet • Elegant</p>
          </div>
        </a>
        <a class="cat reveal reveal-slide-up" href="shop.html">
          <img src="images-new/arabic-category-banner.png" alt="Arabic Perfumes">
          <div>
            <h3>Arabic Perfumes</h3>
            <p>Oud • Musk • Long lasting</p>
          </div>
        </a>
        <a class="cat reveal reveal-slide-up" href="offers.html">
          <img src="images-new/giftset-category-banner.png" alt="Gift Sets">
          <div>
            <h3>Gift Sets</h3>
            <p>Perfect for occasions</p>
          </div>
        </a>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top: 0;">
    <div class="container">
      <div class="banner reveal reveal-scale-in" style="background-image:url('assets/images/brand-lineup.webp')">
        <div class="banner-content">
          <span class="eyebrow" style="color: var(--gold-light);">Featured Brands</span>
          <h2 class="serif" style="color: var(--color-ivory);">Premium names customers already trust.</h2>
          <p>Showcase Lacoste, Burberry, Guerlain, Lancôme, Lattafa, Armaf, Afnan, French Avenue, Paris Corner and Assaf in one clean shopping flow.</p>
          <a class="btn" href="brands.html">View Brands</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top: 0;">
    <div class="container">
      <div class="section-head reveal reveal-slide-up">
        <h2 class="serif">Popular perfumes</h2>
        <p>Product cards designed for quick WhatsApp enquiries, mobile browsing and paid ad traffic. Click on any card for a luxury close-up view.</p>
      </div>
      <div class="filterbar reveal reveal-slide-up">
        <button class="chip active" data-filter="all">All Perfumes</button>
        <button class="chip" data-filter="men">Men's Scents</button>
        <button class="chip" data-filter="women">Women's Scents</button>
        <button class="chip" data-filter="arabic">Arabic Oud</button>
      </div>
      <div class="grid products">
        {product_cards()}
      </div>
    </div>
  </section>

  <section class="section" style="padding-top: 0;">
    <div class="container split">
      <div class="panel reveal reveal-slide-right">
        <span class="eyebrow">Why DEN TIMES</span>
        <h2 class="serif">A perfume store built for mobile buyers.</h2>
        <p>The layout is designed for fast browsing, strong luxury impression, easy enquiry and simple WhatsApp conversion.</p>
        <div class="feature-list">
          <div class="feature">
            <span>✓</span>
            <div>
              <b>Premium quality visual style</b>
              <small>Black, gold and marble-inspired luxury design.</small>
            </div>
          </div>
          <div class="feature">
            <span>✓</span>
            <div>
              <b>WhatsApp-first ordering</b>
              <small>Every product can lead directly to customer enquiry.</small>
            </div>
          </div>
          <div class="feature">
            <span>✓</span>
            <div>
              <b>Brand-focused structure</b>
              <small>Easy navigation by brand, category and offer.</small>
            </div>
          </div>
        </div>
      </div>
      <div class="image-card reveal reveal-slide-left">
        <img src="assets/images/authentic-banner.webp" alt="100% Authentic Fragrances">
      </div>
    </div>
  </section>
</main>
''' + end
(root / 'index.html').write_text(index, encoding='utf-8')

# shop.html
shop = head('Shop') + f'''
<main>
  <section class="page-hero">
    <div class="container reveal reveal-slide-up">
      <span class="breadcrumb">Home / Shop</span>
      <h1 class="serif">Shop Perfumes</h1>
      <p>Browse premium men’s perfumes, women’s perfumes, Arabic fragrances and gift-ready selections. Product names and prices can be edited easily.</p>
    </div>
  </section>
  <section class="section" style="padding-top: 20px;">
    <div class="container">
      <div class="filterbar reveal reveal-slide-up">
        <button class="chip active" data-filter="all">All Products</button>
        <button class="chip" data-filter="men">Men</button>
        <button class="chip" data-filter="women">Women</button>
        <button class="chip" data-filter="arabic">Arabic</button>
        <button class="chip" data-filter="lattafa">Lattafa</button>
        <button class="chip" data-filter="armaf">Armaf</button>
        <button class="chip" data-filter="afnan">Afnan</button>
      </div>
      <div class="grid products">
        {product_cards()}
      </div>
    </div>
  </section>
</main>
''' + end
(root / 'shop.html').write_text(shop, encoding='utf-8')

# brands.html
brands = head('Brands') + '''
<main>
  <section class="page-hero">
    <div class="container reveal reveal-slide-up">
      <span class="breadcrumb">Home / Brands</span>
      <h1 class="serif">Featured Brands</h1>
      <p>Dedicated page for perfume brand discovery. Use this for SEO and to help customers quickly identify the brands available.</p>
    </div>
  </section>
  <section class="section" style="padding-top: 20px;">
    <div class="container">
      <div class="banner reveal reveal-scale-in" style="background-image:url('assets/images/brand-lineup.webp')">
        <div class="banner-content">
          <span class="eyebrow" style="color: var(--gold-light);">Brand Collection</span>
          <h2 class="serif" style="color: var(--color-ivory);">Designer, Arabic and premium perfume selections.</h2>
          <p>Keep the brand list visible and allow future linking to individual brand pages.</p>
        </div>
      </div>
    </div>
  </section>
  <section class="section" style="padding-top: 0;">
    <div class="container">
      <div class="grid brands-grid">
        <div class="brand-tile reveal reveal-scale-in">Lacoste</div>
        <div class="brand-tile reveal reveal-scale-in delay-100">Burberry</div>
        <div class="brand-tile reveal reveal-scale-in delay-200">Guerlain</div>
        <div class="brand-tile reveal reveal-scale-in delay-300">Lancôme</div>
        <div class="brand-tile reveal reveal-scale-in delay-400">Lattafa</div>
        <div class="brand-tile reveal reveal-scale-in">Armaf</div>
        <div class="brand-tile reveal reveal-scale-in delay-100">Afnan</div>
        <div class="brand-tile reveal reveal-scale-in delay-200">French Avenue</div>
        <div class="brand-tile reveal reveal-scale-in delay-300">Paris Corner</div>
        <div class="brand-tile reveal reveal-scale-in delay-400">Assaf</div>
      </div>
    </div>
  </section>
</main>
''' + end
(root / 'brands.html').write_text(brands, encoding='utf-8')

# offers.html
offers = head('Offers') + f'''
<main>
  <section class="page-hero">
    <div class="container reveal reveal-slide-up">
      <span class="breadcrumb">Home / Offers</span>
      <h1 class="serif">Gift Sets & Combos</h1>
      <p>Dedicated offer page for gift boxes, combos, new arrivals and seasonal fragrance bundles.</p>
    </div>
  </section>
  <section class="section" style="padding-top: 20px;">
    <div class="container">
      <div class="banner reveal reveal-scale-in" style="background-image:url('images-new/giftset-category-banner.png')">
        <div class="banner-content">
          <span class="eyebrow" style="color: var(--gold-light);">Perfect Gift</span>
          <h2 class="serif" style="color: var(--color-ivory);">Luxury fragrance sets for every occasion.</h2>
          <p>Create special combo pricing, Eid offers, birthday gifts and corporate gift bundles here.</p>
          <a class="btn" href="https://wa.me/97477763375?text=Hello%20DEN%20TIMES%2C%20I%20am%20interested%20in%20your%20Gift%20Sets%20and%20Combos.%20Please%20share%20availability%20and%20best%20price.">Ask for Combos</a>
        </div>
      </div>
    </div>
  </section>
  <section class="section" style="padding-top: 0;">
    <div class="container">
      <div class="section-head reveal reveal-slide-up">
        <h2 class="serif">Exclusive Combo Selection</h2>
        <p>Premium options pre-selected for quick order and delivery.</p>
      </div>
      <div class="grid products">
        {product_cards(4)}
      </div>
    </div>
  </section>
</main>
''' + end
(root / 'offers.html').write_text(offers, encoding='utf-8')

# about.html
about = head('About') + '''
<main>
  <section class="page-hero">
    <div class="container reveal reveal-slide-up">
      <span class="breadcrumb">Home / About</span>
      <h1 class="serif">About DEN TIMES</h1>
      <p>DEN TIMES Online Store is a perfume-focused e-commerce concept for Qatar, built around premium presentation, trusted brands and easy WhatsApp ordering.</p>
    </div>
  </section>
  <section class="section" style="padding-top: 20px;">
    <div class="container split">
      <div class="panel reveal reveal-slide-right">
        <span class="eyebrow">Our Focus</span>
        <h2 class="serif">Perfumes presented like a luxury boutique.</h2>
        <p>The website is designed to feel premium from the first scroll. It combines strong visuals, brand sections, category browsing and WhatsApp enquiry buttons to convert visitors into buyers.</p>
        <ul>
          <li>Designer and premium fragrance range</li>
          <li>Arabic oud, musk and long-lasting perfumes</li>
          <li>Gift-ready combos and special occasion sets</li>
          <li>Mobile-first browsing and fast enquiry</li>
        </ul>
      </div>
      <div class="image-card reveal reveal-slide-left">
        <img src="assets/images/new-arrivals.webp" alt="New Arrivals">
      </div>
    </div>
  </section>
</main>
''' + end
(root / 'about.html').write_text(about, encoding='utf-8')

# contact.html
contact = head('Contact') + '''
<main>
  <section class="page-hero">
    <div class="container reveal reveal-slide-up">
      <span class="breadcrumb">Home / Contact</span>
      <h1 class="serif">Contact & Order</h1>
      <p>Use this page for WhatsApp enquiries, product requests, delivery questions and customer support.</p>
    </div>
  </section>
  <section class="section" style="padding-top: 20px;">
    <div class="container contact-grid">
      <div class="panel reveal reveal-slide-right">
        <span class="eyebrow">WhatsApp Ordering</span>
        <h2 class="serif">Tell us what perfume you need.</h2>
        <p>Customers can send their preferred brand, budget and occasion. The store team can reply with product availability and price.</p>
        <div class="feature-list">
          <div class="feature">
            <span>☎</span>
            <div>
              <b>Phone / WhatsApp</b>
              <small>+974 7776 3375</small>
            </div>
          </div>
          <div class="feature">
            <span>⌁</span>
            <div>
              <b>Recommended enquiry</b>
              <small>Brand name, perfume type, quantity and delivery location.</small>
            </div>
          </div>
        </div>
        <br>
        <a class="btn" href="https://wa.me/97477763375?text=Hi%20DEN%20TIMES%2C%20I%20want%20to%20order%20perfume">Open WhatsApp</a>
      </div>
      <form class="panel form reveal reveal-slide-left" onsubmit="return false;">
        <input placeholder="Your name" required>
        <input placeholder="Mobile number" required>
        <select>
          <option>Product interest</option>
          <option>Men's Perfumes</option>
          <option>Women's Perfumes</option>
          <option>Arabic Perfumes</option>
          <option>Gift Sets</option>
        </select>
        <textarea placeholder="Message / perfume requirement" required></textarea>
        <button class="btn" onclick="const name = this.form.querySelector('input[placeholder=\\'Your name\\']').value || 'Customer'; const msg = this.form.querySelector('textarea').value || 'Hello'; window.open('https://wa.me/97477763375?text=' + encodeURIComponent('Hi DEN TIMES, my name is ' + name + '. ' + msg));">Send via WhatsApp</button>
      </form>
    </div>
  </section>
</main>
''' + end
(root / 'contact.html').write_text(contact, encoding='utf-8')

# product.html
product = head('Product') + '''
<main>
  <section class="page-hero">
    <div class="container reveal reveal-slide-up">
      <span class="breadcrumb">Home / Product</span>
      <h1 class="serif">Product Detail</h1>
      <p>This is a reusable product detail template. Duplicate it for each perfume or connect it to a CMS/e-commerce backend later.</p>
    </div>
  </section>
  <section class="section" style="padding-top: 20px;">
    <div class="container split">
      <div class="image-card reveal reveal-slide-right">
        <img src="assets/images/burberry-hero.webp" alt="Product Detail">
      </div>
      <div class="panel reveal reveal-slide-left">
        <span class="eyebrow">Burberry</span>
        <h2 class="serif">Burberry Hero</h2>
        <p>Premium masculine fragrance with a modern woody profile. Use this page to add official product details, available sizes, price and stock status.</p>
        <div class="feature-list">
          <div class="feature">
            <span>✦</span>
            <div>
              <b>Category</b>
              <small>Men's Perfume</small>
            </div>
          </div>
          <div class="feature">
            <span>✦</span>
            <div>
              <b>Size</b>
              <small>100ml / based on availability</small>
            </div>
          </div>
          <div class="feature">
            <span>✦</span>
            <div>
              <b>Ordering</b>
              <small>WhatsApp enquiry with product name pre-filled.</small>
            </div>
          </div>
        </div>
        <br>
        <a class="btn" href="https://wa.me/97477763375?text=Hi%20DEN%20TIMES%2C%20I%20want%20Burberry%20Hero%20(QAR%20299)">Enquire on WhatsApp</a>
      </div>
    </div>
  </section>
</main>
''' + end
(root / 'product.html').write_text(product, encoding='utf-8')

print("All luxury templates generated successfully in Python!")
