"""Five "which app do I use" pages, EN, cover-less until one is approved. Our app: Dora (real position, one disclosure line).
Checked 2026-11-02: iTunes lookup and US App Store pages. No quality test. No output or free allowance is claimed unless a listing states it.
Dora Lip Sync: doravideo.com/blog/best-talking-photo-apps-iphone and llms.txt (web only, not in the iPhone app's picker)."""

DAY = "2026-11-02"
TRACK = "Data Used to Track You"
LINKED = "Data Linked to You"
NOTLINKED = "Data Not Linked to You"


def label(*x):
    return "; ".join(x)


def app(name, i, anchor, dev, r, n, ver, date, langs, labels, price, does, best, facts, limits, ours=False):
    d = {"name": name, "id": i, "anchor": anchor, "developer": dev, "rating": (r, n), "best_for": best, "facts": facts, "limits": limits,
         "row": [price, does, str(langs), labels, f"{ver} ({date})", f"{round(r, 1)}"]}
    if ours:
        d["ours"] = True
    return d


def store(a):
    return (f"{a['name']} (App Store)", f"https://apps.apple.com/us/app/id{a['id']}")


DORA_PRICE = "Pro weekly $6.99 for new subscribers, Pro yearly $119.99; coin packs $4.99 (300) to $224.99 (25,000)"


def dora(does, best, facts, limits):
    return app("DORA · AI Video Generator", 6754180384, "dora", "Saga Ltd.", 4.31, 16, "1.4.2", "26 Oct 2026", 11, label(TRACK, NOTLINKED), DORA_PRICE, does, best, facts, limits, True)


def edits(best, facts, limits):
    return app("Edits: Video Editor", 6738967378, "edits", "Instagram, Inc.", 4.79, 100120, "453.1", "27 Oct 2026", 31, LINKED, "Free; the page lists no purchases", "Editor from Instagram with captions and AI animation of images", best, facts, limits)


def vn(best, facts, limits):
    return app("VN: Photo & Video Editor", 1343581380, "vn", "Ubiquiti Labs, LLC", 4.76, 322992, "2.24.0", "30 Oct 2026", 18, label(TRACK, NOTLINKED), "Free to download; VN Pro $7.99 or $69.99; credits $1 to $10", "Multi-track editor with captions and text to speech", best, facts, limits)


def canva(best, facts, limits):
    return app("Canva AI Photo & Video Editor", 897446215, "canva", "Canva Pty Ltd", 4.87, 3599996, "4.233.0", "27 Oct 2026", 83, label(TRACK, LINKED), "Free to download; Pro from $14.99 a month or $119.99 a year; credits from $1.99", "Design app with a video editor and Veo 3 text to video", best, facts, limits)


def capcut(best, facts, limits):
    return app("CapCut: Photo & Video Editor", 1500855883, "capcut", "BYTEDANCE PTE. LTD.", 4.61, 1125712, "19.9.0", "27 Oct 2026", 20, label(TRACK, LINKED), "Free to download; Standard $9.99 a month, Pro $19.99, yearly $89.99", "Editor with keyframes, auto captions and background removal", best, facts, limits)


def captions(best, facts, limits):
    return app("Captions: AI Edits Your Video", 1541407007, "captions", "Captions, LLC", 4.74, 38915, "13.41.0", "28 Oct 2026", 33, label(TRACK, LINKED, NOTLINKED), "Free to download; Basic $5.99 a week, $9.99 a month or $64.99 a year; Max $24.99", "AI editor, text to video and AI avatars", best, facts, limits)


def kling(best, facts, limits):
    return app("Kling AI: AI Image&Video Maker", 6738049229, "kling", "KLING AI PTE. LTD.", 4.67, 32722, "3.9.30", "29 Oct 2026", 5, label(TRACK, LINKED, NOTLINKED), "Free to download; plans $10, $37 and $92 a month; credits from $1.49", "Text or photo to video, up to 15 s, extendable to 3 minutes", best, facts, limits)


def runway(best, facts, limits):
    facts = list(facts) + ["Also works inside ChatGPT as an app, per its ChatGPT listing."]
    return app("Runway: AI Image & Video", 1665024375, "runway", "Runway AI, Inc.", 4.49, 19176, "103.0.0", "1 Nov 2026", 1, label(TRACK, LINKED, NOTLINKED), "Free to start, per its listing; Standard $14.99 a month or $143.99 a year, Pro $35; credits from $10", "Text or photo to video, several models, and an agent", best, facts, limits)


COLS = ["App", "Price (US)", "What it does", "Languages", "App Store privacy label", "Version (date)", "Rating (US)"]
NOTE = "Prices are in-app purchases listed on each US App Store page on 2 November 2026, and pages list only some. Ratings are that day's App Store average."
METHOD = ["On 2 November 2026 we read each app's US App Store page and Apple's lookup data. What each app does comes from its own listing. We ran no quality test, so we do not say which one looks best.", "Prices change often. Check inside each app before paying."]


def page(group, path, ct, title, h1, description, llms, apps, answer, who, cases, faq, extra_sources=()):
    return {"group": group, "lang": "en", "store": "us", "path": path, "ct": ct, "category": "PhotoVideoApplication", "published": DAY, "updated": DAY, "checked": DAY,
            "title": title, "h1": h1, "description": description, "llms": llms, "answer": answer, "columns": COLS, "table_note": NOTE,
            "apps": apps, "who": who, "cases": cases, "method": METHOD, "faq": faq, "sources": [store(a) for a in apps] + list(extra_sources), "cover": None}


CAPCUT = page(
    "capcut-alt", "best-capcut-alternatives-ai-video-iphone/", "rl-capcut-alt",
    "Best CapCut Alternatives for AI Video on iPhone (2026)", "Best CapCut alternatives for AI video on iPhone",
    "Six iPhone apps to use instead of CapCut, for editing or for AI video: Edits, VN, InShot, Canva, Filmora and Dora, with prices and privacy labels.",
    "Six iPhone alternatives to CapCut: Edits, VN, InShot, Canva, Filmora, Dora. Separates editors from AI generators.",
    [
        edits("the closest free replacement if you post to Instagram.", ["Exports in 4K with no watermark, per its listing.", "Automatic captions, green screen and AI animation of images.", "A dashboard with how your reels perform."], "built around Instagram, and its label links data to you. It does not list text to video."),
        vn("a timeline editor without paying.", ["Its listing says free with no watermark.", "Multi-track timeline, auto captions and text to speech.", "Removes filler words and silences from talking clips."], "AI extras run on credits, and it does not list text to video."),
        app("InShot - Video Editor", 997362197, "inshot", "SHANTANU PTE. LTD.", 4.85, 2519992, "2.0.2", "1 Oct 2026", 16, label(TRACK, NOTLINKED), "Free to download; Pro $4.99 a month, $19.99 a year or $49.99 once", "Editor with auto captions, AI cut and text to speech", "a one-time payment instead of a subscription.", ["The only lifetime price on this list: $49.99.", "AI Cut removes silence and filler words.", "Speed from 0.1x to 100x, keyframes and bilingual subtitles."], "it improves videos you already have; its listing does not offer text to video."),
        canva("making video from text inside a design app.", ["Its listing offers Veo 3 video with sound from a text prompt.", "Video editor with captions and Beat Sync, plus templates for everything else you design."], "general design first, and credits or Pro for AI work."),
        app("Filmora: AI Video Editor&Maker", 1019382747, "filmora", "Shenzhen Wondershare Software Co., Ltd", 4.68, 90136, "15.7.62", "26 Oct 2026", 20, label(TRACK, LINKED, NOTLINKED), "Free to download; Pro $9.99 a month or $45.99 a year; AI credit packs from $8.99", "Editor with text to video, image to video and AI captions", "one app that both edits and generates.", ["Lists Image to Video, Text to Video, AI Auto Cut and Dynamic Captions."], "AI credits are sold separately, and its privacy label lists all three data categories."),
        dora("Text or photo to a short video, several models", "generating the clip you would otherwise film, then finishing it in an editor.", ["About two minutes a video, up to 1080p, no watermark, per its listing.", "Shows the coin cost before you generate."], "it is not an editor: no timeline, so it does not replace CapCut's editing. No free video."),
    ],
    ["Which alternative fits depends on what you use CapCut for. To edit clips you filmed, start with Edits or VN, both free according to their listings. To make video from a sentence, CapCut's own listing does not describe that, so look at Canva, Filmora or Dora.", "For reference, CapCut itself is at version 19.9.0 (27 October 2026), rated 4.6 from over 1.1 million ratings, with Standard at $9.99 a month and Pro at $19.99."],
    ["<strong>Free editing for Instagram:</strong> Edits.", "<strong>A free timeline:</strong> VN.", "<strong>Pay once:</strong> InShot.", "<strong>Text to video with design tools:</strong> Canva.", "<strong>Editing and generating together:</strong> Filmora.", "<strong>A generated clip to finish elsewhere:</strong> Dora."],
    ["Replacing CapCut for captions and quick cuts.", "Avoiding a monthly plan.", "Adding generated shots to a video you filmed."],
    [("What is the best free alternative to CapCut on iPhone?", "Edits and VN both describe themselves as free with no watermark on their listings. Edits lists no purchases; VN sells a Pro plan and credits."),
     ("Which CapCut alternative makes AI video from text?", "On this list Canva, Filmora and Dora describe that on their listings. Edits, VN and InShot do not."),
     ("Does Dora replace CapCut?", "No. Dora generates clips and has no timeline. You would still edit in another app.")],
    [store({"name": "CapCut: Photo & Video Editor", "id": 1500855883})],
)

REELS = page(
    "reels-apps", "best-ai-video-apps-for-instagram-reels-iphone/", "rl-reels",
    "Best AI Video Apps for Instagram Reels on iPhone (2026)", "Best AI video apps for Instagram Reels on iPhone",
    "Six iPhone apps for making Instagram Reels with AI: Edits, CapCut, Canva, Captions, Dora and Kling, sorted by whether you film or generate.",
    "Six iPhone apps for Instagram Reels with AI: Edits, CapCut, Canva, Captions, Dora, Kling.",
    [
        edits("Reels from clips you filmed, from Instagram itself.", ["Captures clips up to 10 minutes and exports in 4K with no watermark.", "Reels performance and trending audio inside the app.", "AI animation of images and automatic captions."], "it does not list text to video, and its label links data to you."),
        capcut("detailed editing, with Instagram named as a destination on its listing.", ["Keyframes, auto captions, text to speech and background removal.", "Speed from 0.1x to 100x."], "the listing describes editing tools rather than generating video from a prompt; its label includes tracking and data linked to you."),
        canva("Reels that match your other designs.", ["Its listing names social media reels and offers Veo 3 video with sound from text.", "Captions and Beat Sync in the editor."], "AI work needs credits or Pro, and the app covers far more than video."),
        captions("talking-to-camera Reels, or an avatar instead of filming.", ["A chat-based editor applies cuts, B-roll and effects from what you describe.", "AI Twin makes a video of you from one selfie, per its listing.", "AI Scale resizes videos for other aspect ratios."], "the avatar look may not suit every account; we did not test it."),
        dora("Text or photo to a short video, several models", "a vertical clip for a Reel with nothing filmed.", ["9:16 for Reels, up to 1080p, no watermark, per its listing.", "About two minutes a video, with the coin cost shown first."], "it does not publish to Instagram or edit on a timeline. No free video."),
        kling("longer generated scenes.", ["Up to 15 seconds in 1080p or 4K, extendable to 3 minutes, per its listing.", "A community feed to clone ideas from."], "credits go quickly on longer clips, and only 5 languages."),
    ],
    ["If you film your Reels, start with Edits, Instagram's own free editor, or CapCut for finer control. If you talk to camera, Captions is built for that. If you have nothing filmed, Canva, Dora or Kling generate video from text.", "None of these apps can promise reach. Edits is the only one here whose listing shows Reels performance inside the app."],
    ["<strong>You film, and want it free:</strong> Edits.", "<strong>You film, and edit in detail:</strong> CapCut.", "<strong>On-brand designs:</strong> Canva.", "<strong>Talking to camera or an avatar:</strong> Captions.", "<strong>Nothing filmed, one short clip:</strong> Dora.", "<strong>Nothing filmed, longer scenes:</strong> Kling AI."],
    ["A faceless Reel from one sentence.", "Captions on a clip you filmed.", "A product clip for a small shop's account."],
    [("What size should an AI video for Reels be?", "Vertical 9:16. Choose it before you generate: resizing a horizontal clip later cuts off the sides."),
     ("Can these apps post to Instagram for me?", "Edits lists easy sharing to Instagram. Dora does not publish for you: you save the clip and upload it yourself."),
     ("Is there a free way to make Reels with AI?", "Edits is free according to its listing and includes AI animation of images and automatic captions. It does not list text to video.")],
)

FREE = page(
    "free-video", "is-there-a-free-ai-video-app-iphone/", "rl-free-video",
    "Is There a Free AI Video App for iPhone? (2026)", "Is there a free AI video app for iPhone?",
    "Mostly no: generating video costs money. What Edits, Runway, VN, iMovie, Grok and Dora really offer for free on iPhone, from their listings.",
    "Honest answer on free AI video apps for iPhone: Edits, Runway, VN, iMovie, Grok, Dora. Dora has no free video.",
    [
        edits("the most you can do for free, according to a listing.", ["Its listing calls it a free video editor, and the page lists no purchases.", "AI animation of images, automatic captions, 4K export with no watermark."], "it does not list text to video, and the listing states no limit either way for AI animation."),
        runway("trying real text to video before paying.", ["Its listing says \"Free to start\", with plans for more credits, higher resolution and faster generation.", "Text to video, image to video and an agent."], "the listing does not say how much is free, and English only."),
        vn("free editing, with AI as an extra.", ["Its listing says free with no watermark.", "Auto captions and text to speech."], "it does not generate video from text. Credits and Pro are sold."),
        app("iMovie", 377298193, "imovie", "Apple Inc.", 4.42, 320070, "3.0.6", "22 Oct 2026", 33, label(LINKED, NOTLINKED), "Free; the page lists no purchases", "Apple's editor, Magic Movies from your own clips", "a finished video from your own photos and clips, at no cost.", ["Magic Movies builds a video from an album with titles, transitions and music.", "20 storyboards to get started."], "it is not generative AI in the sense of making scenes from text. Needs iOS 27."),
        app("Grok", 6670324846, "grok", "X Corp.", 4.87, 1567769, "1.4.61", "1 Nov 2026", 38, label(TRACK, LINKED, NOTLINKED), "Free to download; SuperGrok Lite $10, SuperGrok $30, higher plans to $300", "Assistant with short videos with sound, from text or a photo", "people who may already pay for the assistant.", ["Grok Imagine makes short videos with sound and animates photos, per its listing."], "the listing does not say what video is included without a plan, so we do not call it free."),
        dora("Text or photo to a short video, several models", "paying per clip, with the cost shown before you generate.", ["Each video costs coins, and failed generations return them, per its listing.", "The cost shows before you generate.", "Dora also works inside ChatGPT as an app: <a href=\"https://doravideo.com/chatgpt?utm_source=reviewland&amp;utm_campaign=chatgpt_cta\">how to connect it</a>."], "Dora is not free. There is no free video: you need a plan or coins."),
    ],
    ["Mostly no. Free to download is not free to use: making video with AI costs the app money per clip, so nearly all of them sell plans or credits, and most listings do not say how much you get without paying.", "The closest we found on a listing: Edits is free and includes AI animation of images, but no text to video. Runway says \"Free to start\" for real text to video, without saying how much. Dora is not free, but it shows the cost of each clip before you generate: about $0.52 for 8 seconds with sound on the smallest coin pack, in the <a href=\"https://apps.apple.com/us/app/id6754180384?pt=118348020&amp;ct=rl-free-video\">iPhone app</a> or in the browser at <a href=\"https://doravideo.com/?utm_source=reviewland&amp;utm_medium=guide&amp;utm_campaign=is-there-a-free-ai-video-app-iphone\">doravideo.com</a>."],
    ["<strong>Free editing plus AI animation:</strong> Edits.", "<strong>A first try at text to video:</strong> Runway.", "<strong>A free timeline:</strong> VN.", "<strong>A film from your own clips:</strong> iMovie.", "<strong>You already pay for the assistant:</strong> Grok."],
    ["Testing whether AI video is for you before paying.", "Captions and small edits at no cost.", "A family video from clips you already have."],
    [("Is Dora free?", "No. Dora is free to download, but video needs a Pro plan or coins. Weekly is $6.99 for new subscribers, yearly $119.99, and coin packs start at $4.99 for 300 coins."),
     ("Why do free AI video apps ask for money after installing?", "Each generated clip has a real cost for the app, so free to download usually means a paywall or limited credits. Read the in-app purchases on the App Store page before installing."),
     ("Is there an unlimited free AI video app?", "We found no listing on this page that promises unlimited free AI video generation."),
     ("Do free AI video apps add a watermark?", "It varies. Edits and VN state no watermark on their listings; Dora states none on its videos, but Dora is paid. Others do not say.")],
)

# 7 Nov 2026: ChatGPT cites this page, so its ratings and versions were re-checked (iTunes lookup) and its prices on the US App Store pages (unchanged).
FRESH_7NOV = {"edits": (4.79, 101705, "454.0", "2 Nov 2026"), "runway": (4.49, 19662, "103.0.0", "1 Nov 2026"), "vn": (4.76, 323777, "2.24.0", "30 Oct 2026"),
              "imovie": (4.42, 321064, "3.0.6", "22 Oct 2026"), "grok": (4.87, 1582846, "1.4.62", "6 Nov 2026"), "dora": (4.12, 17, "1.4.2", "26 Oct 2026")}
FREE["apps"] = [dict(a, rating=FRESH_7NOV[a["anchor"]][:2], row=a["row"][:4] + [f"{FRESH_7NOV[a['anchor']][2]} ({FRESH_7NOV[a['anchor']][3]})", f"{round(FRESH_7NOV[a['anchor']][0], 1)}"]) for a in FREE["apps"]]
FREE.update(updated="2026-11-07", checked="2026-11-07", table_note=NOTE.replace("2 November 2026", "7 November 2026"),
            method=[METHOD[0] + " Ratings, versions and prices were re-checked on 7 November 2026.", METHOD[1]])

HOWTO = page(
    "make-video", "how-to-make-an-ai-video-on-iphone/", "rl-make-video",
    "How to Make an AI Video on iPhone: Step by Step (2026)", "How to make an AI video on iPhone, step by step",
    "Choose what you start from, pick a suitable app, check the cost and fix one thing at a time. Five iPhone apps compared: Kling, Runway, Dora, Canva, Captions.",
    "Step-by-step guide to making an AI video on iPhone, with five apps compared: Kling AI, Runway, Dora, Canva, Captions.",
    [
        kling("high resolution and longer scenes.", ["Text or image to video, up to 15 seconds in 1080p or 4K, extendable to 3 minutes, per its listing.", "Clone & Try reuses an idea from the community."], "credits go quickly on long clips; 5 languages."),
        runway("choosing among several models, or describing a whole video.", ["Text, image or video to video.", "Runway Agent plans the shots and assembles them, per its listing.", "Its listing says the first generation takes about two minutes."], "English only."),
        dora("Text or photo to a short video, several models", "a first short vertical clip, with templates if you do not want to write.", ["Pick a template or describe your idea, then add a photo if you want.", "About two minutes a video, up to 1080p, no watermark, per its listing.", "The coin cost shows first, and failed generations return the coins."], "short clips, not long edited videos. No free video."),
        canva("adding a generated clip to a design.", ["Veo 3 video with sound from a text prompt, per its listing.", "An editor with captions afterwards."], "needs credits or Pro for AI work."),
        captions("videos of a person talking, without filming each one.", ["Text to video, an AI avatar from one selfie, and a chat-based editor."], "the look of an avatar may not suit everything; we did not test it."),
    ],
    ["1. Decide what you start from: a sentence, a photo, or clips you filmed. 2. Pick an app that does that: the table below shows which. 3. Choose the shape first: vertical 9:16 for TikTok, Reels or Shorts. 4. Keep it short, because longer clips usually cost more. 5. Check the cost before you generate. 6. Look at the result and change one thing at a time. 7. Save it, and add captions in an editor if you post it.",
     "For a first try, write one sentence with who, what happens and where, such as: a grey cat walks along a rainy window ledge at night, slow camera move. Long scripts need an app that builds several scenes."],
    ["<strong>Best resolution and length on a listing:</strong> Kling AI.", "<strong>Several models or a whole video:</strong> Runway.", "<strong>A first short clip with templates:</strong> Dora.", "<strong>Inside a design:</strong> Canva.", "<strong>A talking person:</strong> Captions."],
    ["A clip from one sentence.", "An old photo that moves.", "A short ad for a small shop."],
    [("How long does an AI video take on iPhone?", "Dora and Runway both say about two minutes on their listings. Longer or higher-resolution clips can take more."),
     ("Do I need editing skills?", "No, for one clip. To join several clips and add captions you need a simple editor afterwards, such as Edits or VN."),
     ("Which iPhone do I need?", "Check the minimum on each listing: Dora needs iOS 18.6, Captions iOS 16, Runway iOS 16.4, Canva iOS 15.4 and Kling iOS 14.")],
)

TALK = page(
    "photo-talk-family", "best-ai-apps-to-make-a-photo-talk-for-family-iphone/", "rl-photo-talk-family",
    "Best AI Apps to Make a Family Photo Talk on iPhone (2026)", "Best AI apps to make a family photo talk on iPhone",
    "For a birthday message or an old family portrait: Avatarify, Revive, MyHeritage, Dora and HeyGen compared, and what to ask before animating someone.",
    "Five iPhone apps for animating family photos or making them talk: Avatarify, Revive, MyHeritage, Dora, HeyGen. Includes advice on consent. Dora's lip sync is web only.",
    [
        app("Avatarify: AI Face Animator", 1512669147, "avatarify", "Avatarify, Inc.", 4.75, 44677, "2.0.32", "12 Mar 2026", 11, label(TRACK, NOTLINKED), "Free to download; premium from $2.49 a week, $3.99 a month or $34.99 a year", "Makes a face in a photo talk, sing or lip-sync", "a short talking greeting from a photo, with your own recording.", ["Upload a photo and record a short video or use audio, per its listing.", "Its listing mentions old photos and portraits, and personalized videos for family."], "no version since March 2026, and much of the listing is about jokes and memes."),
        app("Revive: AI Face Photo Animator", 1616862692, "revive", "RefaceAI Limited", 4.65, 25209, "4.18.0", "1 Jul 2026", 6, label(TRACK, NOTLINKED), "Free to download; PRO from $3.49 a week; lifetime from $18.49", "Animated faces, talking photos and lip sync", "paying once instead of every week.", ["Lip sync with your own voice and expressions, per its listing.", "Lifetime purchases are listed at several prices, from $18.49 to $39.99."], "built around funny filters and effects, so it is less suited to a serious portrait."),
        app("MyHeritage: Family Tree & DNA", 477971748, "myheritage", "MyHeritage Ltd", 4.86, 66488, "7.6.13", "28 Oct 2026", 49, label(LINKED, NOTLINKED), "Free to download; subscriptions listed from $16.99 to $249.99", "Family tree app that animates family photos (Deep Nostalgia, LiveMemory)", "old family photos, when moving is enough.", ["Deep Nostalgia and LiveMemory animate historical and whole-family photos, per its listing.", "Sits alongside your family tree and records."], "its listing promises movement, not speech, so it may not make anyone talk. It is a genealogy service first."),
        dora("A photo to a short video in the app; Lip Sync with your audio on the web", "a clip of a set length, if you already have the audio.", ["Lip Sync takes one photo and one audio file of up to 15 seconds, on doravideo.com.", "It runs in Safari on iPhone."], "the iPhone app itself animates photos without speech: talking is web only. No free video."),
        app("AI Avatar Generator - HeyGen", 6711356409, "heygen", "HeyGen Technology Inc.", 4.78, 30380, "2.8.4", "27 Oct 2026", 3, label(TRACK, LINKED, NOTLINKED), "Free to download; Starter $10 a month, Creator $29, Pro $49 and up; credits from $4.99", "Business avatars; one face photo to a talking video", "reading a typed script, such as a longer family message.", ["One face photo becomes a talking video, and a pasted script is spoken, per its listing."], "made for business, with its examples aimed at agents and founders, so it costs more for one family message."),
    ],
    ["For a short talking message from a photo, Avatarify or Revive do this and use your own recording. For an old family portrait where movement is enough, MyHeritage is built around family history, though its listing does not promise speech. Dora only does talking on the web.",
     "Before you animate someone, ask them, or the closest family if they have died. A voice or face made to say words someone never said can upset people. Say that it was made with AI when you share it, and do not use it to imitate someone to a person who could believe it."],
    ["<strong>A quick talking greeting:</strong> Avatarify.", "<strong>Paying once:</strong> Revive.", "<strong>Old photos that move:</strong> MyHeritage.", "<strong>You have the audio and want a set length:</strong> Dora, on the web.", "<strong>Reading a typed script:</strong> HeyGen."],
    ["A birthday message from a grandparent who agreed to record it.", "A family portrait for a reunion slideshow.", "A short thank-you clip for relatives far away.", "A blurry or scratched old portrait: restore it first with one of the <a href=\"/best-ai-photo-enhancer-apps-iphone/\">AI photo enhancer apps for iPhone</a>, then animate it."],
    [("Can I make a photo of a relative who has died talk?", "Apps can do it, but it is a personal decision. Talk to the closest family first, and avoid putting words in their mouth that they never said. MyHeritage's movement without speech is a gentler option."),
     ("Should I clone a relative's voice?", "Only with their clear permission. It is safer to record your own voice or to have them record the message, which Avatarify and Revive's listings allow for."),
     ("Which photo works best?", "One clear face looking towards the camera is the usual advice. Results depend on the app, and we did not test them."),
     ("Does the Dora iPhone app make photos talk?", "No. The iPhone app animates photos without speech. Lip Sync is on doravideo.com, with an audio file of up to 15 seconds.")],
    [("Dora: best apps to make a photo talk (Lip Sync details)", "https://doravideo.com/blog/best-talking-photo-apps-iphone")],
)

PAGES = [CAPCUT, REELS, FREE, HOWTO, TALK]
