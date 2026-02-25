import re

SECRET_PATTERNS = {
    "jwt": r'eyJ[a-zA-Z0-9-_]{20,}\.[a-zA-Z0-9-_]{20,}\.[a-zA-Z0-9-_]{20,}',
    "api_key": r'(?i)api[_-]?key["\']?\s*[:=]\s*["\']\w{16,}',
    "aws_key": r'AKIA[0-9A-Z]{16}',
    "feature_flags": r'(isAdmin|isBeta|enableDebug|featureToggle)'
}

def analyze_secrets(strings_list):
    results = {}
    for name, pattern in SECRET_PATTERNS.items():
        matches = [s for s in strings_list if re.search(pattern, s)]
        if matches:
            results[name] = matches
    return results