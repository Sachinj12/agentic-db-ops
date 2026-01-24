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
