"""Calm alternatives for iPhone. EN. Our app: Drop (id1462269642), sold as "Sleep Sounds & Focus: Drop".

Checked 2026-10-16: iTunes lookup API + App Store web pages (US). Drop 2.9 was
live that day. Its listing names five nature sounds; the app itself has 32 sounds
(10 free), per the 2.9 code and aisagalab.com/drop.html. ES page: Spain store, same day.
"""

from pages.store_1016 import refresh

CHECKED = "2026-10-16"


def src(cc):
    return [
        ("Drop (App Store)", f"https://apps.apple.com/{cc}/app/id1462269642"),
        ("Calm (App Store)", f"https://apps.apple.com/{cc}/app/id571800810"),
        ("Headspace (App Store)", f"https://apps.apple.com/{cc}/app/id493145008"),
        ("Insight Timer (App Store)", f"https://apps.apple.com/{cc}/app/id337472899"),
        ("BetterSleep (App Store)", f"https://apps.apple.com/{cc}/app/id314498713"),
        ("Medito (App Store)", f"https://apps.apple.com/{cc}/app/id1500780518"),
        ("White Noise Lite (App Store)", f"https://apps.apple.com/{cc}/app/id292987597"),
    ]


EN = {
    "group": "calm-alternatives", "cover": "sleep-sounds", "lang": "en", "store": "us",
    "path": "calm-alternatives-iphone/",
    "ct": "rl-calm-alt",
    "category": "HealthApplication",
    "published": CHECKED, "updated": CHECKED, "checked": CHECKED,
    "title": "Best Calm alternatives for iPhone users who want sleep and meditation (2026)",
    "h1": "Calm alternatives for iPhone in 2026",
    "description": "Seven alternatives to Calm on iPhone: Headspace, Insight Timer, BetterSleep, Medito, White Noise Lite and Drop. Prices, ratings and privacy checked.",
    "llms": "Compares Calm with six alternatives for iPhone (Headspace, Insight Timer, BetterSleep, Medito, White Noise Lite, Drop) by price, content type (meditations, sleep stories, sleep sounds, white noise), privacy label and App Store rating.",
    "disclosure": "Drop is made by Saga Labs, the company behind Reviewland. It is one more option in this list, not placed first because it is ours, and it is a much smaller app than Calm. The other apps are not ours and we get nothing from them; their links go to their normal App Store pages.",
    "answer": [
        "The best Calm alternative depends on what you use Calm for. For guided meditation without paying, Medito is completely free and Insight Timer has a large free library. For sleep sounds and stories, BetterSleep is the closest paid match. For plain white noise, White Noise Lite is free with 50+ sounds. If you only want short breathing sessions with nature sounds and no ads, Drop does that, and nothing else.",
        "Calm itself is a free download with a Premium subscription; Headspace charges $12.99 a month or $69.99 a year in the US. All prices below are the ones listed on the App Store on 16 October 2026.",
    ],
    "columns": ["App", "Price (US)", "What it is best at", "Sleep sounds / white noise", "App Store privacy label", "Version (date)", "Rating (US)"],
    "table_note": "All seven are free to download. Prices are the in-app purchases listed on the US App Store on 16 October 2026 (an app can list several price points for the same plan). Ratings are the App Store average and number of ratings that day.",
    "apps": [
        {
            "name": "Sleep Sounds & Focus: Drop", "id": 1462269642, "ours": True, "anchor": "drop",
            "developer": "Saga Ltd.", "rating": (4.42, 12),
            "row": ["Free (9 sounds); Drop Pro listed as monthly $4.99, access $14.99 and lifetime options", "Short guided-breathing sessions (2 to 20 minutes) and calming sounds with a sleep timer", "53 nature, ambient and noise sounds, 9 free; white noise free, pink and brown noise with Drop Pro",
                    "Data Not Linked to You (usage data)", "2.10 (24 Oct 2026)", "4.4 (12 ratings)"],
            "best_for": "a quiet, ad-free app with calming sounds, a sleep timer and short breathing sessions, when a full meditation library is more than you need.",
            "facts": [
                "Breathing sessions of 2, 5, 10 and 20 minutes with visual breathing guides.",
                "53 sounds in three groups (nature, ambient, noise); 9 are free: white noise, crackling fire, forest, heartbeat, lake, coffee shop, falling snow, desert wind and dolphins. Rain, ocean, pink and brown noise need Drop Pro.",
                "Sleep timer of 15, 30 or 45 minutes, 1, 2 or 8 hours, with a 30-second fade-out.",
                "A plant grows through five stages as you practise; streaks and achievements.",
                "Home screen widgets, works offline, no ads.",
                "6 languages (English, Japanese, Chinese, French, German, Turkish), iOS 18 or later.",
            ],
            "limits": "no sleep stories, no teacher-led meditation library, no sleep tracking and no mixer: one sound at a time, and pink and brown noise need Drop Pro. Only 12 ratings so far, and it needs iOS 18.",
        },
        {
            "name": "Calm", "id": 571800810, "anchor": "calm",
            "developer": "Calm.com, Inc.", "rating": (4.77, 1987792),
            "row": ["Free; Calm Premium subscription (listed $14.99 to $79.99 depending on plan)", "Sleep Stories, guided meditation, breathwork, music", "Sleep sounds and soundscapes (ocean, heavy rain, campfire)",
                    "Data Linked to You (contact info, health and fitness, purchases, search history and more)", "7.3 (8 Oct 2026)", "4.8 (1,987,792 ratings)"],
            "best_for": "bedtime stories read by well-known narrators and a big, polished all-round library.",
            "facts": [
                "100+ Sleep Stories (listing says new ones every month), including ones narrated by Matthew McConaughey and Stephen Fry.",
                "Daily Calm, Daily Jay and other daily sessions; 7- and 21-day programs; breathing exercises.",
                "Saves sessions to Apple Health (Mindful Minutes).",
                "10 languages, iOS 18 or later, 179 MB.",
            ],
            "limits": "most of the content needs Premium, and the privacy label lists several kinds of data linked to you, including health and fitness data.",
        },
        {
            "name": "Headspace: Sleep & Meditation", "id": 493145008, "anchor": "headspace",
            "developer": "Headspace Inc.", "rating": (4.84, 973795),
            "row": ["Free; monthly $12.99, annual $69.99 (Plus listed up to $94.99)", "Guided meditations and courses, with optional therapy and coaching", "Sleep sounds, sleepcasts and sleep meditations",
                    "Data Linked to You (contact info, health and fitness, location and more)", "8.36.1 (15 Oct 2026)", "4.8 (973,795 ratings)"],
            "best_for": "a structured, course-style approach to meditation, with human support available.",
            "facts": [
                "500+ guided meditations, from 3-minute resets to longer sessions.",
                "Sleep tools: sleepcasts, sleep meditations and sleep sounds.",
                "Optional therapy and coaching, plus an AI companion called Ebb, per its listing.",
                "English only, iOS 15.6 or later, 451 MB, the largest app here.",
            ],
            "limits": "the listing is English only, therapy and coaching are separate paid services, and it collects the most data of the apps here.",
        },
        {
            "name": "Insight Timer: Meditate, Sleep", "id": 337472899, "anchor": "insight-timer",
            "developer": "Insight Network Inc", "rating": (4.9, 447855),
            "row": ["Free; Premium listed $9.99 and $59.99, family $89.99", "Huge free library of guided meditations, talks and music", "Thousands of music tracks and ambient sounds",
                    "Data Linked to You (contact info, location, health and fitness, purchases and more)", "20.38.0 (9 Oct 2026)", "4.9 (447,855 ratings)"],
            "best_for": "free guided meditation from many different teachers, plus a meditation timer.",
            "facts": [
                "Thousands of free guided meditations and talks; the listing says 80+ new free ones are added daily.",
                "Meditation timer, stats and milestones, discussion groups and Apple Health Mindful Minutes.",
                "Thousands of music tracks and ambient sounds.",
                "10 languages, iOS 15 or later, 242 MB.",
            ],
            "limits": "the amount of content makes it harder to choose; Premium unlocks extra features, and its privacy label lists many data types linked to you.",
        },
        {
            "name": "BetterSleep: Relax and Sleep", "id": 314498713, "anchor": "bettersleep",
            "developer": "BetterSleep Health, LLC", "rating": (4.74, 390799),
            "row": ["Free; Premium listed from $11.99 to $99.99 depending on plan", "Sleep sounds, sleep stories, sleep tracker and recorder", "300+ sleep sounds and music tracks, including white noise",
                    "Data Linked to You (contact info, purchases, usage and more); some data not linked", "26.18 (8 Oct 2026)", "4.7 (390,799 ratings)"],
            "best_for": "sleep-first people who want a sound mixer, stories and a sleep tracker in one app.",
            "facts": [
                "300+ sleep sounds and music tracks (nature, ASMR, white noise, binaural beats) you can mix.",
                "250+ meditations and hypnosis sessions and 100+ sleep stories.",
                "Sleep tracker and sleep recorder; optional HealthKit integration; bedtime reminders and timers.",
                "10 languages, iOS 15 or later, 317 MB.",
            ],
            "limits": "premium sounds and content need a subscription, and many different price points are listed for it.",
        },
        {
            "name": "Medito: Mindfulness Meditation", "id": 1500780518, "anchor": "medito",
            "developer": "Medito Stichting", "rating": (4.9, 4262),
            "row": ["Free, no in-app purchases (non-profit)", "Free guided meditation, courses and sleep stories", "Soundscapes: rain, ocean, white noise",
                    "Data Linked to You (identifiers); usage data not linked", "2609.27.0 (29 Sep 2026)", "4.9 (4,262 ratings)"],
            "best_for": "completely free guided meditation from a non-profit.",
            "facts": [
                "Courses for daily calm, focus, anxiety and sleep; 7-day starter and 30-day programmes.",
                "Sleep stories and soundscapes; offline mode; breathing timers and body scans.",
                "English only, iOS 15 or later, 87 MB.",
            ],
            "limits": "a smaller library than Calm or Headspace, and English only.",
        },
        {
            "name": "White Noise Lite", "id": 292987597, "anchor": "white-noise-lite",
            "developer": "TMSOFT", "rating": (4.82, 277342),
            "row": ["Free, no in-app purchases listed", "Looped sounds, sound mixer and sleep timer", "50+ sounds incl. white, pink, brown, blue and violet noise",
                    "Data Linked to You (user content); other data not linked", "8.7.3 (3 Oct 2026)", "4.8 (277,342 ratings)"],
            "best_for": "plain white, pink or brown noise and fans, rain or trains, with timers and alarms.",
            "facts": [
                "50+ looped sounds, including white, pink, brown, blue and violet noise.",
                "Mix Pad to build your own mixes; background audio so you can use other apps.",
                "Timers and alarms that fade audio in and out; full-screen clock.",
                "3 languages (English, French, Spanish), iOS 14 or later, 94 MB.",
            ],
            "limits": "no meditation, breathing or sleep stories: it is a sound machine only.",
        },
    ],
    "who": [
        "<strong>You want guided meditation and do not want to pay:</strong> Medito or Insight Timer.",
        "<strong>You want bedtime stories and a polished library:</strong> Calm, or BetterSleep if sleep is your main goal.",
        "<strong>You want courses, and maybe a therapist or coach:</strong> Headspace.",
        "<strong>You only need white noise or brown noise:</strong> White Noise Lite.",
        "<strong>You want calming sounds with a sleep timer, short breathing sessions and no clutter:</strong> Drop.",
    ],
    "cases": [
        "Falling asleep: Sleep Stories (Calm), sleep tracker and mixer (BetterSleep), constant white noise (White Noise Lite).",
        "A two-minute reset between meetings (Drop's 2-minute session or a short Headspace meditation).",
        "Daily meditation on a budget (Medito, Insight Timer).",
        "Masking street or household noise at night (White Noise Lite, BetterSleep).",
    ],
    "method": [
        "On 16 October 2026 we opened each app's US App Store page and Apple's lookup data: in-app purchases, version and release date, rating and number of ratings, languages, size, minimum iOS and the privacy label. Features are the ones each developer lists on its App Store page; for Drop, which is ours, the sound list comes from the app itself (version 2.10, updated 24 October 2026), because its listing only names five. We did not invent ratings or reviews, and we did not test the audio quality of each app.",
    ],
    "faq": [
        ("What is the best alternative to Calm on iPhone?",
         "Headspace is the closest for guided meditation, BetterSleep for sleep sounds and stories, Medito for a completely free option and Insight Timer for the biggest free library. It depends on whether you use Calm for meditation, sleep or sounds."),
        ("Is there a free alternative to Calm?",
         "Yes. Medito is free with no in-app purchases, Insight Timer has a large free library with an optional Premium, and White Noise Lite is free for sounds."),
        ("Which Calm alternative has white noise?",
         "White Noise Lite has white, pink, brown, blue and violet noise. BetterSleep lists white noise among 300+ sounds. Medito lists white noise in its soundscapes. Drop, since version 2.10, has white noise free and pink, brown and deep brown noise with Drop Pro."),
        ("Does Drop have sleep stories like Calm?",
         "No. Drop offers short guided-breathing sessions and 53 calming sounds (9 free) with a sleep timer. It has no sleep stories and no meditation library."),
        ("How much does Calm cost?",
         "Calm is free to download and lists Premium subscription prices from $14.99 to $79.99 on the US App Store, depending on the plan. Check the in-app offer before you subscribe."),
    ],
    "sources": src("us"),
}

refresh(EN, "us")

PAGES = [EN]
