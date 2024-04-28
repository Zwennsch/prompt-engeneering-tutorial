import openai


client = openai.OpenAI()

with open('./code.py', 'r') as file:
    code_content = file.read()

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': 'You are a code review assistant. Provide detailed suggestions to improve given Python code.',

        },
        {
            'role': 'user',
            'content': code_content
        }
    ],
    temperature=0.5,
    max_tokens=1024
)

print(response)
print()
print(response.choices[0].message.content)
