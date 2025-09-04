# musica/data.py

CATALOGO = {
    "rock": {
        "nombre": "Rock",
        "bandas": {
            "pink-floyd": {
                "nombre": "Pink Floyd",
                "discografia": {
                    "the-dark-side-of-the-moon": {
                        "titulo": "The Dark Side of the Moon",
                        "anio": 1973,
                        "portada": "img/disco_the_dark_side_of_the_moon.jpg",
                        "temas": [
                            ("Speak to Me", "1:30"),
                            ("Breathe", "2:43"),
                            ("Time", "6:53"),
                            ("Money", "6:22"),
                        ],
                    },
                    "wish-you-were-here": {
                        "titulo": "Wish You Were Here",
                        "anio": 1975,
                        "portada": "img/wish_you_were_here.webp",
                        "temas": [
                            ("Shine On You Crazy Diamond (I–V)", "13:32"),
                            ("Welcome to the Machine", "7:31"),
                            ("Have a Cigar", "5:08"),
                            ("Wish You Were Here", "5:34"),
                        ],
                    },
                    "animals": {
                        "titulo": "Animals",
                        "anio": 1977,
                        "portada": "img/animals.jpg",
                        "temas": [
                            ("Pigs on the Wing (Part One)", "1:25"),
                            ("Dogs", "17:05"),
                            ("Pigs (Three Different Ones)", "11:26"),
                            ("Sheep", "10:20"),
                        ],
                    },
                },
            },
            "genesis": {
                "nombre": "Genesis",
                "discografia": {
                    "selling-england-by-the-pound": {
                        "titulo": "Selling England by the Pound",
                        "anio": 1973,
                        "portada": "img/selling_england_by_the_pound.jpg",
                        "temas": [
                            ("Dancing with the Moonlit Knight", "8:02"),
                            ("I Know What I Like", "4:06"),
                            ("Firth of Fifth", "9:34"),
                        ],
                    },
                    "the-lamb-lies-down-on-broadway": {
                        "titulo": "The Lamb Lies Down on Broadway",
                        "anio": 1974,
                        "portada": "img/the_lamb_lies_down_on_broadway.jpg",
                        "temas": [
                            ("The Lamb Lies Down on Broadway", "4:52"),
                            ("In the Cage", "8:15"),
                            ("The Carpet Crawlers", "5:16"),
                        ],
                    },
                    "duke": {
                        "titulo": "Duke",
                        "anio": 1980,
                        "portada": "img/duke.jpg",
                        "temas": [
                            ("Behind the Lines", "5:31"),
                            ("Duchess", "6:40"),
                            ("Turn It On Again", "3:50"),
                        ],
                    },
                },
            },
            "yes": {
                "nombre": "Yes",
                "discografia": {
                    "fragile": {
                        "titulo": "Fragile",
                        "anio": 1971,
                        "portada": "img/fragile.webp",
                        "temas": [
                            ("Roundabout", "8:29"),
                            ("Cans and Brahms", "1:43"),
                            ("Heart of the Sunrise", "10:34"),
                        ],
                    },
                    "close-to-the-edge": {
                        "titulo": "Close to the Edge",
                        "anio": 1972,
                        "portada": "img/close_to_the_edge.jpg",
                        "temas": [
                            ("Close to the Edge", "18:12"),
                            ("And You and I", "10:09"),
                            ("Siberian Khatru", "8:55"),
                        ],
                    },
                    "relayer": {
                        "titulo": "Relayer",
                        "anio": 1974,
                        "portada": "img/relayer.jpg",
                        "temas": [
                            ("The Gates of Delirium", "21:55"),
                            ("Sound Chaser", "9:25"),
                            ("To Be Over", "9:08"),
                        ],
                    },
                },
            },
            "king-crimson": {
                "nombre": "King Crimson",
                "discografia": {
                    "in-the-court-of-the-crimson-king": {
                        "titulo": "In the Court of the Crimson King",
                        "anio": 1969,
                        "portada": "img/in_the_court_of_the_crimson_king.jpg",
                        "temas": [
                            ("21st Century Schizoid Man", "7:24"),
                            ("I Talk to the Wind", "6:04"),
                            ("Epitaph", "8:47"),
                        ],
                    },
                    "red": {
                        "titulo": "Red",
                        "anio": 1974,
                        "portada": "img/red.jpg",
                        "temas": [
                            ("Red", "6:18"),
                            ("Fallen Angel", "6:03"),
                            ("Starless", "12:18"),
                        ],
                    },
                    "discipline": {
                        "titulo": "Discipline",
                        "anio": 1981,
                        "portada": "img/discipline.jpg",
                        "temas": [
                            ("Frame by Frame", "5:09"),
                            ("Matte Kudasai", "3:50"),
                            ("Discipline", "5:13"),
                        ],
                    },
                },
            },
            "rush": {
                "nombre": "Rush",
                "discografia": {
                    "2112": {
                        "titulo": "2112",
                        "anio": 1976,
                        "portada": "img/2112.jpg",
                        "temas": [
                            ("2112 Overture/Temples of Syrinx", "10:06"),
                            ("A Passage to Bangkok", "3:34"),
                            ("Something for Nothing", "3:59"),
                        ],
                    },
                    "moving-pictures": {
                        "titulo": "Moving Pictures",
                        "anio": 1981,
                        "portada": "img/moving_pictures.jpg",
                        "temas": [
                            ("Tom Sawyer", "4:33"),
                            ("Red Barchetta", "6:10"),
                            ("YYZ", "4:24"),
                        ],
                    },
                    "permanent-waves": {
                        "titulo": "Permanent Waves",
                        "anio": 1980,
                        "portada": "img/permanent_waves.jpg",
                        "temas": [
                            ("The Spirit of Radio", "4:57"),
                            ("Freewill", "5:23"),
                            ("Natural Science", "9:17"),
                        ],
                    },
                },
            },
        },
    },

    # Otros géneros
    "pop": {
        "nombre": "Pop", 
        "bandas": {
            "the-beatles": {
                "nombre": "The Beatles",
                "discografia": {
                    "abbey-road": {
                        "titulo": "Abbey Road",
                        "anio": 1969,
                        "portada": "img/abbey_road.jpeg",
                        "temas": [
                            ("Come Together", "4:20"),
                            ("Something", "3:03"),
                            ("Here Comes the Sun", "3:05"),
                            ("The End", "2:20"),
                        ],
                    },
                    "sgt-peppers": {
                        "titulo": "Sgt. Pepper's Lonely Hearts Club Band",
                        "anio": 1967,
                        "portada": "img/sgt_peppers.png",
                        "temas": [
                            ("Sgt. Pepper's Lonely Hearts Club Band", "2:02"),
                            ("With a Little Help from My Friends", "2:44"),
                            ("Lucy in the Sky with Diamonds", "3:28"),
                            ("A Day in the Life", "5:33"),
                        ],
                    },
                    "revolver": {
                        "titulo": "Revolver",
                        "anio": 1966,
                        "portada": "img/revolver.jpg",
                        "temas": [
                            ("Eleanor Rigby", "2:06"),
                            ("Yellow Submarine", "2:38"),
                            ("Here, There and Everywhere", "2:24"),
                            ("Tomorrow Never Knows", "2:57"),
                        ],
                    },
                },
            },
            "madonna": {
                "nombre": "Madonna",
                "discografia": {
                    "like-a-virgin": {
                        "titulo": "Like a Virgin",
                        "anio": 1984,
                        "portada": "img/like_a_virgin.jpg",
                        "temas": [
                            ("Material Girl", "4:01"),
                            ("Like a Virgin", "3:38"),
                            ("Into the Groove", "4:44"),
                            ("Angel", "4:10"),
                        ],
                    },
                    "ray-of-light": {
                        "titulo": "Ray of Light",
                        "anio": 1998,
                        "portada": "img/ray_of_light.jpg",
                        "temas": [
                            ("Drowned World/Substitute for Love", "5:09"),
                            ("Ray of Light", "5:50"),
                            ("Candy Perfume Girl", "4:35"),
                            ("Nothing Really Matters", "4:27"),
                        ],
                    },
                    "confessions-on-a-dance-floor": {
                        "titulo": "Confessions on a Dance Floor",
                        "anio": 2005,
                        "portada": "img/confessions.jpg",
                        "temas": [
                            ("Hung Up", "5:36"),
                            ("Sorry", "4:43"),
                            ("Get Together", "5:29"),
                            ("Jump", "3:59"),
                        ],
                    },
                },
            },
            "michael-jackson": {
                "nombre": "Michael Jackson",
                "discografia": {
                    "thriller": {
                        "titulo": "Thriller",
                        "anio": 1982,
                        "portada": "img/thriller.jpg",
                        "temas": [
                            ("Wanna Be Startin' Somethin'", "6:02"),
                            ("Billie Jean", "4:54"),
                            ("Beat It", "4:18"),
                            ("Thriller", "5:57"),
                        ],
                    },
                    "bad": {
                        "titulo": "Bad",
                        "anio": 1987,
                        "portada": "img/bad.jpg",
                        "temas": [
                            ("Bad", "4:07"),
                            ("The Way You Make Me Feel", "4:58"),
                            ("Man in the Mirror", "5:19"),
                            ("Smooth Criminal", "4:17"),
                        ],
                    },
                    "off-the-wall": {
                        "titulo": "Off the Wall",
                        "anio": 1979,
                        "portada": "img/wall.jpg",
                        "temas": [
                            ("Don't Stop 'Til You Get Enough", "6:05"),
                            ("Rock with You", "3:40"),
                            ("Off the Wall", "4:05"),
                            ("She's Out of My Life", "3:38"),
                        ],
                    },
                },
            },
            "abba": {
                "nombre": "ABBA",
                "discografia": {
                    "arrival": {
                        "titulo": "Arrival",
                        "anio": 1976,
                        "portada": "img/arrival.jpg",
                        "temas": [
                            ("Money, Money, Money", "3:06"),
                            ("Knowing Me, Knowing You", "4:02"),
                            ("Dancing Queen", "3:51"),
                            ("Fernando", "4:13"),
                        ],
                    },
                    "the-album": {
                        "titulo": "The Album",
                        "anio": 1977,
                        "portada": "img/the_album.jpg",
                        "temas": [
                            ("Eagle", "5:51"),
                            ("Take a Chance on Me", "4:05"),
                            ("The Name of the Game", "4:52"),
                            ("Thank You for the Music", "3:50"),
                        ],
                    },
                    "waterloo": {
                        "titulo": "Waterloo",
                        "anio": 1974,
                        "portada": "img/waterloo.jpg",
                        "temas": [
                            ("Waterloo", "2:42"),
                            ("Honey, Honey", "2:55"),
                            ("Watch Out", "3:51"),
                            ("What About Livingstone", "2:57"),
                        ],
                    },
                },
            },
            "dua-lipa": {
                "nombre": "Dua Lipa",
                "discografia": {
                    "future-nostalgia": {
                        "titulo": "Future Nostalgia",
                        "anio": 2020,
                        "portada": "img/future.jpg",
                        "temas": [
                            ("Don't Start Now", "3:03"),
                            ("Physical", "3:13"),
                            ("Levitating", "3:23"),
                            ("Break My Heart", "3:41"),
                        ],
                    },
                    "dua-lipa": {
                        "titulo": "Dua Lipa",
                        "anio": 2017,
                        "portada": "img/dua_lipa.jpg",
                        "temas": [
                            ("Genesis", "3:26"),
                            ("New Rules", "3:29"),
                            ("IDGAF", "3:37"),
                            ("Be the One", "3:22"),
                        ],
                    },
                    "radical-optimism": {
                        "titulo": "Radical Optimism",
                        "anio": 2024,
                        "portada": "img/radical_optimism.jpg",
                        "temas": [
                            ("Houdini", "3:06"),
                            ("Training Season", "3:28"),
                            ("Illusion", "3:22"),
                            ("French Exit", "2:34"),
                        ],
                    },
                },
            },
        }
    },
    "jazz": {
        "nombre": "Jazz", 
        "bandas": {
            "miles-davis": {
                "nombre": "Miles Davis",
                "discografia": {
                    "kind-of-blue": {
                        "titulo": "Kind of Blue",
                        "anio": 1959,
                        "portada": "img/kind_of_blue.jpg",
                        "temas": [
                            ("So What", "9:22"),
                            ("Freddie Freeloader", "9:46"),
                            ("Blue in Green", "5:37"),
                            ("All Blues", "11:33"),
                        ],
                    },
                    "bitches-brew": {
                        "titulo": "Bitches Brew",
                        "anio": 1970,
                        "portada": "img/bitches.jpg",
                        "temas": [
                            ("Pharaoh's Dance", "20:05"),
                            ("Bitches Brew", "27:00"),
                            ("Spanish Key", "17:32"),
                            ("John McLaughlin", "4:22"),
                        ],
                    },
                    "sketches-of-spain": {
                        "titulo": "Sketches of Spain",
                        "anio": 1960,
                        "portada": "img/sketches.jpg",
                        "temas": [
                            ("Concierto de Aranjuez", "16:20"),
                            ("Will o' the Wisp", "3:47"),
                            ("The Pan Piper", "3:51"),
                            ("Saeta", "5:05"),
                        ],
                    },
                },
            },
            "john-coltrane": {
                "nombre": "John Coltrane",
                "discografia": {
                    "a-love-supreme": {
                        "titulo": "A Love Supreme",
                        "anio": 1965,
                        "portada": "img/A_Love_Supreme.jpg",
                        "temas": [
                            ("Acknowledgement", "7:43"),
                            ("Resolution", "7:20"),
                            ("Pursuance", "10:42"),
                            ("Psalm", "7:05"),
                        ],
                    },
                    "giant-steps": {
                        "titulo": "Giant Steps",
                        "anio": 1960,
                        "portada": "img/giantsteps.jpg",
                        "temas": [
                            ("Giant Steps", "4:43"),
                            ("Cousin Mary", "5:45"),
                            ("Countdown", "4:22"),
                            ("Spiral", "5:56"),
                        ],
                    },
                    "blue-train": {
                        "titulo": "Blue Train",
                        "anio": 1958,
                        "portada": "img/blue-train.jpg",
                        "temas": [
                            ("Blue Train", "10:42"),
                            ("Moment's Notice", "9:10"),
                            ("Locomotion", "7:13"),
                            ("I'm Old Fashioned", "7:58"),
                        ],
                    },
                },
            },
            "charlie-parker": {
                "nombre": "Charlie Parker",
                "discografia": {
                    "bird-and-diz": {
                        "titulo": "Bird and Diz",
                        "anio": 1952,
                        "portada": "img/bird.jpg",
                        "temas": [
                            ("Bloomdido", "3:05"),
                            ("An Oscar for Treadwell", "3:05"),
                            ("Mohawk", "3:09"),
                            ("Leap Frog", "2:58"),
                        ],
                    },
                    "charlie-parker-with-strings": {
                        "titulo": "Charlie Parker with Strings",
                        "anio": 1950,
                        "portada": "img/parker.jpg",
                        "temas": [
                            ("Just Friends", "3:25"),
                            ("Everything Happens to Me", "3:20"),
                            ("April in Paris", "3:04"),
                            ("Summertime", "3:27"),
                        ],
                    },
                    "now-is-the-time": {
                        "titulo": "Now's the Time",
                        "anio": 1953,
                        "portada": "img/now.jpg",
                        "temas": [
                            ("Now's the Time", "3:15"),
                            ("Billie's Bounce", "3:09"),
                            ("Thriving on a Riff", "2:57"),
                            ("Ko Ko", "2:53"),
                        ],
                    },
                },
            },
            "duke-ellington": {
                "nombre": "Duke Ellington",
                "discografia": {
                    "ellington-at-newport": {
                        "titulo": "Ellington at Newport",
                        "anio": 1956,
                        "portada": "img/duke_ellington_ellington_at_newport_362802.jpg",
                        "temas": [
                            ("Festival Junction", "3:26"),
                            ("Blues to Be There", "3:32"),
                            ("Newport Up", "5:18"),
                            ("Jeep's Blues", "4:45"),
                        ],
                    },
                    "money-jungle": {
                        "titulo": "Money Jungle",
                        "anio": 1962,
                        "portada": "img/money.jpg",
                        "temas": [
                            ("Money Jungle", "7:08"),
                            ("Solitude", "4:22"),
                            ("Very Special", "6:15"),
                            ("Warm Valley", "5:03"),
                        ],
                    },
                    "piano-in-the-background": {
                        "titulo": "Piano in the Background",
                        "anio": 1960,
                        "portada": "img/piano.jpg",
                        "temas": [
                            ("You Better Know It", "3:12"),
                            ("Summertime", "4:28"),
                            ("Happy Reunion", "3:45"),
                            ("Meditation", "4:33"),
                        ],
                    },
                },
            },
            "bill-evans": {
                "nombre": "Bill Evans",
                "discografia": {
                    "waltz-for-debby": {
                        "titulo": "Waltz for Debby",
                        "anio": 1961,
                        "portada": "img/debby.jpg",
                        "temas": [
                            ("My Foolish Heart", "4:58"),
                            ("Waltz for Debby", "6:56"),
                            ("Detour Ahead", "7:36"),
                            ("My Romance", "6:30"),
                        ],
                    },
                    "sunday-at-the-village-vanguard": {
                        "titulo": "Sunday at the Village Vanguard",
                        "anio": 1961,
                        "portada": "img/sunday-at-the-village-vanguard.jpg",
                        "temas": [
                            ("Gloria's Step", "6:03"),
                            ("My Man's Gone Now", "6:23"),
                            ("Solar", "8:51"),
                            ("Alice in Wonderland", "8:25"),
                        ],
                    },
                    "portrait-in-jazz": {
                        "titulo": "Portrait in Jazz",
                        "anio": 1960,
                        "portada": "img/jazz.jpg",
                        "temas": [
                            ("Come Rain or Come Shine", "5:40"),
                            ("Autumn Leaves", "7:02"),
                            ("Witchcraft", "5:30"),
                            ("When I Fall in Love", "4:52"),
                        ],
                    },
                },
            },
        }
    },
    "blues": {
        "nombre": "Blues", 
        "bandas": {
            "bb-king": {
                "nombre": "B.B. King",
                "discografia": {
                    "live-at-the-regal": {
                        "titulo": "Live at the Regal",
                        "anio": 1965,
                        "portada": "img/live.jpg",
                        "temas": [
                            ("Every Day I Have the Blues", "2:55"),
                            ("Sweet Little Angel", "4:20"),
                            ("It's My Own Fault", "3:48"),
                            ("How Blue Can You Get", "4:42"),
                        ],
                    },
                    "completely-well": {
                        "titulo": "Completely Well",
                        "anio": 1969,
                        "portada": "img/completely-well.jpg",
                        "temas": [
                            ("The Thrill Is Gone", "5:25"),
                            ("So Excited", "3:15"),
                            ("No Good", "4:22"),
                            ("You're Losin' Me", "3:55"),
                        ],
                    },
                    "lucille": {
                        "titulo": "Lucille",
                        "anio": 1968,
                        "portada": "img/lucille.jpg",
                        "temas": [
                            ("Lucille", "6:50"),
                            ("You Move Me So", "4:15"),
                            ("Country Girl", "3:42"),
                            ("No Money, No Luck", "4:28"),
                        ],
                    },
                },
            },
            "muddy-waters": {
                "nombre": "Muddy Waters",
                "discografia": {
                    "electric-mud": {
                        "titulo": "Electric Mud",
                        "anio": 1968,
                        "portada": "img/electrid_mud.jpg",
                        "temas": [
                            ("I Just Want to Make Love to You", "3:10"),
                            ("Hoochie Coochie Man", "2:52"),
                            ("Let's Spend the Night Together", "7:17"),
                            ("She's All Right", "2:45"),
                        ],
                    },
                    "folk-singer": {
                        "titulo": "Folk Singer",
                        "anio": 1964,
                        "portada": "img/folk.jpg",
                        "temas": [
                            ("My Home Is in the Delta", "2:45"),
                            ("Long Distance Call", "3:22"),
                            ("My Captain", "2:18"),
                            ("Good Morning Little School Girl", "3:48"),
                        ],
                    },
                    "hard-again": {
                        "titulo": "Hard Again",
                        "anio": 1977,
                        "portada": "img/hard-again.jpg",
                        "temas": [
                            ("Mannish Boy", "5:05"),
                            ("Bus Driver", "3:58"),
                            ("I Want to Be Loved", "4:42"),
                            ("Jealous Hearted Man", "3:15"),
                        ],
                    },
                },
            },
            "stevie-ray-vaughan": {
                "nombre": "Stevie Ray Vaughan",
                "discografia": {
                    "texas-flood": {
                        "titulo": "Texas Flood",
                        "anio": 1983,
                        "portada": "img/texas.jpg",
                        "temas": [
                            ("Love Struck Baby", "2:22"),
                            ("Pride and Joy", "3:40"),
                            ("Texas Flood", "5:22"),
                            ("Tell Me", "2:32"),
                        ],
                    },
                    "couldnt-stand-the-weather": {
                        "titulo": "Couldn't Stand the Weather",
                        "anio": 1984,
                        "portada": "img/weather.jpg",
                        "temas": [
                            ("Scuttle Buttin'", "3:09"),
                            ("Couldn't Stand the Weather", "4:36"),
                            ("The Things (That) I Used to Do", "4:58"),
                            ("Voodoo Child (Slight Return)", "7:32"),
                        ],
                    },
                    "soul-to-soul": {
                        "titulo": "Soul to Soul",
                        "anio": 1985,
                        "portada": "img/soul.jpg",
                        "temas": [
                            ("Say What!", "5:12"),
                            ("Lookin' Out the Window", "2:32"),
                            ("Look at Little Sister", "2:39"),
                            ("Ain't Gone 'n' Give Up on Love", "5:03"),
                        ],
                    },
                },
            },
            "robert-johnson": {
                "nombre": "Robert Johnson",
                "discografia": {
                    "king-of-the-delta-blues": {
                        "titulo": "King of the Delta Blues",
                        "anio": 1961,
                        "portada": "img/king_of_delta.jpg",
                        "temas": [
                            ("Cross Road Blues", "2:38"),
                            ("Terraplane Blues", "3:04"),
                            ("Come On in My Kitchen", "2:48"),
                            ("Walking Blues", "2:31"),
                        ],
                    },
                    "complete-recordings": {
                        "titulo": "Complete Recordings",
                        "anio": 1996,
                        "portada": "img/complete.jpg",
                        "temas": [
                            ("Sweet Home Chicago", "3:02"),
                            ("Ramblin' on My Mind", "3:05"),
                            ("When You Got a Good Friend", "3:08"),
                            ("Kind Hearted Woman Blues", "3:04"),
                        ],
                    },
                    "last-fair-deal": {
                        "titulo": "Last Fair Deal Gone Down",
                        "anio": 1937,
                        "portada": "img/last_fair.jpg",
                        "temas": [
                            ("Last Fair Deal Gone Down", "2:20"),
                            ("Preaching Blues", "2:53"),
                            ("If I Had Possession Over Judgement Day", "2:32"),
                            ("Stones in My Passway", "2:23"),
                        ],
                    },
                },
            },
            "howlin-wolf": {
                "nombre": "Howlin' Wolf",
                "discografia": {
                    "moanin-in-the-moonlight": {
                        "titulo": "Moanin' in the Moonlight",
                        "anio": 1959,
                        "portada": "img/moanin.jpg",
                        "temas": [
                            ("Moanin' at Midnight", "2:58"),
                            ("How Many More Years", "2:48"),
                            ("Smokestack Lightning", "3:03"),
                            ("Baby How Long", "2:55"),
                        ],
                    },
                    "howlin-wolf-album": {
                        "titulo": "The Howlin' Wolf Album",
                        "anio": 1969,
                        "portada": "img/the_howlin.jpg",
                        "temas": [
                            ("Spoonful", "2:55"),
                            ("The Red Rooster", "2:48"),
                            ("Wang Dang Doodle", "2:50"),
                            ("Back Door Man", "2:32"),
                        ],
                    },
                    "evil": {
                        "titulo": "Evil",
                        "anio": 1954,
                        "portada": "img/evil.jpg",
                        "temas": [
                            ("Evil Is Going On", "2:45"),
                            ("Forty Four", "2:38"),
                            ("I Asked for Water", "2:42"),
                            ("All Night Long", "2:55"),
                        ],
                    },
                },
            },
        }
    },
    "clasica": {
        "nombre": "Clásica", 
        "bandas": {
            "ludwig-van-beethoven": {
                "nombre": "Ludwig van Beethoven",
                "discografia": {
                    "symphony-no-9": {
                        "titulo": "Symphony No. 9 'Choral'",
                        "anio": 1824,
                        "portada": "img/symphony.jpg",
                        "temas": [
                            ("I. Allegro ma non troppo", "16:15"),
                            ("II. Molto vivace", "11:45"),
                            ("III. Adagio molto e cantabile", "13:20"),
                            ("IV. Finale: Ode to Joy", "24:30"),
                        ],
                    },
                    "piano-sonata-14": {
                        "titulo": "Piano Sonata No. 14 'Moonlight'",
                        "anio": 1801,
                        "portada": "img/piano_sonata.jpg",
                        "temas": [
                            ("I. Adagio sostenuto", "6:02"),
                            ("II. Allegretto", "2:15"),
                            ("III. Presto agitato", "7:25"),
                        ],
                    },
                    "symphony-no-5": {
                        "titulo": "Symphony No. 5",
                        "anio": 1808,
                        "portada": "img/symphony5.jpg",
                        "temas": [
                            ("I. Allegro con brio", "7:20"),
                            ("II. Andante con moto", "10:25"),
                            ("III. Scherzo: Allegro", "5:30"),
                            ("IV. Allegro", "8:45"),
                        ],
                    },
                },
            },
            "wolfgang-amadeus-mozart": {
                "nombre": "Wolfgang Amadeus Mozart",
                "discografia": {
                    "requiem-in-d-minor": {
                        "titulo": "Requiem in D minor, K. 626",
                        "anio": 1791,
                        "portada": "img/requiem.jpg",
                        "temas": [
                            ("Introitus: Requiem aeternam", "4:45"),
                            ("Kyrie eleison", "2:35"),
                            ("Dies irae", "1:48"),
                            ("Lacrimosa", "3:15"),
                        ],
                    },
                    "symphony-no-40": {
                        "titulo": "Symphony No. 40 in G minor",
                        "anio": 1788,
                        "portada": "img/symphony40.jpg",
                        "temas": [
                            ("I. Molto allegro", "8:15"),
                            ("II. Andante", "9:02"),
                            ("III. Menuetto: Allegretto", "4:38"),
                            ("IV. Allegro assai", "7:45"),
                        ],
                    },
                    "piano-concerto-21": {
                        "titulo": "Piano Concerto No. 21",
                        "anio": 1785,
                        "portada": "img/piano_concerto.jpg",
                        "temas": [
                            ("I. Allegro maestoso", "14:20"),
                            ("II. Andante", "7:25"),
                            ("III. Allegro vivace assai", "6:45"),
                        ],
                    },
                },
            },
            "johann-sebastian-bach": {
                "nombre": "Johann Sebastian Bach",
                "discografia": {
                    "brandenburg-concertos": {
                        "titulo": "Brandenburg Concertos",
                        "anio": 1721,
                        "portada": "img/brandemburg.jpg",
                        "temas": [
                            ("Concerto No. 1 in F major", "21:15"),
                            ("Concerto No. 2 in F major", "11:30"),
                            ("Concerto No. 3 in G major", "10:45"),
                            ("Concerto No. 4 in G major", "15:20"),
                        ],
                    },
                    "well-tempered-clavier": {
                        "titulo": "The Well-Tempered Clavier",
                        "anio": 1722,
                        "portada": "img/the_well.jpg",
                        "temas": [
                            ("Prelude and Fugue No. 1 in C major", "4:15"),
                            ("Prelude and Fugue No. 2 in C minor", "3:45"),
                            ("Prelude and Fugue No. 8 in D-sharp minor", "7:22"),
                            ("Prelude and Fugue No. 21 in B-flat major", "4:58"),
                        ],
                    },
                    "goldberg-variations": {
                        "titulo": "Goldberg Variations",
                        "anio": 1741,
                        "portada": "img/goldberg.jpg",
                        "temas": [
                            ("Aria", "3:45"),
                            ("Variation 1", "1:20"),
                            ("Variation 15 (Canone alla Quinta)", "4:32"),
                            ("Variation 30 (Quodlibet)", "2:15"),
                        ],
                    },
                },
            },
            "frederic-chopin": {
                "nombre": "Frédéric Chopin",
                "discografia": {
                    "nocturnes": {
                        "titulo": "Nocturnes",
                        "anio": 1832,
                        "portada": "img/nocturnes.jpg",
                        "temas": [
                            ("Nocturne in E-flat major, Op. 9 No. 2", "4:30"),
                            ("Nocturne in F-sharp major, Op. 15 No. 2", "3:45"),
                            ("Nocturne in D-flat major, Op. 27 No. 2", "6:15"),
                            ("Nocturne in E minor, Op. 72 No. 1", "4:02"),
                        ],
                    },
                    "ballades": {
                        "titulo": "Ballades",
                        "anio": 1835,
                        "portada": "img/ballades.jpg",
                        "temas": [
                            ("Ballade No. 1 in G minor, Op. 23", "9:15"),
                            ("Ballade No. 2 in F major, Op. 38", "7:30"),
                            ("Ballade No. 3 in A-flat major, Op. 47", "7:45"),
                            ("Ballade No. 4 in F minor, Op. 52", "12:20"),
                        ],
                    },
                    "etudes": {
                        "titulo": "Études, Op. 10",
                        "anio": 1833,
                        "portada": "img/etudes.jpg",
                        "temas": [
                            ("Étude No. 3 in E major 'Tristesse'", "4:15"),
                            ("Étude No. 5 in G-flat major 'Black Keys'", "1:42"),
                            ("Étude No. 12 in C minor 'Revolutionary'", "2:38"),
                            ("Étude No. 25 in A minor 'Winter Wind'", "4:05"),
                        ],
                    },
                },
            },
            "pyotr-ilyich-tchaikovsky": {
                "nombre": "Pyotr Ilyich Tchaikovsky",
                "discografia": {
                    "swan-lake": {
                        "titulo": "Swan Lake Ballet Suite",
                        "anio": 1876,
                        "portada": "img/swan_lake.jpg",
                        "temas": [
                            ("Scene (Lake in the Moonlight)", "2:45"),
                            ("Valse", "7:15"),
                            ("Dance of the Swans", "1:30"),
                            ("Finale", "4:20"),
                        ],
                    },
                    "1812-overture": {
                        "titulo": "1812 Overture",
                        "anio": 1880,
                        "portada": "img/1812overture.jpg",
                        "temas": [
                            ("1812 Overture, Op. 49", "15:30"),
                            ("Romeo and Juliet Overture", "20:15"),
                            ("Marche Slave, Op. 31", "9:45"),
                        ],
                    },
                    "piano-concerto-no-1": {
                        "titulo": "Piano Concerto No. 1",
                        "anio": 1875,
                        "portada": "img/piano_concerto1.jpg",
                        "temas": [
                            ("I. Allegro non troppo e molto maestoso", "21:30"),
                            ("II. Andantino semplice", "7:15"),
                            ("III. Allegro con fuoco", "7:02"),
                        ],
                    },
                },
            },
        }
    },
}
