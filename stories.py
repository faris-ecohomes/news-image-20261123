"""Story data for the 23 November 2026 front page.

Every item happened, or was first reported, on Monday 23 November 2026
and was cross-checked against at least two named sources (wire datelines,
not aggregator timestamps). Chip vocabulary: CONFIRMED (2+ sources),
REPORTED (single named source / one side), CLAIM (one side's account),
FORECAST, ONGOING.
"""

# (number, region tag, headline, detail, chip, region-for-count, pin lat, pin lon)
PANELS = [
    (1, "BENGHAZI · WAR AT SEA",
     "Ukraine sinks Russian corvette in a Libyan port",
     "Seven naval drones sank the corvette Merkury and hit the weapons "
     "freighter Angara. Zelensky confirmed it Monday; the SBU says the "
     "drones came from a mothership.",
     "CONFIRMED – WSJ / CNN", "AFRICA", 32.1, 20.1),
    (2, "SANTA CLARA · MARKETS",
     "Nvidia reinstates Huang — and Wall Street erupts",
     "Shares leapt 31% and the Nasdaq 6.5% after Trump pressed the board "
     "to restore the co-founder, 11 days after his resignation.",
     "CONFIRMED – REUTERS", "AMERICAS", 37.4, -122.0),
    (3, "KYIV REGION · WAR",
     "Russian strikes kill 14 near Kyiv",
     "A Dymer apartment block was destroyed; rescuers pulled a boy and a "
     "woman alive from the rubble. Officials count 21 facilities hit.",
     "REPORTED – KYIV", "EUROPE", 50.4, 30.5),
    (4, "ANTALYA · CLIMATE",
     "After COP31's collapse, calls to reform climate summits",
     "The talks failed Sunday over fossil-fuel wording; on Monday "
     "Erdogan claimed groundwork was laid.",
     "CONFIRMED – REUTERS", "EUROPE", 36.9, 30.7),
    (5, "STRAIT OF HORMUZ · ENERGY",
     "Iran vows 'every means' to defy US blockade",
     "Trump warns Tehran of a 'very traumatic' outcome without a "
     "nuclear deal; three more ships struck.",
     "REPORTED – AL JAZEERA", "MIDDLE EAST", 26.5, 56.3),
    (6, "AUSTIN · TECH DEALS",
     "CrowdStrike to buy Zscaler for $43.9bn",
     "The all-stock deal creates a cybersecurity giant as AI-era threats "
     "mount and rivals consolidate.",
     "CONFIRMED – REUTERS", "AMERICAS", 30.3, -97.7),
    (7, "WASHINGTON · POLITICS",
     "Democrats clinch a House majority of at least 258",
     "Their largest since 1992 — Hubbard's defeat of 11-term Rep. Foxx "
     "pushes the tally toward 259.",
     "REPORTED – WIRES", "AMERICAS", 38.9, -77.0),
    (8, "RICHMOND · AI LAW",
     "Virginia and Oregon sue Musk's SpaceX over Grok",
     "The first state suits say Grok's 'spicy mode' flooded X with "
     "sexualised deepfakes, some of children.",
     "CONFIRMED – REUTERS / AP", "AMERICAS", 37.5, -77.5),
    (9, "INDONESIA · DISASTER",
     "34 missing in candy factory fire",
     "The search went on through Monday as investigators opened a probe "
     "into the blaze and families waited for news.",
     "REPORTED – BBC", "ASIA", -6.2, 106.8),
    (10, "BRUSSELS · STRIKE",
     "General strike grounds flights across Belgium",
     "An anti-austerity walkout shut airports and halted trains "
     "nationwide in a day of transport chaos.",
     "CONFIRMED – BBC", "EUROPE", 50.8, 4.4),
    (11, "NEW DELHI · DIPLOMACY",
     "Modi hosts Nepal's Balen Shah in a Delhi thaw",
     "Eight MoUs, from space to security — and an offshore IIT campus "
     "for Nepal.",
     "REPORTED – HINDUSTAN TIMES", "ASIA", 28.6, 77.2),
    (12, "WASHINGTON · CHIP WAR",
     "US to blacklist Megaspeed over AI chips for China",
     "The firm is accused of funneling Nvidia chips to China in the "
     "fallout of the Huang scandal.",
     "REPORTED – BBC", "AMERICAS", 40.0, -76.0),
    (13, "MANCHESTER · ARENA SCARE",
     "89 treated after arena substance scare",
     "12,000 fans were evacuated from Don Toliver's Sunday show; the "
     "probe widened Monday, London date moved.",
     "CONFIRMED – THE TIMES", "EUROPE", 53.5, -2.2),
    (14, "ZURICH · FOOTBALL",
     "US-led bid wins the 2031 Women's World Cup; UK gets 2035",
     "FIFA confirmed four-nation hosts for both editions, each expanded "
     "to 48 teams, on Monday.",
     "CONFIRMED – FIFA / AP", "EUROPE", 47.4, 8.5),
]

# (big figure, caption) — all from Monday's reporting
NUMBERS = [
    ("+31%", "Nvidia's surge as Huang returns"),
    ("$43.9bn", "CrowdStrike's deal for Zscaler"),
    ("258+", "House seats — most since 1992"),
    ("34", "missing in Indonesia factory fire"),
    ("7", "naval drones that sank the Merkury"),
    ("89", "treated after Manchester arena scare"),
]

# (time UTC, text) — wire timestamps of Monday's reports
TIMELINE = [
    ("13:50", "M&S seeks franchise partners for Czech, Greek stores"),
    ("14:37", "Arsenal's Raya ruled out of Tuesday's Dortmund clash"),
    ("20:55", "Alberta arms itself to fund and build gas pipelines"),
    ("21:00", "Closing bell: Nasdaq +6.5% on the Nvidia surge"),
    ("21:51", "Clariant and CD&R in talks to buy Ashland"),
    ("22:17", "AustralianSuper backs Brookfield's $2.53bn bid"),
]

# (place, text) — numbered 15..36 on the page
ALSO_ON = [
    ("WASHINGTON", "Rep. Jimmy Gomez to resign after ethics report"),
    ("HARRISBURG", "Measles deaths rise to nine; 1,638 cases logged"),
    ("ATLANTA", "Delta cancels 92 more flights as outage ripples on"),
    ("LAFAYETTE", "Amtrak cancels Sunset Limited after derailment"),
    ("DHAKA", "Garment workers reject owners' wage offer at talks"),
    ("ZURICH", "Clariant and CD&R in talks to buy Ashland"),
    ("SAO PAULO", "Braskem creditors back $4.9bn restructuring plan"),
    ("CALGARY", "Alberta can fund and build gas pipelines itself"),
    ("LONDON", "M&S hunts franchise partners for Czech, Greek stores"),
    ("SYDNEY", "AustralianSuper backs Brookfield's $2.53bn RWC bid"),
    ("MADRID", "Left parties savage PP–Vox pact in live TV debate"),
    ("TEHRAN", "Singer and her team flogged, Iranian website says"),
    ("BRIDGETOWN", "Guterres urges tougher global rules for AI"),
    ("ITURI", "Fighting disrupts Ebola response, WHO warns"),
    ("ABUJA", "Presidential villa hit by water and power cuts"),
    ("LONDON", "Burnham defies ex-PMs in EU rejoin row"),
    ("MELBOURNE", "Prespakis wins AFLW best and fairest award"),
    ("MOSCOW", "Kremlin warns Albania over drone claims — denied"),
    ("WASHINGTON", "Democrats plan 12 debates for 2028 primary"),
    ("MARKETS", "Bitcoin back to $61K after two-year-low plunge"),
    ("IOWA", "Trump halts Army's toxic-explosives detonation plan"),
    ("SPACE", "NASA's picture of the day: nebula Lynds 1251"),
]

DATE_CHECK_EARLIER = (
    "Left out on purpose — they broke before Monday: Huang's resignation "
    "amid scandal (12 Nov); the Benghazi attack itself (dawn, Sun 22 Nov); "
    "the COP31 collapse (Sun 22 Nov); Delta's tech outage (Sun 22 Nov); "
    "the Sunset Limited derailment (Sun 22 Nov)."
)
DATE_CHECK_FUTURE = (
    "Not yet: South Korea's rate decision (Thu 26 Nov); Arsenal v "
    "Dortmund (Tue 24 Nov); Spain's 29-N election (Sun 29 Nov)."
)

TOTAL_STORIES = len(PANELS) + len(ALSO_ON)
