# soc-home-lab
This project is a draft of soc home lab

# Mini Home SOC – Proof of Concept

**Project Status: DRAFT / Proof of Concept – Work in Progress**

This repository is an attempt to build a small, self-hosted **Security Operations Center (SOC)** using Docker containers.

The main goal was to create a complete lab environment to:

- Generate various types of logs (web, application, database, system)
- Collect and centralize those logs
- Index and visualize them using the Elastic Stack (Elasticsearch + Kibana)
- Experiment with detection rules and alerting

## Current Architecture (What Works)

### Deployed Components

- **Elasticsearch** (single-node) – log storage and indexing
- **Kibana** – visualization interface and rule/alert creation
- **Filebeat** – lightweight log shipper (main collection method used here)
- **DVWA** (Damn Vulnerable Web Application) – intentionally vulnerable web app to generate HTTP/Apache logs
- **MariaDB** – database backend for DVWA (connection logs, SQL queries, etc.)
- **ubuntu-lab** – manual Ubuntu container for system log simulation and testing

### Achievements & Successful Tests

- Log collection and parsing with **Filebeat**:
  - Apache access & error logs from DVWA
  - System logs (syslog, auth.log, etc.) from the Ubuntu container
  - MariaDB logs (connections, SQL errors, etc.)

- Successful ingestion into Elasticsearch
- Log visualization in Kibana (Discover + basic dashboards)
- Creation and testing of **detection rules / alerts** in Kibana, including:
  - Failed DVWA login attempts
  - HTTP 500 errors on the web application
  - Typical brute-force or SQL injection patterns
  - Failed SSH login attempts (when simulated in ubuntu-lab)

→ **Filebeat** was sufficient for most use cases → **Logstash** was not ultimately activated in this version.

## Current Limitations & Technical Choices

- No SSL/TLS enabled (plain HTTP) → Elasticsearch and Kibana are exposed without encryption
- Basic username/password authentication (no certificates or service tokens yet)
- No high availability (single-node Elasticsearch only)
- Kibana configuration persistence is manual (no automated backup/restore)
- Python startup script used to enforce sequential startup and avoid early connection failures

## Planned Next Steps (Not Yet Implemented)

- Enable **HTTPS** with self-signed or Let's Encrypt certificates
- Properly configure **X-Pack Security** (roles, users, API keys, service tokens)
- Add **Logstash** for more advanced parsing/enrichment pipelines if needed
- Integrate a lightweight **SOAR** solution (e.g. Shuffle, TheHive, or Wazuh-style response)
- Add a ticketing/incident management platform (TheHive, MISP, GLPI, osTicket, etc.)
- Build richer **dashboards**, **watchers**, and advanced alerting
- Possibly integrate **Wazuh** or the full **Elastic SIEM** module

## Quick Start

```bash
# 1. Update passwords in docker-compose.yml
# 2. Start core services
docker compose up -d elasticsearch
sleep 20
docker compose up -d kibana dvwa db

# 3. (optional) Start log collection
docker compose up -d filebeat

# Or use the provided Python startup script for better control
python start.py
