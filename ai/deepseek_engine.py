"""
Naruto RPG Simülasyon Motoru

Local Ollama AI Engine
"""


import requests





class DeepSeekEngine:


    def __init__(self):

        self.url = (
            "http://localhost:11434/api/generate"
        )

        self.model = (
            "deepseek-coder-v2:16b-lite-instruct-q4_K_M"
        )





    def generate(
        self,
        system,
        prompt
    ):


        full_prompt = f"""

{system}


KULLANICI İSTEĞİ:

{prompt}


SADECE HİKAYE YAZ.

"""



        try:


            response = requests.post(

                self.url,

                json={

                    "model": self.model,

                    "prompt": full_prompt,

                    "stream": False,

                    "options": {

                        "temperature": 0.65,

                        "top_p": 0.9,

                        "repeat_penalty": 1.15

                    }

                },

                timeout=180

            )



            if response.status_code != 200:

                return (
                    "Ollama bağlantı hatası: "
                    + response.text
                )



            data = response.json()



            return data.get(
                "response",
                ""
            )



        except Exception as e:


            return (
                f"Ollama AI hatası: {e}"
            )