import os
import openai
import keys

with open('Prompt_amiass.txt', 'r') as f:
    prompt = f.read()

openai.api_key = keys.OPENAI_API_KEY

def get_transript(topic):

    topic = prompt + topic

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= topic,
        temperature=0.93,
        max_tokens=1210,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["Customer:", " AI:"]
        )
    return(response.choices[0].text)

if __name__ == "__main__":
    topic = input("input topic: ")
    print(get_transript(topic))
