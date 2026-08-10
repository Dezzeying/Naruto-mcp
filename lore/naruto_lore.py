"""
Naruto RPG Simülasyon Motoru

AI Lore Management System

Naruto evren bilgilerini AI promptlarına sağlar.
"""


from typing import Any

from .clans import CLAN_DATABASE



class NarutoLore:
    """
    Naruto evrenindeki lore verilerini yöneten sistem.
    AI hikaye üretimi için bağlam sağlar.
    """


    def __init__(self) -> None:
        """
        Lore veritabanını başlatır.
        """


        self.clans = CLAN_DATABASE


        self.villages: dict[str, dict[str, Any]] = {


            "Konohagakure":
            {
                "country":
                "Fire Country",

                "leader":
                "Hokage",

                "specialties":
                [
                    "Dengeli ninja eğitimi",
                    "Çok çeşitli jutsu stilleri",
                    "Klan çeşitliliği"
                ],

                "culture":
                [
                    "Will of Fire",
                    "Takım çalışması",
                    "Köy koruması"
                ]
            },



            "Kirigakure":
            {
                "country":
                "Water Country",

                "leader":
                "Mizukage",

                "specialties":
                [
                    "Water Release",
                    "Suikast teknikleri",
                    "Kılıç ustaları"
                ],

                "culture":
                [
                    "Dayanıklılık",
                    "Güç",
                    "Hayatta kalma"
                ]
            },



            "Sunagakure":
            {
                "country":
                "Wind Country",

                "leader":
                "Kazekage",

                "specialties":
                [
                    "Kum teknikleri",
                    "Puppet teknikleri",
                    "Savunma"
                ]
            },



            "Kumogakure":
            {
                "country":
                "Lightning Country",

                "leader":
                "Raikage",

                "specialties":
                [
                    "Lightning Release",
                    "Taijutsu",
                    "Fiziksel güç"
                ]
            },



            "Iwagakure":
            {
                "country":
                "Earth Country",

                "leader":
                "Tsuchikage",

                "specialties":
                [
                    "Earth Release",
                    "Dayanıklılık",
                    "Savaş disiplini"
                ]
            }

        }



        self.bijuu = {


            "Shukaku":
            {
                "tails":1,
                "element":"Wind",
                "personality":"Gururlu ve öfkeli"
            },


            "Matatabi":
            {
                "tails":2,
                "element":"Fire",
                "personality":"Asil ve sakin"
            },


            "Isobu":
            {
                "tails":3,
                "element":"Water",
                "personality":"Sessiz"
            },


            "Son Goku":
            {
                "tails":4,
                "element":"Fire",
                "personality":"Gururlu savaşçı"
            },


            "Kokuo":
            {
                "tails":5,
                "element":"Steam",
                "personality":"Sakin"
            },


            "Saiken":
            {
                "tails":6,
                "element":"Water",
                "personality":"Nazik"
            },


            "Chomei":
            {
                "tails":7,
                "element":"Wind",
                "personality":"Özgür ruhlu"
            },


            "Gyuki":
            {
                "tails":8,
                "element":"Ink",
                "personality":"Bilge"
            },


            "Kurama":
            {
                "tails":9,
                "element":"Chakra",
                "personality":"Gururlu ve güçlü"
            }

        }



        self.ranks = {


            "Academy Student":
            "Ninja akademisi öğrencisi",


            "Genin":
            "Yeni mezun ninja",


            "Chunin":
            "Takım liderliği yapabilen ninja",


            "Jonin":
            "Elit seviye ninja",


            "ANBU":
            "Gizli operasyon uzmanı",


            "Kage":
            "Köy lideri"

        }
        self.kekkei_genkai: dict[str, dict[str, Any]] = {


            "Sharingan":
            {
                "type":
                "Dojutsu",

                "clan":
                "Uchiha",

                "abilities":
                [
                    "Hareket analizi",
                    "Genjutsu",
                    "Kopyalama"
                ],

                "evolution":
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
                "type":
                "Dojutsu",

                "clan":
                "Hyuga",

                "abilities":
                [
                    "360 derece görüş",
                    "Chakra noktalarını görme",
                    "Gentle Fist"
                ]
            },



            "Rinnegan":
            {
                "type":
                "Legendary Dojutsu",

                "origin":
                "Six Paths chakra",

                "abilities":
                [
                    "Six Paths teknikleri",
                    "Gravity manipulation",
                    "Chakra absorption"
                ]
            },



            "Wood Release":
            {
                "type":
                "Nature Kekkei Genkai",

                "elements":
                [
                    "Earth",
                    "Water"
                ],

                "known_users":
                [
                    "Hashirama Senju"
                ],

                "abilities":
                [
                    "Bijuu kontrolü",
                    "Orman oluşturma",
                    "Chakra bastırma"
                ]
            },



            "Ice Release":
            {
                "type":
                "Nature Kekkei Genkai",

                "elements":
                [
                    "Water",
                    "Wind"
                ],

                "clan":
                "Yuki",

                "abilities":
                [
                    "Ice mirrors",
                    "Buz silahları",
                    "Alan kontrolü"
                ]
            },



            "Ketsuryugan":
            {
                "type":
                "Dojutsu",

                "clan":
                "Chinoike",

                "abilities":
                [
                    "Genjutsu",
                    "Kan manipülasyonu"
                ]
            }

        }



        self.jutsu_categories: dict[str, str] = {


            "Ninjutsu":
            "Chakra kullanılarak yapılan teknikler.",


            "Taijutsu":
            "Fiziksel savaş ve yakın dövüş teknikleri.",


            "Genjutsu":
            "Rakibin algısını değiştiren illüzyon teknikleri.",


            "Fuinjutsu":
            "Mühürleme teknikleri.",


            "Dojutsu":
            "Göz teknikleri.",


            "Senjutsu":
            "Doğal enerjiyi kullanan teknikler.",


            "Medical Ninjutsu":
            "İyileştirme ve tıbbi chakra teknikleri."

        }



        self.locations: dict[str, dict[str, Any]] = {


            "Valley of the End":
            {
                "type":
                "Historical Battlefield",

                "importance":
                "Uchiha ve Senju tarihinin önemli noktası",

                "atmosphere":
                "Sessiz, ağır ve geçmiş savaşların izlerini taşıyan bölge"
            },



            "Forest of Death":
            {
                "type":
                "Training Area",

                "importance":
                "Chunin Exam alanı",

                "danger":
                "Yüksek seviye vahşi canlılar"
            },



            "Mount Myoboku":
            {
                "type":
                "Sage Location",

                "importance":
                "Toad Sage eğitimi",

                "special":
                "Senjutsu bilgisi"
            },



            "Land of Iron":
            {
                "type":
                "Samurai Country",

                "importance":
                "Beş Kage zirvesi bölgesi",

                "culture":
                "Ninja yerine samuray geleneği"
            },



            "Amegakure":
            {
                "type":
                "Hidden Village",

                "history":
                [
                    "Savaşlarla yıpranmış köy",
                    "Akatsuki geçmişi"
                ]
            }

        }



        self.organizations: dict[str, dict[str, Any]] = {


            "Akatsuki":
            {
                "type":
                "Criminal Organization",

                "goal":
                "Bijuu gücünü toplamak",

                "members":
                [
                    "S-Rank rogue ninja"
                ],

                "reputation":
                "Dünya çapında tehdit"
            },



            "ANBU":
            {
                "type":
                "Black Ops",

                "purpose":
                "Gizli köy operasyonları",

                "members":
                [
                    "Elite shinobi"
                ]
            },



            "Root":
            {
                "type":
                "Secret Organization",

                "purpose":
                "Konoha'nın gizli güvenlik yapılanması",

                "methods":
                [
                    "Casusluk",
                    "Manipülasyon"
                ]
            },



            "Seven Ninja Swordsmen":
            {
                "type":
                "Kirigakure Elite",

                "specialty":
                "Efsanevi ninja kılıçları"
            }

        }


    def get_village_info(
        self,
        village_name: str
    ) -> dict:
        """
        Köy bilgisi döndürür.
        """

        return self.villages.get(
            village_name,
            {}
        )



    def get_clan_info(
        self,
        clan_name: str
    ) -> dict:
        """
        Klan bilgisi döndürür.
        """

        return self.clans.get(
            clan_name,
            {}
        )



    def get_bijuu_info(
        self,
        name: str
    ) -> dict:
        """
        Bijuu bilgisi döndürür.
        """

        return self.bijuu.get(
            name,
            {}
        )

    def get_lore_context(
        self,
        query: str
    ) -> str:
        """
        AI promptlarında kullanılacak lore özeti üretir.
        """

        query_lower = query.lower()

        result = []


        for clan, data in self.clans.items():

            if clan.lower() in query_lower:

                result.append(
                    f"Klan: {clan}\n{data}"
                )


        for village, data in self.villages.items():

            if village.lower() in query_lower:

                result.append(
                    f"Köy: {village}\n{data}"
                )


        for location, data in self.locations.items():

            if location.lower() in query_lower:

                result.append(
                    f"Mekan: {location}\n{data}"
                )


        if not result:

            return "Bu konu için özel lore bulunamadı."


        return "\n\n".join(result)

    def get_timeline_context(
        self,
        year_range: tuple[int, int]
    ) -> str:
        """
        Belirli dönem için tarih özeti döndürür.
        """

        start, end = year_range

        return (
            f"Ninja tarihi {start}-{end} yılları arasındaki "
            "olaylar AI tarafından simüle edilmelidir."
        )



    def generate_lore_seed(
        self
    ) -> str:
        """
        Yeni hikaye üretimi için rastgele lore tohumu verir.
        """

        seeds = [

            "Kayıp bir klanın eski mühür tekniği ortaya çıktı.",

            "Unutulmuş bir savaş alanında eski bir chakra kalıntısı bulundu.",

            "Bir köyde yasaklanmış bir jutsu araştırması başladı.",

            "Eski bir shinobi ailesinin mirası yeniden ortaya çıktı."

        ]
        import random
        return random.choice(
            seeds
        )



    def is_lore_accurate(
        self,
        statement: str
    ) -> bool:
        """
        Basit lore doğrulama kontrolü.
        """

        known_terms = [

            "Sharingan",
            "Byakugan",
            "Rinnegan",
            "Hokage",
            "Akatsuki",
            "Bijuu",
            "Kage",
            "Chakra"

        ]


        statement_lower = statement.lower()


        for term in known_terms:

            if term.lower() in statement_lower:

                return True


        return False