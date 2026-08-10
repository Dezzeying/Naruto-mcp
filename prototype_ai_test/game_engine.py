import json
import os

from database import CLANS
from jutsu_database import JUTSUS




class NarutoGame:



    def __init__(self):

        self.player = None

        self.save_folder = "saves"

        os.makedirs(
            self.save_folder,
            exist_ok=True
        )







    def create_character(
        self,
        name,
        clan,
        village
    ):



        clan_data = CLANS.get(
            clan,
            {}
        )



        self.player = {



            "Name":
            name,



            "Clan":
            clan,



            "Village":
            village,



            "Rank":
            "Academy Student",



            "Level":
            1,



            "Experience":
            0,



            "HP":
            100,



            "Chakra":
            100,



            "Stats":
            {


                "Strength":
                10,


                "Speed":
                10,


                "Intelligence":
                10,


                "ChakraControl":
                10,


                "Taijutsu":
                10,


                "Ninjutsu":
                10,


                "Genjutsu":
                10

            },



            "Abilities":
            [],



            "Jutsu":
            [],



            "Inventory":
            [

                "Kunai",

                "Shuriken",

                "Basic Ninja Bag"

            ],



            "Relationships":
            {},



            "Mission":
            None,


            "ClanData":
            clan_data

        }







        # Clan bonusları

        for stat,value in clan_data.get(
            "Bonuses",
            {}
        ).items():


            if stat in self.player["Stats"]:


                self.player["Stats"][stat] += value


            else:


                self.player[stat] = value







        # Clan yetenekleri

        self.player["Abilities"] = clan_data.get(
            "Abilities",
            []
        )







        # Başlangıç jutsuları

        for jutsu,data in JUTSUS.items():


            if data.get(
                "RequiredClan"
            ) == clan:


                self.player["Jutsu"].append(
                    jutsu
                )



        return self.player







    def get_player(
        self
    ):


        return self.player







    def update_stat(
        self,
        stat,
        amount
    ):


        if not self.player:

            return False



        if stat in self.player["Stats"]:


            self.player["Stats"][stat] += amount



        return True







    def add_jutsu(
        self,
        jutsu
    ):


        if jutsu not in self.player["Jutsu"]:


            self.player["Jutsu"].append(
                jutsu
            )








    def use_jutsu(
        self,
        jutsu
    ):


        if not self.player:


            return "Karakter yok."





        if jutsu not in self.player["Jutsu"]:


            return "Bu jutsuyu bilmiyorsun."





        data = JUTSUS.get(
            jutsu
        )



        if not data:


            return "Jutsu bulunamadı."





        cost = data.get(
            "ChakraCost",
            0
        )





        if self.player["Chakra"] < cost:


            return "Yeterli chakra yok."






        self.player["Chakra"] -= cost






        return {



            "Jutsu":

            jutsu,



            "Type":

            data.get(
                "Type"
            ),



            "Damage":

            data.get(
                "Damage",
                0
            ),



            "Effect":

            data.get(
                "Effect"
            ),



            "Remaining Chakra":

            self.player["Chakra"]

        }








    def add_experience(
        self,
        amount
    ):


        self.player["Experience"] += amount





        if self.player["Experience"] >= 100:


            self.player["Rank"] = "Genin"









    def train(
        self,
        stat
    ):


        if stat not in self.player["Stats"]:


            return "Stat bulunamadı."



        self.player["Stats"][stat] += 1



        self.player["Experience"] += 10



        return {


            "Training":

            stat,


            "New Value":

            self.player["Stats"][stat]

        }









    def save(
        self
    ):


        if not self.player:


            return False





        path = os.path.join(

            self.save_folder,

            "player.json"

        )





        with open(

            path,

            "w",

            encoding="utf-8"

        ) as file:


            json.dump(

                self.player,

                file,

                indent=4,

                ensure_ascii=False

            )



        return True







    def load(
        self
    ):


        path = os.path.join(

            self.save_folder,

            "player.json"

        )





        if not os.path.exists(
            path
        ):


            return False






        with open(

            path,

            "r",

            encoding="utf-8"

        ) as file:


            self.player = json.load(
                file
            )



        return self.player