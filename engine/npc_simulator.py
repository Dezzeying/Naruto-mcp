class NPCSimulator:



    def __init__(
        self,
        npc_engine,
        npc_brain,
        training_engine,
        memory=None
    ):

        self.npc_engine = npc_engine

        self.npc_brain = npc_brain

        self.training_engine = training_engine

        self.memory = memory







    def simulate_day(
        self,
        name
    ):


        decision = self.npc_brain.think(
            name
        )


        if not decision:

            return None




        action = decision.get(
            "Action"
        )



        result = {


            "NPC":
            name,


            "Action":
            action,


            "Changes":
            []

        }







        if action == "Training":


            change = self.training(
                name
            )


            result["Changes"].append(
                change
            )







        elif action == "Search For Strong Techniques":


            result["Changes"].append(

                {

                    "Type":
                    "Searching",


                    "Result":
                    "Searching for hidden techniques"

                }

            )







        elif action == "Mission":


            result["Changes"].append(

                {

                    "Type":
                    "Mission",


                    "Result":
                    "Mission completed"

                }

            )







        elif action == "Patrol":


            result["Changes"].append(

                {

                    "Type":
                    "Patrol",


                    "Result":
                    "Area secured"

                }

            )






        self.save_memory(
            result
        )



        return result











    def training(
        self,
        name
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None






        npc["Experience"] = (

            npc.get(
                "Experience",
                0
            )

            +

            1

        )






        stats = npc.get(
            "Stats",
            {}
        )



        stats["ChakraControl"] = (

            stats.get(
                "ChakraControl",
                0
            )

            +

            1

        )



        stats["Stamina"] = (

            stats.get(
                "Stamina",
                0
            )

            +

            1

        )



        npc["Stats"] = stats






        self.npc_engine.create_npc(

            name,

            **npc

        )






        return {


            "Type":
            "Training",


            "Experience":
            "+1",


            "ChakraControl":
            "+1",


            "Stamina":
            "+1"

        }









    def save_memory(
        self,
        data
    ):


        if not self.memory:

            return




        self.memory.add_event(

            "NPC Daily Simulation",

            data

        )