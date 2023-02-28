from pathlib import Path
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import pdf

import os 
import openai 

openai.api_key_path = ("/home/thrash/openai")

var1 = input("Name : ")
var2 = input("Company Name: ")
var3 = input("Job Title: ")
var4 = input("Location: ")
var5 = input("experience 1: ")
var6 = input("experience 2: ")


model_engine = "text-davinci-003"
prompt = "Can you write me a formatted cover letter. my name is {}, I am applying to {} to be a {}. The company is located in {}. My previous experiences include {} and {}".format(var1,var2, var3, var4, var5, var6)

print(prompt)

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)


response = completion.choices[0].text

print(response)





