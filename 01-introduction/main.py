from openai import OpenAI

client = OpenAI()

"""

Request Data

model
- ID of model to use.
- https://platform.openai.com/docs/models
- https://openai.com/pricing

messages
- A list of messages comprising the conversation so far.
- consists of an array of message object
    - each message object has a role ("system", "user" or "assistant") and a content
    - Typically, a conversation is formatted with a system message first, followed by alternating user and assistant messages. -> system, user, assistant, user, assistant, u.....
    - The system message helps set the behavior of the assistant. For example, you can modify the personality of the assistant or provide specific instructions about how it should behave throughout the conversation. 
    - However note that the system message is optional and the model’s behavior without a system message is likely to be similar to using a generic message such as "You are a helpful assistant."
    - The user messages provide requests or comments for the assistant to respond to.
    - Assistant messages store previous assistant responses, but can also be written by you to give examples of desired behavior.


temperature
- What sampling temperature to use, between 0 and 2.
- Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and 
  deterministic.

max_tokens
- The maximum number of tokens to generate in the chat completion.
- most 4 letter words are one token
"""

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Which NHL team plays in Pittsburgh?'},
    ],
    temperature=0.5,
    max_tokens=1024
)

"""
Response data: chat completion object

https://platform.openai.com/docs/api-reference/chat/object

{
  "id": "chatcmpl-7sz349tSCvgxedXZSHbl7XSt6Eein",
  "object": "chat.completion",
  "created": 1693338738,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The NHL team that plays in Pittsburgh is the Pittsburgh Penguins."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 24,
    "completion_tokens": 12,
    "total_tokens": 36
  }
}
"""


print(response.choices[0].message.content)
print(response.usage.completion_tokens)