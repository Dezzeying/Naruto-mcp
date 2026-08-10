import json


class WorldState:


    def __init__(
        self,
        memory
    ):

        self.memory = memory



    def get_world(self):

        world = self.memory.world.read()


        if not world:

            world = {

                "Year": 0,

                "VillageStatus":
                {
                    "Konoha":
                    "Peaceful"
                },


                "Wars":
                [],


                "Events":
                [],


                "Characters":
                {},


                "UnlockedSecrets":
                []

            }


            self.memory.world.update(
                **{
                    "data":
                    json.dumps(
                        world,
                        ensure_ascii=False
                    )
                }
            )


        else:

            world = json.loads(
                world["data"]
            )


        return world





    def save_world(
        self,
        world
    ):


        self.memory.world.update(
            **{
                "data":
                json.dumps(
                    world,
                    ensure_ascii=False
                )
            }
        )





    def advance_time(
        self,
        amount=1
    ):


        world = self.get_world()


        world["Year"] += amount


        self.save_world(
            world
        )


        return world["Year"]





    def add_event(
        self,
        event_name,
        description
    ):


        world = self.get_world()


        event = {

            "Name":
            event_name,


            "Description":
            description,


            "Year":
            world["Year"]

        }


        world["Events"].append(
            event
        )


        self.save_world(
            world
        )


        return event





    def change_village_status(
        self,
        village,
        status
    ):


        world = self.get_world()


        world["VillageStatus"][village] = status


        self.save_world(
            world
        )


        return status





    def set_character_state(
        self,
        character,
        state
    ):


        world = self.get_world()


        world["Characters"][character] = state


        self.save_world(
            world
        )





    def get_character_state(
        self,
        character
    ):


        world = self.get_world()


        return world["Characters"].get(
            character,
            None
        )





    def unlock_secret(
        self,
        secret
    ):


        world = self.get_world()


        if secret not in world["UnlockedSecrets"]:

            world["UnlockedSecrets"].append(
                secret
            )


        self.save_world(
            world
        )


        return secret