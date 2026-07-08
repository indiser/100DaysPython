/**
 * particles.js — Canvas Particle System
 * Lightweight, self-contained — no dependencies
 */

(function () {
  'use strict';

  let canvas, ctx, particles = [], raf;
  const CONFIG = {
    count: 60,
    minR: 0.8,
    maxR: 2.0,
    minSpeed: 0.08,
    maxSpeed: 0.35,
    opacity: 0.55,
    colors: ['#3B82F6', '#8B5CF6', '#22C55E', '#60A5FA', '#A78BFA'],
    connectionDist: 120,
    connectionOpacity: 0.08,
  };

  function rand(min, max) {
    return Math.random() * (max - min) + min;
  }

  function createParticle(w, h) {
    return {
      x: rand(0, w),
      y: rand(0, h),
      vx: rand(-CONFIG.maxSpeed, CONFIG.maxSpeed),
      vy: rand(-CONFIG.maxSpeed, CONFIG.maxSpeed),
      r: rand(CONFIG.minR, CONFIG.maxR),
      color: CONFIG.colors[Math.floor(rand(0, CONFIG.colors.length))],
      opacity: rand(0.2, CONFIG.opacity),
    };
  }

  function resize() {
    if (!canvas) return;
    const rect = canvas.parentElement.getBoundingClientRect();
    canvas.width = rect.width;
    canvas.height = rect.height;
  }

  function draw() {
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    // Draw connections
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < CONFIG.connectionDist) {
          const alpha = (1 - dist / CONFIG.connectionDist) * CONFIG.connectionOpacity;
          ctx.beginPath();
          ctx.strokeStyle = `rgba(59,130,246,${alpha})`;
          ctx.lineWidth = 0.6;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }

    // Draw particles
    particles.forEach(p => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = p.color + Math.round(p.opacity * 255).toString(16).padStart(2, '0');
      ctx.fill();
    });
  }

  function update() {
    const w = canvas.width;
    const h = canvas.height;

    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;

      if (p.x < -p.r) p.x = w + p.r;
      if (p.x > w + p.r) p.x = -p.r;
      if (p.y < -p.r) p.y = h + p.r;
      if (p.y > h + p.r) p.y = -p.r;
    });
  }

  function loop() {
    update();
    draw();
    raf = requestAnimationFrame(loop);
  }

  function init() {
    canvas = document.getElementById('particles-canvas');
    if (!canvas) return;

    ctx = canvas.getContext('2d');
    resize();

    particles = [];
    const w = canvas.width;
    const h = canvas.height;
    for (let i = 0; i < CONFIG.count; i++) {
      particles.push(createParticle(w, h));
    }

    if (raf) cancelAnimationFrame(raf);
    loop();

    window.addEventListener('resize', () => {
      resize();
      particles = [];
      for (let i = 0; i < CONFIG.count; i++) {
        particles.push(createParticle(canvas.width, canvas.height));
      }
    });
  }

  // Pause when tab is hidden (performance)
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      cancelAnimationFrame(raf);
    } else {
      loop();
    }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
