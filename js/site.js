/* =====================================================
   NIRAMAYA Hospital - shared site.js
   ===================================================== */
(function () {
  // Reveal animations
  if ('IntersectionObserver' in window) {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          obs.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -50px 0px' });
    document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
  }

  // Scroll-to-top FAB
  const st = document.getElementById('scrollTop');
  if (st) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) st.classList.add('show');
      else st.classList.remove('show');
    });
  }

  // Year in footer
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // Min date for any date input
  const di = document.querySelectorAll('input[type="date"]');
  if (di.length) {
    const today = new Date().toISOString().split('T')[0];
    di.forEach(input => input.setAttribute('min', today));
  }

  // Mobile menu toggle
  const menuBtn = document.querySelector('.menu-toggle');
  const navList = document.querySelector('.nav-list');
  if (menuBtn && navList) {
    menuBtn.addEventListener('click', () => {
      const isOpen = navList.classList.contains('mobile-open');
      if (isOpen) {
        navList.classList.remove('mobile-open');
        navList.removeAttribute('style');
      } else {
        navList.classList.add('mobile-open');
        navList.style.cssText = 'display:flex;flex-direction:column;position:absolute;top:100%;left:0;right:0;background:#fff;padding:14px 20px;box-shadow:0 8px 24px rgba(0,80,130,0.10);z-index:1000;';
      }
    });
  }

  // Filter pills (doctors page)
  const pills = document.querySelectorAll('.filter-pill');
  const grid = document.getElementById('doctorsGrid');
  if (pills.length && grid) {
    pills.forEach(pill => {
      pill.addEventListener('click', () => {
        pills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        const filter = pill.getAttribute('data-filter');
        grid.querySelectorAll('.doctor-card').forEach(card => {
          if (filter === 'all') { card.style.display = ''; }
          else {
            const photo = card.querySelector('.doctor-photo');
            if (photo && photo.classList.contains('bg-' + filter)) { card.style.display = ''; }
            else { card.style.display = 'none'; }
          }
        });
      });
    });
  }

  // Form submit (appointment + contact)
  const forms = document.querySelectorAll('form.appointment-form, form.contact-form');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const req = form.querySelectorAll('[required]');
      let ok = true;
      req.forEach(f => {
        if (!f.value.trim()) { f.style.borderColor = '#e74c3c'; ok = false; }
        else f.style.borderColor = '';
      });
      if (!ok) return;
      const success = form.querySelector('.form-success');
      if (success) {
        success.classList.add('show');
        setTimeout(() => success.classList.remove('show'), 6000);
      }
      form.reset();
    });
  });

  // Lightbox for gallery
  const lightbox = document.getElementById('lightbox');
  if (lightbox) {
    const lbImg = lightbox.querySelector('img');
    document.querySelectorAll('.gallery-grid img').forEach(img => {
      img.addEventListener('click', () => {
        lbImg.src = img.src;
        lbImg.alt = img.alt;
        lightbox.classList.add('show');
      });
    });
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox || e.target.classList.contains('lightbox-close')) {
        lightbox.classList.remove('show');
      }
    });
  }
  // Hero Background Slider
  (function initHeroBgSlider() {
    const slidesContainer = document.getElementById('heroBgSlides');
    if (!slidesContainer) return;
    const slides = slidesContainer.querySelectorAll('.hero-bg-slide');
    const dots = document.querySelectorAll('#heroCleanDots .hero-clean-dot');
    const prevBtn = document.getElementById('heroPrevBtn');
    const nextBtn = document.getElementById('heroNextBtn');
    if (!slides.length) return;

    let currentIndex = 0;
    const slideCount = slides.length;
    let timer = null;

    function goToSlide(index) {
      if (index < 0) index = slideCount - 1;
      if (index >= slideCount) index = 0;
      slides.forEach((s, i) => {
        if (i === index) s.classList.add('active');
        else s.classList.remove('active');
      });
      dots.forEach((d, i) => {
        if (i === index) d.classList.add('active');
        else d.classList.remove('active');
      });
      currentIndex = index;
    }

    function nextSlide() { goToSlide(currentIndex + 1); }
    function prevSlide() { goToSlide(currentIndex - 1); }

    function startAutoPlay() {
      stopAutoPlay();
      timer = setInterval(nextSlide, 5000);
    }
    function stopAutoPlay() {
      if (timer) clearInterval(timer);
    }

    if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); startAutoPlay(); });
    if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); startAutoPlay(); });

    dots.forEach(dot => {
      dot.addEventListener('click', () => {
        const idx = parseInt(dot.getAttribute('data-slide'), 10);
        if (!isNaN(idx)) { goToSlide(idx); startAutoPlay(); }
      });
    });

    const heroSection = document.getElementById('home');
    if (heroSection) {
      heroSection.addEventListener('mouseenter', stopAutoPlay);
      heroSection.addEventListener('mouseleave', startAutoPlay);
    }

    startAutoPlay();
  })();

})();
