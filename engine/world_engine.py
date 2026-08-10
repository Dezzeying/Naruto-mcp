from datetime import datetime


class WorldEngine:

    def __init__(self, memory):

        self.memory = memory

    def get_world_state(self):

        return self.memory.world.read()

    def update_world(self, **changes):

        self.memory.world.update(**changes)

    def add_event(self, event):

        timeline = self.memory.timeline.read()

        day = datetime.now().strftime("%Y-%m-%d")

        timeline[day] = event

        self.memory.timeline.update(**timeline)

    def world_report(self):

        return {
            "world": self.memory.world.read(),
            "timeline": self.memory.timeline.read()
        }