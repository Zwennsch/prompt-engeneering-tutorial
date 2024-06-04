import os
from promptlayer import PromptLayer
promptlayer_client = PromptLayer(api_key=os.environ.get("PROMPTLAYER_API_KEY"))
OpenAI = promptlayer_client.openai.OpenAI

client = OpenAI()

"""
Prompt templates are customizable prompt strings with placeholders for variables.
"""

# This brings in the entire dictionary, the latest version of it.
programming_framework = promptlayer_client.templates.get("programming w framework")
# for key, value in programming_framework.items():
#     print(key, value)



# You can optionally pass a version to get an older version of prompt.
# By default the newest version of a prompt is returned.
# My name of the template is 'programming w framework'
# You can set a specific version of your template to use if you want to:
    # programming_framework = promptlayer.prompts.get('programming w framework', version=1)

variables = {
    'language' : 'Dart',
    'framework' : 'Flutter'
}

# You need to go inside the programming w framework - dictionary and pull out the actual template
# you actually have multiple template if you use multiple different roles
# ['messages'][0] is always the 'system' role
# the template keyword is actually returning the string with the {} syntax we set in promptlayer

programming_framework_template = programming_framework['prompt_template']['messages'][0]['content'][0]['text']
print(programming_framework_template)
# # now that we have the template we format that by putting the variables into it:

content = programming_framework_template.format(**variables)
print(content)

# This return a tuple with two things:
# the first object is the response object from our chat completion call
# the second object is the pl_request_id from promptlayer
# like this: ({....}, 12345)
response, pl_request_id = client.chat.completions.create(
    model='gpt-3.5-turbo-1106',
    messages=[
        {'role': 'system', 'content': content},
        {'role': 'user', 'content': 'What is the best way to create a mobile app?'}
    ],
    return_pl_id=True
)

answer = response.choices[0].message.content
print(answer)

promptlayer_client.track.prompt(request_id=pl_request_id,
    prompt_name='programming w framework', prompt_input_variables=variables)


promptlayer_client.track.metadata(
  request_id=pl_request_id,
  metadata={
      "user":"Hans",
      "post_id": "2sadfjö"
  }
)


