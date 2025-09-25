import os
from openai import OpenAI

# Load OpenAI API key from environment variable
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("⚠ Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)


def run_ocr(file_path: str) -> str:
    """
    Extract text from an uploaded document/image using OpenAI OCR (GPT-4o-mini).
    """
    with open(file_path, "rb") as f:
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # OCR + vision model
            messages=[
                {"role": "user", "content": "Extract all readable text from this image/document."}
            ],
            files={"image": f}  # send file directly
        )

    return response.choices[0].message.content.strip()
