/**
 * timeline.js — Interactive Journey Timeline
 * Accordion-style expand/collapse
 */

(function () {
  'use strict';

  const STAGES = [
    {
      id: 'stage-beginner',
      phase: 'Phase 01',
      title: 'Beginner',
      days: 'Days 1–14',
      emoji: '🌱',
      color: '#22C55E',
      desc: 'Foundations of Python — variables, data types, control flow, functions, and first complete games.',
      skills: ['Variables & Data Types', 'Control Flow & Conditionals', 'Functions & Parameters', 'Lists & Dictionaries', 'Loops & Iteration', 'Random Module', 'ASCII Art & Games'],
      projects: ['Band Name Generator', 'BMI Calculator', 'Treasure Island', 'Rock Paper Scissors', 'Hangman', 'Blackjack', 'Higher or Lower'],
      milestone: 'First complete game with AI dealer logic (Blackjack)',
    },
    {
      id: 'stage-intermediate',
      phase: 'Phase 02',
      title: 'Intermediate',
      days: 'Days 15–31',
      emoji: '🔵',
      color: '#3B82F6',
      desc: 'OOP, GUI development with Tkinter, Turtle graphics, file I/O, and first capstone project.',
      skills: ['Object-Oriented Programming', 'Tkinter GUI', 'Turtle Graphics', 'File I/O (CSV, JSON)', 'Error Handling', 'Canvas & Animations', 'Timer Management'],
      projects: ['Coffee Machine (OOP)', 'Snake Game', 'Pong', 'Pomodoro Timer', 'Password Manager', 'FlashCard App (Capstone)'],
      milestone: 'FlashCard App — first full-featured GUI application with data persistence',
    },
    {
      id: 'stage-intermediate-plus',
      phase: 'Phase 03',
      title: 'Intermediate+',
      days: 'Days 32–58',
      emoji: '🟣',
      color: '#8B5CF6',
      desc: 'API integrations, web scraping, automation bots, Flask web development, and multi-API pipelines.',
      skills: ['REST APIs', 'SMTP Email', 'BeautifulSoup', 'Selenium', 'Flask Basics', 'Jinja2 Templates', 'Bootstrap'],
      projects: ['ISS Tracker', 'Trivia Quiz GUI', 'Rain Alert (Twilio)', 'Cheap Flights (Capstone)', 'Billboard → Spotify', 'LinkedIn Bot', 'Instagram Bot'],
      milestone: 'Flight Deal Finder — first multi-API pipeline with automated SMS alerts',
    },
    {
      id: 'stage-advanced',
      phase: 'Phase 04',
      title: 'Advanced',
      days: 'Days 59–81',
      emoji: '🔴',
      color: '#EF4444',
      desc: 'Full-stack Flask apps, SQLAlchemy, authentication, REST API design, and data science with Pandas & NumPy.',
      skills: ['Flask-WTF Forms', 'SQLAlchemy ORM', 'Flask-Login Auth', 'RESTful API Design', 'Pandas & NumPy', 'Matplotlib & Seaborn', 'Plotly', 'Linear Regression', 'Jupyter Notebooks'],
      projects: ['Multi-User Blog (Capstone)', 'Cafe REST API', 'Top Movies DB', 'User Auth System', 'Nobel Prize Analysis', 'Space Race Analysis', 'Linear Regression ML'],
      milestone: 'Multi-User Blog — production-ready full-stack app with authentication and admin system',
    },
    {
      id: 'stage-professional',
      phase: 'Phase 05',
      title: 'Professional',
      days: 'Days 82–100',
      emoji: '🏆',
      color: '#F59E0B',
      desc: 'Production-grade projects: e-commerce platform, AI content pipeline, custom APIs, computer vision, and data science capstones.',
      skills: ['FastAPI (async)', 'Cloudinary', 'Computer Vision (PyAutoGUI)', 'AI / LLM Integration', 'Video Composition', 'PDF Generation', 'Multi-platform Automation', 'Data Science Capstone'],
      projects: ['Chrome Dino Bot (CV)', 'Tic Tac Toe AI (Minimax)', 'Manga API (FastAPI)', 'The Fake Shop E-Commerce (Capstone)', 'Viral Content Factory (Capstone)', 'Police Shootings Analysis (Capstone)'],
      milestone: 'The Fake Shop — production-ready e-commerce with auth, payments, admin dashboard, and cloud storage',
    },
  ];

  function buildTimeline() {
    const container = document.getElementById('journey-timeline');
    if (!container) return;

    container.innerHTML = STAGES.map((stage, i) => `
      <div class="timeline-item ${i === 0 ? 'active' : ''}" id="${stage.id}" role="button" tabindex="0" aria-expanded="${i === 0}">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
          <div class="timeline-header">
            <div>
              <div class="flex items-center gap-3" style="margin-bottom:var(--space-2)">
                <span class="section-label" style="margin:0;font-size:0.65rem;color:${stage.color};background:${stage.color}1a;border-color:${stage.color}40;">${stage.phase}</span>
                <span style="font-size:0.75rem;font-family:var(--font-mono);color:var(--text-subtle)">${stage.days}</span>
              </div>
              <div class="timeline-title">${stage.emoji} ${stage.title}</div>
              <div class="timeline-subtitle">${stage.desc}</div>
            </div>
            <div class="timeline-chevron" aria-hidden="true">▼</div>
          </div>
          <div class="timeline-body" role="region">
            <div style="margin-top:var(--space-6);display:grid;grid-template-columns:1fr 1fr;gap:var(--space-6)">
              <div>
                <div style="font-size:var(--text-xs);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--text-subtle);margin-bottom:var(--space-3)">Skills Learned</div>
                <div class="achievement-list">
                  ${stage.skills.map(s => `<div class="achievement-item">${s}</div>`).join('')}
                </div>
              </div>
              <div>
                <div style="font-size:var(--text-xs);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--text-subtle);margin-bottom:var(--space-3)">Key Projects</div>
                <div class="achievement-list">
                  ${stage.projects.map(p => `<div class="achievement-item" style="color:var(--text-secondary)">${p}</div>`).join('')}
                </div>
              </div>
            </div>
            <div style="margin-top:var(--space-5);padding:var(--space-4);background:rgba(${hexToRgb(stage.color)},0.06);border:1px solid rgba(${hexToRgb(stage.color)},0.2);border-radius:var(--radius-lg)">
              <div style="font-size:var(--text-xs);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:${stage.color};margin-bottom:var(--space-2)">🏆 Milestone</div>
              <div style="font-size:var(--text-sm);color:var(--text-secondary)">${stage.milestone}</div>
            </div>
          </div>
        </div>
      </div>
    `).join('');

    // Interaction
    container.querySelectorAll('.timeline-item').forEach(item => {
      function toggle() {
        const isActive = item.classList.contains('active');
        container.querySelectorAll('.timeline-item').forEach(el => {
          el.classList.remove('active');
          el.setAttribute('aria-expanded', 'false');
        });
        if (!isActive) {
          item.classList.add('active');
          item.setAttribute('aria-expanded', 'true');
        }
      }

      item.addEventListener('click', toggle);
      item.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); }
      });
    });
  }

  function hexToRgb(hex) {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result
      ? `${parseInt(result[1], 16)},${parseInt(result[2], 16)},${parseInt(result[3], 16)}`
      : '59,130,246';
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildTimeline);
  } else {
    buildTimeline();
  }
})();
