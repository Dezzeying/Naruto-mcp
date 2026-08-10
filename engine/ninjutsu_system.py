class NinjutsuSystem:


    def calculate(
        self,
        npc
    ):


        stats = npc.get(
            "Stats",
            {}
        )


        skills = npc.get(
            "Skills",
            {}
        )



        chakra = stats.get(
            "Chakra",
            0
        )


        control = stats.get(
            "ChakraControl",
            0
        )


        ninjutsu_skill = skills.get(
            "Ninjutsu",
            0
        )



        power = (

            chakra * 0.35

            +

            control * 0.30

            +

            ninjutsu_skill * 0.35

        )



        power += self.calculate_nature_bonus(
            npc
        )


        power += self.calculate_special_bonus(
            npc
        )


        return power






    def calculate_nature_bonus(
        self,
        npc
    ):


        bonus = 0



        nature = npc.get(
            "Nature",
            []
        )



        if "Fire" in nature:

            bonus += 10



        if "Wind" in nature:

            bonus += 10



        if "Lightning" in nature:

            bonus += 10



        if "Water" in nature:

            bonus += 10



        if "Earth" in nature:

            bonus += 10



        return bonus






    def calculate_special_bonus(
        self,
        npc
    ):


        bonus = 0



        abilities = npc.get(
            "Abilities",
            []
        )



        if "Sharingan" in abilities:

            bonus += 20



        if "Sage Mode" in abilities:

            bonus += 40



        if "Tailed Beast Chakra" in abilities:

            bonus += 50



        if "Six Paths Power" in abilities:

            bonus += 100



        return bonus