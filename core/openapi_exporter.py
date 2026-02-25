def generate_openapi(endpoints):
    openapi = {
        "openapi": "3.0.0",
        "info": {"title": "JSScalper API Map", "version": "1.0"},
        "paths": {}
    }
    for ep in endpoints:
        openapi["paths"][ep] = {
            "get": {
                "description": "Discovered endpoint",
                "responses": {"200": {"description": "OK"}}
            }
        }
    return openapi