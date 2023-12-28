from entities import Orchestra, Musician, MusicianOrchestra

orchestras = (
    Orchestra(1, "Mariinsky Theatre Orchestra"),
    Orchestra(2, "St. Petersburg Philharmonic Orchestra"),
    Orchestra(3, "Bolshoi Theatre Orchestra"),
    Orchestra(4, "Moscow City Symphony - Russian Philharmonic"),
    Orchestra(5, "State Academic Symphony Orchestra of Russia"),
    Orchestra(6, "Novosibirsk Symphony Orchestra"),
)

musicians = [
    Musician(1, "Valery Gergiev", "Conductor", 1),
    Musician(2, "Vadim Repin", "Violin", 1),
    Musician(3, "Anna Netrebko", "Soprano", 3),
    Musician(4, "Daniil Trifonov", "Piano", 2),
    Musician(5, "Yuri Bashmet", "Viola", 4),
    Musician(6, "Denis Matsuev", "Piano", 5),
    Musician(7, "Marina Abramova", "Cello", 2),
    Musician(8, "Maxim Vengerov", "Violin", 1),
    Musician(9, "Evgeny Kissin", "Piano", 3),
    Musician(10, "Natalia Gutman", "Cello", 6),
]


musicians_orchestras = [
    MusicianOrchestra(1, 2),
    MusicianOrchestra(1, 4),
    MusicianOrchestra(1, 5),
    MusicianOrchestra(2, 6),
    MusicianOrchestra(2, 3),
    MusicianOrchestra(3, 1),
    MusicianOrchestra(3, 2),
    MusicianOrchestra(4, 1),
    MusicianOrchestra(4, 6),
    MusicianOrchestra(6, 1),
    MusicianOrchestra(6, 2),
    MusicianOrchestra(6, 6),
    MusicianOrchestra(5, 3),
    MusicianOrchestra(7, 4),
    MusicianOrchestra(7, 5),
    MusicianOrchestra(8, 6),
]
