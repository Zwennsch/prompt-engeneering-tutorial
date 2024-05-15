from promptlayer import PromptLayer
import os
promptlayer_client = PromptLayer(api_key=os.environ.get("PROMPTLAYER_API_KEY"))


# Instead of `import openai` we will use
OpenAI = promptlayer_client.openai.OpenAI
openai = OpenAI()

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {'role':'system', 'content':'You are a helpful assistant.'},
        {'role':'user', 'content':'Who was the first chancellor of Germany?'}
    ],
    temperature=0.5,
    max_tokens=64,
    pl_tags=['German chancellor']
)

print(response)