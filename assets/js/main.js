/**
 * DEN TIMES ONLINE STORE — INTERACTIVE ENGINE
 * Main JavaScript controller for luxury effects, scroll animations,
 * interactive product drawers, and category filters.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Utility selectors
  const $ = (s, root = document) => root.querySelector(s);
  const $$ = (s, root = document) => [...root.querySelectorAll(s)];

  /* =========================================
     1. STICKY GLASS HEADER ON SCROLL
     ========================================= */
  const header = $('.nav');
  if (header) {
    const handleScroll = () => {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Initial check
  }

  /* =========================================
     2. PARALLAX HERO BACKGROUND
     ========================================= */
  const heroSection = $('.hero');
  if (heroSection) {
    window.addEventListener('scroll', () => {
      const scrollPos = window.scrollY;
      // Shift hero background position slightly to create depth
      if (scrollPos < window.innerHeight) {
        heroSection.style.setProperty('--scroll-y', `${scrollPos * 0.35}px`);
        // We will apply this via a dynamically updated transform on the pseudo element
        // or directly shifting background position.
        // In style.css we have a transform. Let's apply it to a CSS variable.
        const scaleVal = 1.01 + (scrollPos * 0.0001);
        heroSection.style.backgroundPositionY = `${scrollPos * 0.15}px`;
      }
    });
  }

  /* =========================================
     3. ADVANCED SCROLL-BASED ENTRANCE ANIMATIONS
     ========================================= */
  const revealElements = $$('.reveal');
  
  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Add the active animation class
          entry.target.classList.add('show');
          // Once animated, we don't need to observe it anymore
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null, // Viewport
      threshold: 0.1, // Trigger when 10% of element is visible
      rootMargin: '0px 0px -40px 0px' // Offset slightly before element hits viewport
    });

    revealElements.forEach((el, index) => {
      // Dynamically add default transition types if not set in HTML
      if (![...el.classList].some(cls => cls.startsWith('reveal-'))) {
        el.classList.add('reveal-slide-up');
      }
      
      // Auto-stagger grid items for a premium wave reveal
      const gridParent = el.closest('.products, .category-grid, .brands-grid');
      if (gridParent) {
        const siblings = $$(el.tagName, gridParent);
        const sibIndex = siblings.indexOf(el);
        if (sibIndex >= 0 && sibIndex < 6) {
          el.style.transitionDelay = `${sibIndex * 80}ms`;
        }
      }
      
      revealObserver.observe(el);
    });
  } else {
    // Fallback for older browsers
    revealElements.forEach(el => el.classList.add('show'));
  }

  /* =========================================
     4. INTERACTIVE CATEGORY FILTER (WITH SMOOTH FADE)
     ========================================= */
  const chips = $$('.chip');
  const products = $$('.product');

  if (chips.length > 0 && products.length > 0) {
    chips.forEach(chip => {
      chip.addEventListener('click', () => {
        // Toggle active chip classes
        chips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');

        const filter = chip.dataset.filter.toLowerCase();

        products.forEach(p => {
          const cat = p.dataset.cat ? p.dataset.cat.toLowerCase() : '';
          const brand = p.dataset.brand ? p.dataset.brand.toLowerCase() : '';
          const isMatch = filter === 'all' || cat === filter || brand === filter;

          if (isMatch) {
            // Smoothly animate matching items in
            p.style.display = 'flex';
            setTimeout(() => {
              p.style.opacity = '1';
              p.style.transform = 'translateY(0) scale(1)';
            }, 50);
          } else {
            // Smoothly animate non-matching items out
            p.style.opacity = '0';
            p.style.transform = 'translateY(12px) scale(0.96)';
            setTimeout(() => {
              p.style.display = 'none';
            }, 300);
          }
        });
      });
    });
  }

  /* =========================================
     5. MOBILE MENU HAMBURGER DRAWER
     ========================================= */
  const drawer = $('.drawer');
  const menuBtn = $('.menu');
  const closeBtn = $('.close-drawer');

  if (menuBtn && drawer) {
    menuBtn.addEventListener('click', () => {
      drawer.classList.add('open');
      document.body.style.overflow = 'hidden'; // Stop page scrolling under drawer
    });
  }

  const closeDrawerFunc = () => {
    if (drawer) {
      drawer.classList.remove('open');
      document.body.style.overflow = '';
    }
  };

  if (closeBtn) {
    closeBtn.addEventListener('click', closeDrawerFunc);
  }

  if (drawer) {
    drawer.addEventListener('click', (e) => {
      if (e.target === drawer) {
        closeDrawerFunc();
      }
    });
  }

  /* =========================================
     6. WHATSAPP ENQUIRY PRE-FILLER
     ========================================= */
  const waNumber = '97477763375';
  
  // Set click handlers for standard WhatsApp buttons
  $$('[data-wa]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const name = btn.dataset.wa;
      const text = `Hello DEN TIMES, I am interested in ${name}. Please share availability and best price.`;
      btn.href = `https://wa.me/${waNumber}?text=${encodeURIComponent(text)}`;
    });
  });

  /* =========================================
     7. PREMIUM PRODUCT QUICK-VIEW MODAL DRAWER
     ========================================= */
  // Create & Inject Modal Markup if it doesn't exist
  let qvModal = $('.qv-modal');
  if (!qvModal) {
    qvModal = document.createElement('div');
    qvModal.className = 'qv-modal';
    qvModal.innerHTML = `
      <div class="qv-content">
        <button class="qv-close" aria-label="Close modal">×</button>
        <div class="qv-grid">
          <div class="qv-image">
            <img src="" alt="Product Quick View">
          </div>
          <div class="qv-details">
            <span class="tag">Brand • Category</span>
            <h2>Product Name</h2>
            <p>Product description goes here.</p>
            <div class="qv-specs">
              <div class="qv-spec"><span>✓</span> 100% Authentic Designer Fragrance</div>
              <div class="qv-spec"><span>✓</span> Premium Boutique Packaging</div>
              <div class="qv-spec"><span>✓</span> Hand-delivered in Qatar</div>
            </div>
            <div class="qv-price-row">
              <div class="qv-price">QAR ---</div>
              <a class="btn qv-wa-btn" href="#" target="_blank">Order on WhatsApp</a>
            </div>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(qvModal);
  }

  const qvImg = $('.qv-image img', qvModal);
  const qvTag = $('.tag', qvModal);
  const qvName = $('h2', qvModal);
  const qvDesc = $('p', qvModal);
  const qvPrice = $('.qv-price', qvModal);
  const qvWaBtn = $('.qv-wa-btn', qvModal);
  const qvCloseBtn = $('.qv-close', qvModal);

  // Function to open quick view
  const openQuickView = (productData) => {
    qvImg.src = productData.img;
    qvImg.alt = productData.name;
    qvTag.textContent = `${productData.brand} • ${productData.cat}`;
    qvName.textContent = productData.name;
    qvDesc.textContent = productData.desc;
    qvPrice.textContent = productData.price;
    
    // Set WhatsApp link
    const text = `Hello DEN TIMES, I am interested in ${productData.name}. Please share availability and best price.`;
    qvWaBtn.href = `https://wa.me/${waNumber}?text=${encodeURIComponent(text)}`;

    qvModal.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  const closeQuickView = () => {
    qvModal.classList.remove('open');
    document.body.style.overflow = '';
  };

  if (qvCloseBtn) {
    qvCloseBtn.addEventListener('click', closeQuickView);
  }

  qvModal.addEventListener('click', (e) => {
    if (e.target === qvModal) {
      closeQuickView();
    }
  });

  // Bind Quick-View event to all product cards
  $$('.product').forEach(card => {
    // Click on image or title should trigger Quick View
    const triggerElements = $$( 'h3, .img', card);
    
    // Extract info from DOM elements
    const name = $('h3', card)?.textContent || '';
    const brandTag = $('.tag', card)?.textContent || '';
    const brand = brandTag.split('•')[0]?.trim() || '';
    const cat = brandTag.split('•')[1]?.trim() || '';
    const desc = $('p', card)?.textContent || '';
    const price = $('.price b', card)?.textContent || '';
    const img = $('img', card)?.src || '';

    const productData = { name, brand, cat, desc, price, img };

    triggerElements.forEach(el => {
      el.style.cursor = 'pointer';
      el.addEventListener('click', (e) => {
        e.preventDefault();
        openQuickView(productData);
      });
    });
  });

  // Highlight Current Navigation Page Link
  const currentPath = window.location.pathname;
  const navLinks = $$('.links a, .bottom-nav a, .drawer-panel a');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href && currentPath.endsWith(href)) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
});
