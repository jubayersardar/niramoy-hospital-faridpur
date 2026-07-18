/* =========================================
   আরোগ্য সদন হাসপাতাল — Modern JS
   ========================================= */

(function ($) {
    'use strict';

    // ============== PRELOADER ==============
    $(window).on('load', function () {
        $('#preloader').addClass('hide');
        setTimeout(function () { $('#preloader').remove(); }, 600);
        if (typeof AOS !== 'undefined') AOS.refresh();
    });

    $(document).ready(function () {

        // ============== YEAR ==============
        $('#year').text(new Date().getFullYear());

        // ============== AOS INIT ==============
        if (typeof AOS !== 'undefined') {
            AOS.init({
                duration: 900,
                easing: 'ease-out-cubic',
                once: true,
                offset: 60,
                disable: function () { return window.innerWidth < 480; }
            });
        }

        // ============== CUSTOM CURSOR ==============
        if (window.innerWidth >= 1024) {
            const cursor = document.getElementById('cursor');
            const follower = document.getElementById('cursorFollower');

            if (cursor && follower) {
                let cx = 0, cy = 0, fx = 0, fy = 0;

                document.addEventListener('mousemove', (e) => {
                    cx = e.clientX; cy = e.clientY;
                });

                function updateCursor() {
                    fx += (cx - fx) * 0.18;
                    fy += (cy - fy) * 0.18;
                    cursor.style.transform = `translate(${cx}px, ${cy}px) translate(-50%, -50%)`;
                    follower.style.transform = `translate(${fx}px, ${fy}px) translate(-50%, -50%)`;
                    requestAnimationFrame(updateCursor);
                }
                updateCursor();

                document.querySelectorAll('a, button, .dept-card, .doctor-card, .service-card, .facility-card, .ach-card, .gallery-item, .why-card, .filter-tab, .testimonial-card, .btn, .nav-cta, .filter-search').forEach(el => {
                    el.addEventListener('mouseenter', () => follower.classList.add('expand'));
                    el.addEventListener('mouseleave', () => follower.classList.remove('expand'));
                });
            }
        }

        // ============== HERO PARTICLES ==============
        const particlesContainer = document.getElementById('particles');
        if (particlesContainer) {
            const particleCount = window.innerWidth < 768 ? 20 : 40;
            for (let i = 0; i < particleCount; i++) {
                const p = document.createElement('span');
                p.className = 'particle';
                const size = Math.random() * 6 + 2;
                p.style.width = size + 'px';
                p.style.height = size + 'px';
                p.style.left = Math.random() * 100 + '%';
                p.style.animationDuration = (Math.random() * 20 + 10) + 's';
                p.style.animationDelay = (Math.random() * 15) + 's';
                p.style.background = Math.random() > 0.5 ? 'var(--gold)' : 'var(--white)';
                particlesContainer.appendChild(p);
            }
        }

        // ============== NAVBAR SCROLL ==============
        const navbar = document.getElementById('navbar');
        const scrollProgress = document.getElementById('scrollProgress');
        const backToTop = document.getElementById('backToTop');

        window.addEventListener('scroll', () => {
            const scrolled = window.scrollY;
            const total = document.documentElement.scrollHeight - window.innerHeight;
            const pct = (scrolled / total) * 100;

            if (scrollProgress) scrollProgress.style.width = pct + '%';

            if (navbar) {
                if (scrolled > 80) navbar.classList.add('scrolled');
                else navbar.classList.remove('scrolled');
            }

            if (backToTop) {
                if (scrolled > 600) backToTop.classList.add('visible');
                else backToTop.classList.remove('visible');
            }
        });

        // ============== MOBILE NAV ==============
        const navToggle = document.getElementById('navToggle');
        const navMenu = document.getElementById('navMenu');

        if (navToggle && navMenu) {
            navToggle.addEventListener('click', () => {
                navToggle.classList.toggle('active');
                navMenu.classList.toggle('open');
                document.body.style.overflow = navMenu.classList.contains('open') ? 'hidden' : '';
            });

            document.querySelectorAll('.nav-link').forEach(link => {
                link.addEventListener('click', () => {
                    navToggle.classList.remove('active');
                    navMenu.classList.remove('open');
                    document.body.style.overflow = '';
                });
            });
        }

        // ============== ACTIVE NAV LINK ON SCROLL ==============
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-link');

        function setActiveLink() {
            let current = '';
            sections.forEach(section => {
                const top = section.offsetTop - 150;
                if (window.scrollY >= top) current = section.getAttribute('id');
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + current) link.classList.add('active');
            });
        }
        window.addEventListener('scroll', setActiveLink);
        setActiveLink();

        // ============== SMOOTH SCROLL ==============
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const target = this.getAttribute('href');
                if (target === '#' || target.length <= 1) return;
                const targetEl = document.querySelector(target);
                if (targetEl) {
                    e.preventDefault();
                    const offset = 90;
                    const top = targetEl.getBoundingClientRect().top + window.pageYOffset - offset;
                    window.scrollTo({ top, behavior: 'smooth' });
                }
            });
        });

        // ============== COUNTER ANIMATION ==============
        function animateCounter(el) {
            const target = parseInt(el.getAttribute('data-count'));
            const duration = 2000;
            const start = performance.now();

            function step(now) {
                const elapsed = now - start;
                const progress = Math.min(elapsed / duration, 1);
                const eased = 1 - Math.pow(1 - progress, 4);
                const val = Math.floor(eased * target);
                el.textContent = val.toLocaleString('en-US');

                if (progress < 1) requestAnimationFrame(step);
                else el.textContent = target.toLocaleString('en-US');
            }
            requestAnimationFrame(step);
        }

        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
                    entry.target.classList.add('counted');
                    animateCounter(entry.target);
                }
            });
        }, { threshold: 0.4 });

        document.querySelectorAll('.stat-num').forEach(el => counterObserver.observe(el));

        // ============== DOCTORS FILTER ==============
        const filterTabs = document.querySelectorAll('.filter-tab');
        const doctorCards = document.querySelectorAll('.doctor-card');
        const doctorSearch = document.getElementById('doctorSearch');

        let currentFilter = 'all';

        filterTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                filterTabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                currentFilter = tab.getAttribute('data-filter');
                applyFilter();
            });
        });

        if (doctorSearch) {
            doctorSearch.addEventListener('input', applyFilter);
        }

        function applyFilter() {
            const q = doctorSearch ? doctorSearch.value.toLowerCase().trim() : '';
            doctorCards.forEach((card, i) => {
                const cat = card.getAttribute('data-category');
                const text = card.textContent.toLowerCase();
                const matchFilter = currentFilter === 'all' || cat.includes(currentFilter);
                const matchSearch = !q || text.includes(q);

                if (matchFilter && matchSearch) {
                    card.style.display = '';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0) scale(1)';
                    }, 50 * i);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px) scale(0.95)';
                    setTimeout(() => { card.style.display = 'none'; }, 250);
                }
            });
        }

        // ============== APPOINTMENT FORM ==============
        const apptForm = document.getElementById('appointmentForm');
        const formStatus = document.getElementById('formStatus');

        if (apptForm) {
            const today = new Date().toISOString().split('T')[0];
            const dateInput = apptForm.querySelector('#date');
            if (dateInput) dateInput.min = today;

            apptForm.addEventListener('submit', function (e) {
                e.preventDefault();
                const data = new FormData(apptForm);

                if (formStatus) {
                    formStatus.className = 'form-status success';
                    formStatus.innerHTML = '<i class="fas fa-check-circle"></i> আপনার অ্যাপয়েন্টমেন্ট সফলভাবে গ্রহণ করা হয়েছে! আমরা শীঘ্রই আপনার সাথে যোগাযোগ করব।';
                    formStatus.style.display = 'block';
                }

                apptForm.reset();

                if (typeof confetti !== 'undefined') {
                    confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
                }

                setTimeout(() => {
                    if (formStatus) {
                        formStatus.style.opacity = '0';
                        setTimeout(() => {
                            formStatus.className = 'form-status';
                            formStatus.style.display = 'none';
                            formStatus.style.opacity = '1';
                        }, 400);
                    }
                }, 5000);
            });
        }

        // ============== NEWSLETTER FORM ==============
        const newsletterForm = document.getElementById('newsletterForm');
        if (newsletterForm) {
            newsletterForm.addEventListener('submit', function (e) {
                e.preventDefault();
                const btn = this.querySelector('button');
                const orig = btn.innerHTML;
                btn.innerHTML = '<i class="fas fa-check"></i> সাবস্ক্রাইবড!';
                btn.style.background = '#22c55e';
                btn.style.color = '#fff';
                this.reset();
                setTimeout(() => {
                    btn.innerHTML = orig;
                    btn.style.background = '';
                    btn.style.color = '';
                }, 3000);
            });
        }

        // ============== GLIGHTBOX ==============
        if (typeof GLightbox !== 'undefined') {
            GLightbox({ selector: '.glightbox', touchNavigation: true, loop: true });
        }

        // ============== BACK TO TOP ==============
        if (backToTop) {
            backToTop.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }

        // ============== TILT EFFECT ON CARDS ==============
        if (window.innerWidth >= 1024) {
            document.querySelectorAll('.doctor-card, .dept-card, .service-card, .facility-card, .ach-card, .gallery-item').forEach(card => {
                card.addEventListener('mousemove', (e) => {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    const centerX = rect.width / 2;
                    const centerY = rect.height / 2;
                    const rotateX = ((y - centerY) / centerY) * -3;
                    const rotateY = ((x - centerX) / centerX) * 3;
                    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px)`;
                });

                card.addEventListener('mouseleave', () => {
                    card.style.transform = '';
                });
            });
        }

        // ============== PARALLAX HERO CARDS ==============
        if (window.innerWidth >= 1024) {
            const heroCards = document.querySelectorAll('.hero-card');
            const hero = document.querySelector('.hero');

            if (hero && heroCards.length) {
                hero.addEventListener('mousemove', (e) => {
                    const x = (e.clientX / window.innerWidth - 0.5) * 2;
                    const y = (e.clientY / window.innerHeight - 0.5) * 2;

                    heroCards.forEach((card, i) => {
                        const intensity = (i + 1) * 8;
                        card.style.transform = `translate(${x * intensity}px, ${y * intensity}px)`;
                    });
                });

                hero.addEventListener('mouseleave', () => {
                    heroCards.forEach(card => card.style.transform = '');
                });
            }
        }

        // ============== HOSPITAL TIME BADGE ==============
        function updateHospitalTime() {
            const el = document.getElementById('hospitalTime');
            if (!el) return;
            const bdTime = new Date().toLocaleString('en-US', { timeZone: 'Asia/Dhaka', hour: '2-digit', minute: '2-digit', hour12: false });
            const hour = parseInt(bdTime.split(':')[0]);
            if (hour >= 8 && hour < 22) el.textContent = 'এখন খোলা: সকাল ৮:০০ - রাত ১০:০০';
            else el.textContent = 'ইমার্জেন্সি ২৪/৭ খোলা';
        }
        updateHospitalTime();
        setInterval(updateHospitalTime, 60000);

        // ============== LANG SWITCHER ==============
        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                // Optional: load corresponding translation. For now just a visual indication.
                const lang = btn.getAttribute('data-lang');
                document.documentElement.lang = lang === 'bn' ? 'bn' : 'en';
            });
        });

        // ============== FAQ SINGLE TOGGLE ==============
        document.querySelectorAll('.faq-item').forEach(item => {
            item.addEventListener('toggle', () => {
                if (item.open) {
                    document.querySelectorAll('.faq-item').forEach(other => {
                        if (other !== item) other.open = false;
                    });
                }
            });
        });

        // ============== LIVE BADGE ANIMATION ==============
        document.querySelectorAll('.doctor-online').forEach(badge => {
            badge.querySelector('i').style.animation = 'livePulse 1.5s ease-in-out infinite';
        });
        document.head.insertAdjacentHTML('beforeend',
            '<style>@keyframes livePulse { 0%,100%{opacity:1} 50%{opacity:0.4} }</style>'
        );

    });
})(jQuery);
