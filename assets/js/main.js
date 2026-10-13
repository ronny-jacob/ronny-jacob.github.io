/* 1) "Long name to short keyword" demo: plays once when scrolled into view. Final state is the default (no JS, reduced motion). */
(function () {
  var demo = document.getElementById('demo');
  if (!demo || (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches)) return;
  function play() { demo.classList.add('is-reset'); void demo.offsetWidth; demo.classList.remove('is-reset'); }
  if ('IntersectionObserver' in window) {
    demo.classList.add('is-reset');
    new IntersectionObserver(function (e, o) { if (e[0].isIntersecting) { o.disconnect(); setTimeout(play, 200); } }, { threshold: .6 }).observe(demo);
  }
})();

/* 2) Live app previews: a "Try it live" tap enables the embedded app, so it never traps page scrolling on touch screens. */
(function () {
  document.querySelectorAll('.live').forEach(function (box) {
    var btn = box.querySelector('.try');
    if (!btn) return;
    box.classList.add('gated');
    var fr = box.querySelector('iframe'); if (fr) fr.tabIndex = -1;
    btn.addEventListener('click', function () {
      box.classList.add('on');
      var f = box.querySelector('iframe'); if (f) { f.tabIndex = 0; f.focus(); }
    });
  });
})();

/* 3) Scroll reveal: fade-up as sections enter the viewport. Respects reduced motion; content stays visible without JS. */
(function () {
  if (!('IntersectionObserver' in window) || (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches)) return;
  var items = document.querySelectorAll('.pcard, .why > div, .path-strip li, .contact > *, .brief, .lane, .dbox, .steps li');
  if (!items.length) return;
  document.documentElement.classList.add('js-reveal');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: .12, rootMargin: '0px 0px -6% 0px' });
  items.forEach(function (el, i) { el.classList.add('rv'); el.style.setProperty('--d', i % 3); io.observe(el); });
  // Once revealed, drop the reveal class so hover lift and shadow transitions work normally.
  document.addEventListener('transitionend', function (e) { if (e.propertyName === 'opacity' && e.target.classList.contains('in')) e.target.classList.remove('rv'); });
})();

/* 4) Count-up on the headline chart values, in step with the bars growing. Final value is always the real figure. */
(function () {
  if (!('IntersectionObserver' in window) || (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches)) return;
  var vals = document.querySelectorAll('.pcard.big .b-val');
  if (!vals.length) return;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      io.unobserve(e.target);
      var end = parseInt(e.target.textContent, 10), t0 = null;
      if (isNaN(end)) return;
      (function step(t) {
        if (t0 === null) t0 = t;
        var p = Math.min((t - t0) / 1300, 1), k = 1 - Math.pow(1 - p, 3);
        e.target.textContent = Math.round(end * k) + '%';
        if (p < 1) requestAnimationFrame(step);
      })(performance.now());
    });
  }, { threshold: .6 });
  vals.forEach(function (v) { io.observe(v); });
})();


/* 5) Hero polish: word-by-word headline, card spotlight, magnetic main button. Pointer effects skip touch and reduced motion. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var h1 = document.querySelector('.hero h1');
  if (h1 && !reduce) {
    if ('IntersectionObserver' in window) document.documentElement.classList.add('js-reveal');
    var i = 0;
    (function wrap(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            var s = document.createElement('span'); s.className = 'w'; s.style.setProperty('--wi', i++); s.textContent = part; frag.appendChild(s);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1) { wrap(n); }
      });
    })(h1);
  }
  if (reduce || !window.matchMedia('(hover: hover)').matches) return;
  document.querySelectorAll('.pcard').forEach(function (c) {
    c.addEventListener('pointermove', function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) + 'px'); c.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });
  var b = document.querySelector('.hero .btn-primary');
  if (b) {
    b.addEventListener('pointermove', function (e) {
      var r = b.getBoundingClientRect();
      b.style.setProperty('--tx', ((e.clientX - r.left - r.width / 2) * .12) + 'px');
      b.style.setProperty('--ty', ((e.clientY - r.top - r.height / 2) * .2) + 'px');
    });
    b.addEventListener('pointerleave', function () { b.style.removeProperty('--tx'); b.style.removeProperty('--ty'); });
  }
})();
