# External Data Ingestion Platform – Roadmap

## Goal

Build a small but realistic **DataOps-oriented platform** that periodically ingests external API data and stores it locally for long-term use, analysis, and reliability.

Initial data source: **OpenWeather API**  
Initial use case: **scheduled weather data collection for Malaysia**

---

## Current State (Day 0)

- Manual Python script pulls weather data from OpenWeather API
- Configuration via environment variables (`.env`)
- Data fetch verified via Postman and CLI
- No persistence yet (stdout only)

---

## Roadmap

### Phase 1 – Safe Configuration & Validation
- Validate required environment variables on startup
- Add `.env.example` and `.gitignore`
- Fail fast on missing or invalid configuration
- Produce clean, minimal console output

---

### Phase 2 – Local Data Persistence
- Store API responses locally
- Choose storage format:
  - JSONL (append-only), or
  - SQLite (recommended)
- Store timestamp, location, and key metrics
- Preserve raw API response for replay/debugging

---

### Phase 3 – Multi-Location Ingestion
- Define representative Malaysian cities via config (`cities.json`)
- Loop ingestion across all configured locations
- Normalize stored data schema across locations

---

### Phase 4 – Scheduling & Automation
- Automate ingestion via `cron`
- Log execution output and errors
- Ensure idempotent, repeatable runs

---

### Phase 5 – Retention & Storage Control
- Implement data retention policy (e.g. keep last 30 days)
- Prevent uncontrolled disk growth
- Document storage strategy and limits

---

### Phase 6 – Operational Visibility
- Track last run time and status
- Record basic ingestion stats per run
- Provide simple health/status indicators for ops verification

---

## Non-Goals (Explicitly Out of Scope)

- Real-time streaming
- High availability / clustering
- User-facing dashboards
- Paid API tiers
- Large-scale analytics

---

## Long-Term Direction

This platform is designed to be extensible to other external data sources, such as:
- Blockchain RPC data
- Market pricing APIs
- Public telemetry feeds

---

## Design Philosophy

- Small, incremental, and verifiable steps
- Operability over feature count
- Realistic constraints (API limits, storage, scheduling)
- Clear separation between ingestion, storage, and future consumption
