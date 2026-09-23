# Validation Report (autonomous desk-validation phase, 2026-09-23)

Starting corpus: ledger [1]–[145]. This phase added 56 sources → ledger [146]–[201]. Design + falsification criteria: `cycles/01-validation-design.md`. Ranked but NON-PRESCRIPTIVE — no build decision; Section 5 names experiments, not products.

## 1. Per-hypothesis verdicts

### VH1 — Pre-value funnel friction: NARROWED to dead-vs-productive friction (V1 full verdict)
- Support (6 NEW before/after cases, banned-story angles excluded, composites rejected): Intruder 21-step removal → −78% time-to-activate, +30% activation, +33% MRR [220, A] · Speechify forced-auth post-value → 3.0%→5.3% (+76%) [221, A] · 27-step form → conversational → 37.9%→50.0% complete [222, A] · one verification field moved later → 1.6%→8.2% (+413%) [223, B] · Lokalise redesign → signup→aha 3%→12.7%, trial-to-customer +200% [224, B] · email-gate removal A/B → 5.1%→10.2% (+99.5%) [225, B]. Kill bar (<4) NOT met.
- Kill stream (4 counter-cases, all admitted): Yammer −2 steps → retention fell "pretty significantly", steps kept [227, A] · dmgoi frictionless hero → more taps, fewer signups, "lost twice" [228, B] · AtticusLi: 3-of-4 brands negative lift from simplification; modal-vs-page −double-digits [229 + 168, B] · Improvely: dropping card requirement 2x trials but halved trial→paid + more support → restored [230, B]; verification-email removal "no meaningful impact" [231, C].
- Traffic-source confound is REAL and must be controlled (Basecamp 1.06%→0.89% on mix shift [232, A]; branded 8–12% vs cold-social 0.5–1% identical pages [233][234]) — but does NOT explain away within-source A/B lifts.
- Narrowed thesis (V1): "Pre-value asks that feed neither personalization nor qualification suppress activation 20–80%; removing THEM lifts step and paid conversion within source segments. Productive friction (commitment, personalization seed, qualification, downstream-retention steps) is neutral-to-harmful to remove." The broad "any friction removal wins" is KILLED.
- Falsifying experiment (V1-designed, supersedes earlier): live SaaS ≥1,000 signups/variant, pre-registered A/B removing ONE pre-value ask, source-segmented, trial→paid primary over full window. Falsified if activation lifts but paid flat/down, or lift vanishes within segments. Cost ~2–4 wks eng + one trial cycle.

### VH2 — Churn-truth gap: SURVIVES, SPLIT into VH2a (conditional) + VH2b (standalone) — V2 full verdict, kill triggers unfired
- Stated≠actual (new): SEOJuice ~340 churned subs — "too expensive" 38%→22% after usage-pairing + reword; "never got started" → ~1/3; 41% of price-clicks never ran one audit [237, B] · Quitlo 50k AI exit conversations: stated 28% price vs 4% genuine; truth = 38% never activated, 22% team-adoption failure, 17% billing confusion [238, C-vendor] · CurseCut case-level divergence (56 clean tasks vs "long files") [32, B].
- Involuntary/micro (new): Churnkey/Stripe 25M+ subs — 22% of all churn involuntary; 35% under-$10 price point [239, B+] · Recurly network — 33% share (1.06 of 3.22%/yr); $10–25 ARPC 1.30% vs $250+ 0.18% = micro skew CONFIRMED [240, A-] · Baremetrics Dec-2024: 148 customers reclaimed $1.35M/mo, median 410% ROI; May-2026: 119 B2B SaaS $1.24M, 95% self-funding month one; ChurnBuster avg 50.3% (top 94.5%); Churnkey 70% of detected involuntary recovered 2024 [157][241][239, C→B vendor] · indie anecdote: 11/40 churns (27.5%) involuntary ≈ $26K/yr, founder "could quote CAC, not recovery rate" [242, C].
- Kill-seek results: "involuntary small at micro" NOT FOUND — direction runs opposite (micro shares highest; only enterprise/high-ARPC small, out of scope). Exit-program failures found (Ebb: reactive tools fail <$1M ARR without owner [243]; GrowSurf CSM/webinars failed, segmentation won [84]; "churn score without owner useless") — these NARROW VH2a to owner+triangulation condition, don't kill.
- Surviving split: (a) stated reasons mislead unless triangulated (price = polite excuse for failed activation in ~40–90% of price clicks); (b) involuntary = 20–35% of micro churn / ~9% MRR at risk, dunning lifts recovery ~25–40pts (micro table: 25–35% no-dunning → 55–70% with [35]).
- Falsifying experiment (V2-designed, supersedes earlier): 30 consecutive cancels at <$10K MRR Stripe SaaS — freeze stated reason, pull 30-day usage + support + payment-failure flag. Killed if ≥50% of "price" cites come from high-usage/activated/payment-healthy accounts AND 30-day dunning recovers <10% of failed-payment MRR.

### VH3 — Founder support/ops tax (P8/O3): SURVIVES (V3 full verdict: kill 0/3 on both legs)
- V3 kill hunt FAILED both legs: 0 cases of sustained-~zero after one-time fix (best cuts leave residue: Applighter docs −70% but humans still reply to every ticket [212]; LujanDev 40→8/mo with 35min/mo residue [97]; Indpro 4,200→1,100/mo, team 12→6 not zero [213]); 0 cases of Fin-class FULL absorption (Gamma: 75% resolved but 20 agents + BPO retained [214]; Intercom-on-itself: 81% resolved yet created new AI-support roles [215]; ceiling 50–80% everywhere, never 100%).
- New recurrence mechanisms: Velor answers-vs-actions — docs-grounded answers did NOT kill load ("still got a ticket… can you just add me manually"); closed-loop +~40% only after ACTIONS (plan changes, refunds w/ audit log); remainder = judgment calls [205]. Fortuna: every refund held for human approve (~3s vs 15min) — compressed, not eliminated [206]. Ferndesk: docs stale "right from day 1" / after every release — maintenance is permanent owner-cost [210][211].
- New magnitude rows: HostiFi $100k ARR — support took "days, nights, weekends" → first hire absorbed 80%+ [202]. FAQ Hub: 15h/wk tier-1 theft [204]. HappierLeads: 4 yrs in, still 100% tickets himself, AI-drafts + human sends, <40min replies [203]. $10k-MRR solo + full-time job: 4h/wk support, planned $800/mo VA for ~15h/mo [209].
- Billing-ops economics: 5–9% recurring charges fail first attempt; good dunning recovers 40–70%; ~$128 all-in per chargeback (~$82 internal); founder recouped ~$1,900/mo on ~$42k base via retries alone [207][208].
- So the survivor is the ACTIONS + JUDGMENT residue loop (billing, entitlements, refunds, onboarding ops, docs maintenance), not generic "support chat." RECURRING (daily), ECONOMIC (hires + bills + recoveries). One-time fixes reliably cut volume 60–80% and reliably fail to finish the job.
- Falsifying experiment (V3-designed): 15–20 solo/small SaaS ($2k–30k MRR) log founder min/day 30 days; ship one-time fix only (docs rewrite + grounded chatbot, frozen); 90-day founder-minutes + same-issue reopen per-1k-users — dies if median <10min/day with no new categories despite shipping/growth.

### VH4 — Merge test: MERGED 9/9 with a genuine boundary (V4 full verdict + case file)
- Sample: 10 NEW cases, zero corpus overlap (4 IH fetched-A, 1 blog-A, 5 Reddit-B/C; snapquo honestly excluded uncodable → 9/9 codable = 100%, 9/10 = 90%, bar 67%). Full table: `evidence/stream-V4-mergetest.md`.
- Strongest causal exhibits: Velor same-copy ICP-shift → replies + trial [244] · 47 demos → $0 wrong problem [249] · BrandingStudio 98% activation → 0.25% pay ("curious, not buying") [245] · Postmint 1.7% reach register, output-not-product landing [246] · DP Templates saturated/no-differentiator [247] · 465 AI calls 1 owner-convo, wrong buyer [250].
- GENUINE REFUTATION FOUND (bounds the merge): RenderArchi — 2.5K users, 7.1% reg→paid, architects paying; traffic "the final boss" [254, A]. Unlimited traffic WOULD convert here. Partial second: 5-channel 90-day test — cold email 5,000→180→12→3 customers (CAC $166, "WINNER — will scale") when ICP/offer right [255, B]: channel isn't dead, mistargeted offer is.
- Merge-confirming sequence: $1K-MRR playbook — "stopped all marketing… rebuilt onboarding/positioning" THEN "stack outreach once funnel healthy… converting and staying" [256, A].
- Final form: merge holds PRE-traction (offer-without-urgency × blurry ICP × unconverting funnel; volume knobs multiply ~zero). Post-conversion volume ("scale proven funnel") is a SEPARATE downstream stage per D1 — the bounty is closed, converted into a staged model. Corroborated independently: 50-audit PMF-timing pattern [169]; Hormozi unlimited-traffic test [5]; Marc Lou 95%/4x [118].

### VH5 — Economic commitment: SURVIVES, SCOPED (not uniform)
- V5 full findings (`evidence/v5-economic-commitment-findings.md` + ledger rows): strongest trail SUPPORT/OPS (four hires $400–$10K/mo + ~$5K/yr Intercom bills + regret-switches); middle FUNNEL ($2.4K consultant wasted-A, $2.5K audit wasted-ish; budget exists, satisfaction doesn't); NONE independent for CHURN/DUNNING (vendor-only: SPI $8.3K, Grokability $150K, 119-cohort $1.24M/mo, price lists $58–250/mo).
- Lead adds: CRO audit $2–5K / retainers $3–7K with "under £50K/mo don't buy" floor [173][175]; VA $6/hr → $200–320/wk + mgmt [186][187]; Intercom 5x-hike churn-to-Crisp.
- No-WTP kill does NOT trigger (support clears it alone). Churn-WTP at indie scale: UNCONFIRMED (scope flag, needs experiment not more desk).

### VH6 — Kill-2 (incumbents already solve O1–O3): KILL-2 FAILED on all three (V6 full verdicts)
- (1) Funnel audit: 0 founders saying PostHog/Mixpanel + Hotjar fully diagnosed AND fixed conversion. Only consultant-sells-audit posts (pain persists; tools don't auto-fix). Residual, grade A (Retentionly founder Mihir Thakkar): "The funnel did not prove why merchants stopped. Analytics rarely does." — WHERE without WHY [217].
- (2) Micro-dunning: only 1 generic positive + incentivizable Trustpilot + vendor testimonials (excluded) — far short of 3. Residual, grade A (r/SaaS founder trial): Churnkey "utterly dismal… 5% of cancellations saved — 1 cancellation… $300/mo minimum irrespective of what they save ($50 total)" [218]; second founder: survey "20% response rate, generic answers, 30+ min/customer to piece together their story" [V6 report].
- Residual (Metageeks): "most tickets end in a system change rather than an explanation → Fin's ceiling structurally low" [183]; founders "still answering themselves" 2–3h/day [219][205].
- Ruling: incumbents own MEASUREMENT and partial ANSWERING; the loops (diagnose→fix→verify; truth→recover; triage→act→maintain) remain unowned at micro scale. V6 killed nothing.

## 2. Recurring-problem vs generic-frustration audit
| Pain | Recurring mechanism observed | Frustration-only residue | Ruling |
|---|---|---|---|
| Funnel friction | Pre-value asks + silent onboarding + empty states, every cohort | "My copy sucks" generality | RECURRING (mechanism-specific) |
| Churn truth | Survey-lies + habit fade + failed payments, monthly | "Churn is high" generality | RECURRING (two legs) |
| Ops tax | Same-5-questions + billing actions + fragmentation, daily | "Support is hard" generality | RECURRING (actions-leg) |
| Silence/positioning/outreach | Always co-present with funnel/offer defect (9/9) | Loudest complaints, least separable | MERGED upstream |
| Ads pain | Burns recur but always downstream of offer/funnel | Loudest dollar stories | SYMPTOM, not pain |

## 3. Stated / behavioral / economic separation (where it matters)
- VH1: stated (flat signups) → behavioral (before/after deltas, 6+ independent) → economic (CRO $2–5K tickets, wasted). Strongest chain in corpus.
- VH2b: stated (silent cancels) → behavioral (usage-vs-survey splits) → economic (vendor-only at indie scale; 15–25% save-rate benchmarks). Chain breaks at indie-$ — hence experiment.
- VH3-actions: stated (drowning) → behavioral (15min/ticket, 61%-FAQ, 4-day-cancel) → economic (hires $400–10K/mo, tool bills). Strongest $ chain.
- VH5 verdict: money moves for relief (support) and diagnosis (funnel, wastefully); nobody observed paying for churn-truth at indie scale.

## 4. Unresolved uncertainties (desk cannot close)
1. Prevalence denominators + hr/day distributions across MRR bands (no survey data found).
2. All six validation streams fully delivered and integrated — no pending verdicts. Diminishing-returns stop: V1/V2/V4 added new cases but no new MECHANISMS beyond dead/productive friction, stated-vs-usage split, and upstream collapse; further desk work is not recommended.
3. VH2a ROI conditional on "owner + triangulation" — organizational, needs field test.
4. RenderArchi-class post-conversion volume economics (CAC $166 outbound at small B2B — replication scope unknown; one case + one test).
5. Fin-at-micro trajectory (vendor improving; today's gap may narrow — time-box any conclusion to ~6 mo).

## 5. Recommended paid/manual experiments (1–3, no interviews, human-founder-run)
1. **Funnel-friction audit ×2** (~$0–500 tooling + founder time): instrument → name ONE causal pre-value step → remove → pre-registered conversion target. Kills VH1 if both flat. [Strongest evidence/cost ratio.]
2. **Micro-dunning concierge, 60 days** (~$0 + time vs $250/mo Churnkey quote): card-updater + smart retry + 3-email sequence on one micro-SaaS; recovered-MRR ledger. Kills VH2b if recovery < cost; simultaneously manufactures the missing indie-$ trail.
3. **Inbox residue protocol, 30+90 days** (~$0, V3-designed): 15–20 solo/small SaaS ($2–30k MRR) log founder min/day 30 days; ship one-time fix only, frozen; track 90-day founder-minutes + reopen rate per-1k-users. Kills VH3-residual if median <10min/day with no new categories. (Lower priority — do 1+2 first.)

## 6. Final separation
- **VERIFIED / STRONGLY SUPPORTED:** VH1-narrowed (diagnosis-first friction audit) · VH2b (micro involuntary recovery gap) · VH3-narrowed (ops actions-loop) · VH4-merge (upstream collapse) · VH5-scoped (support-$ proven; funnel-$-wasted) · VH6 (incumbents don't own the loops).
- **PLAUSIBLE BUT UNVERIFIED:** VH2a standalone exit-interview ROI · churn-WTP at indie scale · prevalence/hr-day distributions · V3/V4-detail-dependent nuances (pending deliveries) · Fin-gap durability beyond ~6 mo.
- **KILLED (reaffirmed):** outreach-volume automation · standalone ads-genius · content-volume generation · traffic-first ordering · "incumbents solved it" · P1/P2/P5 as independent pains (merged).
