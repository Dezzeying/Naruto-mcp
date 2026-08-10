class RelationshipSystem:



    def __init__(
        self,
        npc_engine
    ):


        self.npc_engine = npc_engine




        self.relationship_types = {



            "Friend":

            {

                "Min":
                50,


                "Effect":
                "Trust Increase"

            },





            "Rival":

            {

                "Min":
                30,


                "Effect":
                "Growth Bonus"

            },





            "Enemy":

            {

                "Max":
                -50,


                "Effect":
                "Hostility"

            },





            "Master":

            {

                "Effect":
                "Training Bonus"

            },





            "Student":

            {

                "Effect":
                "Learning Bonus"

            },





            "Family":

            {

                "Effect":
                "Blood Connection"

            }

        }








    def add_relationship(
        self,
        npc1,
        npc2,
        relation_type,
        value
    ):


        character = self.npc_engine.get_npc(
            npc1
        )


        if not character:

            return None





        relations = character.get(
            "Relationships",
            {}
        )



        relations[npc2] = {


            "Type":
            relation_type,


            "Value":
            value

        }



        character["Relationships"] = relations



        self.npc_engine.create_npc(
            npc1,
            **character
        )



        return relations[npc2]









    def get_relationship(
        self,
        npc1,
        npc2
    ):


        character = self.npc_engine.get_npc(
            npc1
        )


        if not character:

            return None



        return character.get(
            "Relationships",
            {}
        ).get(
            npc2
        )









    def change_relationship(
        self,
        npc1,
        npc2,
        amount
    ):


        relation = self.get_relationship(
            npc1,
            npc2
        )


        if not relation:

            return None





        relation["Value"] += amount



        relation["Value"] = max(

            min(

                relation["Value"],

                100

            ),

            -100

        )





        character = self.npc_engine.get_npc(
            npc1
        )


        character["Relationships"][npc2] = relation



        self.npc_engine.create_npc(
            npc1,
            **character
        )



        return relation







    def get_trust_level(
        self,
        npc1,
        npc2
    ):


        relation = self.get_relationship(
            npc1,
            npc2
        )


        if not relation:

            return 0



        return relation["Value"]







    def create_team(
        self,
        team_name,
        members
    ):


        return {


            "Team":
            team_name,


            "Members":
            members

        }