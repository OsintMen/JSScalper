def generate_markdown(intelligence_map, risk_data, output_file):
    md = f"# JSScalper Report\n\n"
    md += f"## Risk Score: {risk_data['risk_score']}/100\n\n"
    md += "### Risk Details\n"
    for d in risk_data['details']:
        md += f"- {d}\n"
    md += "\n### JS Files Collected\n"
    for js in intelligence_map['js_files']:
        md += f"- {js}\n"
    md += "\n### Endpoints Discovered\n"
    for ep in intelligence_map['endpoints']:
        md += f"- {ep}\n"
    md += "\n### GraphQL Operations\n"
    for gql in intelligence_map['graphql_operations']:
        md += f"- {gql}\n"
    md += "\n### WebSockets\n"
    for ws in intelligence_map['websockets']:
        md += f"- {ws}\n"
    md += "\n### SPA Routes\n"
    for route in intelligence_map['routes']:
        md += f"- {route}\n"
    md += "\n### Recon Hints\n"
    for hint in intelligence_map['recon_hints']:
        md += f"- {hint}\n"

    with open(output_file, "w") as f:
        f.write(md)