class GameEngine:



    def __init__(
        self,
        world_tick,
        npc_engine,
        training_engine,
        npc_simulator=None,
        mission_engine=None,
        relationship_engine=None,
        memory=None
    ):


        self.world_tick = world_tick

        self.npc_engine = npc_engine

        self.training_engine = training_engine

        self.npc_simulator = npc_simulator

        self.mission_engine = mission_engine

        self.relationship_engine = relationship_engine

        self.memory = memory







    def run_day(
        self
    ):


        result = {


            "Day":
            None,


            "Events":
            [],


            "NPC":
            [],


            "Training":
            [],


            "Missions":
            [],


            "Changes":
            []

        }







        # =====================
        # ZAMAN
        # =====================


        day = self.world_tick.advance()


        result["Day"] = day







        # =====================
        # DÜNYA EVENTLERİ
        # =====================


        events = self.world_tick.check_events(
            day
        )



        for event in events:


            result["Events"].append(

                event.get(
                    "Name"
                )

            )


            self.apply_event(
                event
            )











        # =====================
        # NPC GÜNLÜK HAYATI
        # =====================


        if self.npc_simulator:


            npcs = self.npc_engine.memory.npcs.read()



            for name in npcs.keys():


                npc_result = self.npc_simulator.simulate_day(

                    name

                )


                if npc_result:


                    result["NPC"].append(

                        npc_result

                    )











        # =====================
        # MEMORY
        # =====================


        if self.memory:


            self.memory.add_event(

                "World Day",

                result

            )





        return result











    def apply_event(
        self,
        event
    ):



        changes = event.get(

            "NPCChanges",

            {}

        )




        for npc_name,data in changes.items():


            self.npc_engine.update_npc(

                npc_name,

                **data

            )









        unlocks = event.get(

            "Unlocks",

            []

        )



        for ability in unlocks:


            self.handle_unlock(

                ability

            )









    def handle_unlock(
        self,
        ability
    ):


        # ileride global ability event sistemi

        pass