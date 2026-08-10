from data.jutsu_database import JUTSU_DATABASE




class JutsuEngine:



    def __init__(
        self,
        npc_engine
    ):

        self.npc_engine = npc_engine

        self.jutsu_database = JUTSU_DATABASE







    def get_jutsu(
        self,
        name
    ):

        return self.jutsu_database.get(
            name
        )










    def get_stat(
        self,
        npc,
        stat
    ):


        return npc.get(
            "Stats",
            {}
        ).get(
            stat,
            0
        )











    def can_learn_jutsu(
        self,
        npc,
        jutsu
    ):


        data = self.get_jutsu(
            jutsu
        )


        if not data:

            return False





        requirements = data.get(
            "Requirements",
            {}
        )





        for key,value in requirements.items():




            # Clan

            if key == "Clan":


                if npc.get(
                    "Clan"
                ) != value:


                    return False





            # Nature

            elif key == "Nature":


                if value not in npc.get(
                    "Nature",
                    []
                ):


                    return False





            # Stats

            elif self.get_stat(
                npc,
                key
            ) < value:



                skill_value = npc.get(
                    "Skills",
                    {}
                ).get(
                    key,
                    0
                )


                if skill_value < value:


                    return False





        return True











    def learn_jutsu(
        self,
        name,
        jutsu
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None





        if not self.can_learn_jutsu(
            npc,
            jutsu
        ):


            return {


                "Success":
                False,


                "Reason":
                "Requirements not met"

            }







        jutsus = npc.get(
            "Jutsu",
            []
        )



        if jutsu not in jutsus:

            jutsus.append(
                jutsu
            )



        npc["Jutsu"] = jutsus





        mastery = npc.get(
            "JutsuMastery",
            {}
        )


        mastery[jutsu] = 1



        npc["JutsuMastery"] = mastery






        self.npc_engine.create_npc(

            name,

            **npc

        )



        return {


            "Success":
            True,


            "Learned":
            jutsu

        }









    def increase_mastery(
        self,
        name,
        jutsu,
        amount
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None





        mastery = npc.get(
            "JutsuMastery",
            {}
        )



        current = mastery.get(
            jutsu,
            0
        )



        mastery[jutsu] = min(

            current + amount,

            100

        )



        npc["JutsuMastery"] = mastery




        self.npc_engine.create_npc(

            name,

            **npc

        )



        return mastery[jutsu]









    def get_mastery(
        self,
        npc,
        jutsu
    ):


        return npc.get(
            "JutsuMastery",
            {}
        ).get(
            jutsu,
            0
        )











    def has_jutsu(
        self,
        npc,
        jutsu
    ):


        return jutsu in npc.get(
            "Jutsu",
            []
        )









    def get_all_jutsu(
        self
    ):


        return list(
            self.jutsu_database.keys()
        )