class DojutsuSystem:



    def __init__(
        self,
        npc_engine,
        ability_system
    ):

        self.npc_engine = npc_engine

        self.ability_system = ability_system



        self.dojutsu_database = {


            "Sharingan":
            {

                "Stages":
                [

                    "1 Tomoe",

                    "2 Tomoe",

                    "3 Tomoe",

                    "Mangekyo Sharingan",

                    "Eternal Mangekyo Sharingan"

                ]

            },


            "Byakugan":
            {

                "Stages":
                [

                    "Byakugan",

                    "Advanced Byakugan"

                ]

            },


            "Rinnegan":
            {

                "Stages":
                [

                    "Rinnegan",

                    "Rinne Sharingan"

                ]

            }

        }







    def create_eye_data(
        self,
        eye_type,
        stage
    ):


        tomoe = 0


        if "1 Tomoe" in stage:

            tomoe = 1


        elif "2 Tomoe" in stage:

            tomoe = 2


        elif "3 Tomoe" in stage:

            tomoe = 3




        return {


            "Type":
            eye_type,


            "Stage":
            stage,


            "Tomoe":
            tomoe,


            "Abilities":
            []

        }










    def give_eye(
        self,
        npc_name,
        eye,
        side,
        stage
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None




        if "Dojutsu" not in npc:


            npc["Dojutsu"] = {


                "LeftEye": None,


                "RightEye": None

            }






        npc["Dojutsu"][side] = self.create_eye_data(

            eye,

            stage

        )




        # Göz açıldığında temel ability açılır

        if self.ability_system:


            self.ability_system.add_ability(

                npc_name,

                eye,

                reason="Dojutsu Awakening"

            )





        self.npc_engine.create_npc(

            npc_name,

            **npc

        )



        return npc["Dojutsu"][side]











    def remove_eye(
        self,
        npc_name,
        side
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None




        npc["Dojutsu"][side] = None




        self.npc_engine.create_npc(

            npc_name,

            **npc

        )



        return True










    def get_eye_count(
        self,
        npc,
        eye_type
    ):


        count = 0



        dojutsu = npc.get(

            "Dojutsu",

            {}

        )



        for side in [

            "LeftEye",

            "RightEye"

        ]:


            eye = dojutsu.get(
                side
            )



            if eye:


                if eye.get(
                    "Type"
                ) == eye_type:


                    count += 1




        return count











    def calculate_eye_power(
        self,
        npc
    ):


        power = 0



        dojutsu = npc.get(

            "Dojutsu",

            {}

        )



        for side in [

            "LeftEye",

            "RightEye"

        ]:


            eye = dojutsu.get(
                side
            )


            if not eye:

                continue




            stage = eye.get(
                "Stage"
            )



            values = {


                "1 Tomoe":10,


                "2 Tomoe":20,


                "3 Tomoe":40,


                "Mangekyo Sharingan":80,


                "Eternal Mangekyo Sharingan":120,


                "Rinnegan":150,


                "Rinne Sharingan":200

            }



            power += values.get(

                stage,

                0

            )



        return power










    def evolve_eye(
        self,
        npc_name,
        side,
        new_stage
    ):


        npc = self.npc_engine.get_npc(

            npc_name

        )



        if not npc:

            return None




        eye = npc.get(

            "Dojutsu",

            {}

        ).get(

            side

        )



        if not eye:

            return None




        eye["Stage"] = new_stage




        if "Tomoe" in eye:

            if "1 Tomoe" in new_stage:

                eye["Tomoe"] = 1

            elif "2 Tomoe" in new_stage:

                eye["Tomoe"] = 2

            elif "3 Tomoe" in new_stage:

                eye["Tomoe"] = 3





        npc["Dojutsu"][side] = eye



        self.npc_engine.create_npc(

            npc_name,

            **npc

        )



        return eye










    def check_double_eye_bonus(
        self,
        npc
    ):


        dojutsu = npc.get(

            "Dojutsu",

            {}

        )


        left = dojutsu.get(
            "LeftEye"
        )


        right = dojutsu.get(
            "RightEye"
        )



        if not left or not right:

            return False




        return left.get(
            "Type"
        ) == right.get(
            "Type"
        )