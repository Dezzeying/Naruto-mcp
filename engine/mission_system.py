class MissionSystem:



    def __init__(
        self,
        npc_engine
    ):


        self.npc_engine = npc_engine




        self.missions = {



            "Lost Cat":

            {

                "Rank":
                "D",


                "Difficulty":
                10,


                "Reward":
                {

                    "Ryo":500,

                    "Experience":20

                },


                "Type":
                "Search"

            },







            "Escort Merchant":

            {

                "Rank":
                "C",


                "Difficulty":
                30,


                "Reward":
                {

                    "Ryo":1500,

                    "Experience":60

                },


                "Type":
                "Escort"

            },








            "Bandit Elimination":

            {

                "Rank":
                "B",


                "Difficulty":
                60,


                "Reward":
                {

                    "Ryo":5000,

                    "Experience":150

                },


                "Type":
                "Combat"

            },








            "Missing Ninja":

            {

                "Rank":
                "A",


                "Difficulty":
                85,


                "Reward":
                {

                    "Ryo":15000,

                    "Experience":400

                },


                "Type":
                "Capture"

            },








            "Akatsuki Threat":

            {

                "Rank":
                "S",


                "Difficulty":
                100,


                "Reward":
                {

                    "Ryo":50000,

                    "Experience":1000

                },


                "Type":
                "Extreme"

            }

        }







    def get_mission(
        self,
        name
    ):


        return self.missions.get(
            name
        )









    def assign_mission(
        self,
        npc_name,
        mission
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        if mission not in self.missions:

            return {


                "Success":
                False,


                "Reason":
                "Mission not found"

            }






        missions = npc.get(
            "ActiveMissions",
            []
        )



        if mission not in missions:


            missions.append(
                mission
            )



        npc["ActiveMissions"] = missions



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return {


            "Success":
            True,


            "Mission":
            mission

        }









    def complete_mission(
        self,
        npc_name,
        mission
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        data = self.get_mission(
            mission
        )


        if not data:

            return None






        rewards = data.get(
            "Reward",
            {}
        )



        npc["Ryo"] = (

            npc.get(
                "Ryo",
                0
            )

            +

            rewards.get(
                "Ryo",
                0
            )

        )




        npc["Experience"] = (

            npc.get(
                "Experience",
                0
            )

            +

            rewards.get(
                "Experience",
                0
            )

        )







        completed = npc.get(
            "CompletedMissions",
            []
        )



        if mission not in completed:


            completed.append(
                mission
            )



        npc["CompletedMissions"] = completed






        active = npc.get(
            "ActiveMissions",
            []
        )



        if mission in active:


            active.remove(
                mission
            )



        npc["ActiveMissions"] = active





        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return {


            "Success":
            True,


            "Reward":
            rewards

        }









    def get_rank(
        self,
        mission
    ):


        data = self.get_mission(
            mission
        )


        if not data:

            return None



        return data["Rank"]