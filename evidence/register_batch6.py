#!/usr/bin/env python3
"""Register experiment-target sources. Run once."""
import subprocess
S = "/root/.hermes/skills/research/grounded-citations/scripts/sources.py"
URLS = [
 ("Caspar 10K revenue lessons", "https://casparwre.de/blog/lessons-learned-after-10k-revenue/"),
 ("Caspar 12 months solo", "https://casparwre.de/blog/12-months-as-a-solo-developer/"),
 ("IH VC-money Caspar 11K", "https://www.indiehackers.com/post/vc-money-broke-tech-20c2c72807"),
 ("IndieHustle KeepTheScore 190K ARR", "https://www.indiehustle.co/p/from-side-project-to-a-190000-arr"),
 ("IH GuideJar 4K solo", "https://www.indiehackers.com/post/how-shri-vatz-grew-guidejar-to-4k-mrr-solo-d5ab64601a"),
 ("Fakemayo GuideJar 4K", "https://www.fakemayo.com/p/how-shri-vatz-grew-his-side-hustle-guidejar-into-a-4k-mrr-success"),
 ("IH GuideJar 1100 MRR", "https://www.indiehackers.com/post/no-big-following-no-marketing-genius-how-guidejar-reached-1100-mrr-f90dbd612f"),
 ("r/SideProject GuideJar 1100", "https://www.reddit.com/r/SideProject/comments/1egsyv4/i_grew_guidejar_to_1100_mrr_with_a_good_product/"),
 ("IH Stagetimer 15K niche", "https://www.indiehackers.com/post/tech/turning-a-simple-b2b-solution-into-a-15k-mrr-saas-by-exploiting-a-market-niche-xIxrVwn24DVsN8b3PYD3"),
 ("IH Stagetimer couple 10K", "https://www.indiehackers.com/post/lukas-and-liz-make-10k-a-month-selling-countdown-timers-Nh3Ysb387zBjFbw5Seqa"),
 ("Stagetimer team pricing blog", "https://stagetimer.io/blog/product-update-2-11-team-feature/"),
 ("ScreenshotOne about Dmytro", "https://screenshotone.com/about/"),
 ("TrueStack ScreenshotOne review", "https://thetruestack.com/tools/screenshotone"),
 ("Nusii book-a-demo", "https://nusii.com/demo/"),
 ("Nusii homepage small-team", "https://nusii.com/"),
 ("Kaeda Senja 1M ARR negative-screen", "https://kaeda.co/cases/senja"),
 ("Senja about 2-person", "https://senja.io/about"),
 ("Senja LinkedIn kill-free-tier", "https://www.linkedin.com/posts/olivermeakings_i-want-to-kill-senjas-free-tier-when-we-activity-7300162692747571200-ObFX"),
 ("SiteGPT quickstart email-only", "https://sitegpt.ai/docs/setup/quickstart"),
 ("Famewall about Goutham", "https://famewall.io/about/"),
 ("Supademo homepage negative-screen", "https://supademo.com/"),
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
