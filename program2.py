import os
from urllib.parse import urlparse
FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "urls.txt")
def get_tld(url):
    """Повертає домен 1-го рівня (наприклад, 'com' для https://www.google.com/search)."""
    if "//" not in url:
        url = "//" + url
    host = urlparse(url).hostname
    return host.rsplit(".", 1)[-1] if host else ""
if not os.path.exists(FILE):
    with open(FILE, "w", encoding="utf-8") as f:
        f.write("https://www.google.com/search?q=python\n"
                "https://uk.wikipedia.org/wiki/Python\n"
                "http://www.rada.gov.ua\n"
                "https://www.bbc.co.uk/news\n"
                "https://www.python.org\n"
                "https://github.com/user/repo\n")
with open(FILE, "r", encoding="utf-8") as f:
    for line in f:
        url = line.strip()
        if url:
            print(url, "->", get_tld(url))