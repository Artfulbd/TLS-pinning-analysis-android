import logging
from mitmproxy import ctx, http

def request(flow: http.HTTPFlow) -> None:
    # a random condition to make this example a bit more interactive
    if flow.request.pretty_url == "http://example.com/path":
        logging.info("Shutting down everything...")
        ctx.master.shutdown()