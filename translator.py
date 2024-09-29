
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


if openai.api_key is None:
    raise ValueError("OpenAI API key not found. Please set it in the .env file.")

english_text = "Hello, how are you?"

#english_text = input("Enter the English text to translate: ")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f'Translate the following English text to Persian: "{english_text}"'
            }
        ]
    )

    # Step 4: Extract and print the Persian translation
    persian_translation = response['choices'][0]['message']['content'].strip()
    print("Persian Translation:")
    print(persian_translation)

except Exception as e:
    print(f"An error occurred: {e}")

