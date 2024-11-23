import ollama

response = ollama.chat(
    model='llama3',
    messages=[
        {
            "role": "user",
            "content": "I want to know about the constitution of India"
        }
    ]
)


print(response.message['content'])
