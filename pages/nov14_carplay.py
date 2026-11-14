"""Best CarPlay widget and video apps for iPhone. EN. Our app: CarScreen (id6833951195), on sale 13 Nov 2026.

Checked 2026-11-14 (JST): iTunes lookup for the six competitors and the US App Store web page for all seven.
CarScreen: the iTunes lookup still returned 0 results (indexing delay), so name, price and in-app purchases come
from apps.apple.com/us/app/id6833951195 (200) and the rating is "New". Features only from each listing's own text.
Title chosen from App Store search hints (US, 14 Nov): "carplay widgets" (7 hints), "car screen widgets", "carplay screen mirror".
"""

DAY = "2026-11-14"
AS_OF = "Nov 14, 2026"


def src(cc="us"):
    return [
        ("CarDash: Video Player for Cars (App Store)", f"https://apps.apple.com/{cc}/app/id6797764175"),
        ("APTV - Car TV Player & Cast (App Store)", f"https://apps.apple.com/{cc}/app/id6476621657"),
        ("CarTV - M3U IPTV Player & Cast (App Store)", f"https://apps.apple.com/{cc}/app/id6800211040"),
        ("CarPlay Screen Mirroring (App Store)", f"https://apps.apple.com/{cc}/app/id6740481525"),
        ("CarScreen: Car Widgets & Video (App Store)", f"https://apps.apple.com/{cc}/app/id6833951195"),
        ("myCar: Car Widgets・Play Themes (App Store)", f"https://apps.apple.com/{cc}/app/id6755033589"),
        ("Car Connect, Play, Widgets (App Store)", f"https://apps.apple.com/{cc}/app/id1665625393"),
    ]


EN = {
    "group": "carplay-apps", "lang": "en", "store": "us", "cover": None,
    "path": "best-carplay-widget-and-video-apps-iphone/",
    "ct": "rl-carplay-widgets-video",
    "category": "UtilitiesApplication",
    "published": DAY, "updated": DAY, "checked": DAY,
    "ours_rank": 5,
    "title": "Best CarPlay Widget and Video Apps for iPhone (2026)",
    "h1": "Best CarPlay widget and video apps for iPhone (2026)",
    "description": "Seven iPhone apps for your car's dashboard screen compared: CarPlay widgets, parked video, M3U playlists and price. Checked on the App Store on 14 November 2026.",
    "llms": "Compares seven iPhone apps for the car's CarPlay screen (CarDash, APTV, CarTV, CarPlay Screen Mirroring, CarScreen, myCar, Car Connect) by video while parked, widgets, M3U playlists, price and rating. States that car video only works while parked and only in cars whose maker supports it.",
    "answer": [
        "If you want widgets and video on your car's screen, CarDash, APTV and CarTV are the listings built around video and your own M3U playlists, and myCar and Car Connect are the ones built around photos and widgets without video. We checked seven apps on the App Store on Nov 14, 2026.",
        "Video on a car screen only plays while the car is parked and only in cars whose maker supports it, so a paid app can do nothing in your car. Check that first: one of the seven (CarScreen) plays a free 5-second test clip before you pay, and most of the others say in their descriptions that video is for when you are parked.",
    ],
    "columns": ["App", "Price (US)", "Video on the car screen", "Widgets or dashboard", "Own M3U playlists", "Rating (US)"],
    "table_note": "Price, in-app purchases and rating are from the US App Store as of Nov 14, 2026; all seven are free to download. The other columns are what each app's own App Store description says; \"Not mentioned\" means the description does not say. CarScreen is new (on sale 13 Nov 2026), so it has no rating yet.",
    "apps": [
        {
            "name": "CarScreen: Car Widgets & Video", "id": 6833951195, "ours": True, "anchor": "carscreen",
            "developer": "Saga Ltd.",
            "row": ["Free; one-time Pro purchase, listed from $4.99 to $14.99", "Yes: your own videos from Photos and Files over AirPlay, parked only, in cars whose maker supports it",
                    "Yes: photo, clock and date, countdown, car name and plate, parking place and time, your own message", "Yes (it includes no channels)", "New"],
            "best_for": "checking whether video works in your car before paying, and paying once instead of subscribing.",
            "facts": [
                "Plays a free 5-second test clip and tells you whether video works in your car before you buy anything.",
                "Plays your own videos from Photos and Files, your own M3U playlists and a simple built-in browser for pages you choose.",
                "Free: the car check, 2 widgets (Photo and Clock) and 1 theme, with no account and no time limit. One payment unlocks video, playlists, the browser, all 6 widgets, all themes and the parking timer; the description says no subscription and no renewals.",
                "Widgets are added in Settings > General > CarPlay > your car > Widgets, per the listing.",
            ],
            "limits": "brand new, so it has no rating yet; video only works while parked and only in cars whose maker supports it; it includes no channels or content, so you bring your own videos and playlists.",
        },
        {
            "name": "CarDash: Video Player for Cars", "id": 6797764175, "anchor": "cardash",
            "developer": "Laigang Wang",
            "row": ["Free; in-app purchases (subscriptions) from $5.99 to $39.99", "Yes: on compatible CarPlay displays, parked only",
                    "Yes: photo, date, countdown and license plate widgets", "Yes (M3U and M3U8)", "4.6"],
            "best_for": "one app that combines parked video, M3U playlists, widgets, sounds and trip scoring.",
            "facts": [
                "Imports local videos from Photos or Files, opens websites in a built-in browser and can start iPhone screen mirroring through the system Screen Broadcast control.",
                "Widgets for photo, date, countdown and license plate, with vehicle and brand designs.",
                "Also scores your trips: route history, acceleration, braking and cornering.",
                "Version 1.3.7 (12 Nov 2026), iOS 17.0 or later.",
            ],
            "limits": "its in-app purchases are subscriptions with many price points; its description says video output depends on your iPhone, iOS version, vehicle and content source, and that a CarPlay audio connection alone does not guarantee video.",
        },
        {
            "name": "APTV - Car TV Player & Cast", "id": 6476621657, "anchor": "aptv",
            "developer": "Ion Danilov",
            "row": ["Free; Premium weekly $9.99 or lifetime $19.99", "Yes: on the CarPlay screen, parked only; needs iOS 27 or later and a vehicle that supports it",
                    "Not mentioned", "Yes (M3U and M3U8, by link or file)", "4.3"],
            "best_for": "an M3U player that also plays on your TV with AirPlay and on a supported car display.",
            "facts": [
                "Browse your playlists and channels on the CarPlay screen; playback stops automatically when you start driving.",
                "Streams to Apple TV and AirPlay-compatible smart TVs; groups channels into categories and keeps favorites.",
                "Plays MKV, MP4, AVI, MOV, WMV and more; it provides no channels or playlists.",
                "Version 2.4.9 (11 Nov 2026), iOS 17.6 or later.",
            ],
            "limits": "its description says CarPlay video needs iOS 27 or later and that many vehicles do not support CarPlay video yet; no widgets are mentioned.",
        },
        {
            "name": "CarTV - M3U IPTV Player & Cast", "id": 6800211040, "anchor": "cartv",
            "developer": "Lyntra Technology Ltd",
            "row": ["Free; weekly $3.99, yearly $45.99 or lifetime $27.00", "Yes: mirrors the whole iPhone screen to the car display", "Not mentioned", "Yes (M3U and M3U8)", "4.5"],
            "best_for": "an M3U and media-server player that mirrors any app to the car display.",
            "facts": [
                "Mirrors your whole iPhone screen to the car display, so any app shows up, even ones without a Cast button.",
                "Plays M3U and M3U8 playlists, HLS and HTTP streams, with subtitles, and connects to your own Jellyfin or Emby server.",
                "Car mode: a landscape layout with large controls for a phone in a dashboard mount, for passengers only.",
                "Version 1.1.6 (23 Oct 2026), iOS 18 or later.",
            ],
            "limits": "no widgets are mentioned, and its description says never to watch while driving and that it is for passenger use only.",
        },
        {
            "name": "CarPlay Screen Mirroring", "id": 6740481525, "anchor": "carplay-screen-mirroring",
            "developer": "Oliver Davis",
            "row": ["Free; weekly subscription $6.99 (with a trial)", "Yes: videos, photos, YouTube and web videos, intended for when the car is parked", "Not mentioned", "Not mentioned", "4.1"],
            "best_for": "casting a video, photos or YouTube to the car screen in a few taps, with a weekly plan.",
            "facts": [
                "Casts videos, photos and albums from your iPhone to the CarPlay display and mirrors the iPhone screen in real time.",
                "Plays videos from websites and can also cast to a smart TV at home.",
                "Version 1.2 (22 Oct 2026), iOS 16.6 or later.",
            ],
            "limits": "the only paid option listed is a weekly subscription, and no widgets or playlists are mentioned.",
        },
        {
            "name": "myCar: Car Widgets・Play Themes", "id": 6755033589, "anchor": "mycar",
            "developer": "KarmaTECH OU",
            "row": ["Free; in-app purchases (subscriptions and one-time) from $0.99 to $34.99", "Not mentioned (photos, icons and GIFs)", "Yes: couple photos, custom icons, animated GIFs, startup sounds", "Not mentioned", "4.6"],
            "best_for": "personalising how the car screen looks with your photos, icons and animated GIFs.",
            "facts": [
                "Add your own photos, choose icons or show animated GIFs on the car screen.",
                "Tap to hear a startup sound, from engine sounds to electric tones.",
                "Premium Mode unlocks more customisation options and layouts.",
                "Version 1.13.0 (7 Nov 2026), iOS 15.1 or later.",
            ],
            "limits": "its description is about looks, not video: no video or playlists are mentioned; many different in-app purchase prices.",
        },
        {
            "name": "Car Connect, Play, Widgets", "id": 1665625393, "anchor": "car-connect",
            "developer": "Bloomup LTD",
            "row": ["Free; subscriptions and lifetime access from $9.99 to $69.99", "Not mentioned", "Yes: weather, photos and other glanceable info on the car display, plus a driving mode", "Not mentioned", "4.7"],
            "best_for": "a driving dashboard with widgets, vehicle stats and a service log rather than video.",
            "facts": [
                "Driving Mode turns your phone into an in-car display with navigation, calls, music and vehicle stats.",
                "Widgets add live weather, your photos or other info to the in-car display.",
                "Tracks fuel, battery, oil life and tire pressure, with a service tracker and reminders.",
                "Version 2.1.3 (13 Nov 2026), iOS 17.6 or later.",
            ],
            "limits": "its description does not mention playing video; full features need a subscription or a lifetime purchase.",
        },
    ],
    "who": [
        "<strong>You want video on a compatible car screen with your own playlists:</strong> CarDash, APTV or CarTV.",
        "<strong>You are not sure your car supports video:</strong> CarScreen plays a free 5-second test clip first; with the others, the paid plan is how you find out.",
        "<strong>You want to pay once, not subscribe:</strong> CarScreen (one-time Pro), or the lifetime options of APTV and CarTV.",
        "<strong>You only want a nicer car screen:</strong> myCar for photos, icons and GIFs, or Car Connect for widgets and a driving dashboard.",
        "<strong>You want to mirror your whole phone to the car:</strong> CarTV or CarPlay Screen Mirroring.",
    ],
    "cases": [
        "Watching your own videos during a charging stop or while waiting in a parked car (CarDash, APTV, CarTV, CarScreen).",
        "Putting a photo, the time and a countdown to a trip on the car screen (CarDash, CarScreen, myCar).",
        "Playing the M3U playlists you already have (CarDash, APTV, CarTV, CarScreen). None of these apps includes channels.",
        "Seeing weather and vehicle stats on the car display (Car Connect).",
    ],
    "method": [
        f"On 14 November 2026 we searched the US App Store for car widget and CarPlay video apps, opened Apple's lookup data for six of them and the US App Store page for all seven, and copied name, price, in-app purchases, rating, version and date. CarScreen went on sale on 13 November and Apple's lookup did not return it yet, so its name and prices come from its App Store page and its rating is shown as New.",
        "Features come only from each app's own App Store description, never from tests of ours: we did not drive or park with every app in every car. Apps are ordered by how well their listing fits video plus widgets on a car screen, not by rating. Widgets on a car screen and parked video depend on your car, your iPhone and your iOS version.",
        "Safety: never watch video while driving. Every listing above says video is for when the car is parked.",
    ],
    "faq": [
        ("Can you watch videos on a car screen with an iPhone?",
         "Only in some cars, and only while parked. The listings of CarDash, APTV, CarScreen and CarPlay Screen Mirroring all say video plays only when the car is parked, and APTV says many vehicles do not support CarPlay video yet. Test with the free clip or the free version before you pay."),
        ("Does CarPlay have widgets?",
         "CarScreen's listing says to add widgets on your iPhone in Settings > General > CarPlay > your car > Widgets. Widgets in CarPlay depend on your iOS version and your car."),
        ("Which of these apps include channels or content?",
         "None. CarDash, APTV, CarTV and CarScreen say they are players: you add your own M3U playlists or videos and must have the right to use them."),
        ("Is there a car video app without a subscription?",
         "CarScreen's listing says one payment unlocks everything, with no subscription. APTV and CarTV list lifetime purchases ($19.99 and $27.00) next to their subscriptions."),
        ("Is it safe to watch video in the car?",
         "Only when the car is parked. Never watch video while driving, and follow local traffic laws."),
    ],
    "sources": src("us"),
}

PAGES = [EN]
