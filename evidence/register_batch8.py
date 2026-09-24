#!/usr/bin/env python3
"""Register H3 + top-up stream sources. Run once."""
import subprocess
S = "/root/.hermes/skills/research/grounded-citations/scripts/sources.py"
URLS = [
 ("xFusion SavvyCal support", "https://xfusion.io/case-studies/savvycal/"),
 ("xFusion SavvyCal case2", "https://xfusion.io/case-studies/savvycal-and-xfusion-case-study/"),
 ("Derrick Reimer work team4", "https://www.derrickreimer.com/work"),
 ("TomHunt Plutio AppSumo support", "https://www.tomhunt.io/blog/ep-024---does-appsumo-work-with-leo-bassam-founder-ceo-at-plutio"),
 ("Encharge about Kalo Slav", "https://encharge.io/about"),
 ("IH Rize 11K AMA", "https://www.indiehackers.com/post/hello-ih-i-cofounded-rize-where-we-got-1-on-product-hunt-in-may-and-just-reached-11-000-in-monthly-sales-ama-97f4c8f30e"),
 ("UserJot home", "https://userjot.com/"),
 ("UserJot intro Shayan", "https://userjot.com/blog/introduction"),
 ("Papermark github solo-conflict", "https://github.com/papermark/papermark"),
 ("Userlist press-kit founders", "https://userlist.com/press-kit/"),
 ("Userlist billing retry-flow", "https://userlist.com/docs/getting-started/billing/"),
 ("Userlist Stripe integration", "https://userlist.com/integrations/stripe/"),
 ("Outseta get-started card", "https://www.outseta.com/get-started"),
 ("StarterStory Outseta breakdown", "https://www.starterstory.com/outseta-breakdown"),
 ("First500 Outseta pricing-exp", "https://the-first-500.webflow.io/course-videos/pricing-experiments"),
 ("FeedHive terms card-hold", "https://www.feedhive.com/terms"),
 ("FeedHive pricing Stripe", "https://www.feedhive.com/pricing"),
 ("Buttondown repricing essay", "https://buttondown.com/blog/repricing"),
 ("Buttondown docs Stripe-native", "https://docs.buttondown.com/paid-subscriptions"),
 ("jmduke github founder", "https://github.com/jmduke"),
 ("Latka SignHouse 550K", "https://getlatka.com/companies/usesignhouse.com"),
 ("SignHouse pricing sub", "https://usesignhouse.com/pricing/"),
 ("Outseta five-years founder", "https://www.outseta.com/posts/five-years-a-founder"),
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
