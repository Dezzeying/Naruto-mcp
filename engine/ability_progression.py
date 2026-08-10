class AbilityProgression:



    def __init__(
        self,
        npc_engine,
        ability_system
    ):

        self.npc_engine = npc_engine

        self.ability_system = ability_system







    EVOLUTIONS = {



        "Sharingan":
        {

            "Next":
            "Mangekyo Sharingan",

            "Requirements":
            {

                "Experience":150,

                "EmotionalTrauma":80

            }

        },





        "Mangekyo Sharingan":
        {

            "Next":
            "Eternal Mangekyo Sharingan",

            "Requirements":
            {

                "Experience":300,

                "TransplantMangekyo":True

            }

        },





        "Eternal Mangekyo Sharingan":
        {

            "Next":
            "Rinnegan",

            "Requirements":
            {

                "SenjuDNA":True,

                "Experience":500

            }

        },





        "Jinchuriki":
        {

            "Next":
            "Perfect Jinchuriki",

            "Requirements":
            {

                "BijuuRelationship":90,

                "ChakraControl":90

            }

        }

    }











    def get_stat(
        self,
        npc,
        stat
    ):


        return npc.get(
            "Stats",
            {}
        ).get(
            stat,
            0
        )











    def can_evolve(
        self,
        npc,
        ability
    ):


        data = self.EVOLUTIONS.get(
            ability
        )


        if not data:

            return False



        requirements = data["Requirements"]





        for key,value in requirements.items():



            if key == "ChakraControl":


                if self.get_stat(
                    npc,
                    "ChakraControl"
                ) < value:

                    return False



                continue






            if isinstance(value,bool):


                if npc.get(
                    key,
                    False
                ) != value:

                    return False





            else:


                if npc.get(
                    key,
                    0
                ) < value:

                    return False





        return True











    def evolve(
        self,
        name,
        ability
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None





        if not self.can_evolve(
            npc,
            ability
        ):


            return {

                "Success":
                False,


                "Reason":
                "Evolution requirements not met"

            }







        new_ability = self.EVOLUTIONS[ability]["Next"]





        return self.ability_system.add_ability(

            name,

            new_ability,

            ability,

            "Evolution"

        )