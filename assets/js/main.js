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
    btn.addEventListener('click', function () {
      box.classList.add('on');
      var f = box.querySelector('iframe'); if (f) f.focus();
    });
  });
})();
