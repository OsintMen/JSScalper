def calculate_risk(intelligence_map):
    score = 0
    details = []

    if intelligence_map["secrets"]:
        score += 40
        details.append("Secrets detected (JWT/API keys/etc.)")

    if intelligence_map["endpoints"]:
        score += 20
        details.append(f"{len(intelligence_map['endpoints'])} endpoints discovered")

    if intelligence_map["graphql_operations"]:
        score += 15
        details.append(f"{len(intelligence_map['graphql_operations'])} GraphQL operations discovered")

    if intelligence_map["websockets"]:
        score += 10
        details.append(f"{len(intelligence_map['websockets'])} WebSocket URLs discovered")

    if intelligence_map["routes"]:
        score += 5
        details.append(f"{len(intelligence_map['routes'])} SPA routes found")

    # Cap score at 100
    score = min(score, 100)

    return {"risk_score": score, "details": details}