def generate_html(intelligence_map, risk_data, output_file):
    html = f"""
    <html><head><title>JSScalper Report</title></head><body>
    <h1>JSScalper Report</h1>
    <h2>Risk Score: {risk_data['risk_score']}/100</h2>
    <h3>Risk Details</h3>
    <ul>{"".join([f"<li>{d}</li>" for d in risk_data['details']])}</ul>
    <h3>JS Files Collected</h3>
    <ul>{"".join([f"<li>{js}</li>" for js in intelligence_map['js_files']])}</ul>
    <h3>Endpoints</h3>
    <ul>{"".join([f"<li>{ep}</li>" for ep in intelligence_map['endpoints']])}</ul>
    <h3>GraphQL Operations</h3>
    <ul>{"".join([f"<li>{gql}</li>" for gql in intelligence_map['graphql_operations']])}</ul>
    <h3>WebSockets</h3>
    <ul>{"".join([f"<li>{ws}</li>" for ws in intelligence_map['websockets']])}</ul>
    <h3>SPA Routes</h3>
    <ul>{"".join([f"<li>{r}</li>" for r in intelligence_map['routes']])}</ul>
    <h3>Recon Hints</h3>
    <ul>{"".join([f"<li>{h}</li>" for h in intelligence_map['recon_hints']])}</ul>
    </body></html>
    """
    with open(output_file, "w") as f:
        f.write(html)