import os
import json



class MemoryFile:



    def __init__(self, path):

        self.path = path

        if not os.path.exists(self.path):

            with open(
                self.path,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    {},
                    f,
                    ensure_ascii=False,
                    indent=4
                )





    def read(self):

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)





    def update(
        self,
        **data
    ):

        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )







class BaseMemory:



    def __init__(self):


        self.npcs = MemoryFile(

            "memory/npcs.json"

        )


        self.memories = MemoryFile(

            "memory/memories.json"

        )


        self.player = MemoryFile(

            "memory/player.json"

        )