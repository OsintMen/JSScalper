import re

FRAMEWORK_PATTERNS = {
    "React": r"react-dom",
    "Vue": r"vue\.runtime",
    "Angular": r"@angular/core",
    "Next.js": r"_next\/static",
    "Webpack": r"webpackBootstrap"
}

def detect_frameworks(js_contents):
    detected = set()
    for content in js_contents.values():
        for name, pattern in FRAMEWORK_PATTERNS.items():
            if re.search(pattern, content):
                detected.add(name)
    return list(detected)