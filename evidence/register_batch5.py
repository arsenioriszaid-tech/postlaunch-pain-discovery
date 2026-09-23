#!/usr/bin/env python3
"""Register V1/V2/V4 full-delivery sources. Run once."""
import subprocess
S = "/root/.hermes/skills/research/grounded-citations/scripts/sources.py"
URLS = [
 ("Intruder 21-step onboarding", "https://iamkeithmason.com/onboarding"),
 ("Speechify Android 3.0-5.3pct", "https://www.trevorbaum.com/speechify"),
 ("Dev Difference 27-step chatbot", "https://www.thedevdifference.com/post/how-our-friendly-chatbot-replaced-a-27-step-form-and-transformed-ai-interviews"),
 ("Fintech one-field 413pct", "https://www.salehbazuhair.com/projects/413-signup-conversion-from-one-field-removed"),
 ("Lokalise 3-to-12.7 aha", "https://www.benshih.design/case-study/onboarding"),
 ("BetterWorld email-gate AB", "https://blog.conversionlab.no/case-study-streamlining-the-path-to-signup-for-better-conversion-rates"),
 ("ConversionLab signup hurting", "https://blog.conversionlab.no/is-your-signup-flow-helping-or-hurting-your-conversions"),
 ("Yammer signup removal backfired", "https://medium.com/yammer-product/testing-yammers-signup-flow-13eeb6435a73"),
 ("dmgoi signup removal lost twice", "https://www.dmgoi.com/blog/removing-signup-input-backfired"),
 ("AtticusLi cognitive-load paradox", "https://atticusli.com/blog/posts/why-shorter-signup-flows-dont-always-convert-better-cognitive-load-paradox/"),
 ("HN Improvely card removal halved", "https://news.ycombinator.com/item?id=6066851"),
 ("HN verification email no-impact", "https://news.ycombinator.com/item?id=23167324"),
 ("Basecamp lost-found millions", "https://signalvnoise.com/posts/3945-how-we-lost-and-found-millions-by-not-ab-testing"),
 ("Kissmetrics conversion benchmarks", "https://kissmetrics.io/blog/conversion-rate-benchmarks"),
 ("Rankcert conversion benchmarks", "https://rankcert.com/blog/conversion-rate-benchmarks"),
 ("Korean IH 15-to-3 fields", "https://dev.to/kunstudio/from-0-mrr-to-first-paying-customer-a-korean-indie-hacker-journal-215p"),
 ("ListenLabs Cognition PR double", "https://listenlabs.com/case-studies/cognition"),
 ("SEOJuice exit-survey skew", "https://seojuice.com/blog/how-bad-exitsurvey-design-skews-your-saas-churn-data/"),
 ("Quitlo 50k cancel truth", "https://www.quitlo.com/blog/why-customers-cancel-saas"),
 ("Churnkey involuntary guide 25M", "https://churnkey.co/guides/reduce-involuntary-churn"),
 ("Recurly churn benchmarks", "https://recurly.com/research/churn-rate-benchmarks/"),
 ("ChurnBuster recovery rate", "https://churnbuster.io/learn/recovery-rate/"),
 ("IH 36K CAC lost 26K cards", "https://www.indiehackers.com/post/spent-36k-to-get-customers-lost-26k-because-their-credit-cards-expired-075d0dc732"),
 ("Ebb reactive churn fails", "https://ebb.nz/blog/reactive-churn-tools-fail"),
 ("V4 Velor 170 emails ICP", "https://www.indiehackers.com/post/170-cold-emails-0-replies-heres-the-icp-mistake-i-made-and-what-finally-worked-5f174f7ee3"),
 ("V4 BrandingStudio 400-to-1", "https://www.indiehackers.com/post/400-signups-from-product-hunt-1-paying-customer-what-4-days-taught-me-about-launch-vs-traction-7c0aacf745"),
 ("V4 Postmint 118-to-0", "https://www.indiehackers.com/post/118-visitors-0-signups-and-the-two-bugs-i-only-found-by-digging-cc665c94e4"),
 ("V4 DP Templates postmortem", "https://www.emanueledipietro.com/blog/first-saas-failure-lessons"),
 ("V4 built-6-SaaS 0 customers", "https://www.reddit.com/r/indiehackers/comments/1rw64vw/built_6_saas_and_got_0_customers_heres_how"),
 ("V4 47 demos zero sales", "https://www.reddit.com/r/SaaS/comments/1op6yll/47_demos_all_went_great_zero_sales_just_realized"),
 ("V4 465 AI calls wrong buyer", "https://www.reddit.com/r/SaaS/comments/1s0s42k/465_ai_cold_calls_0_revenue_heres_what_i_learned"),
 ("V4 100 emails agencies silence", "https://www.reddit.com/r/Entrepreneur/comments/1qbgrq2/sent_100_cold_emails_dozens_of_dms_zero"),
 ("V4 50 emails first users", "https://www.reddit.com/r/SaaS/comments/1udcywf/sent_50_cold_emails_got_0_replies_how_did_you_get"),
 ("V4 snapquo 60 DMs uncodable", "https://www.reddit.com/r/SaaS/comments/1urdmiu/launched_my_first_saas_2_weeks_ago_sent_60_cold"),
 ("V4 RenderArchi volume refutation", "https://www.indiehackers.com/post/from-architect-to-indie-hacker-how-i-built-my-first-saas-with-zero-code-and-hit-7-1-conversion-i7Rnlu1YqvZBTzhRdIEv"),
 ("V4 5-channel 90day outbound", "https://www.reddit.com/r/DigitalMarketing/comments/1oi2e8d/i_tested_5_customer_acquisition_channels_for_90"),
 ("V4 1K MRR playbook merge-confirm", "https://www.indiehackers.com/post/the-exact-playbook-i-used-to-reach-1k-mrr-no-audience-no-ads-tn8xDXbSRelPtzevf3tM"),
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
