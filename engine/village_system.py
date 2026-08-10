class VillageSystem:



    def __init__(
        self,
        npc_engine
    ):


        self.npc_engine = npc_engine




        self.villages = {



            "Konohagakure":
            {

                "Leader":
                "Hokage",


                "MilitaryPower":
                100,


                "Economy":
                90,


                "Relations":
                {

                    "Sunagakure":70,

                    "Kirigakure":50,

                    "Kumogakure":40,

                    "Iwagakure":40

                }

            },






            "Sunagakure":
            {

                "Leader":
                "Kazekage",


                "MilitaryPower":
                70,


                "Economy":
                60,


                "Relations":
                {

                    "Konohagakure":70,

                    "Kirigakure":40,

                    "Kumogakure":50

                }

            },








            "Kirigakure":
            {

                "Leader":
                "Mizukage",


                "MilitaryPower":
                85,


                "Economy":
                70,


                "Relations":
                {

                    "Konohagakure":50,

                    "Sunagakure":40

                }

            },








            "Kumogakure":
            {

                "Leader":
                "Raikage",


                "MilitaryPower":
                95,


                "Economy":
                80,


                "Relations":
                {

                    "Konohagakure":40,

                    "Iwagakure":50

                }

            },








            "Iwagakure":
            {

                "Leader":
                "Tsuchikage",


                "MilitaryPower":
                90,


                "Economy":
                75,


                "Relations":
                {

                    "Kumogakure":50,

                    "Konohagakure":40

                }

            }

        }








    def get_village(
        self,
        village
    ):


        return self.villages.get(
            village
        )









    def add_ninja_to_village(
        self,
        npc_name,
        village
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        if village not in self.villages:

            return {


                "Success":
                False,


                "Reason":
                "Village not found"

            }





        npc["Village"] = village



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return {


            "Success":
            True,


            "Village":
            village

        }









    def change_relation(
        self,
        village1,
        village2,
        amount
    ):


        if village1 not in self.villages:

            return False



        if village2 not in self.villages:

            return False





        relation = self.villages[village1]["Relations"].get(
            village2,
            50
        )



        relation += amount



        relation = max(
            min(
                relation,
                100
            ),
            0
        )



        self.villages[village1]["Relations"][village2] = relation



        return relation







    def get_relation(
        self,
        village1,
        village2
    ):


        if village1 not in self.villages:

            return None



        return self.villages[village1]["Relations"].get(
            village2,
            50
        )








    def declare_war(
        self,
        village1,
        village2
    ):


        self.change_relation(
            village1,
            village2,
            -100
        )


        self.change_relation(
            village2,
            village1,
            -100
        )



        return {


            "War":
            True,


            "Between":
            [

                village1,

                village2

            ]

        }








    def create_alliance(
        self,
        village1,
        village2
    ):


        self.change_relation(
            village1,
            village2,
            50
        )


        self.change_relation(
            village2,
            village1,
            50
        )



        return {


            "Alliance":
            True,


            "Between":
            [

                village1,

                village2

            ]

        }