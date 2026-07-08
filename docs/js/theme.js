/**
 * theme.js — Night Mode Only
 * Forces dark mode; no toggle needed.
 * Also handles: scroll reveal, skill bars, back-to-top
 */

(function () {
  'use strict';

  // Force dark color scheme
  document.documentElement.setAttribute('data-theme', 'dark');

  function init() {
    initScrollReveal();
    initSkillBars();
    initBackToTop();
    initExplorer();
    initSkillsTabs();
  }

  /* ── Scroll Reveal ── */
  function initScrollReveal() {
    const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-scale');
    if (!revealEls.length) return;

    const obs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(el => obs.observe(el));
  }

  /* ── Skill Bars ── */
  function initSkillBars() {
    const bars = document.querySelectorAll('.skill-bar-fill');
    if (!bars.length) return;

    const obs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });

    bars.forEach(bar => obs.observe(bar));
  }

  /* ── Back to Top ── */
  function initBackToTop() {
    const btn = document.getElementById('back-to-top');
    if (!btn) return;

    window.addEventListener('scroll', () => {
      btn.classList.toggle('visible', window.scrollY > 500);
    }, { passive: true });

    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ── Repository Explorer ── */
  function initExplorer() {
    const treeItems = document.querySelectorAll('.tree-folder');
    treeItems.forEach(item => {
      item.addEventListener('click', () => {
        const childrenId = item.dataset.children;
        if (!childrenId) return;
        const children = document.getElementById(childrenId);
        if (!children) return;

        const isOpen = children.classList.toggle('open');
        const icon = item.querySelector('.tree-toggle-icon');
        if (icon) icon.textContent = isOpen ? '▾' : '▸';
        item.classList.toggle('active', isOpen);
      });
    });

    // File click → show description
    document.querySelectorAll('.tree-file').forEach(file => {
      file.addEventListener('click', () => {
        document.querySelectorAll('.tree-item').forEach(i => i.classList.remove('active'));
        file.classList.add('active');

        const contentEl = document.getElementById('explorer-file-content');
        if (contentEl && file.dataset.content) {
          contentEl.innerHTML = file.dataset.content;
        }
      });
    });
  }

  /* ── Skills Tabs ── */
  function initSkillsTabs() {
    const tabs = document.querySelectorAll('.skill-tab');
    const panels = document.querySelectorAll('.skill-panel');

    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const target = tab.dataset.target;

        tabs.forEach(t => t.classList.remove('active'));
        panels.forEach(p => p.style.display = 'none');

        tab.classList.add('active');
        const panel = document.getElementById(target);
        if (panel) {
          panel.style.display = 'block';

          // Trigger bar animation for newly shown panel
          panel.querySelectorAll('.skill-bar-fill').forEach(bar => {
            if (!bar.classList.contains('animate')) {
              setTimeout(() => bar.classList.add('animate'), 50);
            }
          });
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
