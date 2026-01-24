# *Agentic DB Ops – MySQL Slow Query Risk Detection*

---

## *Overview*

This project demonstrates how *MySQL execution behavior* can be automatically analyzed and converted into *actionable risk intelligence* using a lightweight, explainable agent.

Instead of relying on latency alone, the system evaluates *rows examined vs rows returned* to detect *non-scalable query patterns early*, even when execution time appears acceptable.

The implemented pipeline follows:

> *Capture → Parse → Analyze → Decide → Explain → Recommend*

---

## *Problem Statement*

Many SQL queries:

- Execute quickly on small datasets  
- Appear healthy in basic monitoring  
- Hide inefficient access patterns  

As data grows, these queries become *production bottlenecks*.

Traditional tools ask:

> “Is the query slow right now?”

This project asks:

> *“Will this query become dangerous as data grows?”*

---

## *System Architecture*

MySQL Slow Query Log
↓
Log Parser (Python)
↓
Structured Execution Metrics
↓
Rule-Based Risk Agent
↓
Decision + Explanation + Suggested Fix

## *Step 1 – Slow Query Capture*

### *What Was Done*
- Enabled MySQL slow query logging  
- Executed a realistic JOIN + ORDER BY query  
- Captured the slow query log from MySQL  

### *Why This Matters*
The slow query log represents *real execution behavior*, not theoretical plans.

### *Evidence*
- Raw slow query log:  
  logs/mysql_slow.log
- Screenshot proof:  
  screenshots/mysql_slow_query_log.png

---

## *Step 2 – Slow Query Log Parsing*

### *Purpose*

MySQL slow query logs are *unstructured text*.  
To enable automated reasoning, a parser converts them into *structured data*.

---

### *Parser Implementation*

File:  
### *Extracted Fields*
- Query execution time  
- Rows examined  
- Full SQL query text  

---

### *Sample Parsed Output*

Query_time: 0.04

Rows_examined: 50370

Query:
SELECT * FROM orders
JOIN users ON orders.user_id = users.user_id
ORDER BY orders.amount
LIMIT 0, 1000;

This structured output becomes the *input to the agent*.

---

## *Step 3 – Execution Behavior Analysis*

Using *EXPLAIN ANALYZE*, the following behavior was observed:

- Nested Loop Join  
- Full sort on orders.amount  
- Sorting occurs *before LIMIT*  
- ~50,000 rows examined to return 1,000 rows  

### *Key Insight*

The query is *not slow yet, but the access pattern is inefficient and **will not scale*.

### *Evidence*

- Execution plan screenshot:  
  screenshots/Explain_analyse_sort_before_limit.png
- Query-under-analysis screenshot:  
  screenshots/Query_under_analysis.png

---

## *Step 4 – Rule-Based Risk Agent (Core Output)*

### *Agent Role*

The agent consumes parsed execution data and produces *three outputs*:

1. *Decision*  
2. *Explanation*  
3. *Suggested Fix*  

This exactly reflects the *current system behavior*.

---

### *Input Evidence*

- *rows_examined:* 50370  
- *rows_returned:* 1000  

---

### *Agent Rule*

If rows_examined > rows_returned × 10 → HIGH_RISK

Decision: HIGH_RISK

Explanation:
The query scans significantly more rows than it returns.
This indicates inefficient access patterns and potential
performance degradation as data grows.

Suggested Fix:
Consider adding indexes or optimizing ORDER BY usage.

### *Evidence*

- Agent output screenshot:  
  screenshots/phase2_agent_output.png
- Agent explanation screenshot:  
  screenshots/agent_explanation.png

---

## *Why the Agent Classified This as HIGH_RISK*

### *Root Causes Identified*
1. *ORDER BY without supporting index*  
   - Forces full sorting of large result sets  

2. *LIMIT applied after sort*  
   - MySQL must process all rows before limiting  

3. *High scan-to-return ratio*  
   - 50,370 rows examined for only 1,000 results  

---

## *Suggested Fixes (As Produced by the Agent)*

The agent recommends corrective actions based on observed behavior:

- Add appropriate indexes on sorting and join columns  
- Optimize ORDER BY usage to avoid full sorts  
- Reduce rows examined through better access paths  
- Avoid SELECT * when unnecessary  

These recommendations aim to:

- Reduce rows scanned  
- Eliminate expensive sort operations  
- Improve long-term scalability  

---

## *Tech Stack*

- *MySQL 8*
- *Python 3*
- *MySQL Slow Query Log*
- *EXPLAIN ANALYZE*
- *Git & GitHub*

---

## *Project Status*

- ✔ Slow query captured  
- ✔ Log parser implemented  
- ✔ Execution behavior analyzed  
- ✔ Risk agent implemented  
- ✔ Decision, explanation, and suggested fix generated  

This repository represents a *working foundation* for *Agentic Database Operations*.

---

## *Future Enhancements*

- Multi-query ingestion  
- Risk confidence scoring  
- Automatic index recommendation generation  
- Learning-based threshold tuning  
- Integration with monitoring systems  

---

## *Key Takeaway*

This project shows how *raw database execution signals* can be transformed into:

- A clear *risk decision*
- A human-readable *explanation*
- An actionable *suggested fix*

This forms the first step toward *self-aware, proactive database operations*.
