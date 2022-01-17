class Bar:
    def __init__(self, till):
        self.till = till

    def collect_payment_from_rooms(self, rooms):
        for room in rooms:
            self.till += room.till
            room.till = 0

