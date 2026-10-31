// HK Travels - Main Interactive Script
document.addEventListener('DOMContentLoaded', () => {
  // 1. Dynamic Typewriter Animation
  const typewriterEl = document.querySelector('.typewriter-text');
  if (typewriterEl) {
    const words = [
      'Chauffeur-Driven Luxury Sedans',
      'Premium Toyota Innova Crysta MPVs',
      '24/7 Airport On-Time Dispatch',
      'Executive Outstation & Intercity Tours',
      'Force Urbania & Group Travellers'
    ];
    let wordIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    let typingSpeed = 90;

    function type() {
      const currentWord = words[wordIdx];
      if (isDeleting) {
        typewriterEl.textContent = currentWord.substring(0, charIdx - 1);
        charIdx--;
        typingSpeed = 45;
      } else {
        typewriterEl.textContent = currentWord.substring(0, charIdx + 1);
        charIdx++;
        typingSpeed = 90;
      }

      if (!isDeleting && charIdx === currentWord.length) {
        isDeleting = true;
        typingSpeed = 2000;
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        wordIdx = (wordIdx + 1) % words.length;
        typingSpeed = 400;
      }

      setTimeout(type, typingSpeed);
    }
    type();
  }

  // 2. Telemetry Animated Counters
  const telemetryVals = document.querySelectorAll('.telemetry-val');
  if (telemetryVals.length > 0) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-target') || el.textContent.replace(/\D/g, ''), 10);
          const suffix = el.getAttribute('data-suffix') || '';
          if (!isNaN(target)) {
            let start = 0;
            const duration = 1800;
            const step = Math.max(1, Math.floor(target / (duration / 25)));
            const timer = setInterval(() => {
              start += step;
              if (start >= target) {
                el.textContent = target + suffix;
                clearInterval(timer);
              } else {
                el.textContent = start + suffix;
              }
            }, 25);
          }
          obs.unobserve(el);
        }
      });
    }, { threshold: 0.3 });

    telemetryVals.forEach(val => observer.observe(val));
  }

  // 3. Interactive Trip & Fleet Quote Intake Widget
  const tripTypeSel = document.getElementById('tripType');
  const vehicleClassSel = document.getElementById('vehicleClass');
  const destinationSel = document.getElementById('tripDest');
  const estTitle = document.getElementById('estTitle');
  const estTimeline = document.getElementById('estTimeline');
  const estWaBtn = document.getElementById('estWaBtn');

  function updateEstimator() {
    if (!tripTypeSel || !vehicleClassSel || !destinationSel) return;
    const trip = tripTypeSel.value;
    const vehicle = vehicleClassSel.value;
    const dest = destinationSel.value;

    let titleText = `${vehicle} — ${trip}`;
    let specText = `Route: ${dest} | Verified Chauffeur, Sanitized Cabin & Fastag GPS Tracking`;

    if (trip === 'CCU Airport Transfer') {
      specText = `Flight Tracked | Meet & Greet at CCU Terminal | Zero Wait Surcharge | Chauffeur Punctuality Guarantee`;
    } else if (trip === 'Outstation Roundtrip') {
      specText = `Intercity All-India Tourist Permit | Toll & Parking Tracking | Chauffeur Allowance Included`;
    } else if (trip === 'Local City Rental (8 Hr / 80 Km)') {
      specText = `City Business & Shopping Circuit | Chauffeur Wait Available | Doorstep Pickup across Kolkata`;
    }

    if (estTitle) estTitle.textContent = titleText;
    if (estTimeline) estTimeline.textContent = specText;

    if (estWaBtn) {
      const msg = encodeURIComponent(
        `Hello HK Travels Team! I would like to check availability and book a vehicle:\n\n• Trip Type: ${trip}\n• Vehicle Class: ${vehicle}\n• Destination / Pickup: ${dest}\n• Base: Park Circus / Ballygunge / Kolkata\n\nPlease share fleet options and chauffeur assignment!`
      );
      estWaBtn.href = `https://wa.me/918777578947?text=${msg}`;
    }
  }

  if (tripTypeSel && vehicleClassSel && destinationSel) {
    tripTypeSel.addEventListener('change', updateEstimator);
    vehicleClassSel.addEventListener('change', updateEstimator);
    destinationSel.addEventListener('change', updateEstimator);
    updateEstimator();
  }

  // 4. Fleet Filter Rail
  const filterBtns = document.querySelectorAll('.filter-btn');
  const fleetItems = document.querySelectorAll('.fleet-item');
  if (filterBtns.length > 0 && fleetItems.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.getAttribute('data-filter');

        fleetItems.forEach(item => {
          if (filter === 'all' || item.getAttribute('data-category') === filter) {
            item.style.display = 'flex';
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  // 5. Mobile Navigation Drawer Toggle
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer');
  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      drawer.classList.toggle('open');
    });

    document.addEventListener('click', (e) => {
      if (drawer.classList.contains('open') && !drawer.contains(e.target) && !toggleBtn.contains(e.target)) {
        drawer.classList.remove('open');
      }
    });
  }

  // 6. Contact Form WhatsApp Dispatch Bridge
  const contactForm = document.getElementById('bookingForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('bookName')?.value || 'Traveler';
      const phone = document.getElementById('bookPhone')?.value || '';
      const pickup = document.getElementById('bookPickup')?.value || 'Park Circus, Kolkata';
      const trip = document.getElementById('bookTrip')?.value || 'Outstation';
      const vehicle = document.getElementById('bookVehicle')?.value || 'Toyota Innova Crysta';
      const notes = document.getElementById('bookNotes')?.value || 'Trip inquiry';

      const waText = encodeURIComponent(
        `New Trip Booking Request - HK Travels:\n\n• Name: ${name}\n• Phone: ${phone}\n• Pickup Location: ${pickup}\n• Trip Type: ${trip}\n• Preferred Vehicle: ${vehicle}\n• Additional Details: ${notes}`
      );
      window.open(`https://wa.me/918777578947?text=${waText}`, '_blank');
    });
  }
});
