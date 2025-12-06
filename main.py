from mitmproxy import http
import json
import time

# Optional: open a file to save logs
log_file = open("mitm_logs.txt", "a")

def log(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"[{timestamp}] {msg}\n"
    print(full_msg, end="")
    log_file.write(full_msg)
    log_file.flush()

def request(flow: http.HTTPFlow):
    # Log request URL, method, headers, body
    req = flow.request
    log(f"➡️ REQUEST: {req.method} {req.pretty_url}")
    log(f"Headers: {json.dumps(dict(req.headers))}")
    if req.content:
        try:
            log(f"Body: {req.content.decode('utf-8')}")
        except:
            log(f"Body: {req.content}")

def response(flow: http.HTTPFlow):
    # Log response status, headers, body
    res = flow.response
    log(f"⬅️ RESPONSE: {res.status_code} {flow.request.pretty_url}")
    log(f"Headers: {json.dumps(dict(res.headers))}")
    if res.content:
        try:
            log(f"Body: {res.content.decode('utf-8')}")
        except:
            log(f"Body: {res.content}")
