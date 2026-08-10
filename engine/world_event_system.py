class WorldEventSystem:



    def __init__(
        self,
        npc_engine,
        village_system
    ):


        self.npc_engine = npc_engine

        self.village_system = village_system




        self.events = {



            "Chunin Exams":
            {

                "Type":
                "Tournament",


                "Requirements":
                {

                    "Rank":
                    "Genin"

                },


                "Effects":
                [

                    "Rank Promotion",

                    "Reputation Increase"

                ]

            },







            "Akatsuki Attack":
            {

                "Type":
                "Threat",


                "Requirements":
                {

                    "ThreatLevel":
                    70

                },


                "Effects":
                [

                    "Village Defense",

                    "S Rank Missions"

                ]

            },








            "Fourth Ninja War":
            {

                "Type":
                "War",


                "Requirements":
                {

                    "WorldTension":
                    100

                },


                "Effects":
                [

                    "Alliance Creation",

                    "Large Scale Battles"

                ]

            },








            "Clan Conflict":
            {

                "Type":
                "Internal Conflict",


                "Effects":
                [

                    "Clan Reputation Change",

                    "Political Changes"

                ]

            }

        }








    def get_event(
        self,
        event
    ):


        return self.events.get(
            event
        )








    def start_event(
        self,
        event
    ):


        data = self.get_event(
            event
        )


        if not data:

            return {


                "Success":
                False,


                "Reason":
                "Event not found"

            }





        return {


            "Success":
            True,


            "Event":
            event,


            "Type":
            data["Type"]

        }








    def apply_event_effect(
        self,
        event
    ):


        data = self.get_event(
            event
        )


        if not data:

            return None





        return {


            "Event":
            event,


            "Effects":
            data.get(
                "Effects",
                []
            )

        }









    def trigger_war(
        self,
        village1,
        village2
    ):


        result = self.village_system.declare_war(
            village1,
            village2
        )


        return {


            "Event":
            "War",

            "Result":
            result

        }








    def create_peace(
        self,
        village1,
        village2
    ):


        result = self.village_system.create_alliance(
            village1,
            village2
        )


        return {


            "Event":
            "Peace",

            "Result":
            result

        }