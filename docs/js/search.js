/**
 * search.js — Live Project Search & Filter
 */

(function () {
  'use strict';

  function initSearch() {
    const searchInput = document.getElementById('search-input');
    const projectCards = document.querySelectorAll('[data-project]');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const noResults = document.getElementById('no-results');

    if (!searchInput) return;

    let activeFilter = 'all';
    let searchQuery  = '';

    function filterProjects() {
      let visibleCount = 0;

      projectCards.forEach(card => {
        const title    = (card.dataset.title || '').toLowerCase();
        const tags     = (card.dataset.tags  || '').toLowerCase();
        const category = (card.dataset.category || '').toLowerCase();

        const matchSearch = !searchQuery ||
          title.includes(searchQuery) ||
          tags.includes(searchQuery);

        const matchFilter = activeFilter === 'all' ||
          category.includes(activeFilter);

        const visible = matchSearch && matchFilter;
        card.style.display = visible ? '' : 'none';

        if (visible) {
          visibleCount++;
          card.classList.add('animate-fade-up');
        } else {
          card.classList.remove('animate-fade-up');
        }
      });

      if (noResults) {
        noResults.style.display = visibleCount === 0 ? 'block' : 'none';
      }
    }

    searchInput.addEventListener('input', e => {
      searchQuery = e.target.value.trim().toLowerCase();
      filterProjects();
    });

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilter = btn.dataset.filter || 'all';
        filterProjects();
      });
    });

    // Init
    filterProjects();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSearch);
  } else {
    initSearch();
  }
})();
