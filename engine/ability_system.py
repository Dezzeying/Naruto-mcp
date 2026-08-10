class AbilitySystem:



    def __init__(
        self,
        npc_engine
    ):

        self.npc_engine = npc_engine



        self.abilities = {


            "Sharingan":
            {

                "Type":
                "Bloodline",


                "Bonuses":
                {

                    "Perception":30,

                    "Reaction":25,

                    "Genjutsu":20

                }

            },



            "Byakugan":
            {

                "Type":
                "Bloodline",


                "Bonuses":
                {

                    "Perception":50,

                    "Precision":30

                }

            },



            "Sage Mode":
            {

                "Type":
                "Transformation",


                "Bonuses":
                {

                    "Strength":40,

                    "Chakra":50,

                    "Speed":30

                }

            },



            "Eight Gates":
            {

                "Type":
                "Forbidden",


                "Bonuses":
                {

                    "Strength":100,

                    "Speed":100

                },


                "Risk":
                "Body Damage"

            },



            "Wood Release":
            {

                "Type":
                "Kekkei Genkai",


                "Bonuses":
                {

                    "ChakraControl":40,

                    "Ninjutsu":40

                }

            },



            "Nine Tails Chakra":
            {

                "Type":
                "Tailed Beast",


                "Bonuses":
                {

                    "Chakra":100,

                    "Regeneration":50

                }

            }


        }









    def get_ability(
        self,
        name
    ):


        return self.abilities.get(
            name
        )









    def add_ability(
        self,
        npc_name,
        ability,
        previous=None,
        reason=None
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None



        data = self.get_ability(
            ability
        )


        if not data:

            return None





        abilities = npc.get(
            "Abilities",
            []
        )



        if ability not in abilities:

            abilities.append(
                ability
            )



        npc["Abilities"] = abilities




        self.apply_bonus(
            npc,
            data
        )




        if "EvolutionHistory" not in npc:

            npc["EvolutionHistory"] = []



        if previous:


            npc["EvolutionHistory"].append(

                {

                    "From": previous,

                    "To": ability,

                    "Reason": reason

                }

            )



        self.npc_engine.create_npc(

            npc_name,

            **npc

        )



        return npc










    def unlock_ability(
        self,
        npc_name,
        ability
    ):


        return self.add_ability(

            npc_name,

            ability,

            reason="Unlock"

        )









    def apply_bonus(
        self,
        npc,
        ability_data
    ):


        bonuses = ability_data.get(
            "Bonuses",
            {}
        )



        stats = npc.get(
            "Stats",
            {}
        )



        for stat,value in bonuses.items():


            stats[stat] = (

                stats.get(
                    stat,
                    0
                )

                +

                value

            )



        npc["Stats"] = stats



        return npc










    def has_ability(
        self,
        npc,
        ability
    ):


        return ability in npc.get(
            "Abilities",
            []
        )