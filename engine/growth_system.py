class GrowthSystem:


    def __init__(
        self,
        npc_engine
    ):

        self.npc_engine = npc_engine





    def calculate_growth(
        self,
        npc
    ):


        growth = 1



        # Doğal yetenek

        talent = npc.get(
            "Talent",
            50
        )


        growth += (
            talent / 100
        )



        # Eğitim disiplini

        discipline = npc.get(
            "Discipline",
            50
        )


        growth += (
            discipline / 200
        )



        # Klan avantajı

        clan_bonus = npc.get(
            "ClanBonus",
            0
        )


        growth += (
            clan_bonus / 100
        )



        return growth






    def train(
        self,
        name
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None



        multiplier = self.calculate_growth(
            npc
        )



        experience_gain = int(
            1 * multiplier
        )


        chakra_gain = int(
            1 * multiplier
        )



        npc["Experience"] = (
            npc.get(
                "Experience",
                0
            )
            +
            experience_gain
        )



        npc["ChakraControl"] = (
            npc.get(
                "ChakraControl",
                0
            )
            +
            chakra_gain
        )



        self.npc_engine.create_npc(
            name,
            **npc
        )



        return {

            "NPC":
            name,

            "ExperienceGain":
            experience_gain,

            "ChakraGain":
            chakra_gain

        }