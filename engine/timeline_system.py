class TimelineSystem:



    def __init__(
        self
    ):


        self.timeline = {



            "Academy Era":
            {

                "Year":
                1,


                "Events":
                [

                    "Academy Training",

                    "Genin Graduation"

                ]

            },







            "Genin Era":
            {

                "Year":
                2,


                "Events":
                [

                    "Team Formation",

                    "D Rank Missions"

                ]

            },







            "Chunin Exam Era":
            {

                "Year":
                3,


                "Events":
                [

                    "Chunin Exams",

                    "Village Conflict"

                ]

            },







            "Akatsuki Era":
            {

                "Year":
                5,


                "Events":
                [

                    "Akatsuki Activities",

                    "Bijuu Hunting"

                ]

            },







            "War Era":
            {

                "Year":
                7,


                "Events":
                [

                    "Fourth Ninja War",

                    "Alliance Formation"

                ]

            }

        }






        self.current_era = "Academy Era"









    def get_current_era(
        self
    ):


        return self.current_era









    def change_era(
        self,
        era
    ):


        if era not in self.timeline:

            return {


                "Success":
                False,


                "Reason":
                "Era not found"

            }





        self.current_era = era



        return {


            "Success":
            True,


            "CurrentEra":
            era

        }









    def get_events(
        self,
        era
    ):


        data = self.timeline.get(
            era
        )


        if not data:

            return []



        return data.get(
            "Events",
            []
        )









    def add_event(
        self,
        era,
        event
    ):


        if era not in self.timeline:

            return False



        self.timeline[era]["Events"].append(
            event
        )



        return True