import json
from copy import deepcopy

from engine.npc_schema import DEFAULT_NPC


class NPCEngine:

    def __init__(
        self,
        memory
    ):

        self.memory = memory

        self.clan_engine = None


    def connect_clan_engine(
        self,
        clan_engine
    ):

        self.clan_engine = clan_engine


    def create_npc(
        self,
        name,
        **data
    ):

        npcs = self.memory.npcs.read()

        npc = deepcopy(
            DEFAULT_NPC
        )

        npc.update(
            data
        )

        npc["Name"] = name

        npcs[name] = json.dumps(
            npc,
            ensure_ascii=False
        )

        self.memory.npcs.update(
            **npcs
        )

        return npc


    def create_npc_with_clan(
        self,
        name,
        clan,
        **data
    ):

        npc = self.create_npc(
            name,
            Clan=clan,
            **data
        )

        if self.clan_engine:

            npc = self.clan_engine.apply_clan(
                name,
                clan
            )

        return npc


    def get_npc(
        self,
        name
    ):

        npcs = self.memory.npcs.read()

        data = npcs.get(
            name
        )

        if not data:

            return None

        return json.loads(
            data
        )


    def update_npc(
        self,
        name,
        **changes
    ):

        npc = self.get_npc(
            name
        )

        if not npc:

            return None

        if "Experience" in changes:

            npc["Experience"] += changes["Experience"]

            del changes["Experience"]

        for key, value in changes.items():

            npc[key] = value

        return self.create_npc(
            name,
            **npc
        )


    def add_experience(
        self,
        name,
        amount
    ):

        npc = self.get_npc(
            name
        )

        if not npc:

            return None

        npc["Experience"] = (
            npc.get(
                "Experience",
                0
            )
            +
            amount
        )

        return self.create_npc(
            name,
            **npc
        )


    def add_ability(
        self,
        name,
        ability
    ):

        npc = self.get_npc(
            name
        )

        if not npc:

            return None

        abilities = npc.get(
            "Abilities",
            []
        )

        if ability not in abilities:

            abilities.append(
                ability
            )

        npc["Abilities"] = abilities

        return self.create_npc(
            name,
            **npc
        )


    def add_jutsu(
        self,
        name,
        jutsu
    ):

        npc = self.get_npc(
            name
        )

        if not npc:

            return None

        jutsus = npc.get(
            "Jutsu",
            []
        )

        if jutsu not in jutsus:

            jutsus.append(
                jutsu
            )

        npc["Jutsu"] = jutsus

        return self.create_npc(
            name,
            **npc
        )


    def add_memory(
        self,
        name,
        memory
    ):

        npc = self.get_npc(
            name
        )

        if not npc:

            return None

        memories = npc.get(
            "Memories",
            []
        )

        memories.append(
            memory
        )

        npc["Memories"] = memories

        return self.create_npc(
            name,
            **npc
        )