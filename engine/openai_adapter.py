import json

from openai import OpenAI

from .config import MODEL
from .config import OPENAI_API_KEY


class OpenAIAdapter:

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    def ask(self, prompt: str):

        response = self.client.responses.create(

            model=MODEL,

            input=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "Return ONLY valid JSON."
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )

        text = response.output_text.strip()

        return json.loads(text)