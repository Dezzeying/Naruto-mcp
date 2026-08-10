"""
Naruto RPG Simülasyon Motoru

AI Response Validator

AI çıktısında oyuncu karakterinin kontrol edilmesini engeller.
"""


import re
from typing import Tuple, Optional




class ResponseValidator:


    def __init__(
        self,
        player_name: str = "Ajisai"
    ):

        self.player_name = player_name



        self.forbidden_patterns = [

            # Ajisai aktif hareket ediyor
            rf"{player_name}(?: Hatake)?[, ]+.*"
            r"(yürü|ilerle|koş|gitti|geldi|yaklaştı|uzaklaştı|"
            r"çıktı|girdi|oturdu|kalktı|döndü|"
            r"başladı|devam etti|hazırlandı)",



            # Ajisai bir şey yapıyor
            rf"{player_name}(?: Hatake)?[, ]+.*"
            r"(çıkardı|aldı|tuttu|çekti|vurdu|kesti|"
            r"fırlattı|açtı|kapattı|kullandı|uyguladı)",



            # Ajisai düşünce / duygu
            rf"{player_name}(?: Hatake)?[, ]+.*"
            r"(düşündü|hissetti|karar verdi|"
            r"anladı|fark etti|hatırladı|"
            r"korktu|sevindi|gülümsedi|şaşırdı)",



            # Ajisai konuşuyor
            rf"{player_name}(?: Hatake)?[, ]+.*"
            r"(dedi|söyledi|cevap verdi|"
            r"sordu|bağırdı|fısıldadı|mırıldandı)",



            # Ajisai teknik kullanıyor
            rf"{player_name}(?: Hatake)?[, ]+.*"
            r"(chakra|jutsu|Gekisen|Ikazuchi|teknik)"
            r".*(kullandı|aktif etti|oluşturdu)",



            # Ajisai'nin hareketi / eşyası
            rf"{player_name}(?:'nin|'nın|'nun|'nün)"
            r".*(hareket|adım|kılıç|tantō|chakra|"
            r"tekniği).*"
            r"(etti|oldu|başladı|kullandı)"

        ]




        self.forbidden_phrases = [

            "Bu senaryoda",

            "Oyuncu olarak",

            "Ne yapmak istiyorsun",

            "Ne yapacaksın",

            "Kararın ne",

            "Seçenekler:",

            "Seçenekler",

        ]






    def validate(
        self,
        response: str
    ) -> Tuple[bool, str, Optional[str]]:



        if not response:

            return False, "", "Boş cevap"




        text = response.strip()



        if len(text.split()) < 8:

            return False, "", "Cevap çok kısa"





        for index, pattern in enumerate(
            self.forbidden_patterns
        ):

            if re.search(
                pattern,
                text,
                re.IGNORECASE
            ):

                return (
                    False,
                    "",
                    f"Oyuncu kontrolü bulundu ({index})"
                )





        for phrase in self.forbidden_phrases:

            if phrase.lower() in text.lower():

                return (
                    False,
                    "",
                    f"Yasak ifade: {phrase}"
                )





        return True, text, None








    def is_recoverable(
        self,
        response: str
    ) -> bool:



        sentences = re.split(
            r'(?<=[.!?])\s+',
            response
        )


        good = 0

        bad = 0



        for sentence in sentences:


            result, _, _ = self.validate(
                sentence
            )


            if result:

                good += 1

            else:

                bad += 1




        if good + bad == 0:

            return False



        return (
            good / (good + bad)
        ) >= 0.5








    def recover(
        self,
        response: str
    ) -> str:



        sentences = re.split(
            r'(?<=[.!?])\s+',
            response
        )


        clean = []



        for sentence in sentences:


            valid, _, _ = self.validate(
                sentence
            )


            if valid:

                clean.append(
                    sentence.strip()
                )




        return " ".join(
            clean
        )
