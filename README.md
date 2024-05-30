# LLM_code
Sample GenAI code to learn langchain https://python.langchain.com/docs/get_started/introduction   
Note: Please use your own API Keys. Keys are used in the code are already removed.

#### Sample code 1 (HuggingFace):
```
!pip install langchain langchain-community langchain-core
!pip install huggingface_hub

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"]="<API_KEY>"

def get_answer(query):
    llm = HuggingFaceHub(repo_id = "google/flan-t5-large")
    return llm(query)

def get_query():
    return "What is the capital of UK?"

from langchain.llms import HuggingFaceHub
query = get_query()
answer = get_answer(query)

print(answer)
```
```
from huggingface_hub import list_models
def list_most_popular(task: str):
    for rank, model in enumerate(
        list_models(filter=task, sort="downloads", direction=-1)
):
        if rank == 5:
            break
        print(f"{model.id}, {model.downloads}\n")
list_most_popular("text-classification")
```
#### Sample code 2 (OpenAI):
```
!pip install langchain langchain-community langchain-core
!pip install openai

import os
os.environ["OPENAI_API_TOKEN"]="<API_KEY>"

from langchain.llms import OpenAI
llm = OpenAI(model_name = "text-davinci-003")

query = "What is the capital of UK?"
answer = llm(query)
print(answer)
```

#### Sample code 3 (VertexAI):
```
from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain
template = """Question: {question}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm = VertexAI()
llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)
question = "Who won noble price in 1980?"
llm_chain.run(question)

```
