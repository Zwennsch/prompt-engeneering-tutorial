import openai

client = openai.OpenAI()

messages = [{'role' : 'system', 'content' :'You are a helpful grandmother'}]

while True:
    user_text = input('Ian: ')

    messages.append({'role': 'user', 'content': user_text})

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0.5,
        max_tokens=1024
    )

    granny_response = response.choices[0].message.content
    print(f'\nGranny: {granny_response}\n')
    messages.append({'role': 'assistant', 'content': granny_response})