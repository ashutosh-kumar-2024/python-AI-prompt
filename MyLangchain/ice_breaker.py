from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

if __name__ == '__main__':
    load_dotenv()
    
    information = "Elon Musk"

    summary_template = """
    Given the information: about a person - {information}, please create:
    1. A short summary
    2. Two interesting facts about the person
    """

    print(summary_template)
    
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(
        temperature=0, model_name="gpt-4o", api_key=os.environ["OPENAI_API_KEY"]
    )

    chain = summary_prompt_template | llm

    result = chain.invoke(input={"information": information})
    
    print(result)
