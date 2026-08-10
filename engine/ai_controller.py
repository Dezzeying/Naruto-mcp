import random



class AIController:



    def __init__(
        self,
        npc_engine,
        training_engine,
        relationship_engine,
        world_state
    ):


        self.npc_engine = npc_engine

        self.training_engine = training_engine

        self.relationship = relationship_engine

        self.world = world_state





    def analyze_npc(
        self,
        name
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None



        decision = self.make_decision(
            npc
        )


        return decision






    def make_decision(
        self,
        npc
    ):


        goals = npc.get(
            "Goals",
            []
        )


        personality = npc.get(
            "Personality",
            []
        )


        rank = npc.get(
            "Rank",
            "Academy Student"
        )





        if "Become Stronger" in goals:


            return {

                "Action":
                "Training",


                "Reason":
                "Seeking power"

            }






        if "Protect Village" in goals:


            return {

                "Action":
                "Mission",


                "Reason":
                "Village protection"

            }






        if "Revenge" in goals:


            return {

                "Action":
                "Search Power",


                "Reason":
                "Revenge motivation"

            }





        if "Lazy" in personality:


            chance = random.randint(
                1,
                100
            )


            if chance < 30:


                return {


                    "Action":
                    "Rest",


                    "Reason":
                    "Personality"

                }







        if rank == "Jonin":


            return {


                "Action":
                "Guide Students",


                "Reason":
                "Experienced Ninja"

            }






        return {


            "Action":
            "Normal Activity",


            "Reason":
            "No special motivation"

        }









    def execute_action(
        self,
        name,
        action
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None






        if action == "Training":


            xp = npc.get(
                "Experience",
                0
            )


            npc["Experience"] = (
                xp + 1
            )



        elif action == "Mission":


            npc["MissionActivity"] = True






        elif action == "Search Power":


            npc["PowerSeeking"] = True






        elif action == "Guide Students":


            npc["Teaching"] = True






        self.npc_engine.create_npc(
            name,
            **npc
        )



        return npc