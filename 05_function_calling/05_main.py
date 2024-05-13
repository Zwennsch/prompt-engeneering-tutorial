import openai
import json

client = openai.OpenAI()

# This is just dummy information but you could use a real world API instead as well
def get_current_weather(location, unit="celsius"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "24",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)


def run():
    # Step 1: specify any available functions that the model can use
    # https://platform.openai.com/docs/api-reference/chat/create#functions
    functions = [
        {
            "name": "get_current_weather",
            "description": "get the current weather in a given location",
            # The paramters the function accepts, described as a JSON Schema object
            # https://json-schema.org/understanding-json-schema/
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["location"],
            },
        }
    ]

    # Step 2: send the conversation and available functions to GPT:
    messages = [
        {"role": "user", "content": "What is the weather like in Boston?"}]
    first_response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto"  # Though "auto" is default...
    )

    print(first_response)
    print()

    # first_response_message = first_response["choices"][0]["message"]
    first_response_message = first_response.choices[0].message
    print(first_response_message)
    print()

    # Step 3: check if GPT wanted to call a function
    # https://platform.openai.com/docs/api-reference/chat/create#messages-function_call
    if first_response_message.function_call:
        # Step 4: call the function
        # only one function in this example,but you can have multiple
        available_functions = {
            "get_current_weather": get_current_weather,
        }
        function_name = first_response_message["function_call"]["name"]
        # {'location': 'Boston, MA'}
        function_args = json.loads(
            first_response_message["function_call"]["arguments"])
        function_to_call = available_functions[function_name]
        function_return_value = function_to_call(
            location=function_args.get("location"),
            unit=function_args.get("unit"),
        )
    # Step 5: send the details about the function call and return value back to GPT

    # extend conversation with assistant's reply
    messages.append(first_response)

    # extend conversation with function response
    messages.append(
        {
            "role": "function",
            "name": function_name,
            "content": function_return_value,
        }
    )

    # get a new response from GPT where it can see the function response
    second_response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
    )

    print(second_response)
    print()
    print(second_response.choices[0].message.content)


if __name__ == "__main__":
    run()
