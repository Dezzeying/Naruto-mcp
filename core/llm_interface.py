"""
Naruto RPG Simülasyon Motoru

LLM Interface

Local DeepSeek modelleri ile iletişim katmanı.
"""


from __future__ import annotations

import json
import subprocess
from typing import Any

import requests



class LLMInterface:
    """
    Local LLM bağlantı yöneticisi.

    Destek:
    - OpenAI uyumlu API
    - Ollama
    - llama.cpp server
    - text-generation-webui
    - CLI modeller
    """


    def __init__(
        self,
        model_path: str,
        api_base: str = "http://localhost:8000"
    ) -> None:

        self.model_path = model_path

        self.api_base = api_base.rstrip("/")

        self.model_name = "DeepSeek"



    def generate(
        self,
        prompt: str,
        system_message: str,
        temperature: float = 0.7,
        max_tokens: int = 2048
    ) -> str:
        """
        LLM'den ham cevap alır.
        """

        # Önce API dene

        try:

            response = requests.post(
                f"{self.api_base}/v1/chat/completions",
                json={
                    "model": self.model_name,

                    "messages":
                    [
                        {
                            "role": "system",
                            "content": system_message
                        },

                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],

                    "temperature": temperature,

                    "max_tokens": max_tokens
                },

                timeout=120
            )


            response.raise_for_status()


            data = response.json()


            return (
                data
                .get("choices", [{}])[0]
                .get("message", {})
                .get("content", "")
            )


        except Exception:

            pass



        # API yoksa CLI dene

        return self._generate_cli(
            prompt,
            system_message
        )



    def generate_structured(
        self,
        prompt: str,
        system_message: str,
        output_schema: dict[str, Any]
    ) -> dict[str, Any]:
        """
        JSON formatında cevap üretir.
        """


        schema_text = json.dumps(
            output_schema,
            ensure_ascii=False,
            indent=2
        )


        enhanced_prompt = f"""
Sadece geçerli JSON döndür.

Bu şemaya uy:

{schema_text}


İstek:

{prompt}
"""


        raw = self.generate(
            enhanced_prompt,
            system_message,
            temperature=0.4
        )


        return self._parse_json(
            raw
        )



    def ping(self) -> bool:
        """
        LLM server aktif mi kontrol eder.
        """


        try:

            response = requests.get(
                f"{self.api_base}/v1/models",
                timeout=5
            )


            return response.status_code == 200


        except Exception:

            return False



    def get_model_info(self) -> dict[str, Any]:
        """
        Model bilgisi getirir.
        """


        try:

            response = requests.get(
                f"{self.api_base}/v1/models",
                timeout=10
            )


            return response.json()


        except Exception:


            return {

                "model":
                self.model_name,

                "status":
                "offline",

                "api":
                self.api_base
            }



    def _generate_cli(
        self,
        prompt: str,
        system_message: str
    ) -> str:
        """
        DeepSeek CLI desteği.
        """


        try:

            result = subprocess.run(

                [
                    self.model_path,

                    "--system",
                    system_message,

                    "--prompt",
                    prompt

                ],

                capture_output=True,

                text=True,

                timeout=120
            )


            return result.stdout


        except Exception as error:


            return json.dumps(
                {
                    "error":
                    str(error)
                }
            )



    def _parse_json(
        self,
        text: str
    ) -> dict[str, Any]:
        """
        Bozuk JSON cevaplarını temizler.
        """


        text = text.strip()


        if "```json" in text:

            text = (
                text
                .replace("```json", "")
                .replace("```", "")
            )


        try:

            return json.loads(
                text
            )


        except json.JSONDecodeError:


            start = text.find("{")

            end = text.rfind("}")


            if start != -1 and end != -1:

                try:

                    return json.loads(
                        text[start:end + 1]
                    )


                except Exception:

                    pass



        return {

            "error":
            "JSON parse edilemedi",

            "raw":
            text

        }