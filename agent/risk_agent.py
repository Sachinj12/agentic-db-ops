def classify_query_risk(rows_examined, rows_returned):
    if rows_examined > rows_returned * 10:
        return "HIGH_RISK"
    elif rows_examined > rows_returned * 3:
        return "MEDIUM_RISK"
    else:
        return "SAFE"


# Example input based on our slow query
rows_examined = 50370
rows_returned = 1000

decision = classify_query_risk(rows_examined, rows_returned)

print("Agent Decision:", decision)
print("Evidence: rows_examined =", rows_examined,
      ", rows_returned =", rows_returned)

def explain_risk(rows_examined, rows_returned):
    if rows_examined > rows_returned * 10:
        return (
            "The query scans significantly more rows than it returns. "
            "This indicates inefficient access patterns and potential "
            "performance degradation as data grows."
        )
    return "Query access pattern looks efficient."

print("Explanation:", explain_risk(rows_examined, rows_returned))
print("Suggested Fix: Consider adding indexes or optimizing ORDER BY usage.")
