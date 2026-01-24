from risk_agent import classify_query_risk, explain_risk


def parse_slow_log(file_path):
    """
    Parse MySQL slow query log and extract key metrics
    """
    with open(file_path, "r") as f:
        lines = f.readlines()

    query_time = None
    rows_examined = None
    query_lines = []

    for line in lines:
        if "Query_time" in line and "Rows_examined" in line:
            parts = line.split()
            query_time = float(parts[2])
            rows_examined = int(parts[-1])

        elif line.strip().upper().startswith("SELECT"):
            query_lines.append(line.strip())

        elif query_lines:
            query_lines.append(line.strip())

    query = " ".join(query_lines)

    return {
        "query_time": query_time,
        "rows_examined": rows_examined,
        "query": query
    }


if __name__ == "__main__":
    # Step 1: Parse slow query log
    data = parse_slow_log("logs/mysql_slow.log")

    rows_examined = data["rows_examined"]
    rows_returned = 1000  # Example assumption for demo

    # Step 2: Agent decision
    decision = classify_query_risk(rows_examined, rows_returned)
    explanation = explain_risk(rows_examined, rows_returned)

    # Step 3: Output
    print("\n=== Parsed Slow Query Data ===")
    for k, v in data.items():
        print(f"{k}: {v}")

    print("\n=== Agent Decision ===")
    print("Decision:", decision)
    print("Explanation:", explanation)
    print("Suggested Fix: Consider adding indexes or optimizing ORDER BY usage.")