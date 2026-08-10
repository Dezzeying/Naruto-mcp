from data.clan_database import CLAN_DATABASE




class ClanEngine:



    def __init__(
        self,
        npc_engine
    ):

        self.npc_engine = npc_engine

        self.clans = CLAN_DATABASE







    def get_clan_data(
        self,
        clan
    ):

        return self.clans.get(
            clan
        )









    def apply_clan(
        self,
        name,
        clan
    ):


        npc = self.npc_engine.get_npc(
            name
        )


        if not npc:

            return None




        data = self.get_clan_data(
            clan
        )


        if not data:

            return None





        # =====================
        # CLAN
        # =====================


        npc["Clan"] = clan





        # =====================
        # BLOODLINE
        # =====================


        if "Bloodline" in data:

            npc["Bloodline"] = data["Bloodline"]







        # =====================
        # STAT BONUSLARI
        # =====================


        stats = npc.get(
            "Stats",
            {}
        )


        for stat,value in data.get(
            "BaseStats",
            {}
        ).items():


            stats[stat] = (

                stats.get(
                    stat,
                    0
                )

                +

                value

            )



        npc["Stats"] = stats







        # =====================
        # POTENTIAL ABILITIES
        # =====================


        potentials = npc.get(
            "PotentialAbilities",
            []
        )


        for ability in data.get(
            "PotentialAbilities",
            []
        ):


            if ability not in potentials:

                potentials.append(
                    ability
                )



        npc["PotentialAbilities"] = potentials







        # =====================
        # NATURE
        # =====================


        nature = npc.get(
            "Nature",
            []
        )


        for element in data.get(
            "NatureAffinity",
            []
        ):


            if element not in nature:

                nature.append(
                    element
                )



        npc["Nature"] = nature







        # =====================
        # SPECIALTIES
        # =====================


        specialties = npc.get(
            "Specialties",
            []
        )


        for specialty in data.get(
            "Specialties",
            []
        ):


            if specialty not in specialties:

                specialties.append(
                    specialty
                )



        npc["Specialties"] = specialties







        # =====================
        # TRAITS
        # =====================


        traits = npc.get(
            "Traits",
            []
        )


        for trait in data.get(
            "Traits",
            []
        ):


            if trait not in traits:

                traits.append(
                    trait
                )



        npc["Traits"] = traits







        # =====================
        # CLAN TEKNİK POTANSİYELİ
        # =====================


        clan_techniques = npc.get(
            "ClanTechniques",
            []
        )


        for technique in data.get(
            "HiddenJutsu",
            []
        ):


            if technique not in clan_techniques:

                clan_techniques.append(
                    technique
                )



        npc["ClanTechniques"] = clan_techniques






        self.npc_engine.create_npc(

            name,

            **npc

        )



        return npc










    def has_clan_ability(
        self,
        npc,
        ability
    ):


        return ability in npc.get(
            "Abilities",
            []
        )










    def has_potential(
        self,
        npc,
        ability
    ):


        return ability in npc.get(
            "PotentialAbilities",
            []
        )










    def get_all_clans(
        self
    ):


        return list(
            self.clans.keys()
        )










    def clan_exists(
        self,
        clan
    ):


        return clan in self.clans