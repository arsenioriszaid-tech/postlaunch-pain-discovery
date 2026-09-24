#!/usr/bin/env python3
"""Register stream target-report sources. Run once."""
import subprocess
S = "/root/.hermes/skills/research/grounded-citations/scripts/sources.py"
URLS = [
 ("KTS terms auto-renew", "https://keepthescore.com/terms/"),
 ("Caspar pricing strategy post", "https://casparwre.de/blog/saas-pricing-strategy/"),
 ("Inkdrop pricing Stripe", "https://www.inkdrop.app/pricing/"),
 ("Inkdrop docs Stripe faq", "https://docs.inkdrop.app/faq"),
 ("Devaslife doubled price churn", "https://www.devas.life/how-i-successfully-doubled-my-saas-price-to-10-month-and-lowered-the-churn-rate-to-3/"),
 ("Inkdrop forum price change", "https://forum.inkdrop.app/t/inkdrop-price-change/4366"),
 ("StarterStory ScreenshotOne 12K", "https://www.starterstory.com/stories/how-i-built-it-12k-month-micro-saas"),
 ("FounderStories Dmytro 20K", "https://startupfounderstories.com/stories/dmytro-krasun-screenshotone-20k-mrr"),
 ("IH ScreenshotOne family API", "https://www.indiehackers.com/post/tech/working-towards-financial-independence-with-an-api-saas-while-raising-a-family-l8gTzlBLNhN6I4NF4KsC"),
 ("Liinks pricing trial", "https://www.liinks.co/pricing"),
 ("Liinks about Charlie", "https://www.liinks.co/about"),
 ("StarterStory Liinks 25K", "https://www.starterstory.com/stories/liinks-supercharge-your-link-in-bio"),
 ("IH HabitPixel 0-1K", "https://www.indiehackers.com/post/from-0-to-1k-mrr-in-8-months-bootstrapping-habit-pixel-as-a-solo-dev-53d8687d15"),
 ("NocodeExits HabitPixel", "https://nocodeexits.substack.com/p/how-hirvesh-munogee-grew-habit-pixel"),
 ("PlayStore HabitPixel", "http://play.google.com/store/apps/details?hl=en_US&id=com.habitpixel.app"),
 ("Medium indie log 21 Hirvesh", "https://medium.com/@hirvesh/weekly-indie-log-21-b1febf3f1693"),
 ("ARRfounder Shri 5.7K churn", "https://arrfounder.com/@shri_vatz"),
 ("IndieHustle Stagetimer video", "https://www.indiehustle.co/p/a-simple-countdown-timer-for-videos"),
 ("FounderStories Lukas 20K", "https://startupfounderstories.com/stories/lukas-hermann-stagetimer-20k-mrr"),
 ("Nusii blog card defense", "https://nusii.com/blog/why-we-ask-for-a-credit-card"),
 ("Crunchbase Nusii", "https://www.crunchbase.com/organization/nusii"),
 ("Senja authors Olly", "https://senja.io/authors/olly-meakings"),
 ("Podco Senja 800K cofounder", "https://pod.co/product-led-podcast/bootstrapping-senja-to-800k-arr-with-a-co-founder-i-ve-never-met"),
 ("Famewall 1K MRR story", "https://famewall.io/founder-stories/journey-to-1000-mrr/"),
 ("LinkedIn Goutham Famewall", "https://in.linkedin.com/in/goutham-jay-604457140"),
 ("SiteGPT contact founders", "https://sitegpt.ai/contact-us"),
 ("StarterStory SiteGPT PMF", "https://www.starterstory.com/stories/sitegpt"),
 ("LinkedIn SiteGPT 20 onboarded", "https://www.linkedin.com/posts/pbteja1998_we-onboarded-20-new-businesses-to-sitegpt-activity-7401266164330348545-He92"),
 ("SavvyCal company Derrick", "https://savvycal.com/company"),
 ("SavvyCal friendly email", "https://savvycal.com/eim/"),
 ("PostStatus SavvyCal trial", "https://poststatus.com/upcoming-webinar-the-savvycal-story-with-founder-derrick-reimer/"),
 ("UnlockSaaS Cal-vs-SavvyCal", "https://unlocksaas.com/vs/cal-com-vs-savvycal"),
 ("Cal pricing free tier", "https://cal.com/pricing"),
 ("Plausible register 4 asks", "https://plausible.io/docs/register-account"),
 ("Senja pricing free-15", "https://senja.io/pricing"),
 ("BlogRecorder shutdown excluded", "https://blogrecorder.com/"),
]
ok = fail = 0
for title, url in URLS:
    r = subprocess.run(["python3", S, "add", url, "--title", title],
                       capture_output=True, text=True)
    if r.returncode == 0:
        ok += 1
    else:
        fail += 1
        print("FAIL", url, r.stderr[-200:])
print(f"registered {ok}, failed {fail}")
