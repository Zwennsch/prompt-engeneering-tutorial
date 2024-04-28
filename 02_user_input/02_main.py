import openai

user_text = input("What can I help you with today?")

client = openai.OpenAI()

# max_tokens is always the 'completion_tokens' meaning the number used for the answer
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role" : "system", "content": "You are a specialist in Computer Science"},
        {"role": "user", "content": user_text}
        ],
    temperature=0.5,
    max_tokens=1024
)
# Example for inout: Is java a good language?
print(response)
# Output:
'''
ChatCompletion(id='chatcmpl-9IBR19KuY2wvA7BGIyXC77IEjhlGI', choices=[Choice(finish_reason='stop', index=0, logprobs=None, 
message=ChatCompletionMessage(content="Yes, Java is a widely used and versatile programming language that is known for its platform independence, strong community support, and extensive libraries and frameworks. 
It is commonly used for developing web applications, mobile apps, enterprise software, and more. Java's object-oriented nature, robust security features, and scalability make it a popular choice for many software development projects.", 
role='assistant', function_call=None, tool_calls=None))], created=1714120887, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3b956da36b', 
usage=CompletionUsage(completion_tokens=70, prompt_tokens=24, total_tokens=94))
'''
print()
print(response.choices[0].message.content)

# looking at the response.finish_reason:
# "stop" means the assistant could answer without reaching the max_tokens, "length" means, it got till all the all tokens were used