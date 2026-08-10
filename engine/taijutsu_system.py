class TaijutsuSystem:



    def __init__(
        self,
        npc_engine,
        ability_system
    ):


        self.npc_engine = npc_engine

        self.ability_system = ability_system





        self.styles = {


            "Basic Taijutsu":
            {

                "Type":
                "Physical",

                "Bonus":
                {

                    "Strength":5,

                    "Speed":5

                }

            },





            "Gentle Fist":
            {

                "Type":
                "Hyuga Style",


                "Requirements":
                {

                    "Clan":
                    "Hyuga"

                },


                "Bonus":
                {

                    "Precision":30,

                    "ChakraControl":20

                }

            },







            "Strong Fist":
            {

                "Type":
                "Power Style",


                "Bonus":
                {

                    "Strength":25

                }

            },







            "Beast Style":
            {

                "Type":
                "Inuzuka Style",


                "Requirements":
                {

                    "Clan":
                    "Inuzuka"

                },


                "Bonus":
                {

                    "Speed":20,

                    "Senses":30

                }

            },







            "Body Expansion":
            {

                "Type":
                "Akimichi Style",


                "Requirements":
                {

                    "Clan":
                    "Akimichi"

                },


                "Bonus":
                {

                    "Strength":40,

                    "Endurance":30

                }

            }

        }









    def get_style(
        self,
        name
    ):


        return self.styles.get(
            name
        )









    def learn_style(
        self,
        npc_name,
        style
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        data = self.get_style(
            style
        )


        if not data:

            return None





        requirements = data.get(
            "Requirements",
            {}
        )



        for key,value in requirements.items():


            if key == "Clan":


                if npc.get(
                    "Clan"
                ) != value:


                    return {


                        "Success":
                        False,


                        "Reason":
                        "Clan requirement failed"

                    }







        styles = npc.get(
            "TaijutsuStyles",
            []
        )



        if style not in styles:


            styles.append(
                style
            )



        npc["TaijutsuStyles"] = styles



        self.apply_bonus(
            npc,
            data
        )



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return {


            "Success":
            True,


            "Style":
            style

        }









    def apply_bonus(
        self,
        npc,
        data
    ):


        bonuses = data.get(
            "Bonus",
            {}
        )



        for stat,value in bonuses.items():


            npc[stat] = (

                npc.get(
                    stat,
                    0
                )

                +

                value

            )



        return npc









    def train_taijutsu(
        self,
        npc_name,
        amount
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        skills = npc.get(
            "Skills",
            {}
        )



        skills["Taijutsu"] = (

            skills.get(
                "Taijutsu",
                0
            )

            +

            amount

        )



        npc["Skills"] = skills



        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return skills["Taijutsu"]