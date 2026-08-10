"""
Naruto RPG Simülasyon Motoru

AI Context Memory System

AI hikaye motorunun uzun süreli hafızasını yönetir.
"""

from __future__ import annotations

import json
import os

from datetime import datetime
from typing import Any



class ContextManager:
    """
    AI hikaye üretimi için dünya hafızasını yöneten sistem.
    """



    def __init__(
        self,
        max_context_tokens: int = 4000
    ) -> None:

        self.max_context_tokens = max_context_tokens


        # Oyun sırasında oluşan hafıza

        self.story_log: list[dict[str, Any]] = []

        self.active_threads: list[dict[str, Any]] = []

        self.npc_states: dict[str, dict[str, Any]] = {}



        # Kalıcı kayıtlar

        self.player_data: dict[str, Any] = {}

        self.world_data: dict[str, Any] = {}

        self.techniques: dict[str, Any] = {}

        self.campaign_memory: list[dict[str, Any]] = []



        self.world_state_summary: str = (
            "Dünya yeni başlayan bir ninja çağında."
        )


        # JSON kayıtlarını yükle

        self.load_game_data()



    def load_game_data(
        self
    ) -> None:
        """
        data klasöründeki kalıcı oyun kayıtlarını yükler.
        """

        base_path = "data"



        files = {

            "player_data": "player.json",

            "world_data": "world_state.json",

            "techniques": "techniques.json"

        }



        for key, filename in files.items():


            path = os.path.join(
                base_path,
                filename
            )


            if os.path.exists(path):

                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    setattr(
                        self,
                        key,
                        json.load(file)
                    )



        # Campaign hafızası


        campaign_path = os.path.join(
            base_path,
            "campaign_memory.json"
        )


        if os.path.exists(campaign_path):

            with open(
                campaign_path,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                self.campaign_memory = data.get(
                    "events",
                    []
                )



        # NPC kayıtları


        npc_path = os.path.join(
            base_path,
            "npcs.json"
        )


        if os.path.exists(npc_path):

            with open(
                npc_path,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)


                for npc in data.get(
                    "npcs",
                    []
                ):

                    self.npc_states[
                        npc["name"]
                    ] = npc
    def add_event(
        self,
        event_type: str,
        summary: str,
        importance: int,
        related_npcs: list[str],
        related_locations: list[str]
    ) -> None:
        """
        Yeni dünya olayı ekler.
        """

        event = {

            "timestamp":
            datetime.now().isoformat(),

            "event_type":
            event_type,

            "summary":
            summary,

            "importance":
            max(
                1,
                min(
                    importance,
                    10
                )
            ),

            "related_npcs":
            related_npcs,

            "related_locations":
            related_locations

        }


        self.story_log.append(
            event
        )



    def get_recent_context(
        self,
        n: int = 10
    ) -> list[dict[str, Any]]:

        return sorted(
            self.story_log,
            key=lambda x: x.get(
                "importance",
                0
            ),
            reverse=True
        )[:n]



    def get_context_for_prompt(
        self,
        max_tokens: int | None = None
    ) -> str:
        """
        AI prompt içine gidecek hafızayı oluşturur.
        """

        limit = (
            max_tokens
            or self.max_context_tokens
        )


        lines = []


        lines.append(
            "DÜNYA DURUMU:"
        )


        if self.world_data:

            world_name = self.world_data.get(
                "timeline",
                {}
            ).get(
                "current_period",
                ""
            )


            lines.append(
                world_name
            )

        else:

            lines.append(
                self.world_state_summary
            )



        if self.player_data:

            lines.append(
                "\nOYUNCU:"
            )

            lines.append(
                f"{self.player_data.get('name')} - "
                f"{self.player_data.get('rank')}"
            )



        if self.campaign_memory:

            lines.append(
                "\nGEÇMİŞ HİKAYE:"
            )


            for event in self.campaign_memory[-5:]:

                lines.append(
                    f"- {event.get('title')}: "
                    f"{event.get('summary')}"
                )



        lines.append(
            "\nSON OLAYLAR:"
        )


        for event in self.get_recent_context(10):

            lines.append(
                f"- {event['summary']} "
                f"(Önem: {event['importance']}/10)"
            )



        text = "\n".join(
            lines
        )


        words = text.split()


        if len(words) > limit:

            text = " ".join(
                words[:limit]
            )


        return text




    def update_npc_state(
        self,
        npc_id: str,
        **kwargs: Any
    ) -> None:

        if npc_id not in self.npc_states:

            self.npc_states[npc_id] = {}


        self.npc_states[npc_id].update(
            kwargs
        )



    def start_thread(
        self,
        thread_id: str,
        title: str
    ) -> None:

        self.active_threads.append(

            {
                "thread_id": thread_id,
                "title": title,
                "status": "active",
                "started_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "key_events": []
            }

        )



    def update_thread(
        self,
        thread_id: str,
        event_summary: str
    ) -> None:


        for thread in self.active_threads:

            if thread["thread_id"] == thread_id:

                thread["key_events"].append(
                    event_summary
                )

                thread["last_updated"] = (
                    datetime.now().isoformat()
                )

                return




    def close_thread(
        self,
        thread_id: str,
        resolution: str
    ) -> None:


        for thread in self.active_threads:

            if thread["thread_id"] == thread_id:

                thread["status"] = "completed"

                thread["resolution"] = resolution

                return




    def generate_world_summary(
        self
    ) -> str:


        active = [

            thread["title"]

            for thread in self.active_threads

            if thread["status"] == "active"

        ]


        self.world_state_summary = (

            "Aktif hikaye konuları: "
            +
            (
                ", ".join(active)
                if active
                else
                "Yok"
            )

        )


        return self.world_state_summary




    def save(
        self,
        path: str
    ) -> None:


        data = {

            "story_log":
            self.story_log,

            "active_threads":
            self.active_threads,

            "npc_states":
            self.npc_states,

            "world_state_summary":
            self.world_state_summary

        }


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )




    def load(
        self,
        path: str
    ) -> None:


        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )


        self.story_log = data.get(
            "story_log",
            []
        )


        self.active_threads = data.get(
            "active_threads",
            []
        )


        self.npc_states = data.get(
            "npc_states",
            {}
        )


        self.world_state_summary = data.get(
            "world_state_summary",
            ""
        )                    