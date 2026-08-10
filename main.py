from ai.game_controller import GameController
from ai.deepseek_engine import DeepSeekEngine
from ai.context_manager import ContextManager
from ai.prompt_builder import PromptBuilder
from ai.response_parser import ResponseParser

from lore.naruto_lore import NarutoLore



# Hafıza sistemi

memory = ContextManager()


# Lore sistemi

lore = NarutoLore()


# AI prompt sistemi

builder = PromptBuilder(
    memory,
    lore
)


# Ollama bağlantısı

engine = DeepSeekEngine()


# Cevap işleyici

parser = ResponseParser()



# Oyun kontrolcüsü

game = GameController(
    memory,
    builder,
    engine,
    parser
)



# Kayıt dosyasından Ajisai yükleniyor

player = memory.player_data



location = player.get(
    "location",
    "Konohagakure"
)



status = player.get(
    "status",
    {}
)


currency = player.get(
    "currency",
    {}
)



print(f"""
========================

 NARUTO RPG

========================

Oyuncu:
{player.get("name")}

Yaş:
{player.get("age")}

Rütbe:
{player.get("rank")}

Köy:
{player.get("village")}

Takım:
{player.get("team")}

Sensei:
{player.get("sensei")}

Konum:
{location}

Can:
{status.get("health")}

Chakra:
{status.get("chakra")}

Ryō:
{currency.get("ryo")}

========================
""")



# Başlangıç sahnesi

first_action = (
    "Sabah saatlerinde Konohagakure'de bulunuyorum. "
    "Takımımın yeni bir görevi olup olmadığını bekliyorum "
    "ve boş zamanımı değerlendiriyorum."
)



story = game.process_action(
    player,
    location,
    first_action
)



print("\n")

print(story)



# Ana oyun döngüsü

while True:

    print("\n")


    action = input("> ")



    if action.lower() in [
        "exit",
        "quit",
        "çık"
    ]:

        print(
            "Oyun kapatıldı."
        )

        break



    story = game.process_action(
        player,
        location,
        action
    )


    print("\n")

    print(story)