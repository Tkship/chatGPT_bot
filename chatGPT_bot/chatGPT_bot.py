import openai
openai.api_key = f'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'

while True:  
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "can not use"},
            {"role": "assistant", "content": "You are a helpful assistant."},
            {"role": "user", "content": input("You: ")}
        ]
    )
    print(f"============================")
    print(completion)
    print(f"============================")
    print(completion.choices[0].message.content)



