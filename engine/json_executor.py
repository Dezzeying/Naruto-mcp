class JSONExecutor:

    def __init__(self, controller):
        self.controller = controller

    def execute(self, data: dict):

        updates = data.get("updates", {})

        if updates:
            self.controller.apply(updates)

        campaign = data.get("campaign")

        if campaign:

            self.controller.memory.campaign.append(
                campaign.get("player", ""),
                campaign.get("assistant", "")
            )