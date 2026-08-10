from game_engine import NarutoGame
from deepseek_engine import DeepSeekEngine




game = NarutoGame()

ai = DeepSeekEngine()






def create_character():


    print(
        """
============================

       NARUTO RPG AI

============================
"""
    )


    name = input(
        "Ninja adı: "
    )


    clan = input(
        """
Clan:

Uchiha
Hyuga
Uzumaki
Senju
Nara
Akimichi

Seçim:
"""
    )


    village = input(
        """
Köy:

Konohagakure
Sunagakure
Kirigakure
Kumogakure
Iwagakure

Seçim:
"""
    )



    player = game.create_character(

        name,

        clan,

        village

    )



    print("\nKarakter oluşturuldu!\n")


    print(player)








def show_status():


    player = game.get_player()


    print(
        """

========== DURUM ==========

"""
    )


    print(
        "İsim:",
        player["Name"]
    )


    print(
        "Clan:",
        player["Clan"]
    )


    print(
        "Köy:",
        player["Village"]
    )


    print(
        "Rank:",
        player["Rank"]
    )


    print(
        "HP:",
        player["HP"]
    )


    print(
        "Chakra:",
        player["Chakra"]
    )


    print(
        "Yetenekler:"
    )


    for ability in player["Abilities"]:

        print(
            "-",
            ability
        )


    print(
        "Jutsular:"
    )


    for jutsu in player["Jutsu"]:

        print(
            "-",
            jutsu
        )


    print(
        "\n=========================="
    )









def story_action():


    action = input(

        "\nNe yapmak istiyorsun?\n> "

    )



    player = game.get_player()



    prompt = f"""

Naruto RPG karakter bilgisi:

{player}


Oyuncunun hareketi:

{action}


Bu olayı Naruto evreninde bir Game Master gibi anlat.


"""



    response = ai.ask(
        prompt
    )



    print(
        "\n"
    )


    print(
        response
    )








def use_jutsu():


    player = game.get_player()



    print(
        "\nJutsular:"
    )


    for jutsu in player["Jutsu"]:

        print(
            "-",
            jutsu
        )



    choice = input(
        "Kullanılacak jutsu: "
    )



    result = game.use_jutsu(
        choice
    )


    print(
        result
    )








def training():


    stat = input(

        """
Çalışılacak alan:

Strength
Speed
ChakraControl
Taijutsu
Ninjutsu
Genjutsu

:
"""
    )



    print(
        game.train(
            stat
        )
    )









def game_loop():


    while True:


        print(
            """

======================

1 - Hikayeye devam et

2 - Durum göster

3 - Jutsu kullan

4 - Eğitim yap

5 - Kaydet

6 - Çıkış

======================

"""
        )



        choice = input(
            "Seçim: "
        )





        if choice == "1":

            story_action()





        elif choice == "2":

            show_status()





        elif choice == "3":

            use_jutsu()





        elif choice == "4":

            training()





        elif choice == "5":

            game.save()

            print(
                "Kaydedildi."
            )





        elif choice == "6":

            print(
                "Oyun kapatıldı."
            )

            break





        else:

            print(
                "Geçersiz seçim."
            )









if __name__ == "__main__":


    create_character()


    game_loop()