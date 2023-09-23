from langchain.document_loaders import WikipediaLoader
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    PromptTemplate, ChatPromptTemplate,
    SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
)


def analyze_with_chatgpt(query, context_text):
    model = ChatOpenAI()

    template = "Answer this question:\n{question}\n Here is some extra context: \n{document}"
    human_prompt = HumanMessagePromptTemplate.from_template(template)

    chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

    result = model(chat_prompt.format_prompt(
        question=query, document=context_text).to_messages())

    return result.content
