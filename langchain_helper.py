import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
load_dotenv()

def write_story(writer,topics,book,lang):
    llm = ChatOpenAI(temperature = 0.8)
    prompt_template_name = PromptTemplate(
        input_variables=['writer','topics','book','lang'],
        template = 'Create a very short story that uses 700 words in the style of {writer}. Write it in {lang} language. Write the story which covers the topics {topics}. Add a tone similar to the book {book} written by {writer} but do not take the protagonist from the book , create a different protagonist. Carefully connect these topics. The story should have some plot twists. Write an interesting story that keeps the reader involved and makes the reader think.'
    )
    book_chain = LLMChain(llm=llm , prompt=prompt_template_name,output_key='story')
    response = book_chain({'writer' : writer , 'topics' : topics , 'book' : book , 'lang' : lang})
    return response

