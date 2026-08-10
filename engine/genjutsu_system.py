class GenjutsuSystem:



    def __init__(
        self,
        npc_engine
    ):


        self.npc_engine = npc_engine




        self.genjutsu_database = {



            "Basic Genjutsu":
            {

                "Rank":
                "D",


                "Power":
                20,


                "Effect":
                "Illusion"

            },






            "Sharingan Genjutsu":
            {

                "Rank":
                "B",


                "Power":
                70,


                "Effect":
                "Mind Control",


                "Clan":
                "Uchiha"

            },







            "Tsukuyomi":
            {

                "Rank":
                "S",


                "Power":
                150,


                "Effect":
                "Time Distortion",


                "Clan":
                "Uchiha",


                "Requirement":
                "Mangekyo Sharingan"

            },







            "Demonic Illusion":
            {

                "Rank":
                "B",


                "Power":
                80,


                "Effect":
                "Fear Manipulation"

            }

        }







    def get_genjutsu(
        self,
        name
    ):


        return self.genjutsu_database.get(
            name
        )









    def get_resistance(
        self,
        npc
    ):


        resistance = 0



        skills = npc.get(
            "Skills",
            {}
        )


        stats = npc.get(
            "Stats",
            {}
        )



        resistance += skills.get(
            "Genjutsu",
            0
        )


        resistance += stats.get(
            "ChakraControl",
            0
        )


        resistance += stats.get(
            "Willpower",
            0
        )



        return resistance









    def calculate_power(
        self,
        npc,
        genjutsu
    ):


        data = self.get_genjutsu(
            genjutsu
        )


        if not data:

            return 0





        power = data.get(
            "Power",
            0
        )



        skills = npc.get(
            "Skills",
            {}
        )


        power += skills.get(
            "Genjutsu",
            0
        )



        abilities = npc.get(
            "Abilities",
            []
        )



        if "Sharingan" in abilities:


            power += 40



        return power









    def cast_genjutsu(
        self,
        attacker_name,
        target_name,
        genjutsu
    ):


        attacker = self.npc_engine.get_npc(
            attacker_name
        )


        target = self.npc_engine.get_npc(
            target_name
        )



        if not attacker or not target:

            return None






        power = self.calculate_power(
            attacker,
            genjutsu
        )



        resistance = self.get_resistance(
            target
        )



        success = power > resistance





        if success:


            effects = target.get(
                "StatusEffects",
                []
            )



            effects.append(
                genjutsu
            )



            target["StatusEffects"] = effects





            self.npc_engine.create_npc(
                target_name,
                **target
            )






        return {


            "Success":
            success,


            "Genjutsu":
            genjutsu,


            "Power":
            power,


            "Resistance":
            resistance

        }









    def break_genjutsu(
        self,
        npc_name
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        npc["StatusEffects"] = []



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return True