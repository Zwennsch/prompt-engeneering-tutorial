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

print(response)
print()
print(response.choices[0].message.content)

# looking at the response.finish_reason:
# "stop" means the assistant could answer without reaching the max_tokens, "length" means, it got till all the all tokens were used