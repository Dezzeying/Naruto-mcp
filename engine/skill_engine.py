class SkillEngine:

    def __init__(self, memory):

        self.memory = memory



    def add_skill(self, name, skill):

        npc = self.memory.npc_engine.get_npc(
            name
        )

        if not npc:

            return None


        skills = npc.get(
            "Skills",
            []
        )


        if skill not in skills:

            skills.append(
                skill
            )


        npc["Skills"] = skills


        return self.memory.npc_engine.create_npc(
            name,
            **npc
        )



    def remove_skill(self, name, skill):

        npc = self.memory.npc_engine.get_npc(
            name
        )

        if not npc:

            return None


        skills = npc.get(
            "Skills",
            []
        )


        if skill in skills:

            skills.remove(
                skill
            )


        npc["Skills"] = skills


        return self.memory.npc_engine.create_npc(
            name,
            **npc
        )



    def has_skill(self, name, skill):

        npc = self.memory.npc_engine.get_npc(
            name
        )

        if not npc:

            return False


        return skill in npc.get(
            "Skills",
            []
        )



    def discover_skill(self, name):

        npc = self.memory.npc_engine.get_npc(
            name
        )

        if not npc:

            return None


        possible_skills = [

            "Basic Taijutsu",

            "Kunai Mastery",

            "Shadow Clone",

            "Fire Style",

            "Water Style",

            "Lightning Style",

            "Medical Ninjutsu",

            "Tracking",

            "Genjutsu"

        ]


        import random


        skill = random.choice(
            possible_skills
        )


        return self.add_skill(
            name,
            skill
        )