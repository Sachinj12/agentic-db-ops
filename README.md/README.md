# MySQL Slow Query Analysis – Foundations for Agentic DB Ops

## Overview
This project captures and analyzes MySQL slow queries to identify
high-risk query patterns early, based on rows examined and execution behavior.

## What was done
- Enabled MySQL slow query logging
- Generated a real JOIN + ORDER BY query
- Captured slow query logs
- Identified performance risk using rows_examined

## Why this matters
Queries with high rows examined may perform acceptably at small scale
but become critical bottlenecks as data grows.

This project focuses on identifying such risks early.

## Evidence
- Raw MySQL slow query log: /logs/slow.log
- Screenshot proof: /screenshots/mysql_slow_query_log.png

## Tech Stack
- MySQL 8
- Windows
- Slow Query Log

## Status
This repository represents the *foundation stage*.
Future steps will include structured parsing and automated analysis.

## Phase 1 – Runtime Execution Analysis

- Used EXPLAIN ANALYZE to inspect actual execution behavior
- Query performs a Nested Loop Join
- ORDER BY on orders.amount causes a full sort before LIMIT
- ~50,000 rows examined to return 1,000 rows
- Execution time is acceptable now, but pattern is not scalable

 ## Phase 2 – Agentic DB Risk Decision

Goal:
Build an agent that autonomously classifies MySQL queries into
HIGH_RISK, MEDIUM_RISK, or SAFE based on execution behavior and rows examined
The agent focuses on early risk detection rather than runtime latency alone.

### Initial Agent Rule

Rule 1:
If a query examines a significantly high number of rows compared to
rows returned, the agent flags it as HIGH_RISK.

Rationale:
High rows examined indicates poor access patterns and scalability risk,
even if execution time is currently acceptable.

## Agent Decision (Phase 2 – Rule-based Agent)

A lightweight decision agent was implemented to classify query risk
based on execution behavior observed in MySQL.

### Input Evidence
- rows_examined: 50370
- rows_returned: 1000

### Agent Rule
If rows_examined > rows_returned × 10 → HIGH_RISK

### Agent Output
Agent Decision: HIGH_RISK  
Evidence: rows_examined = 50370, rows_returned = 1000

Reasoning:
High scan-to-return ratio indicates inefficient query access pattern,
even though runtime latency is acceptable.

Agent Explanation:
The query is likely to become a scalability bottleneck as data grows.

Suggested Fix:
- Add proper indexes
- Optimize ORDER BY usage
