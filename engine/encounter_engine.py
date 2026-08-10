import random



class EncounterEngine:


    def __init__(
        self,
        npc_engine,
        memory
    ):

        self.npc_engine = npc_engine

        self.memory = memory




    def check_encounter(
        self,
        player
    ):


        encounters = []


        location = player.get(
            "Location"
        )


        year = player.get(
            "Year",
            0
        )



        if location == "Training Ground":


            encounters.extend(
                self.training_ground_events(
                    year
                )
            )



        return encounters





    def training_ground_events(
        self,
        year
    ):


        results = []



        # Naruto'nun Rasenshuriken dönemi


        if year >= 5:


            chance = random.randint(
                1,
                100
            )


            if chance <= 15:


                results.append(

                    {

                        "Type":
                        "NPC Encounter",

                        "NPC":
                        "Naruto",

                        "Event":
                        "Wind Training"

                    }

                )



            if chance <= 5:


                results.append(

                    {

                        "Type":
                        "Special Encounter",

                        "NPC":
                        "Naruto",

                        "Event":
                        "Rasenshuriken Development"

                    }

                )




        # Kakashi Chidori dönemi


        if year >= 1:


            chance = random.randint(
                1,
                100
            )


            if chance <= 10:


                results.append(

                    {

                        "Type":
                        "NPC Encounter",

                        "NPC":
                        "Kakashi Hatake",

                        "Event":
                        "Chidori Training"

                    }

                )



        return results