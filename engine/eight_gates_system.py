class EightGatesSystem:



    def __init__(
        self,
        npc_engine
    ):


        self.npc_engine = npc_engine




        self.gates = {



            "First Gate":
            {

                "Name":
                "Gate of Opening",

                "RequiredTaijutsu":
                30,

                "RequiredEndurance":
                20,


                "Bonus":
                {

                    "Strength":10,

                    "Speed":15

                },


                "Damage":
                5,


                "Technique":
                "Front Lotus"

            },







            "Second Gate":
            {

                "Name":
                "Gate of Healing",

                "RequiredTaijutsu":
                40,

                "RequiredEndurance":
                30,


                "Bonus":
                {

                    "Strength":20,

                    "Speed":25

                },


                "Damage":
                10

            },








            "Third Gate":
            {

                "Name":
                "Gate of Life",

                "RequiredTaijutsu":
                55,

                "RequiredEndurance":
                40,


                "Bonus":
                {

                    "Strength":40,

                    "Speed":40

                },


                "Damage":
                20

            },








            "Fourth Gate":
            {

                "Name":
                "Gate of Pain",

                "RequiredTaijutsu":
                65,

                "RequiredEndurance":
                50,


                "Bonus":
                {

                    "Strength":60,

                    "Speed":60

                },


                "Damage":
                30

            },








            "Fifth Gate":
            {

                "Name":
                "Gate of Limit",

                "RequiredTaijutsu":
                75,

                "RequiredEndurance":
                60,


                "Bonus":
                {

                    "Strength":90,

                    "Speed":90

                },


                "Damage":
                45

            },








            "Sixth Gate":
            {

                "Name":
                "Gate of View",

                "RequiredTaijutsu":
                85,

                "RequiredEndurance":
                70,


                "Bonus":
                {

                    "Strength":130,

                    "Speed":130

                },


                "Damage":
                60,


                "Technique":
                "Morning Peacock"

            },








            "Seventh Gate":
            {

                "Name":
                "Gate of Wonder",

                "RequiredTaijutsu":
                95,

                "RequiredEndurance":
                85,


                "Bonus":
                {

                    "Strength":200,

                    "Speed":200

                },


                "Damage":
                80,


                "Technique":
                "Daytime Tiger"

            },








            "Eighth Gate":
            {

                "Name":
                "Gate of Death",

                "RequiredTaijutsu":
                100,

                "RequiredEndurance":
                100,


                "Bonus":
                {

                    "Strength":500,

                    "Speed":500

                },


                "Damage":
                100,


                "Technique":
                [

                    "Evening Elephant",

                    "Night Guy"

                ],


                "DeathRisk":
                True

            }


        }








    def get_gate(
        self,
        gate
    ):


        return self.gates.get(
            gate
        )









    def can_open_gate(
        self,
        npc,
        gate
    ):


        data = self.get_gate(
            gate
        )


        if not data:

            return False






        skills = npc.get(
            "Skills",
            {}
        )



        taijutsu = skills.get(
            "Taijutsu",
            0
        )



        endurance = npc.get(
            "Endurance",
            0
        )



        if taijutsu < data["RequiredTaijutsu"]:

            return False



        if endurance < data["RequiredEndurance"]:

            return False




        return True







    def open_gate(
        self,
        npc_name,
        gate
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None






        if not self.can_open_gate(
            npc,
            gate
        ):


            return {


                "Success":
                False,


                "Reason":
                "Requirements not met"

            }







        opened = npc.get(
            "OpenedGates",
            []
        )



        if gate not in opened:


            opened.append(
                gate
            )



        npc["OpenedGates"] = opened






        data = self.get_gate(
            gate
        )



        for stat,value in data["Bonus"].items():


            npc[stat] = (

                npc.get(
                    stat,
                    0
                )

                +

                value

            )






        npc["GateDamage"] = (

            npc.get(
                "GateDamage",
                0
            )

            +

            data["Damage"]

        )






        if data.get(
            "DeathRisk",
            False
        ):


            npc["Status"] = "Critical"





        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return {


            "Success":
            True,


            "Gate":
            gate,


            "Technique":
            data.get(
                "Technique"
            )

        }









    def close_all_gates(
        self,
        npc_name
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None




        npc["OpenedGates"] = []



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return True