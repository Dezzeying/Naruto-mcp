"""
Naruto RPG Simülasyon Motoru

AI Lore Database - Clan Definitions

Bu dosya AI hikaye motorunun klan bilgilerini içerir.
Oyun mekaniği içermez.
"""


from typing import Any



CLAN_DATABASE: dict[str, dict[str, Any]] = {


    "Uchiha":
    {
        "origin":
        "Indra Otsutsuki soyundan gelen kadim ninja klanı.",


        "village":
        "Konohagakure",


        "rarity":
        "Legendary",


        "history":
        [
            "Konoha'nın kurucu klanlarından biridir.",
            "Senju klanı ile uzun süre savaşmıştır.",
            "Barış sonrası köy siyasetinde dışlanmıştır.",
            "Uchiha katliamı klanın tarihini değiştirmiştir."
        ],


        "culture":
        [
            "Aile onuru",
            "Güç",
            "Sadakat",
            "Duygusal bağlar"
        ],


        "psychology":
        {
            "strengths":
            [
                "Yüksek motivasyon",
                "Güçlü irade",
                "Sevdikleri için fedakarlık"
            ],

            "weaknesses":
            [
                "Kayıp travması",
                "Öfke kontrolü",
                "Takıntı"
            ]
        },


        "combat_style":
        [
            "Fire Release",
            "Genjutsu",
            "Sharingan analizi",
            "Kenjutsu"
        ],


        "npc_behavior":
        {
            "friendly":
            "Güven kazandığında son derece sadık davranır.",

            "enemy":
            "Soğuk, hesapçı ve stratejik olabilir.",

            "stranger":
            "Mesafeli ve gururludur."
        },


        "story_hooks":
        [
            "Kayıp Uchiha mirası",
            "Gizli Sharingan kullanıcısı",
            "Eski aile sırları"
        ]
    },





    "Senju":
    {
        "origin":
        "Asura Otsutsuki soyundan gelen güçlü yaşam enerjisine sahip klan.",


        "village":
        "Konohagakure",


        "history":
        [
            "Uchiha'nın tarihi rakibidir.",
            "Konoha'nın kuruluşunda önemli rol oynamıştır.",
            "Barış ve birlik anlayışını savunmuştur."
        ],


        "culture":
        [
            "Fedakarlık",
            "Koruma",
            "Birlik"
        ],


        "psychology":
        {
            "strengths":
            [
                "Dayanıklılık",
                "Liderlik",
                "Güçlü yaşam enerjisi"
            ],

            "weaknesses":
            [
                "Kendini feda etme",
                "Başkalarının yükünü alma"
            ]
        },


        "combat_style":
        [
            "Ninjutsu",
            "Medical techniques",
            "Geniş chakra kullanımı"
        ],


        "story_hooks":
        [
            "Kayıp Senju aileleri",
            "Hashirama mirası",
            "Eski teknik araştırmaları"
        ]
    },





    "Uzumaki":
    {
        "origin":
        "Asura Otsutsuki soyundan gelen mühürleme uzmanı klan.",


        "village":
        "Uzushiogakure",


        "history":
        [
            "Uzushiogakure güçlü Fuinjutsu bilgisiyle tanınırdı.",
            "Klan gücü nedeniyle birçok düşman tarafından hedef alındı.",
            "Hayatta kalanlar farklı köylere dağıldı."
        ],


        "culture":
        [
            "Aile",
            "Dayanıklılık",
            "Koruma",
            "Mühürleme bilgisi"
        ],


        "psychology":
        {
            "strengths":
            [
                "Yüksek irade",
                "Kolay pes etmeme"
            ],

            "weaknesses":
            [
                "Geçmiş kayıplar",
                "Aşırı sorumluluk alma"
            ]
        },


        "combat_style":
        [
            "Fuinjutsu",
            "Chakra chains",
            "Dayanıklı savaş"
        ],


        "story_hooks":
        [
            "Kayıp mühür teknikleri",
            "Eski Uzumaki parşömenleri",
            "Hayatta kalan aile üyeleri"
        ]
    },





    "Hyuga":
    {
        "origin":
        "Hamura Otsutsuki soyundan gelen Byakugan kullanıcısı klan.",


        "village":
        "Konohagakure",


        "bloodline":
        "Byakugan",


        "history":
        [
            "Konoha'nın en eski klanlarından biridir.",
            "Ana aile ve yan aile sistemiyle yönetilmiştir."
        ],


        "culture":
        [
            "Disiplin",
            "Gelenek",
            "Onur"
        ],


        "combat_style":
        [
            "Gentle Fist",
            "Chakra noktaları",
            "Hassas saldırılar"
        ],


        "psychology":
        {
            "strengths":
            [
                "Kontrol",
                "Sabır",
                "Analiz"
            ],

            "weaknesses":
            [
                "Gelenek baskısı",
                "Duyguları saklama"
            ]
        },


        "story_hooks":
        [
            "Aile politikaları",
            "Byakugan sırları",
            "Eski teknikler"
        ]
    },





    "Nara":
    {
        "origin":
        "Stratejik zekası ve gölge teknikleriyle tanınan Konoha klanı.",


        "village":
        "Konohagakure",


        "culture":
        [
            "Zeka",
            "Sakinlik",
            "Strateji"
        ],


        "combat_style":
        [
            "Shadow techniques",
            "Savaş alanı kontrolü"
        ],


        "personality":
        "Dışarıdan tembel görünen ancak çok zeki karakterler üretir.",


        "strengths":
        [
            "Planlama",
            "Analiz",
            "Taktik"
        ],


        "weaknesses":
        [
            "Fiziksel savaş isteksizliği",
            "Riskten kaçınma"
        ],


        "story_hooks":
        [
            "Eski strateji kitapları",
            "Savaş planları",
            "Gizli klan bilgileri"
        ]
    },


    "Akimichi":
    {
        "origin":
        "Konoha'nın fiziksel güç ve chakra genişletme teknikleriyle bilinen klanı.",


        "village":
        "Konohagakure",


        "history":
        [
            "Nara ve Yamanaka klanlarıyla eski ittifaka sahiptir.",
            "Takım çalışmasına dayalı savaş stilleri geliştirmiştir.",
            "Konoha savunmasında önemli rol oynamıştır."
        ],


        "culture":
        [
            "Aile",
            "Sadakat",
            "Dostluk",
            "Fedakarlık"
        ],


        "combat_style":
        [
            "Body Expansion Technique",
            "Taijutsu",
            "Chakra güçlendirme"
        ],


        "psychology":
        {
            "strengths":
            [
                "Güçlü irade",
                "Sadakat",
                "Takım ruhu"
            ],


            "weaknesses":
            [
                "Duygusal karar verme",
                "Büyük chakra tüketimi"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Sıcakkanlı ve koruyucu davranır.",

            "enemy":
            "Rakibini ezici güçle bastırmaya çalışır."
        },


        "story_hooks":
        [
            "Eski Akimichi savaş teknikleri",
            "Özel chakra hapları",
            "Kayıp aile tarifleri"
        ]
    },





    "Yamanaka":
    {
        "origin":
        "Zihin teknikleri ve istihbarat konusunda uzmanlaşmış Konoha klanı.",


        "village":
        "Konohagakure",


        "history":
        [
            "Nara ve Akimichi klanlarıyla takım oluşturmuştur.",
            "Konoha istihbaratında önemli görevler üstlenmiştir."
        ],


        "culture":
        [
            "Bilgi",
            "İletişim",
            "Zihinsel disiplin"
        ],


        "combat_style":
        [
            "Mind Transfer",
            "Zihin saldırıları",
            "İstihbarat"
        ],


        "psychology":
        {
            "strengths":
            [
                "Empati",
                "Analiz",
                "İnsan davranışı okuma"
            ],


            "weaknesses":
            [
                "Fiziksel savaşta zayıflık",
                "Teknik bağımlılığı"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Karşısındaki kişinin duygularını anlamaya çalışır.",

            "enemy":
            "Rakibinin zihinsel açıklarını arar."
        },


        "story_hooks":
        [
            "Çalınmış hafıza teknikleri",
            "Gizli istihbarat görevleri",
            "Zihin araştırmaları"
        ]
    },





    "Aburame":
    {
        "origin":
        "Vücutlarında özel böcek kolonileri taşıyan gizemli Konoha klanı.",


        "village":
        "Konohagakure",


        "history":
        [
            "Keşif ve takip görevlerinde kullanılmıştır.",
            "Böcek teknikleri nesilden nesile aktarılmıştır."
        ],


        "culture":
        [
            "Sessizlik",
            "Doğa dengesi",
            "Sabır"
        ],


        "combat_style":
        [
            "Kikaichu",
            "Takip",
            "Alan kontrolü"
        ],


        "psychology":
        {
            "strengths":
            [
                "Soğukkanlılık",
                "Sabır",
                "Analiz"
            ],

            "weaknesses":
            [
                "Duyguları göstermekte zorlanma",
                "Yakın dövüş sınırları"
            ]
        },


        "npc_behavior":
        "Genellikle sakin, az konuşan ve gözlemci karakterlerdir.",


        "story_hooks":
        [
            "Yeni böcek türleri",
            "Gizli takip görevleri",
            "Kayıp böcek kolonileri"
        ]
    },





    "Inuzuka":
    {
        "origin":
        "Ninja köpekleriyle güçlü bağ kuran savaşçı klan.",


        "village":
        "Konohagakure",


        "history":
        [
            "Hayvan ortaklarıyla savaşmalarıyla tanınırlar.",
            "Takip konusunda uzmanlaşmışlardır."
        ],


        "culture":
        [
            "Sadakat",
            "Aile",
            "Hayvan bağı"
        ],


        "combat_style":
        [
            "Beast Transformation",
            "Taijutsu",
            "Tracking"
        ],


        "psychology":
        {
            "strengths":
            [
                "Cesaret",
                "İçgüdü",
                "Sadakat"
            ],


            "weaknesses":
            [
                "Dürtüsellik",
                "Planlama eksikliği"
            ]
        },


        "story_hooks":
        [
            "Kayıp ninja köpeği",
            "Efsanevi hayvan bağı",
            "Av görevleri"
        ]
    },
        "Sarutobi":
    {
        "origin":
        "Konoha'nın eski ve saygın ailelerinden biri olan liderlik geleneğine sahip klan.",


        "village":
        "Konohagakure",


        "history":
        [
            "Birçok güçlü Hokage ve elit ninja yetiştirmiştir.",
            "Will of Fire anlayışının en güçlü temsilcilerinden biridir.",
            "Konoha'nın kuruluşundan beri köy yönetiminde etkili olmuştur."
        ],


        "culture":
        [
            "Will of Fire",
            "Köyü koruma",
            "Liderlik",
            "Fedakarlık"
        ],


        "combat_style":
        [
            "Ninjutsu",
            "Fire Release",
            "Çok yönlü savaş stilleri"
        ],


        "psychology":
        {
            "strengths":
            [
                "Sorumluluk duygusu",
                "Liderlik",
                "Uyum sağlama"
            ],


            "weaknesses":
            [
                "Aşırı fedakarlık",
                "Köy için kendini feda etme"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Yeni nesli destekleyen ve yol gösteren karakterlerdir.",

            "enemy":
            "Onurlu fakat tehlikeli rakipler olabilir.",

            "stranger":
            "Mesafeli ama saygılı yaklaşırlar."
        },


        "story_hooks":
        [
            "Eski Sarutobi teknikleri",
            "Hokage mirası",
            "Köy içi siyasi görevler"
        ]
    },





    "Shimura":
    {
        "origin":
        "Konoha tarihinde sert güvenlik anlayışıyla bilinen eski klan.",


        "village":
        "Konohagakure",


        "history":
        [
            "Konoha'nın kuruluş dönemlerinden beri var olmuştur.",
            "Köy güvenliği ve gizli operasyonlarda etkili olmuştur.",
            "Root organizasyonu ile bağlantılıdır."
        ],


        "culture":
        [
            "Görev",
            "Disiplin",
            "Mutlak sadakat",
            "Sonuç odaklılık"
        ],


        "combat_style":
        [
            "Gizli operasyon",
            "Suikast teknikleri",
            "İstihbarat"
        ],


        "psychology":
        {
            "strengths":
            [
                "Soğukkanlılık",
                "Kararlılık",
                "Strateji"
            ],


            "weaknesses":
            [
                "Aşırı kontrol isteği",
                "Ahlaki sınırları zorlamak"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Kolay güvenmez ancak güvenince koruyucu olur.",

            "enemy":
            "Manipülatif ve hesapçı davranabilir.",

            "stranger":
            "Şüpheci ve araştırmacıdır."
        },


        "story_hooks":
        [
            "Root geçmişi",
            "Gizli Konoha operasyonları",
            "Kayıp istihbarat dosyaları"
        ]
    },





    "Hatake":
    {
        "origin":
        "Az sayıda üyesi olmasına rağmen olağanüstü yetenekleriyle tanınan Konoha klanı.",


        "village":
        "Konohagakure",


        "rarity":
        "Rare",


        "history":
        [
            "Konoha'nın en yetenekli shinobi ailelerinden biridir.",
            "Hatake Sakumo gibi efsanevi savaşçılar yetiştirmiştir.",
            "Adaptasyon ve teknik ustalığıyla tanınır."
        ],


        "culture":
        [
            "Mükemmellik",
            "Görev",
            "Teknik ustalık"
        ],


        "combat_style":
        [
            "Kenjutsu",
            "Lightning Release",
            "Kopyalama ve adaptasyon"
        ],


        "psychology":
        {
            "strengths":
            [
                "Hızlı öğrenme",
                "Analiz",
                "Savaş zekası"
            ],


            "weaknesses":
            [
                "Yalnızlık",
                "Aşırı sorumluluk alma"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Sakin ve güvenilir bir müttefik olur.",

            "enemy":
            "Rakibinin tüm açıklarını analiz eder.",

            "stranger":
            "Sessiz ve gözlemcidir."
        },


        "story_hooks":
        [
            "Kayıp Hatake teknikleri",
            "Eski kılıç ustaları",
            "Konoha elit görevleri"
        ]
    },
        "Kaguya":
    {
        "origin":
        "Kemik yapısını kontrol edebilen eski ve savaşçı bir klan.",


        "village":
        "Kirigakure",


        "bloodline":
        "Shikotsumyaku",


        "rarity":
        "Rare",


        "history":
        [
            "Kendi savaşçı doğaları nedeniyle diğer topluluklardan ayrılmıştır.",
            "Kirigakure'nin eski dönemlerinde korkulan savaşçılardan olmuşlardır.",
            "Klanın aşırı savaş tutkusu kendi yok oluşlarına neden olmuştur."
        ],


        "culture":
        [
            "Savaş tutkusu",
            "Güç",
            "Onur",
            "Hayatta kalma"
        ],


        "combat_style":
        [
            "Bone Manipulation",
            "Yakın dövüş",
            "Acımasız saldırılar"
        ],


        "psychology":
        {
            "strengths":
            [
                "Korkusuzluk",
                "Yüksek dayanıklılık",
                "Savaş içgüdüsü"
            ],


            "weaknesses":
            [
                "Kontrolsüz öfke",
                "Savaş bağımlılığı",
                "Diplomasi eksikliği"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Gücü takdir eder, zayıflığa karşı sabırsız olabilir.",

            "enemy":
            "Son derece agresif ve direkt saldırır.",

            "stranger":
            "Rakibini test etmeye çalışır."
        },


        "story_hooks":
        [
            "Hayatta kalan Kaguya üyeleri",
            "Kayıp kemik teknikleri",
            "Eski savaş ritüelleri"
        ]
    },





    "Hozuki":
    {
        "origin":
        "Vücudunu sıvıya dönüştürebilen gizemli Kirigakure klanı.",


        "village":
        "Kirigakure",


        "bloodline":
        "Hydrification Technique",


        "history":
        [
            "Kirigakure'nin güçlü savaşçı ailelerinden biridir.",
            "Bazı üyeleri Yedi Ninja Kılıç Ustaları arasında yer almıştır.",
            "Su teknikleri ve gizli operasyonlarla tanınmıştır."
        ],


        "culture":
        [
            "Uyum sağlama",
            "Hayatta kalma",
            "Güç dengesi"
        ],


        "combat_style":
        [
            "Water Release",
            "Hydrification",
            "Kılıç kullanımı"
        ],


        "psychology":
        {
            "strengths":
            [
                "Esneklik",
                "Strateji",
                "Zor durumlarda hayatta kalma"
            ],


            "weaknesses":
            [
                "Su kaynaklarına ihtiyaç",
                "Aşırı özgüven"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Rahat ve kendinden emin davranabilir.",

            "enemy":
            "Zor tahmin edilen savaş tarzı kullanır.",

            "stranger":
            "Şakacı ama dikkatli olabilir."
        },


        "story_hooks":
        [
            "Yedi Kılıç mirası",
            "Kayıp su teknikleri",
            "Kirigakure suikast görevleri"
        ]
    },





    "Yuki":
    {
        "origin":
        "Buz salınımı kullanabilen nadir kan bağı klanı.",


        "village":
        "Kirigakure / Eski Su Ülkesi bölgeleri",


        "bloodline":
        "Ice Release",


        "rarity":
        "Rare",


        "history":
        [
            "Kan bağı kullanıcılarına karşı korku ve nefret yaşanan dönemlerde avlanmışlardır.",
            "Bazı üyeleri kimliklerini gizlemek zorunda kalmıştır.",
            "Buz teknikleri nedeniyle hem korkulmuş hem saygı duyulmuştur."
        ],


        "culture":
        [
            "Gizlilik",
            "Sabır",
            "Hayatta kalma"
        ],


        "combat_style":
        [
            "Ice Release",
            "Savunma teknikleri",
            "Alan kontrolü"
        ],


        "psychology":
        {
            "strengths":
            [
                "Sakinlik",
                "Kontrol",
                "Sabır"
            ],


            "weaknesses":
            [
                "Geçmiş travmaları",
                "Toplumdan uzaklaşma"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Güven kazandığında son derece sadık olur.",

            "enemy":
            "Soğuk ve hesaplı savaşır.",

            "stranger":
            "Kendini gizlemeye çalışır."
        },


        "story_hooks":
        [
            "Gizli Yuki aileleri",
            "Buz teknikleri araştırmaları",
            "Kan bağı avcıları"
        ]
    },
        "Yotsuki":
    {
        "origin":
        "Kumogakure'nin güçlü fiziksel savaşçı geleneğine sahip klanı.",


        "village":
        "Kumogakure",


        "rarity":
        "Rare",


        "history":
        [
            "Kumo'nun askeri gücünde önemli rol oynamıştır.",
            "Lightning Release ve yüksek fiziksel güçleriyle tanınırlar.",
            "Dördüncü Raikage dönemindeki savaş kültürünün temel taşlarından biridir."
        ],


        "culture":
        [
            "Güç",
            "Dayanıklılık",
            "Onur",
            "Savaş disiplini"
        ],


        "combat_style":
        [
            "Lightning Release",
            "Taijutsu",
            "Lightning Armor",
            "Yakın dövüş"
        ],


        "psychology":
        {
            "strengths":
            [
                "Cesaret",
                "Fiziksel dayanıklılık",
                "Savaş kararlılığı"
            ],


            "weaknesses":
            [
                "Direkt saldırıya eğilim",
                "Gurur"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Güçlü rakiplere ve savaşçılara saygı duyar.",

            "enemy":
            "Doğrudan ve baskın bir savaş tarzı kullanır.",

            "stranger":
            "Önce gücünü ve niyetini ölçer."
        },


        "story_hooks":
        [
            "Kayıp Lightning teknikleri",
            "Raikage muhafızları",
            "Kumo savaş turnuvaları",
            "Eski savaşçı aileleri"
        ]
    },





    "Kinkaku Lineage":
    {
        "origin":
        "Altı Yol Bilgesi dönemine uzanan eski chakra mirasına sahip savaşçı soy.",


        "village":
        "Kumogakure",


        "rarity":
        "Legendary",


        "history":
        [
            "Kinkaku ve Ginkaku kardeşler bu soyun en bilinen temsilcileridir.",
            "Dokuz Kuyruklu'nun chakra mirasıyla bağlantılıdır.",
            "Altı Yol Hazineleri ile ilişkilendirilen nadir savaşçılardır."
        ],


        "culture":
        [
            "Güç gösterisi",
            "Savaş mirası",
            "Efsanevi soy bilinci"
        ],


        "combat_style":
        [
            "Yüksek chakra kullanımı",
            "Özel silah kullanımı",
            "Bijuu chakra dönüşümleri"
        ],


        "psychology":
        {
            "strengths":
            [
                "Aşırı chakra kapasitesi",
                "Savaş deneyimi",
                "Dayanıklılık"
            ],


            "weaknesses":
            [
                "Güce aşırı güven",
                "Kontrol sorunları"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Güçlü müttefiklere değer verir.",

            "enemy":
            "Ezici güç kullanarak korku yaratmaya çalışır.",

            "stranger":
            "Kendisini üstün görme eğilimi gösterebilir."
        },


        "story_hooks":
        [
            "Altı Yol hazineleri",
            "Kayıp chakra mirası",
            "Bijuu bağlantıları",
            "Eski savaş kalıntıları"
        ]
    },
     "Kamizuru":
    {
        "origin":
        "Iwagakure kökenli eski böcek teknikleri kullanan ninja klanı.",


        "village":
        "Iwagakure",


        "rarity":
        "Rare",


        "history":
        [
            "Aburame klanına benzer şekilde böcek teknikleri kullanmıştır.",
            "Geçmişte güçlü bir klan olmasına rağmen zamanla etkisini kaybetmiştir.",
            "Iwa'nın gizli operasyonlarında kullanılmıştır."
        ],


        "culture":
        [
            "Araştırma",
            "Kontrol",
            "Doğa ile uyum",
            "Sabır"
        ],


        "combat_style":
        [
            "Bee techniques",
            "Recon",
            "Tracking",
            "Ninjutsu"
        ],


        "psychology":
        {
            "strengths":
            [
                "Analiz yeteneği",
                "Sabır",
                "Uzun vadeli planlama"
            ],


            "weaknesses":
            [
                "Doğrudan güç savaşlarında dezavantaj",
                "Hazırlığa ihtiyaç duyma"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Bilgi paylaşmaya açık ama kontrollüdür.",

            "enemy":
            "Rakibini izleyerek zayıf noktasını arar.",

            "stranger":
            "Mesafeli ve gözlemci davranır."
        },


        "story_hooks":
        [
            "Kayıp böcek teknikleri",
            "Iwa araştırma laboratuvarları",
            "Eski klan rekabetleri"
        ]
    },





    "Explosion Release Clan":
    {
        "origin":
        "Patlama Salınımı kullanan nadir savaşçı aileler.",


        "village":
        "Iwagakure",


        "bloodline":
        "Explosion Release",


        "rarity":
        "Rare",


        "history":
        [
            "Iwagakure'nin saldırı gücünde önemli rol oynamıştır.",
            "Patlayıcı teknikleri savaş alanında korkulan yeteneklerdir.",
            "Bazı kullanıcılar özel askeri operasyonlarda görev almıştır."
        ],


        "culture":
        [
            "Yaratıcılık",
            "Yıkıcı güç",
            "Askeri başarı"
        ],


        "combat_style":
        [
            "Explosion Release",
            "Alan hasarı",
            "Uzaktan saldırı",
            "Yıkım teknikleri"
        ],


        "psychology":
        {
            "strengths":
            [
                "Yüksek saldırı gücü",
                "Savaş alanı kontrolü",
                "Yaratıcı teknik kullanımı"
            ],


            "weaknesses":
            [
                "Kontrol kaybı riski",
                "Yakın savunmada zayıflık"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Güçlü teknikleri olan kişilere saygı duyar.",

            "enemy":
            "Mesafeyi koruyarak baskı kurar.",

            "stranger":
            "Kabiliyetini göstermeye eğilimli olabilir."
        },


        "story_hooks":
        [
            "Kayıp patlama teknikleri",
            "Savaş mühendisliği görevleri",
            "Yasak patlayıcı araştırmaları"
        ]
    },
        "Chinoike":
    {
        "origin":
        "Ketsuryugan göz tekniğine sahip, nadir ve karanlık geçmişi olan klan.",


        "village":
        "Land of Lightning",


        "bloodline":
        "Ketsuryugan",


        "rarity":
        "Legendary",


        "history":
        [
            "Kan kontrolü yetenekleri nedeniyle korkulan bir klan olmuştur.",
            "Bazı dönemlerde diğer topluluklar tarafından dışlanmıştır.",
            "Gizli yaşamaya zorlanan üyeleri vardır."
        ],


        "culture":
        [
            "Hayatta kalma",
            "Gizlilik",
            "Kan bağı gururu",
            "Bilgi"
        ],


        "combat_style":
        [
            "Ketsuryugan",
            "Genjutsu",
            "Kan teknikleri",
            "Manipülasyon"
        ],


        "psychology":
        {
            "strengths":
            [
                "Zihinsel dayanıklılık",
                "Manipülasyon yeteneği",
                "Gizlilik"
            ],


            "weaknesses":
            [
                "Toplumdan dışlanma",
                "Güven problemleri"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Güveni zor verir fakat sadakati güçlüdür.",

            "enemy":
            "Rakibinin korkularını kullanmaya çalışır.",

            "stranger":
            "Gizemli ve mesafeli davranır."
        },


        "story_hooks":
        [
            "Kayıp Ketsuryugan kullanıcıları",
            "Kan teknikleri araştırması",
            "Eski yasak ritüeller"
        ]
    },





    "Fuma":
    {
        "origin":
        "Çeşitli bölgelerde yaşayan savaşçı ve paralı ninja aileleri.",


        "village":
        "Various",


        "rarity":
        "Common",


        "history":
        [
            "Birçok bölgede paralı asker olarak görev yapmışlardır.",
            "Silah kullanımı ve suikast teknikleriyle tanınırlar."
        ],


        "culture":
        [
            "Hayatta kalma",
            "Para",
            "Savaş becerisi"
        ],


        "combat_style":
        [
            "Shuriken teknikleri",
            "Silah kullanımı",
            "Suikast"
        ],


        "psychology":
        {
            "strengths":
            [
                "Uyum sağlama",
                "Pratik zeka",
                "Savaş deneyimi"
            ],


            "weaknesses":
            [
                "Bağlılık eksikliği",
                "Paraya önem verme"
            ]
        },


        "npc_behavior":
        {
            "friendly":
            "Anlaşma ve çıkar ilişkisine önem verir.",

            "enemy":
            "Kirli savaş yöntemleri kullanabilir.",

            "stranger":
            "Profesyonel ve mesafelidir."
        },


        "story_hooks":
        [
            "Paralı ninja görevleri",
            "Kayıp Fuma silahları",
            "Yeraltı organizasyonları"
        ]
    },





    "Iburi":
    {
        "origin":
        "Duman formuna dönüşebilen gizli bir klan.",


        "village":
        "Unknown",


        "bloodline":
        "Smoke Transformation",


        "rarity":
        "Rare",


        "history":
        [
            "Klan üyeleri özel duman yetenekleri nedeniyle gizlenmiştir.",
            "Kontrol sorunları nedeniyle izole yaşamışlardır."
        ],


        "culture":
        [
            "Gizlilik",
            "Aile koruması",
            "Hayatta kalma"
        ],


        "combat_style":
        [
            "Smoke Body",
            "Sızma",
            "Casusluk"
        ],


        "psychology":
        {
            "strengths":
            [
                "Görünmezlik",
                "Kaçış yeteneği",
                "Casusluk"
            ],


            "weaknesses":
            [
                "Kontrol problemleri",
                "Fiziksel saldırılara bağımlılık"
            ]
        },


        "story_hooks":
        [
            "Kayıp Iburi aileleri",
            "Duman teknik araştırmaları",
            "Gizli casus görevleri"
        ]
    },





    "Tsuchigumo":
    {
        "origin":
        "Yasak teknikler ve örümcek temelli yeteneklerle bilinen eski klan.",

        "village":
        "Unknown",

        "rarity":
        "Rare",

        "history":
        [
            "Güçlü yasak tekniklere sahip olmuştur.",
            "Bazı üyeleri köylerden uzak yaşamıştır."
        ],

        "culture":
        [
            "Bilgi",
            "Teknik geliştirme",
            "Gizlilik"
        ],

        "combat_style":
        [
            "Fuinjutsu",
            "Trap techniques",
            "Spider techniques"
        ],

        "psychology":
        {
            "strengths":
            [
                "Hazırlık",
                "Strateji",
                "Teknik bilgisi"
            ],

            "weaknesses":
            [
                "Uzun hazırlık süresi",
                "Doğrudan savaş zayıflığı"
            ]
        },

        "npc_behavior":
        {
            "friendly":
            "Bilgi paylaşımı karşılığında yardım eder.",

            "enemy":
            "Tuzak ve planlarla savaşır.",

            "stranger":
            "Şüpheli ve gizemlidir."
        },

        "story_hooks":
        [
            "Yasak teknik araştırmaları",
            "Eski mühürler",
            "Kayıp klan kalıntıları"
        ]
    }


}


def get_all_clans() -> list[str]:
    return list(CLAN_DATABASE.keys())