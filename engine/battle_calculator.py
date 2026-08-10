class BattleCalculator:


    def __init__(
        self,
        taijutsu_system,
        ninjutsu_system,
        genjutsu_system,
        kenjutsu_system
    ):


        self.taijutsu_system = taijutsu_system

        self.ninjutsu_system = ninjutsu_system

        self.genjutsu_system = genjutsu_system

        self.kenjutsu_system = kenjutsu_system





    def calculate_battle_power(
        self,
        npc
    ):


        total_power = 0



        taijutsu = self.taijutsu_system.calculate(
            npc
        )


        ninjutsu = self.ninjutsu_system.calculate(
            npc
        )


        genjutsu = self.genjutsu_system.calculate(
            npc
        )


        kenjutsu = self.kenjutsu_system.calculate(
            npc
        )




        total_power += (
            taijutsu * 0.30
        )


        total_power += (
            ninjutsu * 0.35
        )


        total_power += (
            genjutsu * 0.15
        )


        total_power += (
            kenjutsu * 0.20
        )



        return {


            "TotalPower":
            total_power,


            "Breakdown":
            {

                "Taijutsu":
                taijutsu,


                "Ninjutsu":
                ninjutsu,


                "Genjutsu":
                genjutsu,


                "Kenjutsu":
                kenjutsu

            }

        }






    def compare(
        self,
        fighter1,
        fighter2
    ):


        power1 = self.calculate_battle_power(
            fighter1
        )


        power2 = self.calculate_battle_power(
            fighter2
        )



        if power1["TotalPower"] > power2["TotalPower"]:


            winner = fighter1["Name"]



        else:


            winner = fighter2["Name"]





        return {


            "Winner":
            winner,


            "Fighter1":
            power1,


            "Fighter2":
            power2

        }