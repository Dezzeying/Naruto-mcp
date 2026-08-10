class TrainingEngine:



    def __init__(
        self,
        npc_engine,
        jutsu_engine=None
    ):


        self.npc_engine = npc_engine

        self.jutsu_engine = jutsu_engine







    def train_stat(
        self,
        name,
        stat,
        amount
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None






        stats = npc.get(
            "Stats",
            {}
        )



        stats[stat] = (

            stats.get(
                stat,
                0
            )

            +

            amount

        )



        npc["Stats"] = stats





        self.npc_engine.create_npc(

            name,

            **npc

        )



        return npc










    def train_skill(
        self,
        name,
        skill,
        amount
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None






        skills = npc.get(
            "Skills",
            {}
        )



        skills[skill] = (

            skills.get(
                skill,
                0
            )

            +

            amount

        )



        npc["Skills"] = skills






        self.npc_engine.create_npc(

            name,

            **npc

        )



        return npc










    def gain_experience(
        self,
        name,
        amount
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

            amount

        )



        self.npc_engine.create_npc(

            name,

            **npc

        )



        return npc










    def attempt_learn_jutsu(
        self,
        name,
        jutsu
    ):


        if not self.jutsu_engine:

            return None



        return self.jutsu_engine.learn_jutsu(

            name,

            jutsu

        )











    def practice_jutsu(
        self,
        name,
        jutsu,
        amount=5
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None





        if not self.jutsu_engine.has_jutsu(

            npc,

            jutsu

        ):


            return {


                "Success":
                False,


                "Reason":
                "Jutsu not known"

            }






        mastery = self.jutsu_engine.increase_mastery(

            name,

            jutsu,

            amount

        )



        return {


            "Success":
            True,


            "Jutsu":
            jutsu,


            "Mastery":
            mastery

        }









    def training_session(
        self,
        name,
        activity
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None






        training = npc.get(

            "Training",

            {}

        )



        completed = training.get(

            "Completed",

            []

        )



        completed.append(

            activity

        )



        training["Completed"] = completed



        npc["Training"] = training




        self.npc_engine.create_npc(

            name,

            **npc

        )



        return npc