import re

ROUTE_PATTERNS = [
    r'path:\s*["\']([^"\']+)["\']',
    r'Route\s+path=["\']([^"\']+)["\']',
]

def extract_routes(js_content):
    routes = []
    for pattern in ROUTE_PATTERNS:
        routes.extend(re.findall(pattern, js_content))
    return list(set(routes))