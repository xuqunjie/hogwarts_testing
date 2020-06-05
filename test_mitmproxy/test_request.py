"""
This example shows how to send a reply from the proxy immediately
without sending any data to the remote server.
"""
from mitmproxy import http


# def request(flow: http.HTTPFlow) -> None:
#     # pretty_url takes the "Host" header of the request into account, which
#     # is useful in transparent mode where we usually only have the IP otherwise.
#
#     if flow.request.pretty_url == "http://example.com/path":
#         flow.response = http.HTTPResponse.make(
#             200,  # (optional) status code
#             b"Hello World",  # (optional) content
#             {"Content-Type": "text/html"}  # (optional) headers
#         )

def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.

    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        with open("/Users/seveniruby/ke/lagou_1/mitmproxy/quote.json") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )