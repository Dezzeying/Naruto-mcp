import random



class MissionEngine:



    def __init__(
        self,
        npc_engine,
        world_state,
        relationship_engine
    ):

        self.npc_engine = npc_engine
        self.world = world_state
        self.relationship = relationship_engine





    def get_mission_database(
        self
    ):


        return {


            "D":
            [

                {

                "Name":
                "Find Lost Cat",


                "Rank":
                "D",


                "Reward":
                50,


                "Type":
                "Normal"

                },


                {

                "Name":
                "Deliver Package",


                "Rank":
                "D",


                "Reward":
                80,


                "Type":
                "Delivery"

                }

            ],



            "C":
            [

                {

                "Name":
                "Escort Merchant",


                "Rank":
                "C",


                "Reward":
                200,


                "Type":
                "Escort"

                }

            ],



            "B":
            [

                {

                "Name":
                "Enemy Shinobi Investigation",


                "Rank":
                "B",


                "Reward":
                500,


                "Type":
                "Combat"

                }

            ],



            "A":
            [

                {

                "Name":
                "Village Defense",


                "Rank":
                "A",


                "Reward":
                1000,


                "Type":
                "War"

                }

            ]

        }







    def generate_mission(
        self,
        player
    ):


        rank = player.get(
            "Rank",
            "D"
        )


        database = self.get_mission_database()



        missions = database.get(
            rank,
            database["D"]
        )



        mission = random.choice(
            missions
        )



        return mission







    def generate_special_mission(
        self,
        player
    ):


        missions = []



        world = self.world.get_world()



        if world.get(
            "VillageStatus",
            {}
        ).get(
            "Konoha"
        ) == "War":



            missions.append(

                {

                "Name":
                "War Support Mission",


                "Rank":
                "A",


                "Reward":
                1500

                }

            )





        relationships = player.get(
            "Relationships",
            {}
        )



        if "Kakashi" in relationships:



            trust = relationships["Kakashi"].get(
                "Trust",
                0
            )



            if trust >= 80:


                missions.append(

                    {

                    "Name":
                    "Secret Kakashi Training",


                    "Rank":
                    "Special",


                    "Reward":
                    0

                    }

                )





        if not missions:

            return None



        return random.choice(
            missions
        )







    def accept_mission(
        self,
        player,
        mission
    ):


        active = player.get(
            "ActiveMissions",
            []
        )



        active.append(
            mission
        )


        player["ActiveMissions"] = active



        return player







    def complete_mission(
        self,
        player,
        mission
    ):


        active = player.get(
            "ActiveMissions",
            []
        )


        if mission in active:

            active.remove(
                mission
            )



        completed = player.get(
            "CompletedMissions",
            []
        )



        completed.append(
            mission
        )



        player["ActiveMissions"] = active


        player["CompletedMissions"] = completed



        reward = mission.get(
            "Reward",
            0
        )



        player["Ryo"] = (
            player.get(
                "Ryo",
                0
            )
            +
            reward
        )



        return player