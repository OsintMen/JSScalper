import re

def extract_graphql(strings_list):
    graphql_patterns = [
        r'query\s+\w+',
        r'mutation\s+\w+',
        r'subscription\s+\w+'
    ]
    results = []
    for s in strings_list:
        for pattern in graphql_patterns:
            if re.search(pattern, s):
                results.append(s)
    return list(set(results))