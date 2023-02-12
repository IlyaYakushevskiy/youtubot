import os
import openai

with open('./prompts/Prompt_amiass.txt', 'r', encoding = "UTF-8") as f:
    prompt = f.read()


openai.api_key = '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'

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

def filewriter(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()
    return print("txt written")
    

    

#get the output's last sentence/name of output and throw it into the movie_render_AI.py

if __name__ == "__main__":
    inp = input("input topic: ")
    print(get_transript(inp))