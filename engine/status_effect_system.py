class StatusEffectSystem:



    def __init__(
        self,
        npc_engine
    ):


        self.npc_engine = npc_engine




        self.effects = {



            "Burn":

            {

                "Type":
                "Damage Over Time",


                "Damage":
                10,


                "Duration":
                3

            },





            "Poison":

            {

                "Type":
                "Damage Over Time",


                "Damage":
                8,


                "Duration":
                5

            },






            "Bleeding":

            {

                "Type":
                "Physical Damage",


                "Damage":
                5,


                "Duration":
                4

            },






            "Paralyzed":

            {

                "Type":
                "Disable",


                "Duration":
                2

            },






            "Genjutsu":

            {

                "Type":
                "Mental Control",


                "Duration":
                3

            },






            "Exhausted":

            {

                "Type":
                "Stat Reduction",


                "SpeedReduction":
                20

            },






            "Chakra Exhaustion":

            {

                "Type":
                "Resource",

                "ChakraReduction":
                30

            }

        }








    def add_effect(
        self,
        npc_name,
        effect
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        if effect not in self.effects:

            return {


                "Success":
                False,


                "Reason":
                "Effect not found"

            }






        statuses = npc.get(
            "StatusEffects",
            []
        )



        if effect not in statuses:


            statuses.append(
                effect
            )



        npc["StatusEffects"] = statuses



        self.apply_initial_effect(
            npc,
            effect
        )



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return {


            "Success":
            True,


            "Effect":
            effect

        }









    def remove_effect(
        self,
        npc_name,
        effect
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        statuses = npc.get(
            "StatusEffects",
            []
        )



        if effect in statuses:

            statuses.remove(
                effect
            )



        npc["StatusEffects"] = statuses



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )


        return True







    def apply_initial_effect(
        self,
        npc,
        effect
    ):


        if effect == "Chakra Exhaustion":


            npc["Chakra"] = max(

                npc.get(
                    "Chakra",
                    0
                )
                -
                30,

                0

            )





        if effect == "Exhausted":


            npc["Speed"] = max(

                npc.get(
                    "Speed",
                    0
                )
                -
                20,

                0

            )



        return npc







    def process_turn(
        self,
        npc_name
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None






        statuses = npc.get(
            "StatusEffects",
            []
        )



        damage = 0



        for effect in statuses:


            data = self.effects.get(
                effect
            )


            if not data:

                continue



            damage += data.get(
                "Damage",
                0
            )



        if damage > 0:


            npc["HP"] = max(

                npc.get(
                    "HP",
                    100
                )
                -
                damage,

                0

            )



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return {


            "DamageTaken":
            damage,


            "HP":
            npc["HP"]

        }