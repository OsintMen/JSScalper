# JSScalper v5

**JSScalper v5** is a professional, ethical, bug bounty–grade JavaScript reconnaissance and intelligence tool.  
It scans websites to collect all JavaScript files (including dynamically loaded/lazy-loaded files), extracts routes, endpoints, GraphQL operations, WebSockets, secrets, and generates structured intelligence reports with risk scoring.

---

## ⚡ Features

- **Dynamic JS collection** using Playwright for SPA rendering  
- **Multi-threaded JS fetching** for faster scans  
- **SPA route extraction** (React, Vue, Angular, Next.js)  
- **REST endpoint detection** (fetch / axios / XHR)  
- **GraphQL operation detection** (query / mutation / subscription)  
- **WebSocket detection** (ws:// / wss://)  
- **Secrets & feature flags detection** (JWT, API keys, AWS keys, etc.)  
- **Recon hints generator** for bug bounty guidance  
- **OpenAPI-style preview of endpoints**  
- **JS dependency & framework fingerprinting** (React, Vue, Angular, Webpack, Next.js)  
- **Risk scoring** (0–100) based on discovered assets  
- **Markdown & optional HTML reports**  
- **Modular & professional codebase** for maintenance & extension  
- **CLI scan profiles** (`light` / `full`) for flexibility  

---

## ⚙ Installation

### Requirements
```bash
- Python 3.10+  
- Playwright: `pip install playwright`  
- Requests: `pip install requests`  
```
### Install Playwright Browsers

```bash
playwright install
```
## Clone or Extract JSScalper
```bash
git clone https://github.com/yourusername/JSScalper.git
cd JSScalper
```
## 🏃 Usage

 **Basic Scan (Full Profile)**
```bash
python main.py -u https://example.com
```
**Light Scan (Faster)**
```bash
python main.py -u https://example.com --profile light
```
**Generate HTML Report**
```bash
python main.py -u https://example.com --html
```
**Control Parallel JS Downloads**
```bash
python main.py -u https://example.com --threads 10
```
## 📂 Output

**All output is saved in the output/ folder for the scanned target:**

```bash 
output/
└── example.com/
    ├── intelligence_map.json    # Full JSON map with JS, endpoints, GraphQL, WebSockets, secrets
    ├── report.md                # Markdown report with risk scoring & hints
    └── report.html              # Optional HTML visual report
```
## 🧩 Scan Profiles
              
**light:**	      
       `Only dynamic JS collection & secrets (fast)`

**full:**	                
       `Full intelligence scan(endpoints, GraphQL, WebSockets, routes, reports)`


## 🔎 Risk Scoring & Hints

- JSScalper calculates a risk score (0–100) based on:

- Discovered secrets (JWT, API keys, AWS keys, etc.)

- Number of endpoints detected

- GraphQL operations

- WebSocket URLs

- SPA routes

- It also provides ethical recon hints for bug bounty investigations.

## 🛠 CLI Options

```bash 
-u, --url       Target URL (required)
--profile       Scan profile: light / full (default: full)
--threads       Number of threads for parallel JS download (default: 5)
--html          Generate HTML report (optional)

```

## 💡 Example Full Scan
```bash
python main.py -u https://example.com --profile full --threads 10 --html
```

## Output Example:
```bash
[INFO] Collected 45 JS files
[INFO] 15 REST endpoints discovered
[INFO] 3 GraphQL operations found
[INFO] 2 WebSocket URLs detected
[INFO] SPA Routes: /, /dashboard, /login
[INFO] Secrets found: JWT, API_KEY
[SUCCESS] Markdown report saved: output/example.com/report.md
[SUCCESS] HTML report saved: output/example.com/report.html
[SUCCESS] JSON intelligence map saved: output/example.com/intelligence_map.json
[SUCCESS] Risk Score: 85/100
[SUCCESS] Detected frameworks: React, Webpack
```
## ⚖ Ethical Usage

- Only scan in-scope targets for bug bounty programs or your own applications.

- JSScalper does not include IP rotation, firewall bypass, or exploitation modules.

- Always obtain permission before scanning external systems.

## 🧱 Extensibility

**JSScalper is fully modular:**

- Add more JS analyzers (token extractors, library fingerprinting, etc.)

- Extend report generators (Excel, PDF, dashboards)

- Integrate with other recon frameworks

## 👨‍💻 Developer Notes

- Dynamic JS collector uses Playwright for rendering SPAs

- Threaded JS fetcher speeds up scans for large applications

- Intelligence map JSON is the core data structure, feeding reports & OpenAPI previews

- Reports are optional, human-readable, and include risk hints

- Configurable via `config.py`
