#!/usr/bin/env python3
"""Register validation-phase sources (V5 findings + lead spot-checks). Run once."""
import subprocess
S = "/root/.hermes/skills/research/grounded-citations/scripts/sources.py"
URLS = [
 ("r/SaaS 2400 growth consultant wasted", "https://www.reddit.com/r/SaaS/comments/1p918x5/spent_2400_on_a_growth_consultant_heres_what_i/"),
 ("r/Shopify 2500 CRO audit", "https://www.reddit.com/r/Shopify_Guide/comments/1rcjdbj/i_hired_a_cro_consultant_for_2500_his_entire/"),
 ("r/B2BSaaS experimentation 17pct", "https://www.reddit.com/r/B2BSaaS/comments/1n5nfw2/we_spent_on_ads_features_still_flat/"),
 ("r/agency CRO not worth it", "https://www.reddit.com/r/agency/comments/1g3awnp/unpopular_opinion_cro_agencies_are_not_worth_it/"),
 ("IH copywriter 40-100 page", "https://www.indiehackers.com/post/copywriter-looking-for-projects-c533924838"),
 ("IH Quratulain copy services", "https://www.indiehackers.com/post/launching-quratulain-creatives-saas-copy-conversion-services-f7c6f89caf"),
 ("IH unlimited copy 499mo", "https://www.indiehackers.com/post/im-offering-unlimited-saas-copywriting-for-499-month-testing-a-new-service-model-aad9e9e4d9"),
 ("Baremetrics pricing", "https://baremetrics.com/pricing"),
 ("Recoverflow Baremetrics compare", "https://recoverflow.org/compare/baremetrics"),
 ("SubRevival Baremetrics Recover review", "https://subrevival.com/reviews/baremetrics-recover-review"),
 ("Baremetrics SPI 8.3K case", "https://baremetrics.com/customers/how-smart-passive-income-grew-its-private-membership-community-and-recovered-8k-in-failed-payments-with-baremetrics"),
 ("Baremetrics recovery benchmarks", "https://baremetrics.com/blog/subscription-payment-recovery-benchmarks"),
 ("r/SaaS Baremetrics vs ChartMogul", "https://www.reddit.com/r/SaaS/comments/193g44m/what_makes_baremetrics_and_chartmogul_worth_the/"),
 ("Churnkey pricing 250 flat", "https://churnkey.co/pricing"),
 ("Churn Buster pricing guide", "https://subrevival.com/guides/churn-buster-pricing"),
 ("TechCrunch Paddle-ProfitWell 200M", "https://techcrunch.com/2022/05/25/paddle-acquires-profitwell-for-200m-to-bring-analytics-and-retention-tools-to-its-saas-payments-platform"),
 ("Rob Norback 1K support rep", "https://www.robnorback.com/blog/growing-a-micro-saas-business-the-power-of-outsourcing-customer-support"),
 ("tsmeaning AI replaced 2 hires", "https://tsmeaning.com/i-replaced-2-full-time-support-hires-with-ai-agents-heres-the-honest-math/"),
 ("Levelup 10K MRR 47 tickets", "https://levelup.gitconnected.com/i-built-a-saas-and-made-10k-mrr-in-6-months-heres-my-exact-process-a-comedy-of-errors-that-b4180ac083a4"),
 ("Supportson replace Intercom", "https://supportson.com/blog/how-small-saas-teams-replace-intercom-save-money"),
 ("Medium dumped Intercom Crisp", "https://medium.com/@Codename_One/why-we-dumped-intercom-and-moved-to-crisp-and-so-should-you-e991a3b07411"),
 ("r/indianstartups 1cr burn", "https://www.reddit.com/r/indianstartups/comments/1rxw97h/i_burned_close_to_1_crore_on_marketing_and_sales/"),
 ("AtticusLi UX better conv dropped", "https://atticusli.com/blog/posts/we-made-the-ux-better-and-conversion-dropped/"),
 ("IH onboarding fails not UX 50 audits", "https://www.indiehackers.com/post/why-saas-onboarding-fails-and-it-s-not-ux-d37bf23a49"),
 ("thecrit removing onboarding +47", "https://thecrit.co/resources/removing-onboarding-increased-activation"),
 ("OperatorBook rewrite onboarding 10K", "https://www.operatorbook.dev/stories/the-month-i-rewrote-onboarding-at-10k-mrr"),
 ("Pages.report DIY CRO 4h", "https://www.pages.report/blog/how-to-do-a-cro-audit"),
 ("GrowWithBA CRO cost 2-25K", "https://growwithba.com/blog/how-much-does-cro-cost"),
 ("YSG conversion specialist", "https://www.yoursaasgrowth.com/conversion-rate-optimisation-specialist"),
 ("GoGoChimp CRO buyer under-50K", "https://www.gogochimp.com/blog/whitepaper-cro-founders-guide"),
 ("SubRevival Churnkey-vs-Buster", "https://subrevival.com/compare/churnkey-vs-churn-buster"),
 ("Dunlo Buster-vs-Key", "https://dunlo.io/compare/churn-buster-vs-churnkey"),
 ("itechguides Buster-vs-Key", "https://www.itechguides.com/best/dunning-management-software/compare/churn-buster-vs-churnkey/"),
 ("VibeGrowth Churnkey-vs-Buster", "https://vibegrowthstack.io/compare/churnkey-vs-churn-buster"),
 ("SubRevival Churnkey worth-250", "https://subrevival.com/reviews/churnkey-review"),
 ("Builts Fin 500 tickets 38pct", "https://builts.ai/blog/intercom-fin-ai-review/"),
 ("TrustRadius Fin 2-person 90pct", "https://www.trustradius.com/reviews/fin-by-intercom-2026-03-16-08-31-46"),
 ("Metageeks Fin strong-answers weak-actions", "https://www.metageeks.tech/insights/intercom-fin-review"),
 ("Dailytimespro Fin SMB", "https://dailytimespro.com/intercom-fin-review/"),
 ("HelpdeskSmallBiz Intercom", "https://helpdeskforsmallbusiness.com/intercom"),
 ("GGC VA pricing", "https://ggcva.com/pricing"),
 ("HireVA from-6hr", "https://hireva.org/"),
 ("AweVirtual 150wk starter", "https://awevirtual.com/pricing"),
 ("VWO CRO tips SaaS", "https://vwo.com/blog/conversion-rate-optimization-tips-saas-website"),
 ("Rob Palmer landing copy cold", "https://robpalmer.com/blog/saas-landing-page-copy"),
 ("SaaS Backwards Pierri positioning", "https://podcast.austinlawrence.com/why-most-saas-companies-get-positioning-wrong-with-anthony-pierri"),
 ("MRS SEO-for-SaaS conversions", "https://mrs.digital/blog/guide-to-seo-in-the-world-of-saas"),
 ("SaaS Capital retention benchmarks", "https://www.saas-capital.com/wp-content/uploads/2025/09/RB32WS1-2025-B2B-SaaS-Retention-Benchmarks.pdf"),
 ("RetainFlow 6-10pct failed cards", "https://www.retainflow.online/"),
 ("CancelFlow 34pct saved claim", "https://cancelflow.dev/"),
 ("Lago cancel flows 15-25pct", "https://getlago.com/blog/saas-cancellation-flows-reduce-churn-at-the-exit-point"),
 ("Declined.io recovery platform", "https://declined.io/"),
 ("DunningIQ 42recovered 68pct", "https://www.dunningiq.com/"),
 ("DunningStack prelaunch 15pct", "https://dunningstack.com/"),
 ("Kinde dunning strategies", "https://www.kinde.com/learn/billing/churn/dunning-strategies-for-saas-email-flows-and-retry-logic"),
 ("Chargebee dunning 2026", "https://www.chargebee.com/blog/dunning-management-for-saas-business"),
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
