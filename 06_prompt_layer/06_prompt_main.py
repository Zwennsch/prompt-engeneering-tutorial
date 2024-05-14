from promptlayer import PromptLayer
import os
promptlayer_client = PromptLayer(api_key=os.environ.get("PROMPTLAYER_API_KEY"))

# Swap out your 'from openai import OpenAI'
OpenAI = promptlayer_client.openai.OpenAI
client = OpenAI()

# Do something fun
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system", "content": "You are an AI."
        },
        {
            "role":"user", "content":"Compose a poem please-"
        }
    ],
    pl_tags = ["getting-started"]

)
