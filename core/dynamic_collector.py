from playwright.async_api import async_playwright
from utils.logger import info, warning

async def collect_js(url):
    js_files = set()
    try:
        info(f"Launching browser to collect JS from: {url}")
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()

            page.on("response", lambda response: js_files.add(response.url) if response.url.endswith(".js") else None)

            await page.goto(url)
            await page.wait_for_load_state("networkidle")
            await browser.close()
            info(f"Collected {len(js_files)} JS files.")
    except Exception as e:
        warning(f"Failed to collect JS dynamically: {e}")

    return js_files