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



