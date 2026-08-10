class WorldMemory:


    def __init__(
        self,
        memory
    ):

        self.memory = memory





    def add_event(
        self,
        event_name,
        data=None
    ):


        events = self.memory.world_events.read()



        events.append(

            {

                "Event":
                event_name,


                "Data":
                data or {}

            }

        )


        self.memory.world_events.update(
            events
        )



        return True





    def get_events(
        self
    ):


        return self.memory.world_events.read()






    def has_event(
        self,
        event_name
    ):


        events = self.get_events()



        for event in events:


            if event["Event"] == event_name:

                return True



        return False





    def add_discovery(
        self,
        discovery
    ):


        discoveries = self.memory.discoveries.read()



        if discovery not in discoveries:


            discoveries.append(
                discovery
            )



        self.memory.discoveries.update(
            discoveries
        )


        return True






    def get_discoveries(
        self
    ):


        return self.memory.discoveries.read()