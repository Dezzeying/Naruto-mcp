class DojutsuAbilitySystem:



    def __init__(
        self,
        npc_engine
    ):


        self.npc_engine = npc_engine




        self.abilities = {



            "Amaterasu":
            {

                "EyeType":
                "Mangekyo Sharingan",

                "Type":
                "Fire Dojutsu",

                "ChakraCost":
                80,

                "Effect":
                "Black Flames"

            },



            "Tsukuyomi":
            {

                "EyeType":
                "Mangekyo Sharingan",

                "Type":
                "Genjutsu",

                "ChakraCost":
                100,

                "Effect":
                "Extreme Time Illusion"

            },



            "Kamui":
            {

                "EyeType":
                "Mangekyo Sharingan",

                "Type":
                "Space Time",

                "ChakraCost":
                120,

                "Effect":
                "Dimension Transfer"

            },



            "Kotoamatsukami":
            {

                "EyeType":
                "Mangekyo Sharingan",

                "Type":
                "Mind Control",

                "ChakraCost":
                200,

                "Cooldown":
                "Years",

                "Effect":
                "Invisible Mental Manipulation"

            },



            "Kagutsuchi":
            {

                "EyeType":
                "Mangekyo Sharingan",

                "Type":
                "Fire Control",

                "ChakraCost":
                70,

                "Effect":
                "Black Flame Manipulation"

            },



            "Susanoo":
            {

                "EyeType":
                "Mangekyo Sharingan",

                "Type":
                "Ultimate Defense",

                "ChakraCost":
                150,

                "Effect":
                "Chakra Avatar"

            },



            "Izanagi":
            {

                "EyeType":
                "Sharingan",

                "Type":
                "Forbidden",

                "Cost":
                "Eye Loss",

                "Effect":
                "Reality Alteration"

            },



            "Izanami":
            {

                "EyeType":
                "Sharingan",

                "Type":
                "Forbidden Genjutsu",

                "Cost":
                "Eye Loss",

                "Effect":
                "Infinite Loop"

            }

        }











    def get_ability(
        self,
        name
    ):


        return self.abilities.get(
            name
        )











    def get_eye(
        self,
        npc,
        side
    ):


        return npc.get(

            "Dojutsu",

            {}

        ).get(

            side

        )











    def add_eye_ability(
        self,
        npc_name,
        side,
        ability
    ):


        npc = self.npc_engine.get_npc(
            npc_name
        )


        if not npc:

            return None




        eye = self.get_eye(
            npc,
            side
        )


        if not eye:

            return None




        if "Abilities" not in eye:

            eye["Abilities"] = []



        if ability not in eye["Abilities"]:

            eye["Abilities"].append(
                ability
            )



        npc["Dojutsu"][side] = eye



        self.npc_engine.create_npc(

            npc_name,

            **npc

        )



        return eye










    def has_required_eye_stage(
        self,
        npc,
        required
    ):


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



            if eye.get(
                "Stage"
            ) == required:


                return True




        return False










    def can_unlock(
        self,
        npc,
        ability
    ):


        data = self.get_ability(
            ability
        )


        if not data:

            return False




        required = data.get(
            "EyeType"
        )



        if required == "Mangekyo Sharingan":


            return self.has_required_eye_stage(

                npc,

                "Mangekyo Sharingan"

            )



        if required == "Sharingan":


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


                if eye and eye.get(
                    "Type"
                ) == "Sharingan":

                    return True



        return False










    def can_use_eye_ability(
        self,
        npc,
        ability
    ):


        if not self.can_unlock(
            npc,
            ability
        ):

            return False



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



            if ability in eye.get(
                "Abilities",
                []
            ):

                return True



        return False