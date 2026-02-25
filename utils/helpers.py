import concurrent.futures
import requests
from utils.logger import info

def fetch_js_parallel(js_urls, threads=5):
    results = {}
    def fetch(url):
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                results[url] = resp.text
            else:
                info(f"Failed to fetch JS: {url}")
        except:
            info(f"Exception fetching JS: {url}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(fetch, js_urls)

    return results