from ai.deepseek_engine import DeepSeekEngine
from ai.game_controller import GameController
from ai.context_manager import ContextManager
from ai.prompt_builder import PromptBuilder
from ai.response_parser import ResponseParser

from engine.base_memory import BaseMemory
from engine.memory_engine import MemoryEngine

from engine.npc_engine import NPCEngine
from engine.clan_engine import ClanEngine

from engine.relationship_engine import RelationshipEngine
from engine.world_state import WorldState

from engine.mission_engine import MissionEngine
from engine.rank_system import RankSystem

from engine.jutsu_engine import JutsuEngine
from engine.ability_system import AbilitySystem
from engine.ability_progression import AbilityProgression

from engine.dojutsu_system import DojutsuSystem
from engine.dojutsu_ability_system import DojutsuAbilitySystem

from engine.training_engine import TrainingEngine

from engine.game_engine import GameEngine


class NarutoRPG:

    def __init__(self):

        print(
            "Naruto RPG AI başlatılıyor..."
        )

        # ======================
        # MEMORY
        # ======================

        self.base_memory = BaseMemory()

        self.memory_engine = MemoryEngine(
            self.base_memory
        )

        # ======================
        # AI MEMORY / CONTEXT
        # ======================

        self.context_manager = ContextManager()

        # ======================
        # NPC
        # ======================

        self.npc_engine = NPCEngine(
            self.base_memory
        )

        # ======================
        # CLAN
        # ======================

        self.clan_engine = ClanEngine(
            self.npc_engine
        )

        self.npc_engine.connect_clan_engine(
            self.clan_engine
        )

        # ======================
        # JUTSU
        # ======================

        self.jutsu_engine = JutsuEngine(
            self.npc_engine
        )

        # ======================
        # ABILITY
        # ======================

        self.ability_system = AbilitySystem(
            self.npc_engine
        )

        self.ability_progression = AbilityProgression(
            self.npc_engine,
            self.ability_system
        )

        # ======================
        # DOJUTSU
        # ======================

        self.dojutsu_system = DojutsuSystem(
            self.npc_engine,
            self.ability_system
        )

        self.dojutsu_ability_system = DojutsuAbilitySystem(
            self.npc_engine
        )

        # ======================
        # TRAINING
        # ======================

        self.training_engine = TrainingEngine(
            self.npc_engine,
            self.jutsu_engine
        )

        # ======================
        # RELATIONSHIP
        # ======================

        self.relationship_engine = RelationshipEngine(
            self.npc_engine
        )

        # ======================
        # WORLD
        # ======================

        self.world_state = WorldState(
            self.base_memory
        )

        # ======================
        # MISSION
        # ======================

        self.mission_engine = MissionEngine(
            self.npc_engine,
            self.world_state,
            self.relationship_engine
        )

        # ======================
        # RANK
        # ======================

        self.rank_system = RankSystem(
            self.npc_engine
        )

        # ======================
        # AI
        # ======================

        self.ai = DeepSeekEngine()

        self.prompt_builder = PromptBuilder(
            self.context_manager,
            None
        )

        self.response_parser = ResponseParser()

        # ======================
        # GAME ENGINE
        # ======================

        self.game_engine = GameEngine(
            None,
            self.npc_engine,
            self.training_engine,
            None,
            self.mission_engine,
            self.relationship_engine,
            self.memory_engine
        )

        # ======================
        # CONTROLLER
        # ======================

        self.controller = GameController(
            self.context_manager,
            self.prompt_builder,
            self.ai,
            self.response_parser,
            None
        )

        self.player = None

    # ==================================================
    # PLAYER
    # ==================================================

    def create_player(self):

        print(
            "\n=== Yeni Ninja ===\n"
        )

        name = input(
            "Ninja adı: "
        )

        clan = input(
            "Clan: "
        )

        village = input(
            "Köy: "
        )

        npc = self.npc_engine.create_npc_with_clan(
            name,
            clan,
            Village=village,
            Rank="Academy Student"
        )

        self.player = self.npc_engine.get_npc(
            name
        )

        print(
            "\nKarakter oluşturuldu!"
        )

        print(
            self.player
        )

    # ==================================================
    # STATUS
    # ==================================================

    def show_status(self):

        current = self.npc_engine.get_npc(
            self.player["Name"]
        )

        print("\n====================")
        print(" KARAKTER DURUMU")
        print("====================")
        print(
            f"İsim: {current.get('Name')}"
        )
        print(
            f"Clan: {current.get('Clan')}"
        )
        print(
            f"Köy: {current.get('Village')}"
        )
        print(
            f"Rütbe: {current.get('Rank')}"
        )
        print(
            f"Level: {current.get('Level')}"
        )
        print(
            f"Experience: {current.get('Experience')}"
        )

        print("\nStats:")
        print(
            current.get(
                "Stats",
                {}
            )
        )

        print("\nSkills:")
        print(
            current.get(
                "Skills",
                {}
            )
        )

        print("\nJutsu:")
        print(
            current.get(
                "Jutsu",
                []
            )
        )

        print("\nAbilities:")
        print(
            current.get(
                "Abilities",
                []
            )
        )

        print()

    # ==================================================
    # STORY
    # ==================================================

    def story_action(self):

        action = input(
            "\nNe yapmak istiyorsun:\n> "
        )

        location = self.player.get(
            "Location",
            self.player.get(
                "Village",
                "Konohagakure"
            )
        )

        result = self.controller.process_action(
            self.player,
            location,
            action
        )

        print("\n")
        print(result)

    # ==================================================
    # TRAINING
    # ==================================================

    def training_menu(self):

        print(
            """
====================

1 - Taijutsu çalış
2 - Ninjutsu çalış
3 - Genjutsu çalış
4 - Kenjutsu çalış
5 - Deneyim kazan
6 - Geri

====================
"""
        )

        choice = input(
            "Seçim: "
        )

        name = self.player["Name"]

        if choice == "1":

            result = self.training_engine.train_skill(
                name,
                "Taijutsu",
                5
            )

            self.training_engine.gain_experience(
                name,
                5
            )

            print(
                "\nTaijutsu antrenmanı tamamlandı."
            )

        elif choice == "2":

            result = self.training_engine.train_skill(
                name,
                "Ninjutsu",
                5
            )

            self.training_engine.gain_experience(
                name,
                5
            )

            print(
                "\nNinjutsu antrenmanı tamamlandı."
            )

        elif choice == "3":

            result = self.training_engine.train_skill(
                name,
                "Genjutsu",
                5
            )

            self.training_engine.gain_experience(
                name,
                5
            )

            print(
                "\nGenjutsu antrenmanı tamamlandı."
            )

        elif choice == "4":

            result = self.training_engine.train_skill(
                name,
                "Kenjutsu",
                5
            )

            self.training_engine.gain_experience(
                name,
                5
            )

            print(
                "\nKenjutsu antrenmanı tamamlandı."
            )

        elif choice == "5":

            result = self.training_engine.gain_experience(
                name,
                10
            )

            print(
                "\nExperience kazanıldı."
            )

        elif choice == "6":

            return

        else:

            print(
                "Geçersiz seçim."
            )

            return

        self.player = self.npc_engine.get_npc(
            name
        )

    # ==================================================
    # MISSION
    # ==================================================

    def create_mission(self):

        mission = self.mission_engine.generate_mission(
            self.player
        )

        print("\nGörev:")
        print(mission)

    # ==================================================
    # MAIN LOOP
    # ==================================================

    def start(self):

        self.create_player()

        while True:

            print(
                """
====================

        NARUTO RPG

====================

1 - Hikâyeye devam et
2 - Karakter durumu
3 - Eğitim
4 - Görev oluştur
5 - Zamanı ilerlet
6 - Çıkış

====================
"""
            )

            choice = input(
                "Seçim: "
            )

            if choice == "1":

                self.story_action()

            elif choice == "2":

                self.show_status()

            elif choice == "3":

                self.training_menu()

            elif choice == "4":

                self.create_mission()

            elif choice == "5":

                print(
                    "\nZaman sistemi şu anda bağlanıyor..."
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

    game = NarutoRPG()

    game.start()