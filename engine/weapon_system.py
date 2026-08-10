class WeaponSystem:



    def __init__(
        self,
        npc_engine
    ):


        self.npc_engine = npc_engine




        self.weapon_database = {



            "Kunai":
            {

                "Type":
                "Basic Weapon",


                "Damage":
                10,


                "Bonus":
                {

                    "WeaponSkill":5

                }

            },





            "Shuriken":
            {

                "Type":
                "Projectile",


                "Damage":
                8,


                "Bonus":
                {

                    "Accuracy":10

                }

            },






            "Samehada":
            {

                "Type":
                "Legendary",


                "Damage":
                40,


                "Abilities":
                [

                    "Chakra Absorption",

                    "Self Healing"

                ],


                "Compatibility":
                [

                    "High Chakra Users"

                ]

            },







            "Kubikiribocho":
            {

                "Type":
                "Legendary",


                "Damage":
                50,


                "Abilities":
                [

                    "Blood Regeneration"

                ],


                "Bonus":
                {

                    "Strength":30

                }

            },







            "Kusanagi":
            {

                "Type":
                "Legendary",


                "Damage":
                45,


                "Abilities":
                [

                    "Sharp Blade",

                    "Chakra Conduction"

                ],


                "Bonus":
                {

                    "Kenjutsu":35

                }

            },







            "Gunbai":
            {

                "Type":
                "Legendary",


                "Damage":
                35,


                "Abilities":
                [

                    "Chakra Reflection"

                ],


                "Bonus":
                {

                    "Defense":40

                }

            }



        }







    def get_weapon(
        self,
        name
    ):


        return self.weapon_database.get(
            name
        )








    def equip_weapon(
        self,
        npc_name,
        weapon
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None





        if weapon not in self.weapon_database:

            return {


                "Success":
                False,


                "Reason":
                "Weapon not found"

            }






        weapons = npc.get(
            "Weapons",
            []
        )



        if weapon not in weapons:


            weapons.append(
                weapon
            )



        npc["Weapons"] = weapons



        npc["CurrentWeapon"] = weapon





        self.apply_weapon_bonus(
            npc,
            weapon
        )





        self.npc_engine.create_npc(
            npc_name,
            **npc
        )



        return {


            "Success":
            True,


            "Weapon":
            weapon

        }









    def apply_weapon_bonus(
        self,
        npc,
        weapon
    ):


        data = self.get_weapon(
            weapon
        )



        if not data:

            return npc





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









    def has_weapon(
        self,
        npc,
        weapon
    ):


        return weapon in npc.get(
            "Weapons",
            []
        )








    def weapon_attack_power(
        self,
        npc
    ):


        weapon = npc.get(
            "CurrentWeapon"
        )



        if not weapon:

            return 0





        data = self.get_weapon(
            weapon
        )



        return data.get(
            "Damage",
            0
        )