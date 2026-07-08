/**
 * app.js — Main Application Controller
 * Navigation, smooth scroll, active section tracking
 */

(function () {
  'use strict';

  /* ── Navbar ── */
  function initNav() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    // Shrink on scroll
    let lastScrollY = 0;
    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      navbar.classList.toggle('shrunk', y > 60);
      lastScrollY = y;
    }, { passive: true });

    // Hamburger
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');

    if (hamburger && mobileMenu) {
      hamburger.addEventListener('click', () => {
        const open = hamburger.classList.toggle('open');
        mobileMenu.classList.toggle('open', open);
        hamburger.setAttribute('aria-expanded', open);
        document.body.style.overflow = open ? 'hidden' : '';
      });

      // Close on link click
      mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          hamburger.classList.remove('open');
          mobileMenu.classList.remove('open');
          hamburger.setAttribute('aria-expanded', 'false');
          document.body.style.overflow = '';
        });
      });
    }

    // Active section highlight
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

    if (sections.length && navLinks.length) {
      const obs = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const id = entry.target.id;
            navLinks.forEach(link => {
              link.classList.toggle('active', link.getAttribute('href') === '#' + id);
            });
          }
        });
      }, { rootMargin: '-40% 0px -50% 0px' });

      sections.forEach(s => obs.observe(s));
    }
  }

  /* ── Smooth Scroll ── */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(link => {
      link.addEventListener('click', e => {
        const href = link.getAttribute('href');
        if (href === '#') return;

        const target = document.querySelector(href);
        if (!target) return;

        e.preventDefault();
        const navH = parseInt(
          getComputedStyle(document.documentElement).getPropertyValue('--nav-height') || '64'
        );
        const top = target.getBoundingClientRect().top + window.scrollY - navH - 16;
        window.scrollTo({ top, behavior: 'smooth' });
      });
    });
  }

  /* ── Reveal staggered children ── */
  function initStaggeredReveal() {
    const groups = document.querySelectorAll('[data-stagger]');
    groups.forEach(group => {
      const children = group.querySelectorAll('[data-stagger-item]');
      children.forEach((child, i) => {
        child.style.transitionDelay = (i * 80) + 'ms';
      });
    });
  }

  /* ── Hero typing effect ── */
  function initHeroTyping() {
    const el = document.getElementById('hero-typing');
    if (!el) return;

    const phrases = [
      'Python Developer',
      'Full-Stack Engineer',
      'Automation Specialist',
      'Data Science Explorer',
      'API Builder',
    ];

    let phraseIdx = 0;
    let charIdx = 0;
    let deleting = false;
    let wait = 0;

    function type() {
      const phrase = phrases[phraseIdx];

      if (!deleting) {
        el.textContent = phrase.slice(0, charIdx + 1);
        charIdx++;
        if (charIdx === phrase.length) {
          deleting = true;
          wait = 2000;
        }
      } else {
        el.textContent = phrase.slice(0, charIdx - 1);
        charIdx--;
        if (charIdx === 0) {
          deleting = false;
          phraseIdx = (phraseIdx + 1) % phrases.length;
          wait = 300;
        }
      }

      const speed = deleting ? 40 : 80;
      setTimeout(type, wait > 0 ? wait : speed);
      wait = 0;
    }

    setTimeout(type, 1000);
  }

  /* ── Init all ── */
  function init() {
    initNav();
    initSmoothScroll();
    initStaggeredReveal();
    initHeroTyping();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
