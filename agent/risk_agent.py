def classify_query_risk(rows_examined, rows_returned):
    """
    Classify query risk based on rows examined vs rows returned
    """
    if rows_examined > rows_returned * 10:
        return "HIGH_RISK"
    elif rows_examined > rows_returned * 3:
        return "MEDIUM_RISK"
    else:
        return "SAFE"


def explain_risk(rows_examined, rows_returned):
    """
    Explain why the query was classified with a certain risk
    """
    if rows_examined > rows_returned * 10:
        return (
            "The query scans significantly more rows than it returns. "
            "This indicates inefficient access patterns and potential "
            "performance degradation as data grows."
        )
    elif rows_examined > rows_returned * 3:
        return (
            "The query scans more rows than it returns. "
            "This may cause performance issues at scale."
        )
    else:
        return "Query access pattern looks efficient."