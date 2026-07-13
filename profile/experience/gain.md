# Gain — full experience corpus (Software Engineer, May 2023 – Present)

Detailed record of work at Gain. The /job-search skill may draw on any fact
here when tailoring the resume — this corpus is richer than the resume bullets
and every item in it is true. Ticket IDs are internal references; do not put
them on tailored resumes.

## Achievements

### Data Integration platform (2023 → present)

- Owned the ATI → Redshift → Salesforce ingestion pipeline end-to-end across
  120 tickets and three years — the core of Gain's data flow for claims,
  billings, fundings, transactions, legal personnel, and notes.
- Shipped major new ingestion domains: Legal Personnel (DI-156, DI-170/171,
  DI-293), Patient Notes/Comments RS↔SF (DI-426, DI-439), ATI Tail Claim
  (DI-251, DI-258, DI-597), Notes files in DI pipeline (DI-277), Litigation
  Update files (DI-175).
- Introduced External ID Containers / multi-key support (DI-199, DI-349,
  DI-360) — a foundational change that unblocked complex entity matching
  across opportunities and contacts.
- Built the ATI Reconciliation script with timing-aware discrepancy filtering
  (DI-556, DI-471, DI-506, DI-509) — now a standing tool for spotting drift
  between systems.
- Stood up background task processing with Django-Q (DI-544, DI-569) and
  automated DB migrations in Docker deploys (DI-542) — both meaningful
  production-readiness upgrades.
- Drove platform migrations: F drive → cloud (DI-465), JSON credentials → env
  vars (DI-623), EC2 recon → Postgres (DI-503), and a credentials-management
  overhaul.
- Refactor wins: separated File ingestion from Claim ingestion (DI-303),
  reformatted ingestion automation code (DI-278), refactored RS→SF fundings
  (DI-409), and made arms execute sequentially based on completion (DI-517) —
  reducing race-condition bugs.

### Reporting & audit

- Sole owner of the Gain Audit Report tool (RA project, 8 tickets across 2.5
  years) — repeatedly extended scope, recipients, columns, and case-type
  filters as the business evolved.

### AI / new platform initiatives (2026)

- Architected and shipped the DRS (Document Retrieval / case-context AI)
  initiative — DB model & API endpoints (PA-100), classification & analysis
  core service (PA-101), placement file search tool (PA-118), browser access &
  web crawling module (PA-84), and bar website lookup tool (PA-92).
- Built AI suggestions for Cases (PA-128) and AI summarization of notes
  (SFDC-4005).
- Led the RM Portal POC — service console, AI suggestions, role-based views
  (TECH-260 / GS-3224).

### Documentation & QA

- Wrote Confluence documentation for the closed billing / funding business
  process (DI-553).
- Built a QA / testing framework for DI Integration (DI-209).

## Responsibilities

- Primary engineer for the Data Integration platform: production reliability,
  schema evolution, new feature work, bug fixes, and on-call investigations.
- Data quality custodian: a consistent thread of bug fixes addressing
  duplicates (DI-489, DI-615), out-of-sync withdrawals (DI-464, DI-467),
  missing data (DI-346, DI-398, DI-441, DI-476), batch-size SQL malformations
  (DI-559), and timestamp/ordering correctness (DI-578, DI-579, DI-599).
- Production firefighter: pipeline failure investigations (DI-463, DI-654,
  TECH-695), backlog cleanups (DI-620, DI-440, DI-438, DI-524), and one-time
  data realignments (DI-528).
- Cross-system integrator: Salesforce bulk API, Apex triggers (SFDC-2805),
  SFTP scripts, Redshift, Postgres, and Django.
- Reconciliation & audit owner: both the ATI reconciliation script and the
  Gain Audit Report.
- Increasingly: AI tooling lead. From early 2026 the work shifts heavily
  toward agentic / LLM-backed case-management tooling (PA + TECH + SFDC AI
  tickets).

## Technical breadth

- Languages & frameworks: Python (Django, pandas, Django-Q), SQL (Postgres,
  Redshift), Salesforce (Apex triggers, bulk API), Docker, SFTP, EC2.
- Patterns: ETL/ELT with composable "arms" run sequentially, idempotent
  upserts, manual-review workflows for ambiguous matches, batch processing
  with error containment, external-id-based entity matching.
- Domain: healthcare claims & litigation-funding operations — placements,
  fundings, transactions, withdrawals, settlements, tail claims, legal
  personnel, audit reporting.
- Recent expansion: RAG/agentic AI for case summarization, document
  classification, placement file keyword search, web crawling, and role-based
  service-console UX.

## Arc of the work

2023–2024 was about building out the integration pipeline (new ingestion
types, schema evolution); 2025 was hardening and migrating (Django-Q,
Postgres, Docker, reconciliation, refactors); 2026 is extending into
AI-driven tooling on top of the integration platform.
