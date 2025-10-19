from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Simple DreamVille Core test
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are DreamVille Core, an AI systems assistant."},
        {"role": "user", "content": "System check: confirm DreamVille Core is online and operational."}
    ]
)

print(response.choices[0].message.content)
