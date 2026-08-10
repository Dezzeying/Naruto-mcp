"""
Naruto RPG Simülasyon Motoru

Response Parser

AI çıktısını temizler ve standart hale getirir.
"""


import re





class ResponseParser:



    def __init__(self):

        self.remove_patterns = [

            r"^Açıklama:.*$",

            r"^Analiz:.*$",

            r"^Sonuç:.*$",

            r"^Seçenekler:.*$",

            r"^Öneriler:.*$",

        ]





    def parse(
        self,
        response: str
    ):


        if not response:

            return {
                "narrative": ""
            }



        text = response.strip()



        # Markdown temizliği

        text = text.replace(
            "**",
            ""
        )


        text = text.replace(
            "```",
            ""
        )



        lines = text.split(
            "\n"
        )


        cleaned = []



        for line in lines:


            line = line.strip()


            if not line:

                continue



            skip = False


            for pattern in self.remove_patterns:


                if re.match(
                    pattern,
                    line,
                    re.IGNORECASE
                ):

                    skip = True
                    break



            if not skip:

                cleaned.append(
                    line
                )



        narrative = "\n".join(
            cleaned
        ).strip()



        # AI bazen kendini anlatıyor

        forbidden_meta = [

            "oyuncu karakteri",

            "bu sahnede",

            "bu eylemin sonucu",

            "kurallar gereği",

            "seçenekler"

        ]



        for word in forbidden_meta:

            narrative = narrative.replace(
                word,
                ""
            )



        return {

            "narrative":
            narrative

        }