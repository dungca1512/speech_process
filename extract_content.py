from trafilatura import fetch_url, extract

def extract_content(url):
    downloaded = fetch_url(url)
    result = extract(downloaded)
    return result