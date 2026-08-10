import random



class AbilityEngine:



    def __init__(
        self,
        npc_engine
    ):

        self.npc_engine = npc_engine





    def get_ability_data(
        self,
        ability
    ):


        abilities = {


            "Sharingan":
            {

                "Requirement":
                "Sharingan Potential",


                "Trigger":
                "Extreme Emotion",


                "Level":
                1

            },



            "Byakugan":
            {

                "Requirement":
                "Byakugan Potential",


                "Trigger":
                "Chakra Training",


                "Level":
                1

            },



            "Sage Mode":
            {

                "Requirement":
                "High Chakra Control",


                "Trigger":
                "Nature Energy Training",


                "Level":
                1

            },



            "Advanced Sealing":
            {

                "Requirement":
                "Sealing",


                "Trigger":
                "Sealing Research",


                "Level":
                1

            }

        }


        return abilities.get(
            ability
        )





    def has_potential(
        self,
        npc,
        ability
    ):


        abilities = npc.get(
            "Abilities",
            []
        )


        return (
            ability
            in
            abilities
        )







    def attempt_awaken(
        self,
        name,
        ability,
        trigger
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None





        data = self.get_ability_data(
            ability
        )


        if not data:

            return {

                "Success":
                False,

                "Reason":
                "Unknown ability"

            }





        requirement = data.get(
            "Requirement"
        )



        if requirement:


            if not self.has_potential(
                npc,
                requirement
            ):


                return {


                    "Success":
                    False,


                    "Reason":
                    "No potential"

                }






        if trigger != data.get(
            "Trigger"
        ):


            return {


                "Success":
                False,


                "Reason":
                "Wrong trigger"

            }





        chance = random.randint(
            1,
            100
        )



        if chance > 50:


            return {


                "Success":
                False,


                "Reason":
                "Ability failed to awaken"

            }





        awakened = npc.get(
            "AwakenedAbilities",
            []
        )



        if ability not in awakened:


            awakened.append(
                ability
            )



        npc["AwakenedAbilities"] = awakened




        self.npc_engine.create_npc(
            name,
            **npc
        )



        return {


            "Success":
            True,


            "Ability":
            ability

        }







    def increase_ability_level(
        self,
        name,
        ability
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None



        levels = npc.get(
            "AbilityLevels",
            {}
        )



        levels[ability] = (
            levels.get(
                ability,
                0
            )
            +
            1
        )



        npc["AbilityLevels"] = levels



        self.npc_engine.create_npc(
            name,
            **npc
        )


        return levels[ability]