/* Umami analytics loader (self-hosted, cookieless, no banner).
   Dashboard: https://analytics.kilmaru.com  Site: reviewland.io
   WEBSITE_ID is empty until the site is added in Umami; then paste it here. */
(function () {
  var WEBSITE_ID = '8a2eff76-9ec5-4d68-a050-9dee5c4cd495';
  var UMAMI_SRC = 'https://analytics.kilmaru.com/script.js';
  if (!WEBSITE_ID) return;
  var s = document.createElement('script');
  s.defer = true;
  s.src = UMAMI_SRC;
  s.setAttribute('data-website-id', WEBSITE_ID);
  s.setAttribute('data-domains', 'reviewland.io');
  document.head.appendChild(s);
})();
