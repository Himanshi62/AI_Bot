import ast
from openai import OpenAI
from decouple import config
client = OpenAI(
    api_key= config("openai_api_key")
)

def SupportWithChatCompletion(query):
    print("generating AI Description...")
    sys_prompt = "You are support bot"
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=4000,
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": query }
    ]

)

    print("LLM response received successfully")
    message = completion.choices[0].message
    result = message.content

    return result


