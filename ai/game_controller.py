"""
Naruto RPG Simülasyon Motoru

Game Controller

AI, hafıza ve doğrulama sistemlerini bağlayan ana katman.
"""


class GameController:


    def __init__(
        self,
        memory,
        prompt_builder,
        deepseek_engine,
        response_parser=None,
        validator=None
    ):

        self.memory = memory

        self.prompt_builder = prompt_builder

        self.deepseek = deepseek_engine

        self.parser = response_parser

        self.validator = validator

        self.max_retries = 3





    def process_action(
        self,
        player,
        location,
        action
    ):


        system, prompt = (
            self.prompt_builder.build_story_prompt(
                player,
                location,
                action
            )
        )



        response = None

        last_error = ""




        for attempt in range(
            self.max_retries
        ):


            # İlk deneme normal

            if attempt == 0:

                current_prompt = prompt



            else:


                current_prompt = f"""

ÖNCEKİ CEVAP HATALIYDI.

HATA:

{last_error}


YENİ KURAL:

Sadece çevreyi ve NPC davranışlarını anlat.

Oyuncu karakterinin:

- hareketlerini
- düşüncelerini
- konuşmalarını
- kararlarını

yazma.


Önceki sahne:

{action}


Yeni cevap sadece hikaye olsun.

"""




            response = self.deepseek.generate(

                system,

                current_prompt

            )



            # Parser

            if self.parser:


                try:

                    parsed = self.parser.parse(
                        response
                    )


                    if isinstance(
                        parsed,
                        dict
                    ):

                        response = parsed.get(
                            "narrative",
                            response
                        )


                except Exception:

                    pass




            # Validator yoksa direkt geç

            if not self.validator:

                break




            valid, cleaned, reason = (
                self.validator.validate(
                    response
                )
            )



            if valid:

                response = cleaned
                break



            last_error = reason





        # Eğer hiçbir deneme geçmezse

        if self.validator:


            valid, cleaned, reason = (
                self.validator.validate(
                    response
                )
            )


            if valid:

                response = cleaned


            else:

                response = (
                    "Çevredeki hareketlilik "
                    "devam ederken dünya kendi "
                    "akışı içinde ilerlemeyi "
                    "sürdürdü."
                )






        self.memory.add_event(

            "story_event",

            response,

            7,

            [],

            [
                location
            ]

        )



        return response






    def handle_battle(
        self,
        attacker,
        defender,
        combat_engine=None
    ):


        if combat_engine:

            return combat_engine.calculate(
                attacker,
                defender
            )


        return {
            "result":
            "combat_engine_missing"
        }






    def get_npc_response(
        self,
        npc,
        player_action,
        npc_engine=None
    ):


        if npc_engine:

            return npc_engine.respond(
                npc,
                player_action
            )


        return {

            "npc": npc,

            "response":
            "NPC sistemi bağlı değil."

        }






    def generate_clan_event(
        self,
        clan_name,
        clan_engine=None
    ):


        if clan_engine:

            return clan_engine.generate_event(
                clan_name
            )


        return {

            "clan": clan_name,

            "event":
            "Klan sistemi bağlı değil."

        }






    def create_mission(
        self,
        rank,
        location,
        mission_engine=None
    ):


        if mission_engine:

            return mission_engine.create_mission(
                rank,
                location
            )


        return {

            "mission":
            "Görev sistemi bağlı değil."

        }






    def update_world(
        self,
        event
    ):


        return {

            "world_updated":
            True,

            "event":
            event

        }






    def get_memory_context(
        self
    ):


        return self.memory.get_context_for_prompt()