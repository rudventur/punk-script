// Top nav hide / show for the RudVentur Social pages (browse, invite,
// profile). Needs js/panel-toggle.js first. When hidden, a small "menu" tab
// at the top right brings it back; the choice is remembered on this device.
(function () {
  if (!window.sfPanels || !document.querySelector('.nav')) return;
  sfPanels.register({
    id: 'nav', el: '.nav', label: 'the top menu', side: 'top',
    read: () => !document.body.classList.contains('sf-hidden-nav'),
    apply: open => document.body.classList.toggle('sf-hidden-nav', !open)
  });
  sfPanels.set('nav', sfPanels.saved('nav', true), { noSave: true });
})();
