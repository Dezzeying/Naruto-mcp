WORLD_EVENTS = [


    {


        "Name":
        "Academy Era",


        "Year":
        0,


        "Description":
        "Naruto ve diğer öğrenciler akademide eğitim görüyor.",


        "Unlocks":
        [],


        "NPCChanges":
        {

            "Naruto":
            {

                "Status":
                "Academy Student"

            }

        }


    },





    {


        "Name":
        "Team 7 Formation",


        "Year":
        1,


        "Description":
        "Naruto, Sasuke ve Sakura Team 7 olarak görevlendirilir.",


        "Unlocks":
        [

            "Basic Team Missions"

        ],


        "NPCChanges":
        {


            "Naruto":
            {

                "Status":
                "Genin"

            },


            "Sasuke":
            {

                "Status":
                "Genin"

            }


        }


    },






    {


        "Name":
        "Chunin Exams",


        "Year":
        2,


        "Description":
        "Chunin sınavları başlar. Yeni rakipler ortaya çıkar.",


        "Unlocks":
        [

            "Chunin Missions"

        ],


        "NPCChanges":
        {


            "Gaara":
            {

                "Status":
                "Chunin Candidate"

            }

        }


    },






    {


        "Name":
        "Naruto Rasengan Training",


        "Year":
        3,


        "Description":
        "Naruto Rasengan üzerinde çalışmaya başlar.",


        "Unlocks":
        [

            "Rasengan"

        ],


        "TrainingEvents":
        [

            {

                "NPC":
                "Naruto",


                "Activity":
                "Rasengan Training"


            }

        ]

    },







    {


        "Name":
        "Kakashi Chidori Development",


        "Year":
        1,


        "Description":
        "Kakashi'nin geliştirdiği Chidori artık dünyada kullanılabilir hale gelir.",


        "Unlocks":
        [

            "Raiton: Chidori"

        ],


        "TrainingEvents":
        [

            {

                "NPC":
                "Kakashi Hatake",


                "Activity":
                "Chidori Training"


            }

        ]

    },








    {


        "Name":
        "Naruto Wind Training",


        "Year":
        4,


        "Description":
        "Naruto rüzgar doğasını öğrenmeye başlar.",


        "Unlocks":
        [

            "Wind Nature Training"

        ],


        "TrainingEvents":
        [

            {

                "NPC":
                "Naruto",


                "Activity":
                "Wind Release Training"


            }

        ]

    },








    {


        "Name":
        "Rasenshuriken Creation",


        "Year":
        5,


        "Description":
        "Naruto Rasenshuriken tekniğini geliştirir.",


        "Unlocks":
        [

            "Futon: Rasenshuriken"

        ],


        "TrainingEvents":
        [

            {

                "NPC":
                "Naruto",


                "Activity":
                "Rasenshuriken Development"


            }

        ]

    }







]







def get_events_for_year(
    year
):


    result = []



    for event in WORLD_EVENTS:


        if event["Year"] == year:


            result.append(
                event
            )



    return result







def get_event(
    name
):


    for event in WORLD_EVENTS:


        if event["Name"] == name:

            return event



    return None