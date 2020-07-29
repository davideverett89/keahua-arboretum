from uuid import uuid1


class Identifiable:

    def __init__(self):
        self.id = str(uuid1())[:8]
