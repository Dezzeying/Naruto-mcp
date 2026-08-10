# time_engine.py


class TimeEngine:


    def __init__(self, world_tick):


        self.world_tick = world_tick


        self.day = 1

        self.month = 1

        self.year = 0



    def advance_day(self):


        self.day += 1



        if self.day > 30:


            self.day = 1

            self.advance_month()




    def advance_month(self):


        self.month += 1



        if self.month > 12:


            self.month = 1

            self.advance_year()




    def advance_year(self):


        self.year += 1



        print(
            "\n===== NEW YEAR ====="
        )


        print(
            "Year:",
            self.year
        )



        self.world_tick.advance_year()




    def skip_days(
        self,
        amount
    ):


        for i in range(amount):


            self.advance_day()




    def get_date(self):


        return {

            "Day":
            self.day,


            "Month":
            self.month,


            "Year":
            self.year

        }