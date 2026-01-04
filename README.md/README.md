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