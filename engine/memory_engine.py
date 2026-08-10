import json
import time



class MemoryEngine:



    def __init__(
        self,
        memory
    ):

        self.memory = memory






    def add_memory(
        self,
        npc_name,
        event,
        importance=1
    ):


        memories = self.get_memories(
            npc_name
        )


        memory = {


            "Event":
            event,


            "Importance":
            importance,


            "Time":
            time.time()

        }



        memories.append(
            memory
        )



        self.save_memories(
            npc_name,
            memories
        )



        return memory







    def get_memories(
        self,
        npc_name
    ):


        data = self.memory.memories.read()


        npc_memory = data.get(
            npc_name
        )



        if not npc_memory:

            return []



        return json.loads(
            npc_memory
        )








    def save_memories(
        self,
        npc_name,
        memories
    ):


        data = self.memory.memories.read()



        data[npc_name] = json.dumps(
            memories,
            ensure_ascii=False
        )



        self.memory.memories.update(
            **data
        )









    def search_memory(
        self,
        npc_name,
        keyword
    ):


        memories = self.get_memories(
            npc_name
        )



        results = []



        for memory in memories:


            if keyword.lower() in memory["Event"].lower():

                results.append(
                    memory
                )



        return results







    def get_important_memories(
        self,
        npc_name,
        minimum=5
    ):


        memories = self.get_memories(
            npc_name
        )



        important = []



        for memory in memories:


            if memory["Importance"] >= minimum:

                important.append(
                    memory
                )



        return important







    def create_relationship_memory(
        self,
        npc_name,
        other,
        event
    ):


        text = (
            other
            +
            " ile ilgili: "
            +
            event
        )



        return self.add_memory(
            npc_name,
            text,
            importance=7
        )