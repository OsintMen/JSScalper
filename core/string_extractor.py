import re

def extract_strings(js_content):
    pattern = r'["\']([^"\']{4,})["\']'
    return list(set(re.findall(pattern, js_content)))