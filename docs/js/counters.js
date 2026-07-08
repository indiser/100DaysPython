/**
 * counters.js — Animated Number Counters
 * Intersection Observer based — runs once when visible
 */

(function () {
  'use strict';

  const STATS = [
    { id: 'stat-days',       target: 100,  suffix: '',   label: 'Days Completed' },
    { id: 'stat-projects',   target: 150,  suffix: '+',  label: 'Projects Built' },
    { id: 'stat-libraries',  target: 35,   suffix: '+',  label: 'Libraries Used' },
    { id: 'stat-apis',       target: 25,   suffix: '+',  label: 'APIs Integrated' },
    { id: 'stat-webapps',    target: 20,   suffix: '+',  label: 'Web Applications' },
    { id: 'stat-bots',       target: 10,   suffix: '+',  label: 'Automation Bots' },
    { id: 'stat-capstone',   target: 5,    suffix: '',   label: 'Capstone Projects' },
    { id: 'stat-completion', target: 100,  suffix: '%',  label: 'Completion Rate' },
  ];

  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  function animateCounter(el, target, suffix, duration) {
    const startTime = performance.now();
    const startVal  = 0;

    function tick(now) {
      const elapsed  = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased    = easeOutCubic(progress);
      const current  = Math.round(startVal + (target - startVal) * eased);

      el.textContent = current.toLocaleString() + suffix;

      if (progress < 1) {
        requestAnimationFrame(tick);
      } else {
        el.textContent = target.toLocaleString() + suffix;
      }
    }

    requestAnimationFrame(tick);
  }

  function initCounters() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const stat = STATS.find(s => s.id === el.id);
        if (!stat || el.dataset.counted === 'true') return;

        el.dataset.counted = 'true';
        const duration = 1800 + Math.random() * 400;
        animateCounter(el, stat.target, stat.suffix, duration);
        observer.unobserve(el);
      });
    }, { threshold: 0.3 });

    STATS.forEach(stat => {
      const el = document.getElementById(stat.id);
      if (el) {
        el.textContent = '0' + stat.suffix;
        observer.observe(el);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCounters);
  } else {
    initCounters();
  }
})();
