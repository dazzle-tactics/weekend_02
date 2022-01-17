
class Room:
    def __init__(self, name, capacity, price_per_person):
        self.name = name
        self.capacity = capacity
        self.price_per_person = price_per_person
        self.guests_checked_in = []
        self.song_list = []
        self.till = 0

    def payment(self, guest):
        guest.wallet -= self.price_per_person
        self.till += self.price_per_person

    def check_guests_in(self, group):
        for guest in group:
            self.guests_checked_in.append(guest)
        if len(self.guests_checked_in) > self.capacity:
            self.guests_checked_in = []
            return "Too many guests"
        
    def check_guests_out(self):
        self.guests_checked_in = []

    def add_songs_to_room(self, songs):
        for song in songs:
            self.song_list.append(song)
    
    def guest_cheers_when_fave_song_in_room(self, guest):
        for song in self.song_list:
            if guest.fave_song == song:
                return "O ya beauty!"

    