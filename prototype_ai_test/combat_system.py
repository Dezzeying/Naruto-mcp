import random

from jutsu_database import JUTSUS





class CombatSystem:



    def __init__(
        self,
        game
    ):

        self.game = game





    def create_enemy(
        self,
        name,
        hp,
        chakra,
        level
    ):


        return {


            "Name":
            name,


            "HP":
            hp,


            "Chakra":
            chakra,


            "Level":
            level,


            "Defense":
            10

        }








    def basic_attack(
        self,
        enemy
    ):


        player = self.game.get_player()



        damage = (

            player["Stats"]["Strength"]

            +

            random.randint(5,15)

        )



        enemy["HP"] -= damage



        return {


            "Action":
            "Basic Attack",


            "Damage":
            damage,


            "Enemy HP":
            enemy["HP"]

        }









    def use_jutsu(
        self,
        enemy,
        jutsu
    ):


        result = self.game.use_jutsu(
            jutsu
        )


        if isinstance(result,str):

            return result





        damage = result.get(
            "Damage",
            0
        )



        bonus = self.game.get_player()["Stats"].get(

            "Ninjutsu",

            0

        ) // 2




        total_damage = damage + bonus



        enemy["HP"] -= total_damage



        return {


            "Jutsu":
            jutsu,


            "Damage":
            total_damage,


            "Enemy HP":
            enemy["HP"],


            "Chakra":
            self.game.get_player()["Chakra"]

        }









    def enemy_attack(
        self,
        enemy
    ):


        player = self.game.get_player()



        damage = random.randint(

            5,

            15

        )



        player["HP"] -= damage



        return {


            "Enemy Attack":
            enemy["Name"],


            "Damage":
            damage,


            "Your HP":
            player["HP"]

        }









    def battle(
        self,
        enemy
    ):


        print(
            f"{enemy['Name']} saldırıyor!"
        )


        while enemy["HP"] > 0 and self.game.get_player()["HP"] > 0:


            print(

                """
1 - Normal saldırı
2 - Jutsu kullan
"""

            )


            choice=input(
                "Seçim: "
            )



            if choice=="1":

                print(
                    self.basic_attack(
                        enemy
                    )
                )



            elif choice=="2":


                print(
                    self.game.get_player()["Jutsu"]
                )


                jutsu=input(
                    "Jutsu: "
                )


                print(

                    self.use_jutsu(

                        enemy,

                        jutsu

                    )

                )




            if enemy["HP"] <= 0:

                return {


                    "Result":
                    "Victory",


                    "Enemy":
                    enemy["Name"]

                }





            print(
                self.enemy_attack(
                    enemy
                )
            )



        return {


            "Result":
            "Defeat"

        }