"""
Context Manager

AI hikaye hafızası yönetimi.

Oyundaki:
- önemli olayları
- NPC durumlarını
- hikaye ipliklerini
- dünya özetini

saklar ve LLM promptlarına bağlam sağlar.
"""


from __future__ import annotations

import json
import time

from pathlib import Path
from typing import Any


class ContextManager:
    """
    AI hikaye hafızasını yöneten sistem.

    Uzun oyun oturumlarında LLM'in geçmiş olayları
    hatırlamasını sağlar.
    """

    def __init__(
        self,
        max_context_tokens: int = 4000,
    ) -> None:
        """
        Args:
            max_context_tokens:
                Prompt içine aktarılabilecek maksimum
                bağlam büyüklüğü.
        """

        self.max_context_tokens = max_context_tokens

        self.story_log: list[dict[str, Any]] = []

        self.active_threads: list[dict[str, Any]] = []

        self.npc_states: dict[str, dict[str, Any]] = {}

        self.world_state_summary: str = (
            "Naruto dünyası başlangıç aşamasında."
        )


    def add_event(
        self,
        event_type: str,
        summary: str,
        importance: int,
        related_npcs: list[str] | None = None,
        related_locations: list[str] | None = None,
    ) -> None:
        """
        Yeni hikaye olayı ekler.
        """

        event = {

            "timestamp":
                time.time(),

            "event_type":
                event_type,

            "summary":
                summary,

            "importance":
                max(
                    1,
                    min(
                        10,
                        importance
                    )
                ),

            "related_npcs":
                related_npcs or [],

            "related_locations":
                related_locations or [],

        }


        self.story_log.append(
            event
        )


    def get_recent_context(
        self,
        n: int = 10,
    ) -> list[dict[str, Any]]:
        """
        Son önemli olayları döndürür.
        """

        sorted_events = sorted(
            self.story_log,
            key=lambda x: x["importance"],
            reverse=True,
        )


        return sorted_events[:n]



    def get_context_for_prompt(
        self,
        max_tokens: int | None = None,
    ) -> str:
        """
        AI prompt'una eklenecek hafıza metnini oluşturur.
        """

        limit = (
            max_tokens
            or self.max_context_tokens
        )


        parts: list[str] = []


        parts.append(
            "DÜNYA DURUMU:\n"
            +
            self.world_state_summary
        )


        parts.append(
            "\nSON ÖNEMLİ OLAYLAR:"
        )


        for event in self.get_recent_context(10):

            parts.append(

                f"""
[{event['event_type']}]

{event['summary']}

Etkilenen NPC:
{", ".join(event['related_npcs'])}

Konum:
{", ".join(event['related_locations'])}

"""
            )


        text = "\n".join(parts)


        # Basit token koruması
        words = text.split()


        if len(words) > limit:

            words = words[-limit:]


        return " ".join(words)



    def start_thread(
        self,
        thread_id: str,
        title: str,
    ) -> None:
        """
        Yeni hikaye zinciri başlatır.
        """

        thread = {

            "thread_id":
                thread_id,

            "title":
                title,

            "status":
                "active",

            "started_at":
                time.time(),

            "last_updated":
                time.time(),

            "key_events":
                [],

        }


        self.active_threads.append(
            thread
        )



    def update_thread(
        self,
        thread_id: str,
        event_summary: str,
    ) -> bool:
        """
        Devam eden hikaye zincirine olay ekler.
        """

        for thread in self.active_threads:

            if thread["thread_id"] == thread_id:

                thread["key_events"].append(
                    event_summary
                )

                thread["last_updated"] = (
                    time.time()
                )

                return True


        return False



    def close_thread(
        self,
        thread_id: str,
        resolution: str,
    ) -> bool:
        """
        Hikaye zincirini tamamlar.
        """

        for thread in self.active_threads:

            if thread["thread_id"] == thread_id:

                thread["status"] = "completed"

                thread["resolution"] = resolution

                thread["last_updated"] = (
                    time.time()
                )

                return True


        return False



    def update_npc_state(
        self,
        npc_id: str,
        **kwargs: Any,
    ) -> None:
        """
        NPC hafıza durumunu günceller.
        """

        if npc_id not in self.npc_states:

            self.npc_states[npc_id] = {}


        self.npc_states[npc_id].update(
            kwargs
        )



    def generate_world_summary(
        self,
    ) -> str:
        """
        Dünya durumunun kısa özetini üretir.
        """

        active = [

            thread["title"]

            for thread in self.active_threads

            if thread["status"] == "active"

        ]


        summary = f"""

Dünya Özeti:

{self.world_state_summary}


Aktif Hikayeler:

{", ".join(active) if active else "Yok"}


Bilinen NPC Sayısı:

{len(self.npc_states)}

"""


        return summary.strip()



    def compress_old_events(
        self,
    ) -> None:
        """
        Eski düşük öncelikli olayları sıkıştırır.

        Büyük oyun kayıtlarında token kullanımını azaltır.
        """

        if len(self.story_log) < 100:

            return


        important = []

        compressed_count = 0


        for event in self.story_log:

            if event["importance"] >= 7:

                important.append(
                    event
                )

            else:

                compressed_count += 1


        if compressed_count:

            important.insert(

                0,

                {

                    "timestamp":
                        time.time(),

                    "event_type":
                        "memory_summary",

                    "summary":
                        f"{compressed_count} küçük olay arşivlendi.",

                    "importance":
                        5,

                    "related_npcs":
                        [],

                    "related_locations":
                        [],

                }

            )


        self.story_log = important



    def save(
        self,
        path: str,
    ) -> None:
        """
        Hafızayı JSON olarak kaydeder.
        """

        data = {

            "story_log":
                self.story_log,

            "active_threads":
                self.active_threads,

            "npc_states":
                self.npc_states,

            "world_state_summary":
                self.world_state_summary,

        }


        Path(path).write_text(

            json.dumps(
                data,
                ensure_ascii=False,
                indent=4,
            ),

            encoding="utf-8",

        )



    def load(
        self,
        path: str,
    ) -> None:
        """
        Kayıtlı hafızayı yükler.
        """

        file = Path(path)


        if not file.exists():

            return


        data = json.loads(

            file.read_text(
                encoding="utf-8"
            )

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