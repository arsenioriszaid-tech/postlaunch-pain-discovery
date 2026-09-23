# Hypothesis Matrix (CYCLE 0 → verdict)

| # | Hypothesis | Verdict | Supporting | Counter | Uncertainty remaining |
|---|------------|---------|------------|---------|----------------------|
| H1 | "No users/no traction" is the most frequent stated pain | SUPPORTED | 15 rows Sec. A [1][2][3][4][5][7]–[16] | — | Exact prevalence % unknown (no denominator; forum-selection bias) |
| H2 | Distribution-channel selection (not ads) is the bottleneck; ads minor | SUPPORTED | P1/P5/P6: channel-choice evidence [12][13][15][21][38]; ads-downstream [41][43][44][36] | Winners sometimes used NO systematic distribution (white-glove [61]) | Which channel-order per segment still unknown |
| H3 | Funnel leaks (traffic→signup, signup→payment) dominate raw-traffic shortage | SUPPORTED | [5][22][47][48][55][56], medians [23][24] | G3: some cases ARE wrong-visitor, not funnel [55] | Causal split traffic-vs-funnel per founder unmeasured |
| H4 | Activation/onboarding drop-off is recurring + time-costly | SUPPORTED | [22][56][60][61][62] | G13: manual onboarding is the learning channel — automating early harms [62] | Generalizable friction taxonomy missing |
| H5 | Churn + conflicting feedback → direction paralysis | SUPPORTED (churn) / MED-UNCERTAIN (paralysis mechanics) | [31][32][33][34][35] | Survey-mistrust is anecdotal (n=1 deep case [32]) | How founders actually adjudicate conflicting feedback — thin evidence |
| H6 | Support/ops burden eats founder time weekly, automatable | SUPPORTED | [26][27][28][29][30][60] | Hiring-before-system fails [29]; early automation kills learning [62] | True hr/day distribution across MRR bands unmeasured |
| H7 | Content/outreach burden high-frequency but tool-saturated | SUPPORTED | F1–F3, [57][58], saturated schedulers/writers | Channel itself decayed [53][54] — "saturated" may understate (channel dead, not crowded) | Whether trust-channels (Reddit/YT/Discord) are systematizable |
| H8 | Paid-ads pain real but narrow, NOT top pain | SUPPORTED | $100–$10k burns [41]–[46]; downstream verdict [36][5] | Novice-noise risk: loudest ads complaints are first-timers [42][44] | Optimization-stage pain (post-PMF advertisers) out of scope — different population |
| H9 (kill) | Most "marketing pains" are upstream product/positioning/onboarding misattributions | SUPPORTED | [5][47][48][22][56][36][37] | Cannot quantify "most" — no base rate | The single most-misattributed pain unranked |
| H10 (kill) | Frequent complaints partly novice noise; experts dismiss some | SUPPORTED (partial) | PH-dismissal by experienced [50][51]; "vibe advice" critique [19]; gut-ICP repeat [21] | Novice pains are still REAL costs to novices (money/time burned regardless) | No experience-stratified data; "noise" label risks dismissing payable pain |

## Program-level shared assumption (from kill stream, batch-2)
All attention-supply candidates (traffic/ads/content/launch agents) assume the binding constraint is distributable attention an agent can incrementally supply — rather than downstream conversion, which the counterevidence locates as the actual bottleneck in nearly every case [47][48][55][76][118][119][122][123]. Single validation whose failure fells them all at once: show target-segment visit→signup AND signup→paid rates already healthy with top-of-funnel as the genuine constraint. No retrieved founder evidence shows that profile; all of it shows the reverse.

## Validation-phase verdicts (2026-09-23, criteria in `cycles/01-validation-design.md`, full report `09-validation-report.md`)
| VH | Verdict |
|---|---|
| VH1 funnel friction | NARROWED to dead-vs-productive (6 support A/Bs 30–413%; Yammer/dmgoi/AtticusLi/Improvely kill "any removal wins"; source-confound controlled) |
| VH2 churn truth | SURVIVES SPLIT: VH2a conditional (SEOJuice 38→22%, Quitlo 28%-vs-4%) / VH2b standalone (25M-sub 22%, Recurly micro-skew, recovery rates; indie-$ trail still the gap) |
| VH3 ops tax | SURVIVES, NARROWED to actions-loop (Fin deflects answers 38%-real, weak at actions, sub-300 uneconomic) |
| VH4 merge | MERGED 9/9 (bar 67%), BOUNDED: holds pre-traction; RenderArchi 7.1% proves post-conversion volume is a separate downstream stage |
| VH5 economics | SURVIVES SCOPED: support-$ proven ($400–10K/mo hires) · funnel-$-wasted ($2.4–2.5K) · churn-$-at-indie UNCONFIRMED |
| VH6 kill-2 | FAILED (for the killers): incumbents own measurement, not the loops |

## Killed / narrowed theses (adversarial-validation outcomes)
- KILL: "AI outreach agent that sends more cold email" — evidence says winners exit the channel; automation accelerates failure (P5).
- KILL: "AI ad-campaign genius for early SaaS" — spend is downstream of offer/funnel; readiness-gate only (P6).
- KILL: "More content volume agent" — volume game decayed per its inventor [53][54]; trust-channel fit unproven (P7).
- NARROW: "Support fully-autonomous agent" → bounded triage/draft/approve loop; early-stage manual learning preserved (P8 + G13).
- NARROW: "Positioning decider" → positioning analyst; commit-decision stays human (P2).
- SURVIVE: funnel-friction audit loop (P3), churn-truth + dunning loop (P4), founder-ops shift-plan (P8) — each names the exact human workflow reduced (CYCLE 6 in `06-opportunities-scored.md`).
