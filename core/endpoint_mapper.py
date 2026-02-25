import re

ENDPOINT_PATTERN = r'(https?:\/\/[^\s"\']+|\/api\/[^\s"\']+)'

def extract_endpoints(strings_list):
    endpoints = []
    for s in strings_list:
        matches = re.findall(ENDPOINT_PATTERN, s)
        endpoints.extend(matches)
    return list(set(endpoints))