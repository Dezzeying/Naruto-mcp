"""
Naruto RPG Simülasyon Motoru

AI Prompt Builder

RPG hikaye anlatımı prompt sistemi.
"""


from __future__ import annotations

from typing import Any




class PromptBuilder:


    def __init__(
        self,
        context_manager,
        naruto_lore
    ):

        self.context_manager = context_manager
        self.naruto_lore = naruto_lore





    def get_system_message(
        self
    ) -> str:


        return """

Sen Naruto evreninde geçen bir RPG hikaye anlatıcısısın.


GÖREVİN:

Oyuncunun yaptığı hareketin ardından
dünyada oluşan gelişmeleri anlatmak.


ANLATIM TARZI:

- Üçüncü şahıs anlatımı kullan.
- Roman sahnesi gibi yaz.
- Kısa ve atmosferik anlat.
- Sadece görülebilen olayları yaz.


KAMERA KURALI:

Sen bir kameraman gibisin.

Kamera:

- ortamı görür,
- NPC'leri görür,
- olayları görür,
- sesleri ve hareketleri aktarır.


Kamera şunları yapmaz:

- Oyuncunun zihnine girmez.
- Oyuncunun kararını vermez.
- Oyuncunun yerine hareket etmez.


OYUNCU KARAKTERİ:

Oyuncunun karakteri Ajisai Hatake'tir.

Ajisai'nin kontrolü oyuncudadır.


ASLA YAZMA:

- Ajisai'nin düşünceleri.
- Ajisai'nin duyguları.
- Ajisai'nin konuşmaları.
- Ajisai'nin yapmadığı hareketler.
- Ajisai'nin teknik kullanımları.


YAZABİLİRSİN:

- NPC hareketleri.
- NPC konuşmaları.
- Çevre değişimleri.
- Dünyanın tepkileri.
- Diğer shinobilerin davranışları.


DÜNYA KURALLARI:

- Naruto evrenine sadık kal.
- Genin seviyesini aşırı güçlendirme.
- Sebepsiz büyük olay oluşturma.
- NPC'ler kendi amaçlarıyla hareket eder.


ASLA YAZMA:

"Oyuncu karakteri"
"Bu eylemin sonucu"
"Kurallar gereği"
"Seçenekler"
"Ne yapmak istiyorsun?"


SADECE HİKAYE YAZ.


"""






    def build_story_prompt(
        self,
        player_state: dict[str, Any],
        location: str,
        current_situation: str
    ):


        system_message = self.get_system_message()



        lore = self.naruto_lore.get_lore_context(
            location
        )



        memory = self.context_manager.get_context_for_prompt(
            1000
        )



        npc_text = ""



        for name, data in self.context_manager.npc_states.items():

            npc_text += (
                f"{name}: {data}\n"
            )



        if not npc_text:

            npc_text = "Yakında kayıtlı NPC bilgisi yok."






        user_prompt = f"""


SAHNE:

Konum:

{location}


Zaman:

Sabah



DÜNYA BİLGİSİ:

{lore}



NPC DURUMLARI:

{npc_text}



GEÇMİŞ OLAYLAR:

{memory}



OYUNCUNUN GİRDİĞİ EYLEM:

{current_situation}



Bu hareketten sonra çevrede meydana gelen olayları anlat.


Hatırla:

Oyuncunun karakterini yönetme.

Sadece dünyanın ve NPC'lerin tepkisini göster.


ÇIKTI:

Sadece hikaye metni.


"""



        return (
            system_message,
            user_prompt
        )