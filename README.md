# reviewland.io

Rankings of iPhone apps by task, served by GitHub Pages. Run by Saga Labs.

- Edit or add a ranking in `pages/*.py` (add the module to `PAGE_MODULES` in `build.py`), then `python3 build.py` and commit the generated HTML.
- After publishing: `python3 build.py --indexnow`.
- Rules: our app is one more option, never first (`place_ours()` in build.py), with no "Our app" label and a single disclosure line at the top (rule of 20 Oct 2026); our links carry pt+ct, competitors get a plain App Store link; every price, version and rating copied from the App Store on the `checked` date. Recheck monthly and only change `updated` when the data was actually rechecked.
- Analytics: Umami at analytics.kilmaru.com (`umami.js`; empty WEBSITE_ID means off). App Store campaign links use `ct=rl-<slug>`.
- Common know-how: `Saga-Labs/ios-playbook` → PLAYBOOK.md.
