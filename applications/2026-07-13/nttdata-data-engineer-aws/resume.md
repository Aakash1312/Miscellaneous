# AAKASH PRALIYA

Data Engineering · Salesforce–S3–Redshift Pipelines, Data Quality & Reconciliation

Atlanta, GA | +1-470-815-4242 | aakashpraliya13@gmail.com | linkedin.com/in/aakash-praliya-0940b9128

## Summary

Data engineer with 5+ years building and operating production ETL/ELT pipelines between Salesforce, AWS (S3, Redshift), and PostgreSQL. Sole owner for 3 years of a healthcare claims platform's ingestion pipeline — extraction from external sources and Salesforce (Bulk API), transformation, idempotent loads into Redshift and Salesforce, with reconciliation, data-quality monitoring, and audit reporting built in. Led a legacy file-share → cloud storage migration. Production-grade Python and SQL. US permanent resident.

## Experience

### Software Engineer · Gain (healthcare litigation-funding startup) — May 2023 – Present

Data integration platform for healthcare claims, billings, and fundings

- Owned the end-to-end ingestion pipeline unifying external claims files, Amazon Redshift, and Salesforce — bidirectional Redshift ↔ Salesforce flows for claims, billings, fundings, transactions, legal personnel, and notes, running in production for 3 years
- Built extraction from Salesforce (Bulk API, Apex Triggers), SFTP feeds, and third-party APIs, with scheduled batch processing, error containment, and automated recovery paths
- Implemented idempotent, incremental load patterns: external-ID multi-key entity matching, upserts safe to re-run, and sequential pipeline-arm execution that eliminated race-condition bugs
- Built data-quality and reconciliation tooling: a timing-aware cross-system reconciliation script for spotting drift between systems, plus audit reporting maintained for 2.5 years — fixing duplicates, missing data, and ordering/timestamp correctness at the root
- Drove platform migrations: legacy file-share storage → cloud (S3), reconciliation workloads → PostgreSQL, JSON credential files → environment-variable secrets, and Dockerized deploys with automated DB migrations
- Owned production operations: pipeline failure investigation, backlog cleanups, one-time data realignments, and Django-Q background job processing; wrote runbook-grade documentation and a QA framework for integration testing

### Data Scientist · IBM India — Jul 2018 – Jul 2021

Client-facing AI delivery for enterprise customers (Boston Dynamics, IFFCO-Tokio General Insurance)

- Delivered a computer-vision car damage assessment solution for IFFCO-Tokio, deployed live across India — owning the engagement from model training through production rollout
- Built the orchestration layer routing deep-learning inference results into downstream client systems for Boston Dynamics anomaly detection
- Received the IBM Eminence & Excellence Star Award for successful production delivery

## Skills

- Data Engineering: ETL/ELT design, Amazon Redshift, Amazon S3, PostgreSQL, SQL, incremental/idempotent load patterns, reconciliation & data-quality tooling, batch scheduling & monitoring
- Salesforce: Bulk API, Apex Triggers, bidirectional CRM data sync
- Engineering: Python (production Django systems, FastAPI, pandas), Docker, CI/CD pipelines, TypeScript, C#
- Cloud: AWS (Redshift, S3, EC2, Lambda)
- AI (secondary): LLM applications, RAG systems, LangChain, Qdrant, OpenAI & Anthropic Claude APIs

## Education

**M.S. Computer Science · Georgia Institute of Technology** — Aug 2021 – May 2023
GPA 3.83 / 4.0 · Artificial Intelligence, Natural Language Processing, Machine Learning

**B.Tech (Hons) Computer Science · IIT Bombay** — Jul 2014 – May 2018
GPA 7.72 / 10 · Parallel Programming, Computer Graphics, Operating Systems
