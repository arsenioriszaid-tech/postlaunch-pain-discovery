#!/usr/bin/env python3
"""Register radar evidence-pack sources. Run once."""
import subprocess
S = "/root/.hermes/skills/research/grounded-citations/scripts/sources.py"
URLS = [
 ("Churnkey Wavve 2pct saves", "https://churnkey.co/blog/how-wavve-cut-churn-by-2-over-two-months-with-better-cancellation-flows"),
 ("Chargebee cancel Powtoon", "https://www.chargebee.com/blog/cancellation-flow/"),
 ("IH dashboard 2K retained", "https://www.indiehackers.com/post/my-dashboard-flags-whos-cancelling-before-they-do-stopped-2k-mrr-from-leaving-this-month-23b372b3d5"),
 ("ProfitPath save benchmarks", "https://profitpathlogic.com/saas-cancellation-save-rate-benchmark/"),
 ("MicroSaaSInsider cancel solo", "https://microsaasinsider.com/saas-cancellation-flow-solo-founder"),
 ("Keygen trial extension success", "https://keygen.sh/blog/your-14-day-free-trial-aint-gonna-cut-it/"),
 ("Devto Mixpanel 11users 539", "https://dev.to/vhub_systems_ed5641f65d59/312-trial-starts-this-month-24-converted-i-manually-dug-through-mixpanel-and-found-11-21k4"),
 ("Busnurd trial 12-to-29", "https://busnurd.com/case-studies/saas-email-marketing-conversion/"),
 ("Reddit trial rewrite 12-38", "https://www.reddit.com/r/SideProject/comments/1o6w3xx/stop_sending_your_trial_is_ending_emails_theyre.json"),
 ("Devto 3emails die 12-22", "https://dev.to/speedy_devv/i-shipped-a-saas-mvp-with-three-emails-then-i-watched-it-die-3dej"),
 ("Sequenzy win-back trials", "https://www.sequenzy.com/blog/win-back-expired-trial-users"),
 ("Sequenzy trial-paid sequences", "https://www.sequenzy.com/blog/saas-trial-to-paid-email-sequences"),
 ("ChurnTools trial expiry", "https://churntools.com/blog/how-to-reduce-trial-expiry-abandonment"),
 ("Redo loss free-representment", "https://redo.com/resources/articles/chargebacks/what-happens-if-you-lose-a-chargeback"),
 ("BeastInsights triage 50-75", "https://beastinsights.com/blog/chargeback-representment"),
 ("IH first dispute 0.0078pct", "https://www.indiehackers.com/post/first-dispute-in-stripe-ebf9a690f8"),
 ("IH NotebookBloom cancel-btn", "https://www.indiehackers.com/post/i-spent-a-day-building-the-button-that-lets-people-cancel-and-leave-me-7d9487b76b"),
 ("Fincoro chargeback miss", "https://www.fincoro.com/insights/stripe-chargeback-what-merchants-miss"),
 ("Stripe chargeback reports", "https://stripe.com/resources/more/chargeback-reports"),
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
