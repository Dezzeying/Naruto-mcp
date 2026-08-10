class KekkeiGenkaiSystem:



    def __init__(
        self,
        npc_engine,
        ability_system
    ):


        self.npc_engine = npc_engine

        self.ability_system = ability_system




        self.genkai_database = {


            "Sharingan":
            {

                "Clan":
                "Uchiha",


                "Trigger":
                "Extreme Emotional Event",


                "Evolution":
                [

                    "1 Tomoe Sharingan",

                    "2 Tomoe Sharingan",

                    "3 Tomoe Sharingan",

                    "Mangekyo Sharingan"

                ]

            },





            "Byakugan":
            {

                "Clan":
                "Hyuga",


                "Trigger":
                "Bloodline Activation",


                "Evolution":
                [

                    "Byakugan",

                    "Advanced Byakugan"

                ]

            },





            "Wood Release":
            {

                "Clan":
                "Senju",


                "Trigger":
                "High Chakra Compatibility",


                "Evolution":
                [

                    "Wood Style"

                ]

            },





            "Ice Release":
            {

                "Clan":
                "Yuki",


                "Trigger":
                "Water + Wind Compatibility",


                "Evolution":
                [

                    "Ice Techniques"

                ]

            },





            "Shikotsumyaku":
            {

                "Clan":
                "Kaguya",


                "Trigger":
                "Bloodline Inheritance",


                "Evolution":
                [

                    "Bone Manipulation"

                ]

            }

        }







    def get_genkai(
        self,
        name
    ):


        return self.genkai_database.get(
            name
        )









    def has_potential(
        self,
        npc,
        genkai
    ):


        abilities = npc.get(
            "Abilities",
            []
        )


        potential = npc.get(
            "PotentialAbilities",
            []
        )



        if genkai in abilities:

            return True



        if genkai in potential:

            return True



        return False







    def check_activation(
        self,
        npc,
        genkai,
        event=None
    ):


        data = self.get_genkai(
            genkai
        )


        if not data:

            return False






        clan = data.get(
            "Clan"
        )



        if npc.get(
            "Clan"
        ) != clan:


            return False





        if genkai == "Sharingan":


            if event == "Extreme Emotional Event":


                return True





        if genkai == "Byakugan":


            return True





        if genkai == "Wood Release":


            chakra = npc.get(
                "Chakra",
                0
            )


            control = npc.get(
                "ChakraControl",
                0
            )


            if chakra >= 80 and control >= 70:


                return True






        return False







    def awaken(
        self,
        npc_name,
        genkai,
        event=None
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None






        if not self.check_activation(
            npc,
            genkai,
            event
        ):


            return {


                "Success":
                False,


                "Reason":
                "Activation conditions not met"

            }







        self.ability_system.unlock_ability(
            npc_name,
            genkai
        )



        return {


            "Success":
            True,


            "Awakened":
            genkai

        }