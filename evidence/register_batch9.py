#!/usr/bin/env python3
"""Register radar Day-1 discovery sources. Run once."""
import subprocess
S = "/root/.hermes/skills/research/grounded-citations/scripts/sources.py"
URLS = [
 ("IH save-on-cancel ladder", "https://www.indiehackers.com/post/the-save-on-cancel-ladder-we-use-pause-discount-downgrade-6bbbb15f7c"),
 ("Churnkey Wavve cancel flows", "https://churnkey.co/blog/how-wavve-cut-churn-by-2-over-two-months-with-better-cancellation-flows"),
 ("Baremetrics benchmarks help", "https://help.baremetrics.com/en/articles/5379918-benchmarks"),
 ("Keygen 14day trial cut", "https://keygen.sh/blog/your-14-day-free-trial-aint-gonna-cut-it/"),
 ("Redo Stripe chargeback fees", "https://redo.com/resources/articles/chargebacks/stripe-chargeback-fees"),
 ("Airbyte automating disputes", "https://airbyte.com/blog/automating-stripe-disputes"),
 ("CancelPause micro tool", "https://www.cancelpause.com/"),
 ("CancelGuard micro tool", "https://www.getcancelguard.com/"),
 ("Unchurn micro tool", "https://unchurn.dev/"),
 ("TryRetainly micro tool", "https://tryretainly.com/"),
 ("Triggla trial rescue email", "https://triggla.com/blog/trial-expiration-email-how-to-rescue-trials-before-they-churn."),
 ("Vevee outreach drafts", "https://www.vevee.org/blog/founder-outreach-drafts-not-autosends"),
 ("Vevee trial-end usage email", "https://www.vevee.org/blog/trial-end-email-written-from-usage"),
 ("Gmass solopreneur case", "https://growthhacksuite.com/gmass-solopreneur-case-study"),
 ("IH yoaso profile", "https://www.indiehackers.com/yoaso"),
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
