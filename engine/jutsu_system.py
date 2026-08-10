from ..data.jutsu_database import get_jutsu


class JutsuSystem:


    def __init__(
        self,
        memory
    ):

        self.memory = memory



    def get_status(
        self,
        jutsu
    ):


        jutsu_data = get_jutsu(
            jutsu
        )


        if not jutsu_data:

            return None



        discovered = self.memory.jutsus.read()


        return discovered.get(
            jutsu,
            "Locked"
        )





    def discover_jutsu(
        self,
        jutsu
    ):


        data = get_jutsu(
            jutsu
        )


        if not data:

            return False



        jutsus = self.memory.jutsus.read()


        jutsus[jutsu] = "Discovered"


        self.memory.jutsus.update(
            **jutsus
        )


        return True






    def unlock_jutsu(
        self,
        jutsu
    ):


        data = get_jutsu(
            jutsu
        )


        if not data:

            return False



        jutsus = self.memory.jutsus.read()


        jutsus[jutsu] = "Available"


        self.memory.jutsus.update(
            **jutsus
        )


        return True






    def can_be_learned(
        self,
        jutsu
    ):


        status = self.get_status(
            jutsu
        )


        if status != "Available":

            return False


        return True