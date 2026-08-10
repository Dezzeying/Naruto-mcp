class BijuuSystem:



    def __init__(
        self,
        npc_engine,
        ability_system
    ):


        self.npc_engine = npc_engine

        self.ability_system = ability_system





        self.bijuu_database = {


            "Shukaku":
            {

                "Tails":
                1,

                "Nature":
                "Wind",

                "Chakra":
                80,

                "Abilities":
                [

                    "Sand Manipulation",

                    "Bijuu Chakra"

                ]

            },





            "Matatabi":
            {

                "Tails":
                2,

                "Nature":
                "Fire",

                "Chakra":
                100,

                "Abilities":
                [

                    "Blue Flames",

                    "Bijuu Chakra"

                ]

            },





            "Isobu":
            {

                "Tails":
                3,

                "Nature":
                "Water",

                "Chakra":
                120,

                "Abilities":
                [

                    "Water Style Enhancement",

                    "Bijuu Chakra"

                ]

            },





            "Son Goku":
            {

                "Tails":
                4,

                "Nature":
                "Lava",

                "Chakra":
                150,

                "Abilities":
                [

                    "Lava Release",

                    "Bijuu Chakra"

                ]

            },





            "Kokuo":
            {

                "Tails":
                5,

                "Nature":
                "Steam",

                "Chakra":
                160,

                "Abilities":
                [

                    "Boil Release",

                    "Bijuu Chakra"

                ]

            },





            "Saiken":
            {

                "Tails":
                6,

                "Nature":
                "Water",

                "Chakra":
                170,

                "Abilities":
                [

                    "Acid Release",

                    "Bijuu Chakra"

                ]

            },





            "Chomei":
            {

                "Tails":
                7,

                "Nature":
                "Wind",

                "Chakra":
                180,

                "Abilities":
                [

                    "Flight",

                    "Bijuu Chakra"

                ]

            },





            "Gyuki":
            {

                "Tails":
                8,

                "Nature":
                "Ink",

                "Chakra":
                220,

                "Abilities":
                [

                    "Ink Release",

                    "Bijuu Chakra"

                ]

            },





            "Kurama":
            {

                "Tails":
                9,

                "Nature":
                "Chakra",

                "Chakra":
                300,

                "Abilities":
                [

                    "Nine Tails Chakra",

                    "Chakra Mode",

                    "Healing"

                ]

            }

        }







    def get_bijuu(
        self,
        name
    ):


        return self.bijuu_database.get(
            name
        )









    def seal_bijuu(
        self,
        npc_name,
        bijuu_name
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        bijuu = self.get_bijuu(
            bijuu_name
        )


        if not npc or not bijuu:

            return None






        npc["Bijuu"] = bijuu_name



        npc["Jinchuriki"] = True



        npc["BijuuControl"] = 0



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return {


            "Success":
            True,


            "Bijuu":
            bijuu_name


        }









    def increase_control(
        self,
        npc_name,
        amount
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None



        current = npc.get(
            "BijuuControl",
            0
        )


        npc["BijuuControl"] = min(

            current + amount,

            100

        )



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return npc["BijuuControl"]







    def activate_chakra_mode(
        self,
        npc_name
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        if not npc.get(
            "Jinchuriki",
            False
        ):


            return {


                "Success":
                False,


                "Reason":
                "Not Jinchuriki"

            }







        bijuu = self.get_bijuu(
            npc["Bijuu"]
        )



        control = npc.get(
            "BijuuControl",
            0
        )



        if control < 50:


            return {


                "Success":
                False,


                "Reason":
                "Low control"

            }






        for ability in bijuu.get(
            "Abilities",
            []
        ):


            self.ability_system.unlock_ability(
                npc_name,
                ability
            )



        return {


            "Success":
            True,


            "Mode":
            npc["Bijuu"] + " Chakra Mode"

        }