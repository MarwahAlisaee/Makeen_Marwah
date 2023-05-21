import openai

# Set up your OpenAI API credentials
openai.api_key = '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'


def send_message(message):
    response = openai.Completion.create(
        engine='text-davinci-003',  
        prompt=message,
        max_tokens=50,  
        temperature=0.7, 
        n=1, 
        stop=None,  
    )
    return response.choices[0].text.strip()

# Bot loop
while True:
    user_input = input("User: ")
    bot_response = send_message(user_input)
    print("Bot:", bot_response)
