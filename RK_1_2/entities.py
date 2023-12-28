class Musician:
    def __init__(self, id_: int, name: str, storage: str, orchestra_id: int):
        self.id = id_
        self.name = name
        self.instrument = storage
        self.orchestra_id = orchestra_id


class Orchestra:
    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name


class MusicianOrchestra:
    """
    Class implementing many-to-many binding
    """

    def __init__(self, musician_id: int, orchestra_id: int):
        self.musician_id = musician_id
        self.orchestra_id = orchestra_id
