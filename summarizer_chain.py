from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

load_dotenv()




def get_summary_chain():
    template = """Summarize the following text 5- 6 bullet points in a clear and concise way  :

    {input_text}

    Summary:"""

    prompt = PromptTemplate(
        input_variables=["input_text"],
        template=template,
    )

    llm = HuggingFaceHub(repo_id="facebook/bart-large-cnn",
                          model_kwargs={"temperature": 0.5, 
                                        "max_length": 500})



    chain = LLMChain(llm=llm, prompt=prompt)
    return chain
