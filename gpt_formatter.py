
import openai

def format_menu_with_gpt(ocr_text, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or use "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You format OCR menu text into structured menu data."},
            {"role": "user", "content": f"Convert the following OCR text into JSON menu format:\n\n{ocr_text}"}
        ]
    )
    return eval(response['choices'][0]['message']['content'])  # Assuming GPT returns JSON-compatible dict
