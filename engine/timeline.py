class Timeline:


    def __init__(
        self,
        memory
    ):

        self.memory = memory



    def get_time(
        self
    ):


        data = self.memory.timeline.read()


        return {

            "Year":
            data.get(
                "Year",
                0
            ),


            "Month":
            data.get(
                "Month",
                1
            ),


            "Day":
            data.get(
                "Day",
                1
            ),


            "Era":
            data.get(
                "Era",
                "Unknown"
            )

        }






    def set_time(
        self,
        year,
        month=1,
        day=1,
        era=None
    ):


        data = {


            "Year":
            year,


            "Month":
            month,


            "Day":
            day,


            "Era":
            era

        }


        self.memory.timeline.update(
            **data
        )


        return data








    def advance_day(
        self,
        amount=1
    ):


        current = self.get_time()



        current["Day"] += amount



        while current["Day"] > 30:


            current["Day"] -= 30

            current["Month"] += 1





        while current["Month"] > 12:


            current["Month"] -= 12

            current["Year"] += 1





        self.set_time(
            current["Year"],
            current["Month"],
            current["Day"],
            current["Era"]
        )


        return current







    def get_current_event(
        self
    ):


        time = self.get_time()


        year = time["Year"]



        events = {



            0:
            "Academy Era",



            1:
            "Team Formation Era",



            2:
            "Chunin Exam Era",



            3:
            "Sasuke Departure Era",



            4:
            "Training Era",



            5:
            "Shippuden Era"

        }



        return events.get(
            year,
            "Unknown Era"
        )