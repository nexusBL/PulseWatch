# AI Collaboration Log

# AI Tools Used

- ChatGPT (GPT-5.5)
- VSCode AI Chat

---

# Development Philosophy

AI was used as an accelerator and pair programmer rather than a code generator.

Every generated component was:

1. Reviewed manually
2. Debugged locally
3. Integrated incrementally
4. Modified to fit the project architecture

---

# AI-Assisted Tasks

## Backend Scaffolding

Prompt:

> Create a FastAPI project structure for an uptime monitoring application.

AI helped with:

- Project layout
- SQLAlchemy setup
- Dependency injection

---

## Database Design

Prompt:

> Design database tables for storing monitored URLs and health checks.

AI proposed:

- monitored_urls
- health_checks

The relationships and schema updates were manually refined.

---

## Scheduler

Prompt:

> How can APScheduler periodically monitor URLs in FastAPI?

AI helped with:

- Background job design
- Scheduler integration

---

## Frontend

Prompt:

> Build a React dashboard that polls an API and displays URL health status.

AI helped with:

- Component scaffolding
- Axios integration
- State management ideas

---

## Docker

Prompt:

> Create Dockerfiles and docker-compose setup for a React and FastAPI application.

AI generated the initial configuration, which was later modified to solve networking issues.

---

# Problems Encountered

## Issue 1

Database schema mismatch.

Error:

```text
sqlite3.OperationalError:
table health_checks has no column named is_up
```

Solution:

- Deleted old database
- Recreated schema

---

## Issue 2

Docker networking.

Problem:

```text
http://backend:8000
```

was inaccessible outside containers.

Solution:

Implemented:

```text
VITE_API_URL
```

configuration.

---

## Issue 3

CORS failures.

Solution:

Added:

```python
CORSMiddleware
```

---

# Manual Contributions

The following work was implemented and debugged manually:

- Database relationships
- URL monitoring logic
- Error handling
- Scheduler integration
- Docker troubleshooting
- API refinements
- Frontend debugging
- Delete endpoint
- History endpoint
- Documentation

---

# Final Result

A complete full-stack uptime monitoring application that can be started with:

```bash
docker compose up --build
```

and demonstrates backend, frontend, infrastructure, and AI-assisted development skills.