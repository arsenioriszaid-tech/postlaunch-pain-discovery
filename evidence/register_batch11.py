#!/usr/bin/env python3
"""Register 100-hunt Batch A stream sources. Run once."""
import subprocess
S = "/root/.hermes/skills/research/grounded-citations/scripts/sources.py"
URLS = [
 ("DashThis Jelly reporting case", "https://dashthis.com/blog/digital-reporting-tool-case-study-jelly-marketing/"),
 ("AgencyAnalytics pricing", "https://agencyanalytics.com/pricing"),
 ("Madgicx reporting manual", "https://madgicx.com/blog/digital-marketing-reports"),
 ("LedgerUp metering docs", "https://www.ledgerup.ai/docs/usage-metering"),
 ("Darkhorse CPA", "https://darkhorse.cpa/"),
 ("Sponsy pricing", "https://getsponsy.com/pricing"),
 ("Shiptell", "https://shiptell.com/"),
 ("Turno contact", "https://turno.com/contact-us/"),
 ("Factuarea versioning", "https://docs.factuarea.com/guides/versioning"),
 ("IH 10 DMs failed Stripe", "https://www.indiehackers.com/post/i-sent-10-cold-dms-about-failed-stripe-payments-heres-what-ac"),
 ("IH wrong churn optimize", "https://www.indiehackers.com/post/most-founders-are-optimizing-the-wrong-churn-eb704d3920"),
 ("r/SaaS tickets vs revenue", "https://www.reddit.com/r/SaaS/comments/1s3dtmd/support_tickets_are_growing_faster_than_revenue/"),
 ("r/SaaS reduce tickets solo", "https://www.reddit.com/r/SaaS/comments/1qobmte/how_do_you_reduce_support_tickets_as_a_solo_saas/"),
 ("r/SaaS onboarding nobody", "https://www.reddit.com/r/SaaS/comments/1ojyjp1/your_onboarding_flow_is_probably_why_nobody"),
 ("r/ecommerce disputes still", "https://www.reddit.com/r/ecommerce/comments/1tnwqxt/is_everyone_still_handling_payment_disputes/"),
 ("r/ecommerce chargeback 3hrs", "https://www.reddit.com/r/ecommerce/comments/1tojja7/had_a_chargeback_last_week_and_spent_over_3_hours/"),
 ("r/smallbusiness late invoices", "https://www.reddit.com/r/smallbusiness/comments/1i5ag3r/late_invoices_are_killing_me"),
 ("r/smallbusiness chasing invoices", "https://www.reddit.com/r/smallbusiness/comments/1rn8imt/tired_of_chasing_invoices_as_a_agency_owner_how"),
 ("r/indie onboarding 5 tools", "https://www.reddit.com/r/indie_startups/comments/1t13hgd/employee_onboarding_automation_across_5_saas_tools/"),
 ("r/PPC reporting manual", "https://www.reddit.com/r/PPC/comments/1myo7la/client_reporting_feels_way_more_manual_than_it"),
 ("r/marketingagency reporting", "https://www.reddit.com/r/marketingagency/comments/1q4r6fu/agency_owners_how_do_you_handle_client_reporting"),
 ("r/Accounting reconciliation", "https://www.reddit.com/r/Accounting/comments/1ivjmhd/how_do_you_handle_invoice_reconciliation"),
 ("HN 41994658", "https://news.ycombinator.com/item?id=41994658"),
 ("HN 37087381", "https://news.ycombinator.com/item?id=37087381"),
 ("HN 10540377", "https://news.ycombinator.com/item?id=10540377"),
 ("Fathom pricing card-trial", "https://usefathom.com/pricing"),
 ("EmailOctopus pricing", "https://emailoctopus.com/pricing"),
 ("Podia pricing", "https://www.podia.com/pricing"),
 ("InvoiceNinja pricing", "https://invoiceninja.com/pricing-plans/"),
 ("Loops pricing SaaS-email", "https://loops.so/pricing"),
 ("Resend pricing", "https://resend.com/pricing"),
 ("Knock pricing", "https://knock.app/pricing"),
 ("Canny pricing", "https://canny.io/pricing"),
 ("Tally Pro help", "https://tally.so/help/tally-pro"),
 ("Dub links pricing", "https://dub.co/pricing/links"),
 ("Churned io tool", "https://www.churned.io/"),
 ("Wingback signup links", "https://www.producthunt.com/products/signup-links-by-wingback"),
 ("GoHighLevel API issue 201", "https://api.github.com/repos/GoHighLevel/highlevel-api-docs/issues/201"),
 ("Frappe helpdesk 2967", "https://api.github.com/repos/frappe/helpdesk/issues/2967"),
 ("Devto kanta freemium-paid", "https://dev.to/kanta13jp1/indie-dev-saas-launch-pricing-strategy-stripe-integration-and-freemium-to-paid-design-257f"),
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
