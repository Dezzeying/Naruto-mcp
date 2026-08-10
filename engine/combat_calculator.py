class CombatCalculator:



    def __init__(
        self
    ):

        pass






    def get_stat(
        self,
        npc,
        stat
    ):


        return npc.get(
            stat,
            0
        )








    def get_skill(
        self,
        npc,
        skill
    ):


        skills = npc.get(
            "Skills",
            {}
        )


        return skills.get(
            skill,
            0
        )









    def calculate_ninjutsu_power(
        self,
        npc,
        jutsu_power
    ):


        chakra = self.get_stat(
            npc,
            "Chakra"
        )


        ninjutsu = self.get_skill(
            npc,
            "Ninjutsu"
        )


        control = self.get_stat(
            npc,
            "ChakraControl"
        )



        return (

            jutsu_power

            +

            chakra * 0.3

            +

            ninjutsu * 0.5

            +

            control * 0.2

        )









    def calculate_taijutsu_power(
        self,
        npc
    ):


        strength = self.get_stat(
            npc,
            "Strength"
        )


        speed = self.get_stat(
            npc,
            "Speed"
        )


        taijutsu = self.get_skill(
            npc,
            "Taijutsu"
        )



        return (

            strength * 0.5

            +

            speed * 0.3

            +

            taijutsu * 0.7

        )









    def calculate_kenjutsu_power(
        self,
        npc
    ):


        weapon = npc.get(
            "CurrentWeapon"
        )


        kenjutsu = self.get_skill(
            npc,
            "Kenjutsu"
        )


        strength = self.get_stat(
            npc,
            "Strength"
        )



        return (

            kenjutsu * 0.8

            +

            strength * 0.3

        )









    def calculate_genjutsu_power(
        self,
        npc
    ):


        genjutsu = self.get_skill(
            npc,
            "Genjutsu"
        )


        intelligence = self.get_stat(
            npc,
            "Intelligence"
        )



        dojutsu = npc.get(
            "Dojutsu",
            {}
        )



        bonus = 0



        for eye in dojutsu.values():


            if eye:


                if eye.get(
                    "Type"
                ) == "Sharingan":


                    bonus += 40





        return (

            genjutsu

            +

            intelligence * 0.5

            +

            bonus

        )









    def calculate_defense(
        self,
        npc
    ):


        endurance = self.get_stat(
            npc,
            "Endurance"
        )


        chakra = self.get_stat(
            npc,
            "ChakraControl"
        )


        return (

            endurance * 0.6

            +

            chakra * 0.4

        )