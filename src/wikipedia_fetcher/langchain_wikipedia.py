from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

def fetch_via_langchain(query):
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    return wikipedia.run(query)
