# Miscellaneous

## /job-search — automated job search + resume tailoring

A Claude Code skill that searches online job boards (LinkedIn, Indeed,
Greenhouse, Lever, Ashby, company career pages) for recently posted jobs
matching your profile, tailors your resume to each matching job description,
and outputs the application link alongside the tailored resume.

### Setup (one time)

1. Put your real resume in [`profile/resume.md`](profile/resume.md).
2. Fill in [`profile/preferences.md`](profile/preferences.md) — target roles,
   locations, recency window, deal-breakers, etc.

### Usage

In a Claude Code session in this repo:

```
/job-search
```

Optionally override preferences for a single run:

```
/job-search senior backend engineer, remote, last 3 days
```

### Output

Each run writes to `applications/<date>/`:

```
applications/2026-07-13/
├── SUMMARY.md                     # table: company, role, application link, resume path
├── acme-senior-backend/
│   ├── resume.md                  # resume tailored to Acme's job description
│   ├── resume.pdf                 # rendered if pandoc is installed
│   └── notes.md                   # why it matched, what was changed, gaps to prep for
└── …
```

### Guarantees

- Tailoring is truthful: bullets are reordered, reworded, and re-emphasized to
  mirror the job description, but nothing is fabricated — every fact comes
  from `profile/resume.md`.
- The skill never submits applications or fills forms; you apply yourself via
  the links in `SUMMARY.md`.

### Recurring runs

Ask Claude to "run /job-search every morning" and it will schedule a recurring
run that dedupes against jobs already delivered in earlier summaries.
