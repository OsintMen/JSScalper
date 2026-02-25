import asyncio
import os
import json
import argparse

from config import OUTPUT_BASE, DEFAULT_THREADS, DEFAULT_PROFILE
from utils.banner import show_banner
from utils.logger import info, success, warning, error
from utils.helpers import fetch_js_parallel
from core.dynamic_collector import collect_js
from core.string_extractor import extract_strings
from core.secret_analyzer import analyze_secrets
from core.route_extractor import extract_routes
from core.endpoint_mapper import extract_endpoints
from core.graphql_analyzer import extract_graphql
from core.websocket_detector import detect_websockets
from core.vulnerability_hints import generate_hints
from core.openapi_exporter import generate_openapi
from core.map_engine import build_intelligence_map
from core.dependency_fingerprint import detect_frameworks
from reports.risk_engine import calculate_risk
from reports.markdown_report import generate_markdown
from reports.html_report import generate_html


def create_output_folder(target_url):
    folder_name = target_url.replace("https://", "").replace("http://", "").replace("/", "_")
    folder_path = os.path.join(OUTPUT_BASE, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


async def main():
    parser = argparse.ArgumentParser(description="JSScalper v5 – Ethical JS Recon Tool")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("--html", action="store_true", help="Generate HTML report")
    parser.add_argument("--threads", type=int, default=DEFAULT_THREADS, help="Parallel JS download threads")
    parser.add_argument("--profile", choices=["light", "full"], default=DEFAULT_PROFILE, help="Scan profile")
    args = parser.parse_args()

    show_banner()
    info(f"Starting JSScalper v5 ({args.profile} profile) on {args.url} with {args.threads} threads")

    # Phase 1: Collect JS files dynamically
    js_urls = await collect_js(args.url)
    if not js_urls:
        warning("No JS files collected. Exiting.")
        return

    info(f"Collected {len(js_urls)} JS files, downloading in parallel...")
    js_contents = fetch_js_parallel(js_urls, threads=args.threads)
    info(f"Downloaded {len(js_contents)} JS files successfully")

    # Phase 2: Extract data from JS
    all_strings = []
    routes = []
    endpoints = []
    graphql_ops = []
    websockets = []

    for content in js_contents.values():
        strings = extract_strings(content)
        all_strings.extend(strings)

        if args.profile == "full":
            routes.extend(extract_routes(content))
            endpoints.extend(extract_endpoints(strings))
            graphql_ops.extend(extract_graphql(strings))
            websockets.extend(detect_websockets(strings))

    secrets = analyze_secrets(all_strings)
    hints = generate_hints(endpoints, secrets)
    openapi_map = generate_openapi(endpoints)
    frameworks = detect_frameworks(js_contents)

    # Phase 3: Build intelligence map
    intelligence_map = build_intelligence_map(
        js_urls,
        all_strings,
        secrets,
        list(set(routes)),
        list(set(endpoints)),
        list(set(graphql_ops)),
        list(set(websockets)),
        hints,
        openapi_map
    )

    # Phase 4: Save outputs
    output_folder = create_output_folder(args.url)
    json_path = os.path.join(output_folder, "intelligence_map.json")
    with open(json_path, "w") as f:
        json.dump(intelligence_map, f, indent=4)

    # Phase 5: Risk scoring and reporting
    risk_data = calculate_risk(intelligence_map)
    markdown_file = os.path.join(output_folder, "report.md")
    generate_markdown(intelligence_map, risk_data, markdown_file)
    success(f"Markdown report saved: {markdown_file}")

    if args.html:
        html_file = os.path.join(output_folder, "report.html")
        generate_html(intelligence_map, risk_data, html_file)
        success(f"HTML report saved: {html_file}")

    success(f"JSScalper v5 scan complete!")
    success(f"Risk Score: {risk_data['risk_score']}/100")
    success(f"Detected frameworks: {', '.join(frameworks) if frameworks else 'None'}")
    success(f"JSON intelligence map saved: {json_path}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        warning("Scan interrupted by user")