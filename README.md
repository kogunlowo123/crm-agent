# CRM Agent

[![CI](https://github.com/kogunlowo123/crm-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/crm-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Customer Service | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

CRM automation agent that maintains customer records, logs interactions, tracks customer health scores, triggers engagement workflows, and surfaces account insights for sales and support teams.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `update_contact` | Update customer contact record with new information |
| `log_interaction` | Log a customer interaction in the CRM |
| `calculate_health_score` | Calculate customer health score based on engagement signals |
| `trigger_workflow` | Trigger an automated engagement workflow for a customer |
| `surface_insights` | Surface key account insights for sales or support |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/crm/analyze` | Run analysis |
| `POST` | `/api/v1/crm/execute` | Execute action |
| `GET` | `/api/v1/crm/metrics` | Get metrics |
| `PUT` | `/api/v1/crm/configure` | Update configuration |
| `POST` | `/api/v1/crm/report` | Generate report |

## Features

- Crm
- Analytics
- Automation

## Integrations

- Zendesk
- Intercom
- Salesforce Service
- Freshdesk
- Hubspot Service

## Architecture

```
crm-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── crm_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Customer Service Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
