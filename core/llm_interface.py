"""
LLM Interface

Local büyük dil modelleri ile iletişim katmanı.

Desteklenen sistemler:
- OpenAI compatible API
- Ollama
- llama.cpp server
- text-generation-webui
- CLI tabanlı local modeller

Bu sınıf oyun motorunun AI ile tek iletişim noktasıdır.
"""


from __future__ import annotations

import json
import subprocess
from typing import Any

import requests


class LLMInterface:
    """
    Local DeepSeek veya başka bir LLM modeli ile iletişim sağlar.

    Oyun motoru bu sınıf üzerinden:
    - hikaye üretimi
    - NPC konuşmaları
    - savaş anlatımı
    - dünya simülasyonu

    işlemlerini yapar.
    """

    def __init__(
        self,
        model_path: str,
        api_base: str = "http://localhost:8000",
    ) -> None:
        """
        Args:
            model_path:
                Kullanılan model adı veya dosya yolu.

            api_base:
                Local LLM API adresi.
        """

        self.model_path = model_path
        self.api_base = api_base.rstrip("/")

        self.chat_endpoint = (
            f"{self.api_base}/v1/chat/completions"
        )

        self.models_endpoint = (
            f"{self.api_base}/v1/models"
        )


    def generate(
        self,
        prompt: str,
        system_message: str,
        temperature: float = 0.7,
        max_tokens: int = 1000,
    ) -> str:
        """
        LLM'e normal metin isteği gönderir.

        Öncelik:
        1. OpenAI uyumlu API
        2. CLI fallback

        Returns:
            Ham model cevabı
        """

        try:
            return self._api_generate(
                prompt,
                system_message,
                temperature,
                max_tokens,
            )

        except Exception:

            return self._cli_generate(
                prompt
            )


    def _api_generate(
        self,
        prompt: str,
        system_message: str,
        temperature: float,
        max_tokens: int,
    ) -> str:
        """
        OpenAI uyumlu API çağrısı yapar.
        """

        payload: dict[str, Any] = {

            "model":
                self.model_path,

            "messages":
            [
                {
                    "role":
                    "system",

                    "content":
                    system_message,
                },

                {
                    "role":
                    "user",

                    "content":
                    prompt,
                }
            ],

            "temperature":
                temperature,

            "max_tokens":
                max_tokens,
        }


        response = requests.post(
            self.chat_endpoint,
            json=payload,
            timeout=120,
        )


        response.raise_for_status()


        data = response.json()


        return (
            data["choices"][0]
            ["message"]
            ["content"]
        )



    def generate_structured(
        self,
        prompt: str,
        system_message: str,
        output_schema: dict[str, Any],
    ) -> dict[str, Any]:
        """
        JSON formatında cevap ister.

        AI bazen hatalı JSON döndürebileceği için
        temizleme işlemi yapar.
        """

        schema_prompt = f"""

Sadece JSON formatında cevap ver.

Beklenen format:

{json.dumps(
    output_schema,
    indent=2,
    ensure_ascii=False
)}

"""

        raw = self.generate(
            prompt + schema_prompt,
            system_message,
            temperature=0.4,
        )


        return self._extract_json(
            raw
        )



    def ping(
        self
    ) -> bool:
        """
        LLM servisinin çalışıp çalışmadığını kontrol eder.
        """

        try:

            response = requests.get(
                self.api_base,
                timeout=5,
            )

            return response.status_code < 500


        except Exception:

            return False



    def get_model_info(
        self
    ) -> dict[str, Any]:
        """
        Model bilgilerini döndürür.
        """

        try:

            response = requests.get(
                self.models_endpoint,
                timeout=10,
            )

            response.raise_for_status()


            return response.json()


        except Exception:

            return {

                "model":
                self.model_path,

                "status":
                "unknown",

                "api":
                self.api_base,
            }



    def _cli_generate(
        self,
        prompt: str,
    ) -> str:
        """
        API yoksa CLI üzerinden model çalıştırır.

        Örnek:
        deepseek-cli "prompt"
        """

        try:

            result = subprocess.run(

                [
                    "deepseek-cli",
                    prompt
                ],

                capture_output=True,

                text=True,

                timeout=120,
            )


            return result.stdout



        except Exception as error:

            return json.dumps(
                {
                    "error":
                    str(error)
                }
            )



    def _extract_json(
        self,
        text: str,
    ) -> dict[str, Any]:
        """
        Model çıktısından JSON ayıklar.

        Destek:
        - direkt JSON
        - ```json blokları
        """

        cleaned = text.strip()


        if "```json" in cleaned:

            cleaned = (
                cleaned
                .replace(
                    "```json",
                    ""
                )
                .replace(
                    "```",
                    ""
                )
                .strip()
            )


        try:

            return json.loads(
                cleaned
            )


        except json.JSONDecodeError:


            start = cleaned.find("{")

            end = cleaned.rfind("}")


            if (
                start != -1
                and end != -1
            ):

                try:

                    return json.loads(
                        cleaned[start:end + 1]
                    )

                except json.JSONDecodeError:

                    pass


        return {

            "error":
            "invalid_json",

            "raw":
            text,

        }