"""Best AI trend video apps for iPhone (TikTok and Reels trends from templates). EN. Our app: Dora (id6754180384), 4th of 6.
Checked 2026-11-03 (JST): iTunes lookup and US App Store pages. Criterion: the listing says you pick a trend or template and add your photo or clip.
Excluded: CapCut (editor first; its listing does not describe AI trend templates), AI Video by HUBX and apps with under 1,000 ratings except Pika's own app.
Pika: "AI Video Trend by Pika", seller Mellis, Inc.; its listing links pika.art terms and privacy."""

DAY = "2026-11-03"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"
REELS = '<a href="/best-ai-video-apps-for-instagram-reels-iphone/">AI video apps for Instagram Reels</a>'
SOUND = '<a href="/best-ai-video-generator-apps-with-sound-iphone/">AI video apps with sound</a>'


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, langs, labels, price, trends, you, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, trends, you, str(langs), labels, f"{ver} ({date})", f"{round(r, 1)}"]}
    if ours:
        d["ours"] = True
    return d


APPS = [
    app("ReelMe: AI Photo & Video", 6745781406, "reelme", "TPC INVEST PTE. LTD.", 4.47, 8152, "4.7.0", "29 Sep 2026", 1, label(TRACK, LINKED),
        "Weekly $7.99 to $14.99, yearly $39.99, VIP yearly $59.99; coins $14.99 to $24.99", "Trending video and photo templates, new every week", "One photo",
        "trying this week's trend with one selfie and no prompt.",
        ["Its listing says trending templates are updated every week: tap one, add your photo, done.", "Dance videos, birthday clips, before-and-after transformations and seasonal looks from a single photo.", "The credit balance shows before every generation, per its listing."],
        "English only, weekly plans, and its privacy label includes Data Used to Track You."),
    app("Hula AI: Trend Video Generator", 6739294055, "hula", "Prequel Inc.", 4.59, 13551, "2.20.0", "28 Oct 2026", 7, label(TRACK, NOTLINKED),
        "Premium $6.99 or $9.99 a week, $39.99 a year; packs $2.99 to $4.99", "Selfie to animated video, era and anime styles, video remixes", "One selfie",
        "turning a selfie into a stylised clip, plus stickers from the same photo.",
        ["Turns selfies into animated videos, from travel scenes to magazine looks, per its listing.", "Time-travel styles show you in other eras, and anime styles work on photos and videos.", "Makes sticker packs for iMessage, WhatsApp and more from one selfie."],
        "the listing does not say how long a video is, and the packs are small (2 or 5 creations)."),
    app("AI Video Trend by Pika", 6744712684, "pika", "Mellis, Inc.", 4.59, 273, "1.1.7", "12 Jun 2026", 1, label(LINKED, NOTLINKED),
        "Tokens only: $9.99 (800) to $199.99 (19,200)", "Remix trending styles, sounds and lip-sync templates", "A selfie",
        "lip-sync trends: singing or saying a line with your face, from Pika.",
        ["Its listing says a selfie becomes a video, GIF or meme, and you can remix trending styles, sounds and lip-sync templates.", "AI lip-sync to music or speech, and a community feed.", "Its terms and privacy links go to pika.art, and it sells token packs with no subscription."],
        "English only, and its last update was on 12 June 2026."),
    app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16, "1.4.2", "26 Oct 2026", 11, label(TRACK, NOTLINKED),
        "Pro weekly $4.99 or $6.99, Pro yearly $119.99; coins $4.99 (300) to $224.99 (25,000)", "Era, place and style templates; dance moves copied onto your photo", "One photo",
        "era and place trends and copying a dance onto your own photo, with the cost shown first.",
        ["Its listing says ready-made templates put you in another era, place or style, and Motion Control copies the moves of a dance video onto the person in your photo.", "Vertical 9:16 for TikTok and Reels, up to 1080p, no watermark; the coin cost shows before you tap and failed generations give the coins back.",
         "Videos have sound on the models that support it; the default model makes 8 seconds with sound for 31 coins, per Dora's site."],
        "a subscription with no free video, and it does not post to your accounts for you.", True),
    app("Vids AI - Reels Video Editor", 1634361180, "vids", "Viral Vision Ltd", 4.78, 48712, "1.141.0", "19 Oct 2026", 14, label(TRACK, LINKED, NOTLINKED),
        "Vids Pro $7.99 to $79.99 on the page; Vids AI Max $19.99", "Thousands of AI templates synced to trending music", "Your clips and selfies",
        "trend edits made from your own clips, synced to the beat.",
        ["Its listing says thousands of templates sync your clips with music, effects and transitions.", "Generative AI effects add motion to people or objects, with a full editor to cut and trim.", "14 languages and the highest rating here, 4.8."],
        "it works best with your own footage, and the page lists Pro at many prices."),
    app("Zoomerang - Ai Video Maker", 1361030006, "zoomerang", "Zoomerang, Inc.", 4.62, 174093, "3.4.19", "28 Sep 2026", 8, label(TRACK, NOTLINKED),
        "Weekly $5.99 to $7.99, monthly $4.99, yearly $19.99 to $34.99", "TikTok challenge templates with step-by-step tutorials", "You film yourself",
        "copying a TikTok challenge you film yourself, step by step.",
        ["Its listing says you can send a TikTok challenge and its team makes a template for it; tutorials show each shot.", "Templates with famous songs by hashtag, from 200,000 template creators. The most ratings here, about 174,000."],
        "you film the trend yourself; it does not generate you into a scene from one photo."),
]

PAGES = [{
    "group": "trend-video", "lang": "en", "store": "us", "path": "best-ai-trend-video-apps-iphone/", "ct": "rl-trend-video",
    "category": "PhotoVideoApplication", "published": DAY, "updated": DAY, "checked": DAY, "cover": None,
    "title": "Best AI Trend Video Apps for TikTok on iPhone (2026)", "h1": "Best AI trend video apps for TikTok and Reels on iPhone",
    "description": "Six iPhone apps that turn your photo into this week's TikTok or Reels trend from a template, compared by US price, privacy label and rating on 3 November 2026.",
    "llms": "Six iPhone apps for AI trend videos from templates: ReelMe, Hula AI, Pika, Dora, Vids AI, Zoomerang. What trends each makes, whether one photo is enough, price, privacy label, rating.",
    "answer": [
        "To try this week's trend with one selfie and no prompt, <strong>ReelMe</strong>, whose listing says templates are updated every week. For stylised selfie clips and era looks, <strong>Hula AI</strong>. For lip-sync trends, Pika's own app, <strong>AI Video Trend by Pika</strong>. To put yourself in another era or copy a dance onto your photo, <strong>Dora</strong>.",
        "If you would rather film the trend yourself, <strong>Zoomerang</strong> turns TikTok challenges into step-by-step templates. All six are free to download; the trends need a subscription, coins or tokens.",
    ],
    "columns": ["App", "Price (US)", "Trends, per listing", "What you add", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "Prices are those listed on each US App Store page on 3 November 2026; pages list only some purchases and often several prices for the same plan.",
    "apps": APPS,
    "who": ["<strong>This week's trend, one selfie:</strong> ReelMe.", "<strong>Stylised selfie clips and stickers:</strong> Hula AI.", "<strong>Lip-sync trends:</strong> Pika.",
            "<strong>Eras, places and dance moves on your photo:</strong> Dora.", "<strong>Trend edits of your own clips:</strong> Vids AI.", "<strong>Filming a challenge yourself:</strong> Zoomerang."],
    "cases": ["A 90s or Renaissance look for a Reel: Dora or Hula AI.", "A dance trend without dancing: ReelMe or Dora's Motion Control.", "A sound or lip-sync trend: Pika."],
    "method": ["On 3 November 2026 we read each app's US App Store page and Apple's lookup data. An app is here only if its listing says you pick a trend or template and add your photo or clips. We generated nothing and did not compare results.",
               "CapCut is an editor first and its listing does not describe AI trend templates, so it is not here. Order: first the apps that make the trend from one photo, then the ones built around your own footage. See also " + REELS + " and " + SOUND + "."],
    "faq": [
        ("What app makes AI trend videos from a photo?", "ReelMe, Hula AI, Pika and Dora say one photo or selfie is enough. Vids AI works with your clips, and Zoomerang has you film the trend."),
        ("Which app has new AI trends every week?", "ReelMe's listing says its trending templates are updated every week. Zoomerang says it makes templates for TikTok challenges you send."),
        ("Is there a free AI trend video app?", "All six are free to download, but none of these listings promises free trend videos. They sell subscriptions, coins or tokens; Pika sells token packs with no subscription."),
        ("Do the videos fit TikTok?", "Dora's listing says it makes vertical 9:16 for TikTok and Reels. The others say their videos are made for social or short-form platforms."),
    ],
    "sources": [(f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}") for a in APPS] + [("Dora: models and coins", "https://doravideo.com/models")],
}]
