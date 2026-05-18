# Cursor Prompt — Build DEN TIMES Online Store Website Perfectly

You are an expert frontend developer and conversion-focused e-commerce UI designer. Build a premium, mobile-first perfume e-commerce website for **DEN TIMES ONLINE STORE** in Qatar.

## Business Details
- Store name: **DEN TIMES ONLINE STORE**
- Product: **Perfumes**
- Phone / WhatsApp: **+974 7776 3375**
- Main brands: **Lacoste, Burberry, Guerlain, Lancôme, Lattafa, Armaf, Afnan, French Avenue, Paris Corner, Assaf**
- Core positioning: Premium perfumes, luxury brands, Arabic perfumes, gift sets, easy WhatsApp ordering.

## Design Direction
Create a luxury perfume website with a **black, champagne gold, ivory, warm brown, marble and glass** look. It should feel like a high-end boutique, not a basic online shop.

Use the generated image assets in `/assets/images/`:
- `hero-main.webp` — main homepage hero
- `brand-lineup.webp` — featured brands banner
- `mens-collection.webp` — men’s category
- `womens-collection.webp` — women’s category
- `arabic-collection.webp` — Arabic perfumes category
- `gift-sets.webp` — gift sets/offers
- `burberry-hero.webp`, `lancome-belle.webp`, `lattafa-asad.webp`, `armaf-club.webp`, `afnan-9pm.webp` — product card/product detail images
- `authentic-banner.webp`, `new-arrivals.webp` — marketing banners

## Required Pages
Create these pages:
1. **Home** `/`
2. **Shop** `/shop`
3. **Brands** `/brands`
4. **Offers / Gift Sets** `/offers`
5. **About** `/about`
6. **Contact / Order** `/contact`
7. **Product Detail Template** `/product/[slug]` or `/product.html` if static

## Homepage Structure
The homepage must include:
1. Sticky transparent/dark header with logo text, navigation, WhatsApp CTA.
2. Hero section with big luxury headline:
   - “Luxury scents, delivered with style.”
   - Subtext about premium perfumes, Arabic perfumes, designer brands, WhatsApp ordering.
   - CTAs: “Explore Collection” and “Order on WhatsApp”
3. Brand marquee line:
   - Lacoste • Burberry • Guerlain • Lancôme • Lattafa • Armaf • Afnan • French Avenue • Paris Corner • Assaf
4. Shop by collection cards:
   - Men’s Perfumes
   - Women’s Perfumes
   - Arabic Perfumes
   - Gift Sets & Combos
5. Featured brands banner with large image and CTA.
6. Popular product grid with filter chips:
   - All, Men, Women, Arabic, Lattafa, Armaf, Afnan
7. New Arrivals / Authentic Fragrances banner.
8. Why DEN TIMES section:
   - Premium quality visual style
   - WhatsApp-first ordering
   - Brand-focused structure
   - Mobile-first browsing
9. Footer with quick links, brand list, WhatsApp contact.
10. Floating WhatsApp button and mobile bottom nav.

## Product Card Requirements
Each product card should show:
- Product image
- Brand
- Category
- Product name
- Short description
- Price placeholder, e.g. `QAR 129`
- WhatsApp enquiry button with pre-filled product name.

Sample products:
- Burberry Hero — Men — QAR 299
- Lancôme La Vie Est Belle — Women — QAR 349
- Lattafa Asad — Arabic — QAR 129
- Armaf Club de Nuit Intense — Men — QAR 189
- Afnan 9PM — Men — QAR 159
- Guerlain Inspired Selection — Women — QAR 399
- French Avenue Oud — Arabic — QAR 169
- Paris Corner Emirene — Women — QAR 149

## Animations & Interactions
Add smooth premium animations, not childish effects:
- Scroll reveal fade-up animation using Intersection Observer or Framer Motion.
- Slight image scale on hover.
- Sticky glassmorphism header.
- Product filter buttons.
- Smooth scroll behavior.
- Mobile menu drawer.
- Floating WhatsApp button.
- Optional parallax feel on hero background.

## Mobile Optimization
The website must look excellent on iPhone and Android:
- No horizontal scroll.
- Hero text must not overlap the image.
- Product grid should become 1 column on mobile.
- Category cards should stack cleanly.
- Header should become hamburger menu.
- Add a mobile bottom nav with Home, Shop, Brands, Offers.
- WhatsApp button must not cover important content.

## Tech Options
If building in plain HTML/CSS/JS, keep the file structure clean:
- `/index.html`
- `/shop.html`
- `/brands.html`
- `/offers.html`
- `/about.html`
- `/contact.html`
- `/product.html`
- `/assets/css/style.css`
- `/assets/js/main.js`
- `/assets/images/`

If building in Next.js, use:
- App Router
- Tailwind CSS
- Reusable components:
  - Header
  - Hero
  - Marquee
  - CategoryGrid
  - BrandBanner
  - ProductGrid
  - ProductCard
  - CTASection
  - Footer
  - MobileNav
  - WhatsAppButton
- Use `next/image` for image optimization.

## Copy Tone
Premium but simple. Avoid too much text. The website should convert users quickly.

Suggested lines:
- “Premium perfumes from trusted brands.”
- “Designer, Arabic and gift-ready fragrances in one place.”
- “Order easily through WhatsApp.”
- “Find your signature scent.”
- “Luxury fragrance selections for every occasion.”

## Important Notes
- Generated images are concept visuals. For final production, replace with official product photography if the client provides it.
- Keep all image alt text descriptive for SEO.
- Prepare the design so it can later connect to WooCommerce, Shopify, Supabase, Sanity, or a simple admin panel.
- Make the code clean, readable and easy to edit.

## Final Output Expected
Deliver a polished, responsive, premium perfume e-commerce frontend with all pages working, all images properly loaded, WhatsApp links working, and a smooth mobile experience.
