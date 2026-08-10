import random


class ElementEngine:

    ELEMENTS = [

        "Fire",

        "Water",

        "Wind",

        "Earth",

        "Lightning"

    ]


    def __init__(self, memory):

        self.memory = memory



    def discover_element(self, name):

        npc = self.memory.npc_engine.get_npc(name)


        if not npc:

            return None



        if npc.get("Elements"):

            return npc["Elements"]



        element = random.choice(
            self.ELEMENTS
        )


        npc["Elements"] = [

            element

        ]


        self.memory.npc_engine.create_npc(
            name,
            **npc
        )


        return npc["Elements"]



    def add_element(self, name, element):

        npc = self.memory.npc_engine.get_npc(name)


        if not npc:

            return None



        elements = npc.get(
            "Elements",
            []
        )


        if element not in elements:

            elements.append(
                element
            )


        npc["Elements"] = elements


        return self.memory.npc_engine.create_npc(
            name,
            **npc
        )