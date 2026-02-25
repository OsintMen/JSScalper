def build_intelligence_map(js_files, strings, secrets, routes, endpoints, graphql_ops, websockets, hints, openapi_map):
    return {
        "js_files": list(js_files),
        "strings": strings,
        "secrets": secrets,
        "routes": routes,
        "endpoints": endpoints,
        "graphql_operations": graphql_ops,
        "websockets": websockets,
        "recon_hints": hints,
        "openapi_preview": openapi_map
    }