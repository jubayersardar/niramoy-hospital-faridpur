/* =====================================================
   NIRAMAYA Hospital & Diagnostic Center, Faridpur
   Shared Main Script (site.js)
   ===================================================== */

(function () {
  'use strict';

  // ===== 1. Master Doctors Data =====
  const DOCTORS_DATA = [
    { id: "01", slug: "dr-abu-bakar-siddique", name: "ডা. আবু বকর সিদ্দিক", dept: "med", deptName: "মেডিসিন", deg: "MBBS, BCS, MD (Internal Medicine)", desg: "সহকারী অধ্যাপক, মেডিসিন বিভাগ", days: "প্রতিদিন বিকাল ৪:০০ - রাত ৮:০০", room: "কক্ষ ১০১" },
    { id: "02", slug: "dr-riad-hossain-bappi", name: "ডা. মোঃ রিয়াদ হোসেন বাপ্পি", dept: "med", deptName: "মেডিসিন", deg: "MBBS, BCS, CCD, FCPS (মেডিসিন)", desg: "সহকারী রেজিস্টার, মেডিসিন বিভাগ", days: "শনি - বৃহস্পতি বিকাল ৩:০০ - রাত ৮:০০", room: "কক্ষ ১০২" },
    { id: "03", slug: "dr-srabanti-m-islam", name: "ডা. শ্রাবন্তী এম ইসলাম", dept: "gynae", deptName: "গাইনি ও প্রসূতি", deg: "MBBS, BCS, MCPS, FCPS, MRCOG (শেষ বর্ষ)", desg: "কনসালটেন্ট, গাইনি ও প্রসূতি", days: "প্রতিদিন সকাল ১০:০০ - বিকাল ৩:০০", room: "কক্ষ ৩০১" },
    { id: "04", slug: "dr-moin-uddin", name: "ডা. মো. মঈন উদ্দিন", dept: "ortho", deptName: "অর্থোপেডিক্স", deg: "MBBS, D-Ortho, FCPS (USA)", desg: "সহযোগী অধ্যাপক ও বিভাগীয় প্রধান, অর্থোপেডিক বিভাগ", days: "শনি - বৃহস্পতি বিকাল ৪:৩০ - রাত ৮:৩০", room: "কক্ষ ২০৩" },
    { id: "05", slug: "dr-shashanka-nag", name: "ডা. শশাঙ্ক নাগ (সনেট)", dept: "med", deptName: "মেডিসিন", deg: "MBBS, CCD, DMU, PGT", desg: "মেডিসিন, ডায়াবেটিস ও রোগ বিশেষজ্ঞ", days: "প্রতিদিন সকাল ৯:০০ - দুপুর ২:০০ ও বিকাল ৫:০০ - রাত ৯:০০", room: "কক্ষ ১০৩" },
    { id: "06", slug: "dr-rafiqul-islam", name: "ডা. মোহাম্মদ রফিকুল ইসলাম", dept: "med", deptName: "মেডিসিন", deg: "MBBS, MPH, CCD, PHD (USA)", desg: "সহযোগী অধ্যাপক ও বিভাগীয় প্রধান, কমিউনিটি মেডিসিন", days: "শনি - বৃহস্পতি বিকাল ৫:০০ - রাত ৮:৩০", room: "কক্ষ ১০৪" },
    { id: "07", slug: "dr-utpal-nag", name: "ডা. উৎপল নাগ", dept: "surg", deptName: "সার্জারি", deg: "MBBS, BCS, PGT, FCPS, FRSH", desg: "আর এস সার্জন, জেনারেল ও ল্যাপারোস্কোপিক সার্জারি", days: "প্রতিদিন বিকাল ৪:০০ - রাত ৮:০০", room: "কক্ষ ২০৪" },
    { id: "08", slug: "dr-abu-saleh-sourav", name: "ডা. আবু সালে আহমেদ সৌরভ", dept: "surg", deptName: "সার্জারি", deg: "MBBS, BCS, FCPS, MRCS", desg: "জেনারেল ও ল্যাপারোস্কোপিক সার্জন", days: "শনি - বৃহস্পতি বিকাল ৩:৩০ - রাত ৭:৩০", room: "কক্ষ ২০৫" },
    { id: "09", slug: "dr-nahid-badsha", name: "ডা. নাহিদ বাদশা", dept: "ortho", deptName: "অর্থোপেডিক্স", deg: "MBBS, BCS, MS (অর্থোপেডিক)", desg: "আবাসিক সার্জন (D-অর্থোপেডিক)", days: "প্রতিদিন বিকাল ৪:০০ - রাত ৯:০০", room: "কক্ষ ২০২" },
    { id: "10", slug: "dr-harichand-sheel", name: "ডা. হরিচাঁদ শীল", dept: "gp", deptName: "জেনারেল প্র্যাকটিশনার", deg: "MBBS, BMC", desg: "অধ্যক্ষ, জেনারেল প্র্যাকটিশনার", days: "প্রতিদিন সকাল ৯:০০ - দুপুর ১:০০ ও বিকাল ৪:০০ - রাত ৮:০০", room: "কক্ষ ১০০" },
    { id: "11", slug: "dr-syed-imtiaz-uddin", name: "ডা. সৈয়দ ইমতিয়াজ উদ্দিন", dept: "ent", deptName: "ইএনটি", deg: "MBBS, BCS, DLO", desg: "গলা রোগ বিশেষজ্ঞ ও হেড-নেক সার্জন", days: "শনি - বৃহস্পতি বিকাল ৪:০০ - রাত ৮:০০", room: "কক্ষ ১০৮" },
    { id: "12", slug: "dr-papri-sarkar", name: "ডা. পাপড়ী সরকার", dept: "gynae", deptName: "গাইনি ও প্রসূতি", deg: "MBBS, PGT", desg: "গাইনি ও স্ত্রীরোগ বিশেষজ্ঞ", days: "প্রতিদিন সকাল ১০:০০ - বিকাল ৪:০০", room: "কক্ষ ৩০২" },
    { id: "13", slug: "dr-sm-nur-e-alam", name: "ডা. এস এম নূর ই আলম (বিদ্যুৎ)", dept: "derma", deptName: "চর্ম ও যৌন", deg: "MBBS, BCS, PGT (চর্ম ও যৌন)", desg: "চর্ম, যৌন, সেক্স ও এলার্জি রোগে অভিজ্ঞ", days: "প্রতিদিন বিকাল ৩:০০ - রাত ৮:৩০", room: "কক্ষ ১০৯" },
    { id: "14", slug: "dr-shankar-kumar-dey", name: "ডা. শংকর কুমার দে", dept: "sono", deptName: "আল্ট্রাসনোগ্রাফি", deg: "MBBS, DNM", desg: "আল্ট্রাসনোগ্রাফি বিশেষজ্ঞ", days: "প্রতিদিন সকাল ৮:৩০ - রাত ৯:০০", room: "কক্ষ ১১০" }
  ];

  const DEPT_MAP = {
    "med": "মেডিসিন",
    "surg": "সার্জারি",
    "gynae": "গাইনি ও প্রসূতি",
    "ortho": "অর্থোপেডিক্স",
    "ent": "ইএনটি",
    "derma": "চর্ম ও যৌন",
    "gp": "জেনারেল প্র্যাকটিশনার",
    "sono": "আল্ট্রাসনোগ্রাফি"
  };

  const HOSPITAL_WHATSAPP = "8801731827110";
  const HOSPITAL_PHONE = "+8801729171549";
  const HOSPITAL_EMERGENCY = "+8801731827110";

  // ===== 2. Reveal animations =====
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

  // ===== 3. Scroll-to-top FAB =====
  const st = document.getElementById('scrollTop');
  if (st) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) st.classList.add('show');
      else st.classList.remove('show');
    });
  }

  // ===== 4. Year in footer =====
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // ===== 5. Min date for any date input =====
  const di = document.querySelectorAll('input[type="date"]');
  if (di.length) {
    const today = new Date().toISOString().split('T')[0];
    di.forEach(input => input.setAttribute('min', today));
  }

  // ===== 6. Mobile Menu Toggle =====
  const menuBtn = document.querySelector('.menu-toggle');
  const navList = document.querySelector('.nav-list');
  if (menuBtn && navList) {
    menuBtn.addEventListener('click', () => {
      const isOpen = navList.classList.contains('mobile-open');
      if (isOpen) {
        navList.classList.remove('mobile-open');
        navList.removeAttribute('style');
        document.body.style.overflow = '';
      } else {
        navList.classList.add('mobile-open');
        navList.style.cssText = 'display:flex;flex-direction:column;position:absolute;top:100%;left:0;right:0;background:#ffffff;padding:16px 20px;box-shadow:0 12px 30px rgba(0,50,90,0.15);z-index:1000;border-bottom:2px solid var(--primary);gap:8px;';
      }
    });

    document.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navList.classList.remove('mobile-open');
        navList.removeAttribute('style');
        document.body.style.overflow = '';
      });
    });
  }

  // ===== 7. Mobile Bottom Sticky Action Bar =====
  (function initMobileBottomBar() {
    if (!document.querySelector('.mobile-bottom-bar')) {
      const bar = document.createElement('div');
      bar.className = 'mobile-bottom-bar';
      const isSub = window.location.pathname.includes('/doctors/');
      const rootPrefix = isSub ? '../' : '';
      bar.innerHTML = `
        <div class="mobile-bottom-grid">
          <a href="tel:${HOSPITAL_EMERGENCY}" class="mobile-bottom-item call">
            <i class="fa-solid fa-phone-volume"></i>
            <span>ইমার্জেন্সি</span>
          </a>
          <a href="https://wa.me/${HOSPITAL_WHATSAPP}" target="_blank" rel="noopener" class="mobile-bottom-item whatsapp">
            <i class="fa-brands fa-whatsapp"></i>
            <span>WhatsApp</span>
          </a>
          <a href="${rootPrefix}appointment" class="mobile-bottom-item appoint">
            <i class="fa-regular fa-calendar-check"></i>
            <span>সিরিয়াল নিন</span>
          </a>
          <a href="https://maps.google.com/?q=নিরাময়+হাসপাতাল+ফরিদপুর" target="_blank" rel="noopener" class="mobile-bottom-item map">
            <i class="fa-solid fa-location-dot"></i>
            <span>লোকেশন</span>
          </a>
        </div>
      `;
      document.body.appendChild(bar);
    }
  })();

  // ===== 8. Filter Pills & Live Search on Doctors Page =====
  const pills = document.querySelectorAll('.filter-pill');
  const doctorGrid = document.getElementById('doctorsGrid');
  const doctorSearch = document.getElementById('doctorSearch');

  function filterDoctorCards() {
    if (!doctorGrid) return;
    const activePill = document.querySelector('.filter-pill.active');
    const filter = activePill ? activePill.getAttribute('data-filter') : 'all';
    const query = doctorSearch ? doctorSearch.value.trim().toLowerCase() : '';

    const cards = doctorGrid.querySelectorAll('.doctor-card');
    let visibleCount = 0;

    cards.forEach(card => {
      const photo = card.querySelector('.doctor-photo');
      const text = card.textContent.toLowerCase();
      const matchFilter = filter === 'all' || (photo && photo.classList.contains('bg-' + filter));
      const matchQuery = !query || text.includes(query);

      if (matchFilter && matchQuery) {
        card.style.display = '';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    let noResults = document.getElementById('noDoctorResults');
    if (visibleCount === 0) {
      if (!noResults) {
        noResults = document.createElement('div');
        noResults.id = 'noDoctorResults';
        noResults.style.cssText = 'grid-column:1/-1;text-align:center;padding:40px;color:var(--text-muted);font-size:1.1rem;';
        noResults.innerHTML = '<i class="fa-solid fa-user-slash" style="font-size:2.5rem;margin-bottom:12px;display:block;color:var(--border);"></i> কোনো ডাক্তার খুঁজে পাওয়া যায়নি। অনুগ্রহ করে ফিল্টার পরিবর্তন করুন।';
        doctorGrid.appendChild(noResults);
      }
      noResults.style.display = 'block';
    } else if (noResults) {
      noResults.style.display = 'none';
    }
  }

  if (pills.length && doctorGrid) {
    pills.forEach(pill => {
      pill.addEventListener('click', () => {
        pills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        filterDoctorCards();
      });
    });
  }
  if (doctorSearch) {
    doctorSearch.addEventListener('input', filterDoctorCards);
  }

  // ===== 9. Dynamic Appointment System & WhatsApp Booking =====
  const apptForm = document.getElementById('appointmentForm');
  const deptSelect = apptForm ? apptForm.querySelector('select[name="department"]') : null;
  const docSelect = document.getElementById('doctorSelect') || (apptForm ? apptForm.querySelector('select[name="doctor"]') : null);
  const waBookBtn = document.getElementById('whatsappBookBtn');

  function populateDoctorsDropdown(selectedDeptKey, selectedDocId) {
    if (!docSelect) return;
    const currentVal = selectedDocId || docSelect.value;
    docSelect.innerHTML = '<option value="">— ডাক্তার বাছাই করুন —</option>';

    const filtered = selectedDeptKey 
      ? DOCTORS_DATA.filter(d => d.dept === selectedDeptKey || d.deptName === selectedDeptKey)
      : DOCTORS_DATA;

    filtered.forEach(doc => {
      const opt = document.createElement('option');
      opt.value = doc.id;
      opt.textContent = `${doc.name} — ${doc.deptName}`;
      if (doc.id === currentVal) opt.selected = true;
      docSelect.appendChild(opt);
    });
  }

  if (apptForm && deptSelect && docSelect) {
    // Populate on dept change
    deptSelect.addEventListener('change', () => {
      const val = deptSelect.value;
      let deptKey = '';
      for (const [k, v] of Object.entries(DEPT_MAP)) {
        if (v === val || k === val) { deptKey = k; break; }
      }
      populateDoctorsDropdown(deptKey);
    });

    // Auto update dept when doctor is changed
    docSelect.addEventListener('change', () => {
      const docId = docSelect.value;
      const found = DOCTORS_DATA.find(d => d.id === docId);
      if (found && deptSelect) {
        for (let i = 0; i < deptSelect.options.length; i++) {
          const opt = deptSelect.options[i];
          if (opt.textContent.includes(found.deptName) || opt.value === found.dept || opt.value === found.deptName) {
            deptSelect.selectedIndex = i;
            break;
          }
        }
      }
    });

    // Check URL parameters (e.g. appointment.html?doc=03 or ?dept=gynae)
    const urlParams = new URLSearchParams(window.location.search);
    const paramDoc = urlParams.get('doc');
    const paramDept = urlParams.get('dept');

    if (paramDoc) {
      const foundDoc = DOCTORS_DATA.find(d => 
        d.slug === paramDoc || 
        d.id === paramDoc || 
        d.id === paramDoc.padStart(2, '0') || 
        d.name.includes(paramDoc)
      );
      if (foundDoc) {
        let deptKey = foundDoc.dept;
        for (let i = 0; i < deptSelect.options.length; i++) {
          const opt = deptSelect.options[i];
          if (opt.textContent.includes(foundDoc.deptName) || opt.value === foundDoc.dept || opt.value === foundDoc.deptName) {
            deptSelect.selectedIndex = i;
            break;
          }
        }
        populateDoctorsDropdown(deptKey, foundDoc.id);
        setTimeout(() => {
          apptForm.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }, 300);
      }
    } else if (paramDept) {
      for (let i = 0; i < deptSelect.options.length; i++) {
        const opt = deptSelect.options[i];
        if (opt.value === paramDept || opt.textContent.includes(DEPT_MAP[paramDept] || paramDept)) {
          deptSelect.selectedIndex = i;
          break;
        }
      }
      populateDoctorsDropdown(paramDept);
    }
  }

  // Helper: Format WhatsApp Message
  function buildWhatsAppAppointmentMessage(formData) {
    const docObj = DOCTORS_DATA.find(d => d.id === formData.doctor || d.name === formData.doctor);
    const doctorName = docObj ? `${docObj.name} (${docObj.desg || docObj.deptName})` : (formData.doctor || 'যেকোনো উপলব্ধ ডাক্তার');
    const deptName = formData.department || (docObj ? docObj.deptName : 'সাধারণ');
    const ageText = formData.age ? `${formData.age} বছর` : 'উল্লেখ নেই';
    const genderText = formData.gender || 'উল্লেখ নেই';
    const timeText = formData.time || 'যেকোনো সময়';
    const noteText = formData.message ? formData.message.trim() : 'নেই';

    return (
      `*নতুন অ্যাপয়েন্টমেন্ট রিকোয়েস্ট — নিরাময় হাসপাতাল*\n\n` +
      `👤 *রোগীর নাম:* ${formData.name}\n` +
      `📱 *মোবাইল:* ${formData.phone}\n` +
      `🎂 *বয়স ও লিঙ্গ:* ${ageText}, ${genderText}\n` +
      `🩺 *বিভাগ:* ${deptName}\n` +
      `👨‍⚕️ *ডাক্তার:* ${doctorName}\n` +
      `📅 *পছন্দের তারিখ:* ${formData.date}\n` +
      `⏰ *সময়:* ${timeText}\n` +
      `📝 *লক্ষণ / নোট:* ${noteText}\n\n` +
      `_অনলাইন পোর্টাল থেকে প্রেরিত_`
    );
  }

  // Helper: Form Validation
  function validateFormFields(form) {
    const requiredInputs = form.querySelectorAll('[required]');
    let isValid = true;
    requiredInputs.forEach(f => {
      if (!f.value || !f.value.trim()) {
        f.style.borderColor = '#e74c3c';
        f.style.boxShadow = '0 0 0 3px rgba(231,76,60,0.15)';
        isValid = false;
      } else {
        f.style.borderColor = '';
        f.style.boxShadow = '';
      }
    });
    return isValid;
  }

  // Handle WhatsApp Direct Booking Button
  if (waBookBtn && apptForm) {
    waBookBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (!validateFormFields(apptForm)) {
        alert('অনুগ্রহ করে নাম, মোবাইল নম্বর, ডাক্তার ও তারিখ সঠিকভাবে পূরণ করুন।');
        return;
      }
      const data = Object.fromEntries(new FormData(apptForm).entries());
      const msg = buildWhatsAppAppointmentMessage(data);
      const url = `https://wa.me/${HOSPITAL_WHATSAPP}?text=${encodeURIComponent(msg)}`;
      window.open(url, '_blank');
    });
  }

  // Handle Standard Form Submission
  if (apptForm) {
    apptForm.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!validateFormFields(apptForm)) return;

      const data = Object.fromEntries(new FormData(apptForm).entries());
      const docObj = DOCTORS_DATA.find(d => d.id === data.doctor || d.name === data.doctor);
      const doctorDisplayName = docObj ? docObj.name : data.doctor;

      // Update success card
      const formSuccess = document.getElementById('formSuccess');
      const detailsSummary = document.getElementById('bookingDetailsSummary');
      const sendWaLink = document.getElementById('sendWaAfterSubmit');

      if (detailsSummary) {
        detailsSummary.innerHTML = `<strong>রোগী:</strong> ${data.name} | <strong>ডাক্তার:</strong> ${doctorDisplayName} | <strong>তারিখ:</strong> ${data.date}<br>আমরা খুব শীঘ্রই আপনার মোবাইল নম্বরে (${data.phone}) যোগাযোগ করে সিরিয়াল নিশ্চিত করব।`;
      }
      if (sendWaLink) {
        const msg = buildWhatsAppAppointmentMessage(data);
        sendWaLink.href = `https://wa.me/${HOSPITAL_WHATSAPP}?text=${encodeURIComponent(msg)}`;
      }

      if (formSuccess) {
        formSuccess.style.display = 'block';
        formSuccess.classList.add('show');
        formSuccess.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      // Save to localStorage
      try {
        const history = JSON.parse(localStorage.getItem('niramoy_appointments') || '[]');
        history.push({ ...data, doctorName: doctorDisplayName, submittedAt: new Date().toISOString() });
        localStorage.setItem('niramoy_appointments', JSON.stringify(history));
      } catch (err) {}

      apptForm.reset();
    });
  }

  // Generic Contact Form Submit
  const contactForms = document.querySelectorAll('form.contact-form');
  contactForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!validateFormFields(form)) return;
      const success = form.querySelector('.form-success');
      if (success) {
        success.classList.add('show');
        success.style.display = 'block';
        setTimeout(() => {
          success.classList.remove('show');
          success.style.display = 'none';
        }, 6000);
      }
      form.reset();
    });
  });

  // ===== 10. Live Search for Diagnostic Page =====
  const diagSearchInput = document.getElementById('diagSearch');
  const diagGrid = document.querySelector('.diag-grid');
  if (diagSearchInput && diagGrid) {
    const diagCards = diagGrid.querySelectorAll('.diag-card');
    diagSearchInput.addEventListener('input', () => {
      const q = diagSearchInput.value.trim().toLowerCase();
      let matchCount = 0;
      diagCards.forEach(card => {
        const text = card.textContent.toLowerCase();
        if (!q || text.includes(q)) {
          card.style.display = '';
          matchCount++;
        } else {
          card.style.display = 'none';
        }
      });
      let noDiag = document.getElementById('noDiagResults');
      if (matchCount === 0) {
        if (!noDiag) {
          noDiag = document.createElement('div');
          noDiag.id = 'noDiagResults';
          noDiag.style.cssText = 'grid-column:1/-1;text-align:center;padding:40px;color:var(--text-muted);font-size:1.1rem;';
          noDiag.innerHTML = '<i class="fa-solid fa-microscope" style="font-size:2.5rem;margin-bottom:12px;display:block;color:var(--border);"></i> কোনো টেস্ট খুঁজে পাওয়া যায়নি। অনুগ্রহ করে সঠিক বানান লিখুন বা হটলাইনে কল করুন।';
          diagGrid.appendChild(noDiag);
        }
        noDiag.style.display = 'block';
      } else if (noDiag) {
        noDiag.style.display = 'none';
      }
    });
  }

  // ===== 11. Lightbox for Gallery =====
  const lightbox = document.getElementById('lightbox');
  if (lightbox) {
    const lbImg = lightbox.querySelector('img');
    document.querySelectorAll('.gallery-grid img, .gallery-preview-grid img').forEach(img => {
      img.addEventListener('click', () => {
        if (lbImg) {
          lbImg.src = img.src;
          lbImg.alt = img.alt || 'Gallery image';
        }
        lightbox.classList.add('show');
      });
    });
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox || e.target.classList.contains('lightbox-close') || e.target.closest('.lightbox-close')) {
        lightbox.classList.remove('show');
      }
    });
  }

  // ===== 12. Hero Slider =====
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

