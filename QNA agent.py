import ollama

with open('data.txt','r') as file:
    data=file.read()

print(data)

prompt_01=f"{data}### from this text extract 3 inetersting facts"
print("<agent-01>prompt:"+prompt_01)
print()

print("<agent-01> generating a response.....")
print()

response1 = ollama.chat(
    model='llama3',
    messages=[
        {
            "role": "user",
            "content": prompt_01
        }
    ]
)


print("<agent-01> reponse:"+response1.message['content'])

prompt_02=f"{response1.message['content']}### Explain this to end user in a simple , clear and engaging way, Be concise. Change paragraph and end with Feel free to ask if you want to know in details or about something else."
print("<agent-02>prompt:"+prompt_02)
print()

print("<agent-02> Simplifying the response for you , please sit tight.....")
print()

response2 = ollama.chat(
    model='llama3',
    messages=[
        {
            "role": "user",
            "content": prompt_02
        }
    ]
)


print("<agent-02> reponse:"+response2.message['content'])