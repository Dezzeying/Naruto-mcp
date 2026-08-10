class RinneganSystem:



    def __init__(
        self,
        npc_engine,
        ability_system
    ):


        self.npc_engine = npc_engine

        self.ability_system = ability_system





        self.paths = {



            "Deva Path":
            [

                "Shinra Tensei",

                "Bansho Tenin",

                "Chibaku Tensei"

            ],





            "Asura Path":
            [

                "Mechanical Weapons",

                "Missile Attack"

            ],





            "Human Path":
            [

                "Soul Extraction",

                "Mind Reading"

            ],





            "Animal Path":
            [

                "Summoning"

            ],





            "Preta Path":
            [

                "Chakra Absorption"

            ],





            "Naraka Path":
            [

                "Healing",

                "Judgement"

            ],





            "Outer Path":
            [

                "Rinne Rebirth",

                "Chakra Chains"

            ]

        }







    def can_awaken_rinnegan(
        self,
        npc
    ):


        clan = npc.get(
            "Clan"
        )


        abilities = npc.get(
            "Abilities",
            []
        )


        bloodline = npc.get(
            "Bloodline",
            []
        )



        if "Six Paths Chakra" in abilities:

            return True




        if clan == "Uchiha":


            if "Senju Cells" in abilities:

                return True



        if "Otsutsuki" in bloodline:

            return True



        return False







    def awaken_rinnegan(
        self,
        npc_name
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None






        if not self.can_awaken_rinnegan(
            npc
        ):


            return {


                "Success":
                False,


                "Reason":
                "Requirements failed"

            }






        dojutsu = npc.get(
            "Dojutsu",
            {}
        )



        dojutsu["LeftEye"] = {


            "Type":
            "Rinnegan",


            "Stage":
            "Rinnegan",


            "Abilities":
            []

        }





        dojutsu["RightEye"] = {


            "Type":
            "Rinnegan",


            "Stage":
            "Rinnegan",


            "Abilities":
            []

        }





        npc["Dojutsu"] = dojutsu





        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return {


            "Success":
            True,


            "Awakened":
            "Rinnegan"

        }









    def unlock_path(
        self,
        npc_name,
        path
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        abilities = npc.get(
            "Abilities",
            []
        )



        for technique in self.paths.get(
            path,
            []
        ):


            if technique not in abilities:


                abilities.append(
                    technique
                )



        npc["Abilities"] = abilities




        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return abilities