class KenjutsuSystem:



    def __init__(
        self,
        npc_engine,
        weapon_system
    ):


        self.npc_engine = npc_engine

        self.weapon_system = weapon_system





        self.styles = {


            "Basic Sword Style":
            {

                "Bonus":
                {

                    "Kenjutsu":10,

                    "Accuracy":5

                }

            },





            "Mist Sword Style":
            {

                "Bonus":
                {

                    "Kenjutsu":25,

                    "Speed":15

                },


                "Village":
                "Kirigakure"

            },







            "Seven Swords Style":
            {

                "Bonus":
                {

                    "Kenjutsu":50,

                    "Speed":30

                },


                "Requirement":
                "Multiple Weapons"

            },







            "Samurai Iaido":
            {

                "Bonus":
                {

                    "Kenjutsu":45,

                    "Precision":35

                },


                "Village":
                "Land of Iron"

            },







            "Lightning Blade Style":
            {

                "Bonus":
                {

                    "Kenjutsu":35,

                    "LightningAffinity":20

                },


                "Requirement":
                "Lightning Nature"

            }

        }









    def get_style(
        self,
        style
    ):


        return self.styles.get(
            style
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





        if "Village" in data:


            if npc.get(
                "Village"
            ) != data["Village"]:


                return {


                    "Success":
                    False,


                    "Reason":
                    "Village requirement failed"

                }







        styles = npc.get(
            "KenjutsuStyles",
            []
        )



        if style not in styles:


            styles.append(
                style
            )



        npc["KenjutsuStyles"] = styles





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









    def train_kenjutsu(
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



        skills["Kenjutsu"] = (

            skills.get(
                "Kenjutsu",
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



        return skills["Kenjutsu"]