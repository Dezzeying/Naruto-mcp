class ChakraEngine:

    def __init__(self, memory):

        self.memory = memory


    def set_chakra(self, name, amount):

        npc = self.memory.npc_engine.get_npc(name)

        if not npc:
            return None


        npc["Chakra"] = amount


        return self.memory.npc_engine.create_npc(
            name,
            **npc
        )


    def increase_chakra(self, name, amount):

        npc = self.memory.npc_engine.get_npc(name)

        if not npc:
            return None


        current = npc.get(
            "Chakra",
            0
        )


        npc["Chakra"] = current + amount


        return self.memory.npc_engine.create_npc(
            name,
            **npc
        )


    def get_chakra(self, name):

        npc = self.memory.npc_engine.get_npc(name)

        if not npc:
            return 0


        return npc.get(
            "Chakra",
            0
        )