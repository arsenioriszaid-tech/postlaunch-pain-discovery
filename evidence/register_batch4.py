#!/usr/bin/env python3
"""Register V3 + V6 full-delivery sources. Run once."""
import subprocess
S = "/root/.hermes/skills/research/grounded-citations/scripts/sources.py"
URLS = [
 ("HostiFi solo-to-1 burnout hire", "https://medium.com/hostifi/growing-my-saas-from-solo-founder-to-1-employee-bf367061f578"),
 ("HappierLeads tickets-as-retention", "https://happierleads.com/newsletter/i-answer-every-support-ticket-myself-it-s-my-best-retention-tool"),
 ("IH FAQ Hub 15h-wk", "https://www.indiehackers.com/post/i-was-losing-15-hours-a-week-to-repetitive-support-tickets-so-i-built-faq-hub-live-on-ph-today-KgdLmzqn30qoIf33UAin"),
 ("IH Velor answers-vs-actions 40pct", "https://www.indiehackers.com/post/i-built-an-ai-that-answers-support-questions-founders-still-hated-it-heres-what-i-learned-a2c1dd7970"),
 ("IH Fortuna approve-decline residue", "https://www.indiehackers.com/post/i-replaced-an-entire-customer-service-department-with-ai-heres-what-happened-in-the-first-two-weeks-eA7bTzhGgoHS9vggAzlc"),
 ("BaoDev billing mistakes 5-9pct", "https://www.baodev.studio/blog/saas-billing-mistakes"),
 ("Dunsome failed-payments revenue", "https://dunsome.com/blog/how-much-revenue-is-your-saas-losing-to-failed-payments"),
 ("Medium 10K MRR full-time-job 4h", "https://medium.com/@aryanbanswar49/how-i-built-a-saas-app-that-hit-10k-mrr-while-working-full-time-in-6-months-56853655b1dc"),
 ("Ferndesk docs-go-stale", "https://ferndesk.com/help-center-software"),
 ("Ferndesk 2K MRR story", "https://startupfounderstories.com/stories/wilson-wilson-ferndesk-2k-mrr-ai-help-center"),
 ("Applighter docs 70pct residue", "https://applighter.hashnode.dev/how-we-cut-template-support-load-70-with-better-docs"),
 ("Indpro 4200-to-1100 team-12-6", "https://indpro.se/blog/ai-feature-support-tickets-4200-to-1100"),
 ("Intercom Gamma 75pct 20-agents", "https://www.intercom.com/customers/gamma"),
 ("Intercom-on-itself new-roles", "https://www.intercom.com/blog/automate-customer-service-while-improving-customer-experience"),
 ("Intercom small-biz 60-70pct", "https://www.intercom.com/small-business"),
 ("Mihir funnel-why-not", "https://mihirthakkar.in/saas-activation-funnel-decide-what-to-fix-next.html"),
 ("r/SaaS Churnkey 1-save-50dollars", "https://www.reddit.com/r/SaaS/comments/1jb34vt/churn_and_disappointing_experience_with_churn/"),
 ("IH still-answering-themselves", "https://www.indiehackers.com/post/show-ih-i-built-ai-customer-support-for-founders-who-are-still-answering-support-themselves-8eac48fc62"),
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
