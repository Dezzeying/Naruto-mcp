class NPCBrain:


    def __init__(
        self,
        npc_engine
    ):

        self.npc_engine = npc_engine





    def think(
        self,
        name
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None



        goal = npc.get(
            "Goal",
            None
        )


        if not goal:

            goal = self.assign_goal(
                npc
            )



        action = self.choose_action(
            npc,
            goal
        )



        return {

            "NPC":
            name,

            "Goal":
            goal,

            "Action":
            action

        }







    def assign_goal(
        self,
        npc
    ):


        name = npc.get(
            "Name"
        )


        goals = {


            "Naruto Uzumaki":
            "Become Hokage",


            "Sasuke Uchiha":
            "Gain Power",


            "Kakashi Hatake":
            "Protect Allies",


            "Sakura Haruno":
            "Improve Medical Skills"

        }



        goal = goals.get(
            name,
            "Become Stronger"
        )



        npc["Goal"] = goal



        self.npc_engine.create_npc(
            name,
            **npc
        )



        return goal








    def choose_action(
        self,
        npc,
        goal
    ):



        chakra = npc.get(
            "Chakra",
            0
        )


        experience = npc.get(
            "Experience",
            0
        )



        if goal == "Become Hokage":


            if experience < 50:

                return "Training"


            else:

                return "Mission"





        if goal == "Gain Power":


            return "Search For Strong Techniques"





        if goal == "Protect Allies":


            return "Patrol"





        return "Training"