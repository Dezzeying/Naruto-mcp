class CombatEngine:



    def __init__(
        self,
        npc_engine,
        jutsu_engine,
        calculator,
        nature_system,
        weapon_system
    ):


        self.npc_engine = npc_engine

        self.jutsu_engine = jutsu_engine

        self.calculator = calculator

        self.nature_system = nature_system

        self.weapon_system = weapon_system







    def attack(
        self,
        attacker_name,
        target_name,
        attack_type,
        technique=None
    ):


        attacker = self.npc_engine.get_npc(
            attacker_name
        )


        target = self.npc_engine.get_npc(
            target_name
        )



        if not attacker or not target:

            return None





        damage = 0





        if attack_type == "Ninjutsu":


            jutsu = self.jutsu_engine.get_jutsu(
                technique
            )


            if not jutsu:

                return {


                    "Success":
                    False,


                    "Reason":
                    "Jutsu not found"

                }





            damage = self.calculator.calculate_ninjutsu_power(
                attacker,
                jutsu.get(
                    "Power",
                    0
                )
            )








        elif attack_type == "Taijutsu":


            damage = self.calculator.calculate_taijutsu_power(
                attacker
            )







        elif attack_type == "Kenjutsu":


            damage = self.calculator.calculate_kenjutsu_power(
                attacker
            )



            damage += self.weapon_system.weapon_attack_power(
                attacker
            )








        elif attack_type == "Genjutsu":


            damage = self.calculator.calculate_genjutsu_power(
                attacker
            )








        defense = self.calculator.calculate_defense(
            target
        )





        final_damage = max(

            int(damage - defense),

            0

        )






        target["HP"] = (

            target.get(
                "HP",
                100
            )

            -

            final_damage

        )





        self.npc_engine.create_npc(
            target_name,
            **target
        )





        return {


            "Success":
            True,


            "Attacker":
            attacker_name,


            "Target":
            target_name,


            "Type":
            attack_type,


            "Technique":
            technique,


            "Damage":
            final_damage,


            "RemainingHP":
            target["HP"]

        }