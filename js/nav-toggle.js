(function () {
  var toggler = document.querySelector('.navbar-toggler');
  if (!toggler) return;

  var targets = document.querySelectorAll('#navbarSupportedContent, #header');

  toggler.addEventListener('click', function () {
    var open = toggler.getAttribute('aria-expanded') !== 'true';
    targets.forEach(function (el) {
      el.classList.add('collapse');
      el.classList.toggle('show', open);
    });
    toggler.classList.toggle('collapsed', !open);
    toggler.setAttribute('aria-expanded', open);
  });
})();
