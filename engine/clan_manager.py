import json





class ClanManager:



    def __init__(
        self,
        memory
    ):


        self.memory = memory







    def create_clan(
        self,
        name,
        village,
        population=0,
        status="Active"
    ):


        clans = self.memory.clans.read()



        clan = {


            "Name":
            name,


            "Village":
            village,


            "Population":
            population,


            "Status":
            status,


            "Members":
            [],


            "Relations":
            {}

        }



        clans[name] = json.dumps(
            clan,
            ensure_ascii=False
        )



        self.memory.clans.update(
            **clans
        )



        return clan







    def get_clan(
        self,
        name
    ):


        clans = self.memory.clans.read()



        data = clans.get(
            name
        )


        if not data:

            return None



        return json.loads(
            data
        )








    def add_member(
        self,
        clan,
        npc_name
    ):


        data = self.get_clan(
            clan
        )


        if not data:

            return None




        members = data.get(
            "Members",
            []
        )



        if npc_name not in members:


            members.append(
                npc_name
            )



        data["Members"] = members



        data["Population"] = len(
            members
        )



        self.save_clan(
            clan,
            data
        )



        return data







    def remove_member(
        self,
        clan,
        npc_name
    ):


        data = self.get_clan(
            clan
        )


        if not data:

            return None



        members = data.get(
            "Members",
            []
        )



        if npc_name in members:


            members.remove(
                npc_name
            )



        data["Members"] = members



        data["Population"] = len(
            members
        )



        self.save_clan(
            clan,
            data
        )



        return data









    def change_population(
        self,
        clan,
        amount
    ):


        data = self.get_clan(
            clan
        )


        if not data:

            return None




        data["Population"] = (

            data.get(
                "Population",
                0
            )

            +

            amount

        )




        if data["Population"] <= 0:


            data["Population"] = 0


            data["Status"] = "Extinct"




        self.save_clan(
            clan,
            data
        )



        return data







    def set_relation(
        self,
        clan,
        target,
        value
    ):


        data = self.get_clan(
            clan
        )


        if not data:

            return None



        relations = data.get(
            "Relations",
            {}
        )



        relations[target] = value



        data["Relations"] = relations



        self.save_clan(
            clan,
            data
        )



        return data









    def get_relation(
        self,
        clan,
        target
    ):


        data = self.get_clan(
            clan
        )


        if not data:

            return None



        return data.get(
            "Relations",
            {}
        ).get(
            target,
            0
        )








    def save_clan(
        self,
        name,
        data
    ):


        clans = self.memory.clans.read()



        clans[name] = json.dumps(
            data,
            ensure_ascii=False
        )



        self.memory.clans.update(
            **clans
        )







    def get_all_clans(
        self
    ):


        clans = self.memory.clans.read()



        return list(
            clans.keys()
        )