# LLM_code
Sample GenAI code to learn langchain.  
Note: Please use your own API Keys. Keys are used in the code are already removed.

#### Sample code 1 (HuggingFace):
```
!pip install langchain
!pip install huggingface_hub

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"]="<API_KEY>"

from langchain.llms import HuggingFaceHub
llm = HuggingFaceHub(repo_id = "google/flan-t5-large")

query = "What is the capital of UK?"
answer = llm(query)
print(answer)
```

#### Sample code 2 (OpenAI):
```
!pip install langchain
!pip install openai

import os
os.environ["OPENAI_API_TOKEN"]="<API_KEY>"

from langchain.llms import OpenAI
llm = OpenAI(model_name = "text-davinci-003")

query = "What is the capital of UK?"
answer = llm(query)
print(answer)
```
