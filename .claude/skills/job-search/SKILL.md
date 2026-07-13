---
name: job-search
description: Search online job boards (LinkedIn, Indeed, Greenhouse, Lever, etc.) for recently posted jobs matching the user's profile, tailor their resume to each matching job description, and deliver application links plus tailored resumes. Use when the user asks to find jobs, run a job search, or tailor their resume to openings.
argument-hint: "[optional: role/location/keywords override, e.g. 'senior backend, remote, last 3 days']"
---

# Job Search & Resume Tailor

Find recently posted jobs that match the user's profile, tailor their resume to
each job's description, and produce a summary linking every application page to
its tailored resume.

## Step 0 — Load the profile

Read these files from the repository root:

- `profile/resume.md` — the user's master resume (source of truth for all facts)
- `profile/preferences.md` — target roles, locations, seniority, salary floor,
  keywords, deal-breakers, and recency window
- `profile/experience/*.md` — extended experience corpus (e.g. `gain.md`), a
  richer record of real work than fits on the resume. Facts from here may be
  promoted into a tailored resume when a job description calls for them, but
  internal ticket IDs must never appear on a resume.

If either file is missing or still contains `<!-- TODO -->` placeholders, STOP
and ask the user to fill them in before searching. Do not invent a profile.

If the user passed arguments to the skill (e.g. `/job-search staff SRE, NYC,
last 2 days`), those override the corresponding fields in `preferences.md` for
this run only.

## Step 1 — Search job boards

Use `WebSearch` (and `WebFetch` for board search pages) to find postings that
match the profile. Run multiple targeted queries rather than one broad one:

- `site:linkedin.com/jobs "<role>" <location/remote>`
- `site:indeed.com "<role>" <location/remote>`
- `site:boards.greenhouse.io "<role>"`
- `site:jobs.lever.co "<role>"`
- `site:jobs.ashbyhq.com "<role>"`
- General query: `"<role>" job posting <location> <top 2-3 skills>`

Recency: restrict to the window in `preferences.md` (default: last 7 days).
Prefer search operators / board filters for recency (e.g. Indeed `&fromage=7`,
LinkedIn `&f_TPR=r604800` for 7 days); otherwise check the posting date on the
page and discard anything older than the window.

Practical notes:

- LinkedIn and Indeed frequently block automated page fetches. If `WebFetch`
  on a posting fails or returns a login wall, (a) use the search-result
  snippet, (b) look for the same posting on the company's own careers page or
  its ATS (Greenhouse/Lever/Ashby/Workday), which is fetchable and is also the
  better application link to give the user.
- Collect 10–20 candidates, then score each against the profile (skills
  overlap, seniority, location, deal-breakers). Keep the top 3–7. Never keep a
  job that violates a deal-breaker in `preferences.md`.

## Step 2 — Fetch each job description

For each kept job, `WebFetch` the posting and extract: company, role title,
location/remote policy, posted date, application URL (prefer the direct ATS
"apply" URL over an aggregator link), required skills, preferred skills, and
notable responsibilities. If the full JD is unreachable, work from the snippet
and clearly mark the entry as "JD partially unavailable" in the summary.

## Step 3 — Tailor the resume (one per job)

Starting from `profile/resume.md`, produce a tailored resume for each job.

Hard rules — the resume must stay truthful:

- NEVER invent employers, titles, dates, degrees, certifications, metrics, or
  skills that are not in the master resume or the `profile/experience/`
  corpus. Tailoring means re-emphasis, not fabrication.
- Allowed: reordering bullets and sections, rewording bullets to mirror the
  JD's terminology (only where the underlying fact supports it), expanding a
  relevant bullet, promoting a corpus fact into a bullet, trimming or dropping
  irrelevant ones, rewriting the summary line for the target role, and
  reordering the skills list so JD-matching skills come first.
- Gap rule: when a JD wants a skill/technology that would strengthen the
  resume but appears NOWHERE in the master resume or experience corpus, do
  NOT add it. Instead record it in that job's `notes.md` under "Gaps", and in
  the final chat message ask the user, grouped per job ("For <Company> —
  <Role>: ..."): (a) "Have you ever worked with <X>?" and (b) "If yes, give
  me one bullet point of relevant experience backing it (what you did, where,
  with what outcome)." A skill may be added to the skills list only after the
  user confirms it, and a resume bullet may be written for it only from the
  user's own backing bullet — never drafted from nothing. Ask about every gap
  that would materially improve that job's resume, deduplicating repeated
  skills across jobs. Check `profile/experience/confirmed-skills.md` first:
  never re-ask about a skill already confirmed there, and never ask about (or
  add) one listed as explicitly not confirmed / removed.
- When the user confirms a skill and provides its backing bullet, record both
  in `profile/experience/confirmed-skills.md` (and promote to
  `profile/resume.md` if broadly applicable) so future runs use them without
  asking again.
- Keep it ATS-friendly: plain headings, no tables/columns/graphics, standard
  section names (Summary, Experience, Skills, Education), and include the
  JD's exact keyword spellings where truthful (e.g. "PostgreSQL" if the JD
  says PostgreSQL and the master resume says "Postgres").
- Keep to the same length as the master resume or shorter.

## Step 4 — Write the output

Create a run directory: `applications/<YYYY-MM-DD>/` (today's date). Inside:

- `<company>-<role-slug>/resume.md` — the tailored resume
- `<company>-<role-slug>/notes.md` — 3–5 bullets: why this job matched, what
  was emphasized/changed vs. the master resume, and any gaps the user should
  be ready to address
- `SUMMARY.md` — a table with one row per job: Company | Role | Location |
  Posted | Match highlights | **Application link** | Path to tailored resume

If `pandoc` is available (`command -v pandoc`), also render each resume to PDF
next to its markdown (`resume.pdf`). If not, skip PDFs silently — do not
install anything.

## Step 5 — Deliver

- Send `SUMMARY.md` (and the tailored resume files) to the user with
  `SendUserFile` if available.
- End with a short recap in chat: how many jobs were found vs. kept, and the
  top pick with its application link.
- Do NOT submit any application, create accounts, or fill any forms — the
  user applies themselves via the links.

## Recurring runs (optional)

If the user asks for this to run automatically (e.g. "every morning"), set up
a schedule with the available scheduling tool (CronCreate or a Routine via
create_trigger) whose prompt is simply `/job-search`, and dedupe against links
already present in previous `applications/*/SUMMARY.md` files so the same
posting is never delivered twice.
