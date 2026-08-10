class PromotionEngine:



    def __init__(
        self,
        npc_engine
    ):

        self.npc_engine = npc_engine





    def get_rank_requirements(
        self,
        rank
    ):


        requirements = {


            "Genin":
            {

                "Experience":
                10,


                "Academy":
                True

            },



            "Chunin":
            {

                "Experience":
                50,


                "Leadership":
                40,


                "CompletedMissions":
                10


            },



            "Jonin":
            {

                "Experience":
                150,


                "Leadership":
                80,


                "CompletedMissions":
                50,


                "Reputation":
                70

            },



            "Kage":
            {

                "Experience":
                300,


                "Leadership":
                95,


                "Reputation":
                95,


                "CompletedMissions":
                100

            }


        }


        return requirements.get(
            rank
        )







    def can_promote(
        self,
        npc,
        new_rank
    ):


        requirements = self.get_rank_requirements(
            new_rank
        )


        if not requirements:

            return False




        for key,value in requirements.items():



            if key == "Academy":


                if npc.get(
                    "Academy",
                    False
                ) != value:


                    return False



            elif key == "CompletedMissions":


                missions = len(
                    npc.get(
                        "CompletedMissions",
                        []
                    )
                )



                if missions < value:

                    return False




            else:


                if npc.get(
                    key,
                    0
                ) < value:


                    return False




        return True







    def promote(
        self,
        name,
        new_rank
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None





        if not self.can_promote(
            npc,
            new_rank
        ):


            return {


                "Success":
                False,


                "Reason":
                "Requirements not met"


            }






        old_rank = npc.get(
            "Rank",
            "Academy Student"
        )



        npc["Rank"] = new_rank



        achievements = npc.get(
            "Achievements",
            []
        )


        achievements.append(

            f"Promoted from {old_rank} to {new_rank}"

        )


        npc["Achievements"] = achievements



        self.npc_engine.create_npc(
            name,
            **npc
        )



        return {


            "Success":
            True,


            "OldRank":
            old_rank,


            "NewRank":
            new_rank

        }








    def calculate_promotion_score(
        self,
        npc
    ):


        score = 0



        score += npc.get(
            "Experience",
            0
        )



        score += npc.get(
            "Leadership",
            0
        )


        score += npc.get(
            "Reputation",
            0
        )



        score += len(
            npc.get(
                "CompletedMissions",
                []
            )
        )



        return score