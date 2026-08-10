class NatureSystem:



    def __init__(
        self,
        npc_engine
    ):


        self.npc_engine = npc_engine





        self.natures = {


            "Fire":
            {

                "StrongAgainst":
                [

                    "Wind"

                ],


                "WeakAgainst":
                [

                    "Water"

                ]

            },





            "Wind":
            {

                "StrongAgainst":
                [

                    "Lightning"

                ],


                "WeakAgainst":
                [

                    "Fire"

                ]

            },





            "Lightning":
            {

                "StrongAgainst":
                [

                    "Earth"

                ],


                "WeakAgainst":
                [

                    "Wind"

                ]

            },





            "Earth":
            {

                "StrongAgainst":
                [

                    "Water"

                ],


                "WeakAgainst":
                [

                    "Lightning"

                ]

            },





            "Water":
            {

                "StrongAgainst":
                [

                    "Fire"

                ],


                "WeakAgainst":
                [

                    "Earth"

                ]

            }

        }








        self.combinations = {



            "Ice Release":
            [

                "Water",

                "Wind"

            ],




            "Wood Release":
            [

                "Earth",

                "Water"

            ],




            "Lava Release":
            [

                "Earth",

                "Fire"

            ],




            "Boil Release":
            [

                "Water",

                "Fire"

            ],




            "Storm Release":
            [

                "Lightning",

                "Water"

            ],




            "Dust Release":
            [

                "Earth",

                "Wind",

                "Fire"

            ]

        }









    def get_nature_data(
        self,
        nature
    ):


        return self.natures.get(
            nature
        )








    def add_nature(
        self,
        npc_name,
        nature
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        natures = npc.get(
            "Nature",
            []
        )



        if nature not in natures:


            natures.append(
                nature
            )



        npc["Nature"] = natures



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return natures







    def has_nature(
        self,
        npc,
        nature
    ):


        return nature in npc.get(
            "Nature",
            []
        )








    def check_combination(
        self,
        npc
    ):


        current = npc.get(
            "Nature",
            []
        )



        results = []



        for name,elements in self.combinations.items():


            if all(
                element in current
                for element in elements
            ):


                results.append(
                    name
                )



        return results







    def unlock_combined_release(
        self,
        npc_name
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        releases = self.check_combination(
            npc
        )



        abilities = npc.get(
            "Abilities",
            []
        )



        for release in releases:


            if release not in abilities:


                abilities.append(
                    release
                )



        npc["Abilities"] = abilities



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return releases