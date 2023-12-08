
#!/usr/bin/env python 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv

load_dotenv()

def generate_petname(pet_animal, pet_color):
    llm = OpenAI(temperature=0.1)

    prompt_template_name = PromptTemplate(input_variables=['pet_animal', 'pet_color'],
                                          template="I have a {pet_animal} which is {pet_color} in color. Suggest me five cool hippie names for my pet") 
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='pet_name')

    response = name_chain({'pet_animal': pet_animal, 'pet_color' : pet_color})

    return response

if __name__ == '__main__':
    print(generate_petname("cow", 'green'))
