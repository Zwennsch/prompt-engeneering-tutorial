import os
from promptlayer import PromptLayer
promptlayer_client = PromptLayer(api_key=os.environ.get("PROMPTLAYER_API_KEY"))
OpenAI = promptlayer_client.openai.OpenAI

client = OpenAI()

"""
All promptlayer requests have unique IDs, and these can be optionally returned when logging
the request. Using Promptlayer (and the request ID) we can score a request with an integer
between 0 and 100. This is most often used to understand how effective certain prompts are
 in production

We can test prompts and manually score the answers (100 for 'this is exactly what I wanted and 
0 for 'this doesn't help at all')
"""
response, pl_request_id = client.chat.completions.create(
    model='gpt-3.5-turbo-1106',
    messages=[{'role': 'user', 'content': 'What is the capital of Germany?'}],
    max_tokens=64,
    pl_tags=['scoring_example'],
    return_pl_id=True
)

print(response)
print()
print(pl_request_id)
print()

answer = response.choices[0].message.content
print(answer)
correct_answer = 'berlin' in answer.lower()

# Log the score to Promptlayer
promptlayer_client.track.score(
    request_id=pl_request_id,
    score_name="capital_of_germany",
    score=100 if correct_answer else 0,
)
