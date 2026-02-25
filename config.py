
# Output folder base path
OUTPUT_BASE = "output"

# Playwright settings
PLAYWRIGHT_HEADLESS = True       # Set False to see browser during scan
PLAYWRIGHT_TIMEOUT = 30          # Timeout in seconds for page loading

# Default scan settings
DEFAULT_THREADS = 5
DEFAULT_PROFILE = "full"         # Options: "light" or "full"

# JS string extraction pattern
STRING_PATTERN = r'["\']([^"\']{4,})["\']'

# Endpoint detection regex
ENDPOINT_PATTERN = r'(https?:\/\/[^\s"\']+|\/api\/[^\s"\']+)'

# Secret detection patterns
SECRET_PATTERNS = {
    "jwt": r'eyJ[a-zA-Z0-9-_]{20,}\.[a-zA-Z0-9-_]{20,}\.[a-zA-Z0-9-_]{20,}',
    "api_key": r'(?i)api[_-]?key["\']?\s*[:=]\s*["\']\w{16,}',
    "aws_key": r'AKIA[0-9A-Z]{16}',
    "feature_flags": r'(isAdmin|isBeta|enableDebug|featureToggle)'
}

# Supported SPA route regex patterns
ROUTE_PATTERNS = [
    r'path:\s*["\']([^"\']+)["\']',
    r'Route\s+path=["\']([^"\']+)["\']',
]

# Framework detection patterns
FRAMEWORK_PATTERNS = {
    "React": r"react-dom",
    "Vue": r"vue\.runtime",
    "Angular": r"@angular/core",
    "Next.js": r"_next\/static",
    "Webpack": r"webpackBootstrap"
}

# Recon hint rules
RECON_HINTS = {
    "endpoints": "Check endpoints for IDOR & auth bypass.",
    "jwt": "JWT detected — check for weak signing or none algorithm.",
    "api_key": "API keys detected — verify exposure risk."
}

# Risk scoring weights
RISK_WEIGHTS = {
    "secrets": 40,
    "endpoints": 20,
    "graphql_operations": 15,
    "websockets": 10,
    "routes": 5
}