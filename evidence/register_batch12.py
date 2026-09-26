#!/usr/bin/env python3
"""Register hunt full-text sources. Run once."""
import subprocess
S = "/root/.hermes/skills/research/grounded-citations/scripts/sources.py"
URLS = [
 ("r/SaaS tickets-vs-revenue B01", "https://www.reddit.com/r/SaaS/comments/1s3dtmd/support_tickets_are_growing_faster_than_revenue/"),
 ("r/SaaS refund-3hrs B02", "https://www.reddit.com/r/SaaS/comments/1t8778b/biggest_thing_i_underestimated_in_saas_support/"),
 ("r/SaaS onboarding-tickets B03", "https://www.reddit.com/r/SaaS/comments/1s1agak/we_thought_we_needed_more_support_agents_turns/"),
 ("r/ecommerce 3400-chargeback B05", "https://www.reddit.com/r/ecommerce/comments/1qci3a4/just_got_charged_back_3400_in_one_day_and_i/"),
 ("HN encoderer 25pct-dead-cards", "https://news.ycombinator.com/item?id=10540377"),
 ("IH DunnAI 10-DMs", "https://www.indiehackers.com/post/i-sent-10-cold-dms-about-failed-stripe-payments-heres-what-actually-happened-ab926375a3"),
 ("HN FlyCode 103pts", "https://news.ycombinator.com/item?id=41994658"),
 ("GHL issue-201 web", "https://github.com/GoHighLevel/highlevel-api-docs/issues/201"),
 ("Jobber home", "https://www.getjobber.com/"),
 ("HousecallPro HVAC", "https://www.housecallpro.com/industries/hvac-software/"),
 ("Casestudy Jobber scheduling", "https://www.casestudies.com/company/jobber/case-study/better-scheduling-led-to-this-hvac-business-highest-year-on-record"),
 ("Casestudy Jobber 15M", "https://www.casestudies.com/company/jobber/case-study/growing-a-15-million-hvac-business-with-jobber"),
 ("Casestudy Jobber callbacks", "https://www.casestudies.com/company/jobber/case-study/how-this-plumber-reduced-costs-by-over-50-with-jobber"),
 ("Dentrix engage suite", "https://www.dentrix.com/dental-solutions/marketing-and-patient-experience/dentrix-patient-engage-suite/"),
 ("Valian noshow guide", "https://valiansystems.com/blog/how-to-reduce-patient-no-shows"),
 ("Breezeway automation", "https://www.breezeway.io/task-automation"),
 ("Spotless turnover guide", "https://www.spotlessapp.io/blog/airbnb-turnover-cleaning-guide"),
 ("Ignition Karbon integration", "https://www.ignitionapp.com/news/ignition-and-karbon-launch-new-integration-to-unify-billing-and-workflow-automation"),
 ("EzFileDrop onboarding week-month", "https://www.ezfiledrop.com/articles/bookkeeping-client-onboarding-checklist"),
 ("LegalClarity LemonSqueezy MOR", "https://legalclarity.org/how-lemon-squeezy-handles-sales-tax-as-merchant-of-record/"),
 ("UncleKam splits ledger", "https://unclekam.com/tax-strategy-blog/contractor-online-course-development-2026-tax-guide"),
 ("Canny about team", "https://canny.io/about"),
 ("InvoiceNinja about", "https://invoiceninja.com/about/"),
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
