def detect_websockets(strings_list):
    ws_urls = []
    for s in strings_list:
        if s.startswith("ws://") or s.startswith("wss://"):
            ws_urls.append(s)
    return list(set(ws_urls))