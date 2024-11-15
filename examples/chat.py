"""A simple CLI chatbot"""

import minillm as ml

prompt = f"System: Reply as a helpful assistant. Currently {ml.get_date()}."

while True:
    user_message = input("\nUser: ")

    prompt += f"\n\nUser: {user_message}"

    print(prompt)

    prompt += "\n\nAssistant:"

    response = ml.chat(prompt)
    print(f"\nAssistant: {response}")

    prompt += f" {response}"
