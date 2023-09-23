import wikipedia

def fetch_via_wrapper(query):
    content = wikipedia.page(query).content
    return content
