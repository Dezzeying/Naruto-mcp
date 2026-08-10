class RankSystem:



    def __init__(
        self,
        npc_engine
    ):


        self.npc_engine = npc_engine




        self.ranks = {



            "Academy Student":
            {

                "Level":
                0,


                "Requirements":
                {

                    "Experience":0

                },


                "Access":
                [

                    "Academy Training"

                ]

            },







            "Genin":
            {

                "Level":
                1,


                "Requirements":
                {

                    "Experience":100

                },


                "Access":
                [

                    "D Rank Missions",

                    "Basic Team Missions"

                ]

            },








            "Chunin":
            {

                "Level":
                2,


                "Requirements":
                {

                    "Experience":500,

                    "CompletedMissions":10

                },


                "Access":
                [

                    "C Rank Missions",

                    "Team Leadership"

                ]

            },








            "Jonin":
            {

                "Level":
                3,


                "Requirements":
                {

                    "Experience":2000,

                    "CompletedMissions":50

                },


                "Access":
                [

                    "A Rank Missions",

                    "Advanced Training"

                ]

            },








            "Special Jonin":
            {

                "Level":
                4,


                "Requirements":
                {

                    "Experience":3000

                },


                "Access":
                [

                    "Specialized Missions"

                ]

            },








            "Anbu":
            {

                "Level":
                5,


                "Requirements":
                {

                    "Experience":5000,

                    "Stealth":80

                },


                "Access":
                [

                    "Secret Missions",

                    "Assassination"

                ]

            },








            "Kage":
            {

                "Level":
                6,


                "Requirements":
                {

                    "Experience":10000,

                    "Reputation":100

                },


                "Access":
                [

                    "Village Command",

                    "S Rank Missions"

                ]

            }

        }








    def get_rank_data(
        self,
        rank
    ):


        return self.ranks.get(
            rank
        )









    def check_promotion(
        self,
        npc
    ):


        current = npc.get(
            "Rank",
            "Academy Student"
        )



        exp = npc.get(
            "Experience",
            0
        )


        missions = len(

            npc.get(
                "CompletedMissions",
                []
            )

        )



        stealth = npc.get(
            "Stealth",
            0
        )


        reputation = npc.get(
            "Reputation",
            0
        )



        possible = []



        for rank,data in self.ranks.items():


            requirements = data.get(
                "Requirements",
                {}
            )


            valid = True



            if "Experience" in requirements:


                if exp < requirements["Experience"]:

                    valid = False





            if "CompletedMissions" in requirements:


                if missions < requirements["CompletedMissions"]:

                    valid = False





            if "Stealth" in requirements:


                if stealth < requirements["Stealth"]:

                    valid = False





            if "Reputation" in requirements:


                if reputation < requirements["Reputation"]:

                    valid = False





            if valid:


                possible.append(
                    rank
                )



        return possible







    def promote(
        self,
        npc_name,
        new_rank
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        if new_rank not in self.ranks:

            return {


                "Success":
                False,


                "Reason":
                "Rank not found"

            }





        npc["Rank"] = new_rank



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return {


            "Success":
            True,


            "Rank":
            new_rank

        }








    def get_access(
        self,
        npc
    ):


        rank = npc.get(
            "Rank",
            "Academy Student"
        )


        data = self.get_rank_data(
            rank
        )


        if not data:

            return []



        return data.get(
            "Access",
            []
        )