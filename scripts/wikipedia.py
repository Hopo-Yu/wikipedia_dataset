import wikipedia_api

wiki_wiki = wikipedia_api.Wikipedia('en')

page_py = wiki_wiki.page('Python (programming language)')

print("Page - Title: %s" % page_py.title)
# Page - Title: Python (programming language)
