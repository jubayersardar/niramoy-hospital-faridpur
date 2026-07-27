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

        // ============== HERO SLIDER ==============
        (function initHeroSlider() {
            const track = document.getElementById('heroTrack');
            if (!track) return;

            const slides = track.querySelectorAll('.hero-slide');
            const dots = document.querySelectorAll('#heroDots .hero-slider__dot');
            const prevBtn = document.getElementById('heroPrev');
            const nextBtn = document.getElementById('heroNext');
            const progressBar = document.getElementById('heroProgress');

            if (!slides.length) return;

            let currentIndex = 0;
            const slideCount = slides.length;
            const autoPlayDuration = 6000; // 6 seconds per slide
            let timer = null;
            let progressInterval = null;
            let progressStartTime = null;

            function updateProgress() {
                if (!progressBar) return;
                const elapsed = Date.now() - progressStartTime;
                const pct = Math.min((elapsed / autoPlayDuration) * 100, 100);
                progressBar.style.width = pct + '%';
                if (pct < 100) {
                    progressInterval = requestAnimationFrame(updateProgress);
                }
            }

            function resetProgress() {
                if (progressInterval) cancelAnimationFrame(progressInterval);
                if (progressBar) progressBar.style.width = '0%';
                progressStartTime = Date.now();
                progressInterval = requestAnimationFrame(updateProgress);
            }

            function goToSlide(index) {
                if (index < 0) index = slideCount - 1;
                if (index >= slideCount) index = 0;

                slides.forEach((slide, i) => {
                    if (i === index) {
                        slide.classList.add('active');
                    } else {
                        slide.classList.remove('active');
                    }
                });

                dots.forEach((dot, i) => {
                    if (i === index) {
                        dot.classList.add('active');
                    } else {
                        dot.classList.remove('active');
                    }
                });

                currentIndex = index;
                resetProgress();
            }

            function nextSlide() {
                goToSlide(currentIndex + 1);
            }

            function prevSlide() {
                goToSlide(currentIndex - 1);
            }

            function startAutoPlay() {
                stopAutoPlay();
                resetProgress();
                timer = setInterval(nextSlide, autoPlayDuration);
            }

            function stopAutoPlay() {
                if (timer) clearInterval(timer);
                if (progressInterval) cancelAnimationFrame(progressInterval);
                if (progressBar) progressBar.style.width = '0%';
            }

            if (nextBtn) {
                nextBtn.addEventListener('click', () => {
                    nextSlide();
                    startAutoPlay();
                });
            }

            if (prevBtn) {
                prevBtn.addEventListener('click', () => {
                    prevSlide();
                    startAutoPlay();
                });
            }

            dots.forEach(dot => {
                dot.addEventListener('click', () => {
                    const slideIdx = parseInt(dot.getAttribute('data-slide'), 10);
                    if (!isNaN(slideIdx)) {
                        goToSlide(slideIdx);
                        startAutoPlay();
                    }
                });
            });

            // Pause on hover
            const sliderSection = document.querySelector('.hero-slider');
            if (sliderSection) {
                sliderSection.addEventListener('mouseenter', stopAutoPlay);
                sliderSection.addEventListener('mouseleave', startAutoPlay);
            }

            // Touch Swipe Support
            let touchStartX = 0;
            let touchEndX = 0;

            track.addEventListener('touchstart', e => {
                touchStartX = e.changedTouches[0].screenX;
            }, { passive: true });

            track.addEventListener('touchend', e => {
                touchEndX = e.changedTouches[0].screenX;
                const diff = touchStartX - touchEndX;
                if (Math.abs(diff) > 50) {
                    if (diff > 0) {
                        nextSlide();
                    } else {
                        prevSlide();
                    }
                    startAutoPlay();
                }
            }, { passive: true });

            // Start initial slide & autoplay
            goToSlide(0);
            startAutoPlay();
        })();

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

        // ============== HERO FLOATING PARTICLES ==============
        const heroParticles = document.getElementById('heroParticles');
        if (heroParticles) {
            const count = window.innerWidth < 768 ? 12 : 25;
            for (let i = 0; i < count; i++) {
                const dot = document.createElement('span');
                dot.className = 'hero-particle';
                const size = Math.random() * 4 + 2;
                dot.style.width = size + 'px';
                dot.style.height = size + 'px';
                dot.style.left = Math.random() * 100 + '%';
                dot.style.bottom = -(Math.random() * 20) + 'px';
                dot.style.animationDuration = (Math.random() * 12 + 8) + 's';
                dot.style.animationDelay = (Math.random() * 8) + 's';
                dot.style.opacity = Math.random() * 0.4 + 0.1;
                heroParticles.appendChild(dot);
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

/* =========================================
   SPECIALIZED DEPARTMENT DATA & MODAL LOGIC
   ========================================= */

const DEPARTMENT_DATA = {
    med: {
        id: "med",
        name: "মেডিসিন বিভাগ",
        nameEn: "Department of Internal Medicine",
        badge: "বিশেষায়িত ওপিডি",
        image: "images/departments/dept-medicine.jpg",
        icon: "fa-stethoscope",
        tagline: "সর্বাধুনিক অভ্যন্তরীণ চিকিৎসা ও রূপান্তরমুখী ডায়াগনস্টিক সেবা",
        description: "আমাদের মেডিসিন বিভাগ অভিজ্ঞ কনসালটেন্ট চিকিৎসকদের তত্ত্বাবধানে পরিচালিত। এখানে ডায়াবেটিস, উচ্চ রক্তচাপ, হৃদরোগ, বক্ষব্যাধি, কিডনি ও লিভার সংক্রান্ত জটিলতা এবং মেটাবলিক ডিসঅর্ডারের আধুনিক চিকিৎসা প্রদান করা হয়। প্রতিটি রোগীর জন্য ব্যক্তিগত চিকিৎসাপত্র ও সময়োপযোগী ফলোআপ নিশ্চিত করা হয়।",
        services: [
            "মেডিসিন ও ডায়াবেটিস সম্পূর্ণ ম্যানেজমেন্ট",
            "উচ্চ রক্তচাপ, কোলেস্টেরল ও হৃদরোগের প্রাতিষ্ঠানিক যত্ন",
            "বুক ব্যথা, গ্যাস্ট্রিক ও অ্যাজমা সুচিকিৎসা",
            "জ্বর, ডেঙ্গু, টাইফয়েড ও ইনফেকশাস ডিজিজ কেয়ার",
            "রুটিন স্বাস্থ্য পরীক্ষা (Comprehensive Health Screening)"
        ],
        tech: [
            "১২-লিড ডিজিটাল ইসিজি (12-Lead Digital ECG)",
            "অন-সাইট বায়োকেমিস্ট্রি ও হরমনোলজি ল্যাব",
            "সর্বাধুনিক পেশেন্ট মনিটরিং ও নেবুলাইজেশন ইউনিট"
        ],
        schedule: "প্রতিদিন সকাল ৯:০০ - রাত ৯:০০ (ওপিডি)",
        room: "কক্ষ ১০১, ১ম তলা",
        doctors: [
            { name: "ডা. আবু বকর সিদ্দিক", deg: "MBBS, BCS, MD (Internal Medicine)", title: "সহকারী অধ্যাপক, মেডিসিন বিভাগ", link: "doctors/01.html" },
            { name: "ডা. মোঃ রিয়াদ হোসেন বাপ্পি", deg: "MBBS, BCS, CCD, FCPS (মেডিসিন)", title: "সহকারী রেজিস্টার, মেডিসিন বিভাগ", link: "doctors/02.html" }
        ]
    },
    surg: {
        id: "surg",
        name: "সার্জারি বিভাগ",
        nameEn: "Department of General & Laparoscopic Surgery",
        badge: "আধুনিক ওটি সুবিধা",
        image: "images/departments/dept-surgery.jpg",
        icon: "fa-user-md",
        tagline: "নিরাপদ, আধুনিক ও ল্যাপারোস্কোপিক কি-হোল সার্জারি",
        description: "সার্জারি বিভাগ উন্নত প্রযুক্তি ও দক্ষ সার্জনদের দ্বারা পরিচালিত। এখানে সাধারণ অস্ত্রোপচারের পাশাপাশি আধুনিক ল্যাপারোস্কোপিক পদ্ধতির মাধ্যমে পিত্তথলির পাথর, অ্যাপেন্ডিক্স, হার্নিয়া, পাইলোনিডাল সাইনাস ও ইউরোলজিক্যাল সমস্যার দ্রুত ও ব্যথামুক্ত সমাধান দেওয়া হয়।",
        services: [
            "ল্যাপারোস্কোপিক গলব্লাডার (পিত্তথলি) ও অ্যাপেন্ডিক্স অপারেশন",
            "হার্নিয়া, হাইড্রোসিল ও ইউরোলজি সার্জারি",
            "কলোরেক্টাল, পাইলস, ফিশার ও ফিফটুলা চিকিৎসা",
            "সিস্ট, টিউমার ও ম্যালিগন্যান্সি বায়োপসি ও রিমুভাল",
            "জরুরি ট্রমা ও ইনজুরি সার্জারি (২৪/৭ ওটি)"
        ],
        tech: [
            "HD 4K ল্যাপারোস্কোপিক সার্জারি সেট (Storz)",
            "অ্যাডভান্সড অ্যানেস্থেসিয়া ওয়ার্কস্টেশন ও সি-আর্ম",
            "স্টেরিলাইজড আইসিইউ-সংযুক্ত অপারেশন থিয়েটার"
        ],
        schedule: "প্রতিদিন সকাল ১০:০০ - রাত ৮:০০ (ওপিডি)",
        room: "কক্ষ ২০৪, ২য় তলা",
        doctors: [
            { name: "ডা. শ্রাবন্তী সরকার", deg: "MBBS, FCPS (সার্জারি), MS", title: "সহকারী অধ্যাপক, সার্জারি বিভাগ", link: "doctors/03.html" },
            { name: "ডা. মইন উদ্দিন আহমেদ", deg: "MBBS, BCS, FCPS (সার্জারি)", title: "কনসালটেন্ট সার্জন", link: "doctors/04.html" }
        ]
    },
    gynae: {
        id: "gynae",
        name: "গাইনি ও প্রসূতি বিভাগ",
        nameEn: "Department of Obstetrics & Gynaecology",
        badge: "নারী স্বাস্থ্য ও প্রসূতি",
        image: "images/departments/dept-gynae.jpg",
        icon: "fa-person-pregnant",
        tagline: "নিরাপদ মাতৃত্ব, প্রসূতি যত্ন ও প্রজনন স্বাস্থ্যের বিশ্বস্ত ঠিকানা",
        description: "মহিলাদের সকল বয়সের স্বাস্থ্য নিরাপত্তা, গর্ভকালীন নিবিড় যত্ন (ANC), নরমাল ডেলিভারি, হাই-ঝুঁকিপূর্ণ গর্ভাবস্থা পরিচালনা, বন্ধ্যাত্ব চিকিৎসা ও গাইনোকোলজিক্যাল সার্জারির জন্য আমাদের অভিজ্ঞ মহিলা বিশেষজ্ঞ কনসালটেন্টগণ নিয়োজিত আছেন।",
        services: [
            "গর্ভবতী মায়েদের নিয়মিত চেকআপ (ANC & PNC Care)",
            "ব্যথামুক্ত ও পেইনলেস ডেলিভারি / নরমাল ও সিজারিয়ান",
            "জরায়ুর সিস্ট, টিউমার, ফাইব্রয়েড ও পিরিয়ড জটিলতা",
            "বন্ধ্যাত্ব নির্ণয়, ফার্টিলিটি কাউন্সিলিং ও ট্রিটমেন্ট",
            "জরায়ু ক্যান্সার স্ক্রিনিং ও প্যাসিভ স্ক্রিয়ার (Pap Smear)"
        ],
        tech: [
            "৪ডি কালার ডপলার ফিটাল আল্ট্রাসাউন্ড",
            "ফিটাল মেটারনাল মনিটরিং কার্ডিওটোকোগ্রাফি (CTG)",
            "আধুনিক সুসজ্জিত লেবার ওয়ার্ড ও ক্র্যাডল ওটি"
        ],
        schedule: "প্রতিদিন সকাল ৯:৩০ - রাত ৮:৩০ (ওপিডি)",
        room: "কক্ষ ৩০২, ৩য় তলা",
        doctors: [
            { name: "ডা. শশাঙ্ক নাগ", deg: "MBBS, DGO, FCPS (গাইনি)", title: "কনসালটেন্ট গাইনিকোলজিস্ট", link: "doctors/05.html" },
            { name: "ডা. পাব্রি সরকার", deg: "MBBS, BCS, FCPS (OBGYN)", title: "সহকারী অধ্যাপক, গাইনি ও প্রসূতি", link: "doctors/12.html" }
        ]
    },
    ortho: {
        id: "ortho",
        name: "অর্থোপেডিক্স বিভাগ",
        nameEn: "Department of Orthopedics & Joint Care",
        badge: "হাড় ও ট্রমা কেয়ার",
        image: "images/departments/dept-ortho.jpg",
        icon: "fa-bone",
        tagline: "হাড়-জোড়া, ভাঙা-মচকা, বাতব্যথা ও স্পাইনাল কেয়ার",
        description: "হাড় ভাঙা বা ফ্র্যাকচার, জয়েন্ট রি-কনস্ট্রাকশন, হাঁটু ও কোমরের দীর্ঘমেয়াদী বাতব্যথা, স্পাইনাল কর্ড ডিসঅর্ডার ও ট্রমা রোগীদের নিরাময়ে অর্থোপেডিক্স বিভাগ সর্বাধুনিক ফিক্সেশন ও রিহ্যাবিলিটেশন সেবা নিশ্চিত করে।",
        services: [
            "প্লাস্টার, ডিসলোকেশন ফিক্সেশন ও ট্রমা কেয়ার",
            "আর্থ্রাইটিস, হাঁটু ও পিঠের বাতব্যথা থেরাপি",
            "হাড় জোড়া লাগানোর আধুনিক ইন্টারনাল ফিক্সেশন সার্জারি",
            "স্পোর্টস ইনজুরি ও লিগামেন্ট টিয়ার ট্রিটমেন্ট",
            "ফিজিওথেরাপি ও পোস্ট-অপারেটিভ রিহ্যাব পরামর্শ"
        ],
        tech: [
            "ডিজিটাল এক্স-রে (High Resolution Flat Panel)",
            "সার্জিক্যাল গাইডেন্সের জন্য ইন্ট্রা-ওপ সি-আর্ম (C-Arm)",
            "ফিজিওথেরাপি ও স্পাইনাল ট্রাকশন থেরাপি ইকুইপমেন্ট"
        ],
        schedule: "প্রতিদিন সকাল ১০:০০ - রাত ৯:০০ (ওপিডি)",
        room: "কক্ষ ১০৫, ১ম তলা",
        doctors: [
            { name: "ডা. মোঃ রফিকুল ইসলাম", deg: "MBBS, MS (Orthopedics)", title: "সহযোগী অধ্যাপক ও বিভাগীয় প্রধান", link: "doctors/06.html" },
            { name: "ডা. উৎপল নাগ", deg: "MBBS, D-Ortho", title: "অর্থোপেডিক ও ট্রমা সার্জন", link: "doctors/07.html" }
        ]
    },
    ent: {
        id: "ent",
        name: "ইএনটি (নাক, কান, গলা) বিভাগ",
        nameEn: "Department of ENT & Head-Neck Surgery",
        badge: "মাইক্রো-সার্জারি ইউনিট",
        image: "images/departments/dept-ent.jpg",
        icon: "fa-ear-listen",
        tagline: "নাক, কান, গলা ও হেড-নেক সমস্যার আধুনিক চিকিৎসা",
        description: "নাক বন্ধ থাকা, সাইনুসাইটিস, কানে কম শোনা, কানে পুঁজ পড়া, টনসিল ইনফেকশন, থাইরয়েড ও গলার স্বর ভাঙাসহ হেড-নেকের যেকোনো জটিলতায় আধুনিক এন্ডোস্কোপিক ও মাইক্রো-সার্জারির মাধ্যমে সুচিকিৎসা প্রদান করা হয়।",
        services: [
            "টনসিল ও এডিনয়েড অপারেশন (Micro-Debrider Surgery)",
            "কানের পর্দা ফাঁটা ও কান পাকা রোগের মাইক্রোস্কোপিক অপারেশন",
            "নাকের বাঁকা হাড় (DNS) ও সাইনাস এন্ডোস্কোপিক ক্যারেকশন",
            "থাইরয়েড গ্রন্থি ও হেড-নেক টিউমার স্ক্রিনিং ও অস্ত্রোপচার",
            "শোনার ক্ষমতা পরীক্ষা (Audiometry & Tympanometry)"
        ],
        tech: [
            "ভিডিও এন্ডোস্কোপিক ইএনটি সাকশন ও ক্যাম ক্যামেরা",
            "সাউন্ড-প্রুফ অডিওমেট্রি রুম ও টিম্পানোমিটার",
            "সার্জিক্যাল অপারেটিং মাইক্রোস্কোপ"
        ],
        schedule: "শনিবার - বৃহস্পতিবার বিকাল ৪:০০ - রাত ৮:০০",
        room: "কক্ষ ২০২, ২য় তলা",
        doctors: [
            { name: "ডা. সৌরভ নাগ", deg: "MBBS, DLO, FCPS (ENT)", title: "ইএনটি ও হেড-নেক সার্জন", link: "doctors/08.html" },
            { name: "ডা. ইমতিয়াজ উদ্দিন", deg: "MBBS, BCS, MS (ENT)", title: "সহকারী অধ্যাপক, ইএনটি বিভাগ", link: "doctors/11.html" }
        ]
    },
    derma: {
        id: "derma",
        name: "চর্ম ও যৌন বিভাগ",
        nameEn: "Department of Dermatology & Venereology",
        badge: "স্কিন ও অ্যালার্জি ক্লিনিক",
        image: "images/departments/dept-derma.jpg",
        icon: "fa-hand-dots",
        tagline: "ত্বক, চুল, নখ ও অ্যালার্জি রোগের স্থায়ী ও গোপনীয় সমাধান",
        description: "দীর্ঘস্থায়ী চর্মরোগ, অ্যাকনি/ব্রণ, এলার্জিক র্যাশ, সোরিয়াসিস, চুল পড়া এবং গোপন যৌন রোগের নির্ভুল ডায়াগনোসিস ও গোপনীয়তা বজায় রেখে বিশেষজ্ঞ চিকিৎসকের পরামর্শ সেবা।",
        services: [
            "ব্রণ, ডার্ক স্পট ও পিগমেন্টেশন লেজার কেয়ার",
            "সোরিয়াসিস, এক্সিমা ও ক্রনিক অ্যালার্জি কন্ট্রোল",
            "চুল পড়া বন্ধ ও স্কাল্প হেলথ ট্রিটমেন্ট (PRP Therapy)",
            "আঁচিল, তিল ও স্কিন ট্যাগ ক্যাউটারি রিমুভাল",
            "যৌন স্বাস্থ্য ও গুপ্তরোগের ১০০% গোপনীয় বিশেষজ্ঞ চিকিৎসা"
        ],
        tech: [
            "ডিজিটাল ডার্মাটোস্কোপ (High Zoom Magnifier)",
            "ইলেকট্রো-কাউটারি ও রেডিওফ্রিকোয়েন্সি স্কিন কাট",
            "অ্যালার্জি টেস্ট কিট ও থেরাপিউটিক লাইট সেটআপ"
        ],
        schedule: "প্রতিদিন বিকাল ৩:০০ - রাত ৮:৩০ (ওপিডি)",
        room: "কক্ষ ১০৮, ১ম তলা",
        doctors: [
            { name: "ডা. নাহিদ বাদশা", deg: "MBBS, DDV (Dermatology)", title: "চর্ম, অ্যালার্জি ও যৌন রোগ বিশেষজ্ঞ", link: "doctors/09.html" },
            { name: "ডা. হরিচাঁদ শীল", deg: "MBBS, FCPS (Skin & VD)", title: "কনসালটেন্ট ডার্মাটোলজিস্ট", link: "doctors/10.html" }
        ]
    },
    gp: {
        id: "gp",
        name: "জেনারেল প্র্যাকটিশনার বিভাগ",
        nameEn: "Primary Care & General Medicine OPD",
        badge: "২৪/৭ প্রাইমারি কেয়ার",
        image: "images/departments/dept-gp.jpg",
        icon: "fa-house-medical",
        tagline: "পারিবারিক প্রাথমিক স্বাস্থ্যসেবা ও দ্রুত চিকিৎসা সাপোর্ট",
        description: "পারিবারিক প্রাথমিক পরামর্শ, শিশু স্বাস্থ্য, সাধারণ শারীরিক অসুস্থতা ও ট্রায়াজ মূল্যায়নের জন্য আমাদের জেনারেল প্র্যাকটিশনার টিম সার্বক্ষণিক প্রস্তুত। প্রয়োজন অনুযায়ী বিশেষজ্ঞ ডাক্তারের কাছে রেফারেল সুবিধা প্রদান করা হয়।",
        services: [
            "সাধারণ জ্বর, কাশি, এলার্জি ও পেটের সমস্যা সমাধান",
            "ডায়াবেটিস ও প্রেশার মনিটরিং এবং ওষুধ নির্দেশিকা",
            "ছোটখাটো আঘাতের ক্ষতে সেলাই, ড্রেসিং ও ব্যান্ডেজ",
            "প্রিভেন্টিভ ভ্যাকসিনেশন ও হেলথ কার্ড সুবিধা",
            "জরুরি রোগীকে সঠিক বিভাগে রেফারেল সহায়তা"
        ],
        tech: [
            "মাল্টি-প্যারামিটার ভাইটাল সাইনস মনিটর",
            "ডিজিটাল গ্লুকোমিটার ও ইমার্জেন্সি নেবুলাইজার",
            "প্রাইমারি ফার্স্ট-এইড ট্রায়াজ বেড"
        ],
        schedule: "২৪ ঘণ্টা ৭ দিন খোলা (ইমার্জেন্সি ও ওপিডি)",
        room: "কক্ষ ১০০, নিচ তলা",
        doctors: [
            { name: "ডা. নুরুল আলম", deg: "MBBS, PGT (Medicine)", title: "মেডিকেল অফিসার, ওপিডি", link: "doctors/13.html" },
            { name: "ডা. শংকর দে", deg: "MBBS, CCD", title: "মেডিকেল অফিসার, ওপিডি", link: "doctors/14.html" }
        ]
    },
    sono: {
        id: "sono",
        name: "আল্ট্রাসনোগ্রাফি বিভাগ",
        nameEn: "Department of Ultrasonography & Imaging",
        badge: "হাই-রেজুলেশন ৪ডি",
        image: "images/departments/dept-usg.jpg",
        icon: "fa-wave-square",
        tagline: "নির্ভুল, দ্রুত ও উন্নত ৪ডি আল্ট্রাসাউন্ড টেস্ট সার্ভিস",
        description: "দক্ষ ও অভিজ্ঞ সোনোলজিস্টদের তত্ত্বাবধানে সর্বাধুনিক ৪D কালার ডপলার মেশিনের সাহায্যে গর্ভাবস্থার রিপোর্ট, পেট ও অন্যান্য অঙ্গপ্রত্যঙ্গের নির্ভুল ইমেজিং করা হয়।",
        services: [
            "গর্ভস্থ সন্তানের ৪ডি কালার ডপলার টেস্ট ও এনোমালি স্ক্যান",
            "হোল অ্যাবডোমেন, পেটে ব্যথা ও গলব্লাডার USG",
            "কিডনি, ইউরেটার, প্রোস্টেট ও ব্লাডার স্ক্যান",
            "থাইরয়েড, ব্রেস্ট ও সফট টিস্যু আল্ট্রাসাউন্ড",
            "দ্রুততম সময়ে সঠিক ডিজিটাল রিপোর্ট প্রদান"
        ],
        tech: [
            "GE/Mindray ৪D কালার ডপলার আল্ট্রাসাউন্ড মেশিন",
            "হাই-ফ্রিকোয়েন্সি লিনিয়ার ও ভ্যাজাইনাল প্রোব (TVS)",
            "ডিজিটাল পিএসিএস (PACS) ও হাই-ডেফিনিশন থার্মাল প্রিন্টিং"
        ],
        schedule: "প্রতিদিন সকাল ৮:৩০ - রাত ৯:৩০",
        room: "কক্ষ ১১০, নিচ তলা",
        doctors: [
            { name: "ডা. শশাঙ্ক নাগ", deg: "MBBS, DMU (Ultra), FCPS", title: "কনসালটেন্ট সোনোলজিস্ট", link: "doctors/05.html" },
            { name: "ডা. পাব্রি সরকার", deg: "MBBS, CMU (Sonology)", title: "কনসালটেন্ট সোনোলজিস্ট", link: "doctors/12.html" }
        ]
    }
};

window.openDeptProfile = function(deptId) {
    const data = DEPARTMENT_DATA[deptId];
    if (!data) return;

    const modal = document.getElementById('deptModal');
    const backdrop = document.getElementById('deptModalBackdrop');
    if (!modal || !backdrop) return;

    document.getElementById('deptModalImg').src = data.image;
    document.getElementById('deptModalBadge').textContent = data.badge;
    document.getElementById('deptModalIcon').className = 'fa-solid ' + data.icon;
    document.getElementById('deptModalTitle').textContent = data.name;
    document.getElementById('deptModalSubTitle').textContent = data.nameEn;
    document.getElementById('deptModalTagline').textContent = data.tagline;

    document.getElementById('deptModalDesc').textContent = data.description;

    const sList = document.getElementById('deptModalServices');
    sList.innerHTML = '';
    data.services.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `<i class="fa-solid fa-circle-check"></i> <span>${item}</span>`;
        sList.appendChild(li);
    });

    const tList = document.getElementById('deptModalTech');
    tList.innerHTML = '';
    data.tech.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `<i class="fa-solid fa-microscope"></i> <span>${item}</span>`;
        tList.appendChild(li);
    });

    document.getElementById('deptModalSchedule').textContent = data.schedule;
    document.getElementById('deptModalRoom').textContent = data.room;

    const dGrid = document.getElementById('deptModalDoctors');
    dGrid.innerHTML = '';
    if (data.doctors && data.doctors.length > 0) {
        data.doctors.forEach(doc => {
            const div = document.createElement('div');
            div.className = 'dept-doc-chip';
            div.innerHTML = `
                <div class="dept-doc-chip-info">
                    <h4>${doc.name}</h4>
                    <p>${doc.deg}</p>
                </div>
                <a href="${doc.link}" class="dept-doc-chip-btn">
                    <i class="fa-solid fa-user-doctor"></i> প্রোফাইল
                </a>
            `;
            dGrid.appendChild(div);
        });
    } else {
        dGrid.innerHTML = '<p class="text-muted">এই মুহূর্তে নির্ধারিত কনসালটেন্ট তথ্য প্রক্রিয়াধীন।</p>';
    }

    backdrop.classList.add('active');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
};

window.closeDeptModal = function() {
    const modal = document.getElementById('deptModal');
    const backdrop = document.getElementById('deptModalBackdrop');
    if (modal) modal.classList.remove('active');
    if (backdrop) backdrop.classList.remove('active');
    document.body.style.overflow = '';
};

window.filterDoctorsByDept = function(deptId) {
    const pills = document.querySelectorAll('#filterPills .filter-pill, .filter-tab');
    if (pills.length) {
        pills.forEach(pill => {
            const cat = pill.getAttribute('data-filter');
            if (cat === deptId) {
                pill.click();
            }
        });
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const backdrop = document.getElementById('deptModalBackdrop');
    if (backdrop) {
        backdrop.addEventListener('click', window.closeDeptModal);
    }
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            window.closeDeptModal();
        }
    });
});

/* =========================================
   SPECIALIZED DIAGNOSTIC DATA & MODAL LOGIC
   ========================================= */

const DIAGNOSTIC_DATA = {
    pathology: {
        id: "pathology",
        name: "ক্লিনিক্যাল প্যাথলজি ল্যাব",
        nameEn: "Clinical Pathology & Hematology Laboratory",
        badge: "অটোমেটেড প্যাথলজি",
        image: "images/diagnostic/diag-pathology.jpg",
        icon: "fa-microscope",
        tagline: "শতভাগ স্যাম্পল অটোমেশন ও নির্ভুল প্যাথলজিক্যাল ডায়াগনোসিস",
        tests: [
            "সিবিসি (CBC) ও ইএসআর (ESR) অ্যানালাইসিস",
            "ইউরিন রুটিন ও মাইক্রোস্কোপিক পরীক্ষা (Urine R/E)",
            "স্টুল আরই ও অকাল্ট ব্লাড টেস্ট (Stool R/E & OBT)",
            "ব্লাড গ্রুপিং ও ক্রস-ম্যাচিং (Blood Grouping)",
            "কফ ও বডি ফ্লুইড সাইটোলজি পরীক্ষা"
        ],
        prep: [
            "রুটিন সিবিসি বা ইউরিন টেস্টের জন্য সাধারণত বিশেষ না খেয়ে আসার প্রয়োজন নেই।",
            "প্রস্রাব পরীক্ষার জন্য প্রথম সকালের পরিষ্কার মিড-স্ট্রিম প্রস্রাবের নমুনা সর্বোত্তম।"
        ],
        tech: [
            "Sysmex ৫-পার্ট অটোমেটেড হেমাটোলজি অ্যানালাইজার",
            "হাই-রেজুলেশন বায়োমেডিকেল স্টেরিও মাইক্রোস্কোপ",
            "বারকোড-সিস্টেম স্যাম্পল ট্র্যাকিং সফটওয়্যার"
        ],
        delivery: "স্যাম্পল জমা দেওয়ার ২ থেকে ৪ ঘণ্টার মধ্যে",
        location: "নিচ তলা, ডায়াগনস্টিক ব্লক (কক্ষ ১০২)"
    },
    usg: {
        id: "usg",
        name: "আল্ট্রাসনোগ্রাফি (USG) ও ইকো",
        nameEn: "Ultrasonography & Echocardiography Unit",
        badge: "৪ডি কালার ডপলার",
        image: "images/diagnostic/diag-usg.jpg",
        icon: "fa-wave-square",
        tagline: "উচ্চ রেজুলেশনের ৪ডি কালার ডপলার ও রিয়েল-টাইম ফিটাল ইমেজিং",
        tests: [
            "গর্ভবতী মায়েদের ৪ডি কালার ডপলার ও অ্যানোমালি স্ক্যান",
            "হোল অ্যাবডোমেন ও লোয়ার অ্যাবডোমেন USG",
            "কিডনি, ইউরেটার ও প্রস্টেট (KUB) স্ক্যান",
            "ব্রেস্ট, থাইরয়েড ও স্মল পার্টস আল্ট্রাসাউন্ড",
            "টু-ডি ইকোকার্ডিওগ্রাম (2D Echo & Doppler)"
        ],
        prep: [
            "পেটের (Whole Abdomen/KUB) আল্ট্রাসাউন্ডের জন্য পরীক্ষা করার আগে প্রচুর পানি পান করে প্রস্রাবের চাপ রাখতে হবে।",
            "ফাস্টিং USG-এর জন্য সকালের পরীক্ষার আগে ৬-৮ ঘণ্টা খালি পেটে থাকতে হবে।"
        ],
        tech: [
            "GE / Mindray হাই-এন্ড ৪D HD কালার ডপলার আল্ট্রাসাউন্ড",
            "মাল্টি-ফ্রিকোয়েন্সি কনভেক্স, লিনিয়ার ও টিভিএস (TVS) প্রোব",
            "হাই-ডেফিনিশন থার্মাল ইমেজ প্রিন্টার"
        ],
        delivery: "পরীক্ষা সম্পন্ন হওয়ার ১৫ থেকে ৩০ মিনিটের মধ্যে",
        location: "নিচ তলা, রুম ১১০ (USG রুম)"
    },
    ecg: {
        id: "ecg",
        name: "ডিজিটাল ইসিজি (ECG) ল্যাব",
        nameEn: "Digital ECG & Cardiac Diagnostic Unit",
        badge: "ডিজিটাল হৃদরোগ ইউনিট",
        image: "images/diagnostic/diag-ecg.jpg",
        icon: "fa-heart-pulse",
        tagline: "হৃদপিণ্ডের ইলেকট্রিক্যাল অ্যাক্টিভিটির সুনির্দিষ্ট ১২-লিড ট্র্যাকিং",
        tests: [
            "১২-লিড স্ট্যান্ডার্ড ডিজিটাল ইসিজি (12-Lead ECG)",
            "হার্ট রেট ভ্যারিয়াবিলিটি ও অ্যারিথমিয়া ডিটেকশন",
            "প্রি-অপারেটিভ কার্ডিয়াক ইসিজি ক্লিয়ারেন্স",
            "জরুরি চেস্ট পেইন ও ইমার্জেন্সি ইসিজি টেস্ট"
        ],
        prep: [
            "ইসিজি টেস্টের জন্য কোনো বিশেষ ডায়েট বা ফাস্টিং-এর প্রয়োজন নেই।",
            "পরীক্ষার সময় ঢিলেঢালা পোশাক পরা সুবিধাজনক।"
        ],
        tech: [
            "১২-চ্যানেল ডিজিটাল কম্পিউটারাইজড ইসিজি মেশিন",
            "কার্ডিওগ্রাফিক ফিল্টারিং ও স্পাইক রিডাকশন অ্যালগরিদম",
            "তাত্ক্ষণিক থার্মাল প্রিন্টআউট ও ডিজিটাল রেকর্ড"
        ],
        delivery: "টেস্ট শেষের ৫ থেকে ১০ মিনিটের মধ্যে",
        location: "নিচ তলা, ইসিজি রুম (কক্ষ ১০৪)"
    },
    xray: {
        id: "xray",
        name: "ডিজিটাল এক্স-রে (High-Res)",
        nameEn: "Digital Radiography & X-Ray Unit",
        badge: "হাই-রেজুলেশন এক্স-রে",
        image: "images/diagnostic/diag-xray.jpg",
        icon: "fa-x-ray",
        tagline: "কম রেডিয়েশনে ক্রিস্টাল ক্লিয়ার ডিজিটাল ইমেজিং ও বোনস ডিটেইলিং",
        tests: [
            "চেস্ট (বুক) এক্স-রে (PA & Lateral View)",
            "হাড়ের ফ্র্যাকচার ও জয়েন্ট এক্স-রে (Knee, Spine, Shoulder)",
            "প্যারান্যাসাল সাইনাস (PNS) ও স্কাল এক্স-রে",
            "অ্যাবডোমেন ও কোমর এক্স-রে (KUB / Erect view)"
        ],
        prep: [
            "এক্স-রে কক্ষে প্রবেশের সময় ঘড়ি, চেইন, ধাতব বোতাম বা অলঙ্কার খুলে রাখতে হবে।",
            "গর্ভবতী মহিলাদের এক্স-রে করানোর আগে টেকনোলজিস্টকে জানাতে হবে।"
        ],
        tech: [
            "হাই-রেজুলেশন ডিজিটাল ফ্ল্যাট প্যানেল ডিটেক্টর (CR/DR)",
            "মিনিমাম রেডিয়েশন এক্সপোজার টেকনোলজি",
            "লেজার ডিজিটাল ফিল্ম প্রসেসর"
        ],
        delivery: "পরীক্ষার ৩০ থেকে ৪৫ মিনিটের মধ্যে",
        location: "নিচ তলা, এক্স-রে রুম (কক্ষ ১০৩)"
    },
    biochem: {
        id: "biochem",
        name: "বায়োকেমিস্ট্রি ল্যাব",
        nameEn: "Clinical Biochemistry & Metabolic Diagnostic Lab",
        badge: "অটোমেটেড অ্যানালাইজার",
        image: "images/diagnostic/diag-biochem.jpg",
        icon: "fa-droplet",
        tagline: "মেটাবলিক ডিসঅর্ডার, রক্তে শর্করা, লিভার ও কিডনির নির্ভুল অ্যানালাইসিস",
        tests: [
            "ফাস্টিং (FBS) ও ২ ঘণ্টা পরের ব্লাড সুগার (2hABF)",
            "লিপিড প্রোফাইল (Cholesterol, Triglyceride, HDL, LDL)",
            "লিভার ফাংশন টেস্ট - LFT (Bilirubin, SGPT, SGOT, ALK)",
            "কিডনি ফাংশন টেস্ট - KFT (Creatinine, Urea, Uric Acid)",
            "ইলেক্ট্রোলাইটস (Sodium, Potassium, Chloride)"
        ],
        prep: [
            "ফাস্টিং সুগার ও লিপিড প্রোফাইল টেস্টের জন্য ৮ থেকে ১২ ঘণ্টা খালি পেটে আসতে হবে (শুধু পানি পান করা যাবে)।"
        ],
        tech: [
            "Fully-Automated কেমিলাইট বায়োকেমিস্ট্রি অটো-অ্যানালাইজার",
            "আয়ন সেলেক্টিভ ইলেকট্রোড (ISE) ইলেকট্রোলাইট রিডার",
            "প্রিসিশন পাইপেটিং রোবোটিক্স"
        ],
        delivery: "স্যাম্পল সংগ্রহের ৩ থেকে ৫ ঘণ্টার মধ্যে",
        location: "নিচ তলা, বায়োকেমিস্ট্রি উইং (কক্ষ ১০৬)"
    },
    hormone: {
        id: "hormone",
        name: "হরমোন ও ইমিউনোলজি টেস্ট",
        nameEn: "Hormonology & Specialized Immunology Lab",
        badge: "ইমিউনোলজি কেয়ার",
        image: "images/diagnostic/diag-hormone.jpg",
        icon: "fa-vial-virus",
        tagline: "থাইরয়েড, প্রজনন হরমোন, ভিটামিন ও টিউমার মার্কারের সুনির্দিষ্ট পরীক্ষা",
        tests: [
            "থাইরয়েড প্রোফাইল (FT3, FT4, TSH)",
            "ডায়াবেটিক গড় ট্র্যাকিং (HbA1c)",
            "ভিটামিন ডি৩ (Vitamin D3) ও ভিটামিন বি১২",
            "ফার্টিলিটি হরমোনস (FSH, LH, Prolactin, Testosterone)",
            "টিউমার মার্কারস (PSA, CEA, CA-125)"
        ],
        prep: [
            "HbA1c বা থাইরয়েড টেস্টের জন্য খালি পেটে থাকার প্রয়োজন নেই, তবে সকালের স্যাম্পল উত্তম।",
            "হরমোনের ওষুধ খেলে টেস্টের আগে চিকিৎসককে অবহিত করুন।"
        ],
        tech: [
            "Chemiluminescence Immunoassay (CLIA) অটো-অ্যানালাইজার",
            "উচ্চ সংবেদনশীল রিএজেন্ট কিটস",
            "কম্পিউটারাইজড কোয়ালিটি কন্ট্রোল স্ট্যাটিস্টিক্স"
        ],
        delivery: "একই দিন বিকালে অথবা সর্বোচ্চ ২৪ ঘণ্টার মধ্যে",
        location: "নিচ তলা, হরমোন ল্যাব (কক্ষ ১০৭)"
    }
};

window.openDiagProfile = function(diagId) {
    const data = DIAGNOSTIC_DATA[diagId];
    if (!data) return;

    const modal = document.getElementById('diagModal');
    const backdrop = document.getElementById('diagModalBackdrop');
    if (!modal || !backdrop) return;

    document.getElementById('diagModalImg').src = data.image;
    document.getElementById('diagModalBadge').textContent = data.badge;
    document.getElementById('diagModalIcon').className = 'fa-solid ' + data.icon;
    document.getElementById('diagModalTitle').textContent = data.name;
    document.getElementById('diagModalSubTitle').textContent = data.nameEn;
    document.getElementById('diagModalTagline').textContent = data.tagline;

    const tList = document.getElementById('diagModalTests');
    tList.innerHTML = '';
    data.tests.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `<i class="fa-solid fa-vial"></i> <span>${item}</span>`;
        tList.appendChild(li);
    });

    const pList = document.getElementById('diagModalPrep');
    pList.innerHTML = '';
    data.prep.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `<i class="fa-solid fa-circle-info"></i> <span>${item}</span>`;
        pList.appendChild(li);
    });

    const techList = document.getElementById('diagModalTech');
    techList.innerHTML = '';
    data.tech.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `<i class="fa-solid fa-gears"></i> <span>${item}</span>`;
        techList.appendChild(li);
    });

    document.getElementById('diagModalDelivery').textContent = data.delivery;
    document.getElementById('diagModalLocation').textContent = data.location;

    backdrop.classList.add('active');
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
};

window.closeDiagModal = function() {
    const modal = document.getElementById('diagModal');
    const backdrop = document.getElementById('diagModalBackdrop');
    if (modal) modal.classList.remove('active');
    if (backdrop) backdrop.classList.remove('active');
    document.body.style.overflow = '';
};

document.addEventListener('DOMContentLoaded', () => {
    const dBackdrop = document.getElementById('diagModalBackdrop');
    if (dBackdrop) {
        dBackdrop.addEventListener('click', window.closeDiagModal);
    }
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            window.closeDiagModal();
        }
    });
});

/* =========================================
   INLINE SCRIPTS MOVED FROM FOOTER
   ========================================= */
document.addEventListener('DOMContentLoaded', () => {
  if ('IntersectionObserver' in window) {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -50px 0px' });
    document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
  }
  
  const st = document.getElementById('scrollTop');
  if (st) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) st.classList.add('show'); else st.classList.remove('show');
    });
  }
  
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
  
  const di = document.querySelector('input[type="date"]');
  if (di) di.setAttribute('min', new Date().toISOString().split('T')[0]);
  
  const pills = document.querySelectorAll('#filterPills .filter-pill');
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
  
  const form = document.getElementById('appointmentForm');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const req = form.querySelectorAll('[required]');
      let ok = true;
      req.forEach(f => { if (!f.value.trim()) { f.style.borderColor='#e74c3c'; ok=false; } else f.style.borderColor=''; });
      if (!ok) return;
      const success = document.getElementById('formSuccess');
      if (success) {
        success.classList.add('show');
        setTimeout(() => success.classList.remove('show'), 6000);
      }
      form.reset();
    });
  }
  
  const menuBtn = document.querySelector('.menu-toggle');
  const navList = document.querySelector('.nav-list');
  if (menuBtn && navList) {
    menuBtn.addEventListener('click', () => {
      const isOpen = navList.style.display === 'flex';
      navList.style.display = isOpen ? '' : 'flex';
      navList.style.flexDirection = 'column';
      navList.style.position = 'absolute';
      navList.style.top = '100%';
      navList.style.left = '0';
      navList.style.right = '0';
      navList.style.background = '#fff';
      navList.style.padding = '14px 20px';
      navList.style.boxShadow = '0 8px 24px rgba(0,80,130,0.10)';
    });
  }
});


