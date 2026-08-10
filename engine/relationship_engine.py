class RelationshipEngine:



    def __init__(
        self,
        npc_engine
    ):

        self.npc_engine = npc_engine





    def get_relationship(
        self,
        character1,
        character2
    ):


        npc = self.npc_engine.get_npc(
            character1
        )


        if not npc:

            return None



        relationships = npc.get(
            "Relationships",
            {}
        )


        return relationships.get(
            character2,
            {

                "Friendship":0,

                "Trust":0,

                "Respect":0,

                "Fear":0,

                "Rivalry":0

            }
        )







    def create_relationship(
        self,
        character1,
        character2
    ):


        npc = self.npc_engine.get_npc(
            character1
        )


        if not npc:

            return None



        relationships = npc.get(
            "Relationships",
            {}
        )


        if character2 not in relationships:


            relationships[character2] = {


                "Friendship":0,


                "Trust":0,


                "Respect":0,


                "Fear":0,


                "Rivalry":0


            }



        npc["Relationships"] = relationships



        self.npc_engine.create_npc(
            character1,
            **npc
        )


        return relationships[character2]







    def change_relationship(
        self,
        character1,
        character2,
        stat,
        amount
    ):


        npc = self.npc_engine.get_npc(
            character1
        )


        if not npc:

            return None




        relationships = npc.get(
            "Relationships",
            {}
        )



        if character2 not in relationships:


            self.create_relationship(
                character1,
                character2
            )


            npc = self.npc_engine.get_npc(
                character1
            )


            relationships = npc.get(
                "Relationships",
                {}
            )





        relation = relationships[character2]



        relation[stat] = max(

            0,

            min(

                100,

                relation.get(
                    stat,
                    0
                )
                +
                amount

            )

        )



        npc["Relationships"] = relationships



        self.npc_engine.create_npc(
            character1,
            **npc
        )



        return relation







    def get_reaction(
        self,
        character,
        target
    ):


        relation = self.get_relationship(
            character,
            target
        )



        if not relation:

            return "Unknown"




        friendship = relation.get(
            "Friendship",
            0
        )


        trust = relation.get(
            "Trust",
            0
        )


        rivalry = relation.get(
            "Rivalry",
            0
        )




        if trust >= 80:

            return "Trusted Ally"



        if friendship >= 70:

            return "Friend"



        if rivalry >= 70:

            return "Rival"



        if friendship <= 20:

            return "Stranger"



        return "Neutral"





    def add_memory(
        self,
        character,
        event
    ):


        npc = self.npc_engine.get_npc(
            character
        )


        if not npc:

            return None



        memories = npc.get(
            "RelationshipMemories",
            []
        )



        memories.append(
            event
        )



        npc["RelationshipMemories"] = memories



        self.npc_engine.create_npc(
            character,
            **npc
        )


        return event