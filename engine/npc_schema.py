# npc_schema.py


DEFAULT_NPC = {


    # =====================
    # TEMEL BİLGİLER
    # =====================

    "Name": "",

    "Age": 12,

    "Gender": "",

    "Village": "Konohagakure",

    "Location": "Konohagakure",

    "Clan": "",


    # =====================
    # RÜTBE / GELİŞİM
    # =====================

    "Rank": "Academy Student",

    "Level": 1,

    "Experience": 0,

    "Reputation": 0,

    "Achievements": [],



    # =====================
    # SAVAŞ STATLARI
    # =====================

    "HP": 100,

    "MaxHP": 100,

    "Chakra": 100,

    "MaxChakra": 100,


    "Stats":
    {

        "Chakra": 50,

        "ChakraControl": 50,

        "Strength": 10,

        "Speed": 10,

        "Endurance": 10,

        "Intelligence": 50,

        "Willpower": 20,

        "Stamina": 50

    },



    # =====================
    # NINJA YETENEKLERİ
    # =====================

    "Skills":
    {

        "Taijutsu": 0,

        "Ninjutsu": 0,

        "Genjutsu": 0,

        "Kenjutsu": 0,

        "Fuinjutsu": 0,

        "MedicalNinjutsu": 0,

        "WeaponSkill": 0

    },



    # =====================
    # CHAKRA DOĞALARI
    # =====================

    "Nature":
    [],



    # =====================
    # JUTSU SİSTEMİ
    # =====================

    "Jutsu":
    [],


    "JutsuMastery":
    {},



    # =====================
    # YETENEKLER
    # =====================

    "Abilities":
    [],


    "PotentialAbilities":
    [],



    # =====================
    # DOJUTSU
    # =====================

    "Dojutsu":
    {

        "LeftEye":
        {

            "Type": "None",

            "Stage": 0,

            "Tomoe": 0,

            "Abilities": []

        },


        "RightEye":
        {

            "Type": "None",

            "Stage": 0,

            "Tomoe": 0,

            "Abilities": []

        }

    },



    # =====================
    # KEKKEI GENKAI
    # =====================

    "Bloodline":
    "",



    # =====================
    # İLİŞKİLER
    # =====================

    "Relationships":
    {},



    # =====================
    # HAFIZA
    # =====================

    "Memories":
    [],



    # =====================
    # EĞİTİM
    # =====================

    "Training":
    {

        "Current": None,

        "Completed": []

    },



    # =====================
    # GÖREVLER
    # =====================

    "ActiveMissions":
    [],


    "CompletedMissions":
    [],



    # =====================
    # ENVANTER
    # =====================

    "Inventory":
    [],



    "Weapons":
    [],



    # =====================
    # KİŞİLİK
    # =====================

    "Personality":
    {},


    "Goal":
    "",


    "Status":
    "Alive"


}