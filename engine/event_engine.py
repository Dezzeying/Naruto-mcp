class EventEngine:


    def __init__(
        self,
        world_events,
        encounter_engine,
        npc_engine,
        jutsu_system,
        memory=None
    ):

        self.world_events = world_events

        self.encounter_engine = encounter_engine

        self.npc_engine = npc_engine

        self.jutsu_system = jutsu_system

        self.memory = memory





    def process_year(
        self,
        year
    ):


        results = []


        events = self.world_events.get_events_for_year(
            year
        )


        for event in events:


            result = self.apply_world_event(
                event
            )


            results.append(
                result
            )



        return results






    def apply_world_event(
        self,
        event
    ):


        changes = event.get(
            "NPCChanges",
            {}
        )


        for npc,data in changes.items():


            self.npc_engine.update_npc(
                npc,
                **data
            )




        unlocks = event.get(
            "Unlocks",
            []
        )


        for jutsu in unlocks:


            self.jutsu_system.discover_jutsu(
                jutsu
            )



        return {

            "Event":
            event["Name"],

            "Applied":
            True

        }






    def check_player_encounters(
        self,
        player
    ):


        return self.encounter_engine.check_encounter(
            player
        )