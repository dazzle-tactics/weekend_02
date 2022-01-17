import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):

        self.room1 = Room("Venice Suite", 7, 5)
        self.song1 = Song("The Love Shack", "The B52's")
        self.song2 = Song("Africa", "Toto")
        self.song3 = Song("Burning Down the House", "Talking Heads")
        self.guest1 = Guest("Rabbie Burns", 40, self.song1)
        self.songs = [self.song1, self.song2, self.song3]

    def test_guest_name(self):
        self.assertEqual("Rabbie Burns", self.guest1.name)

    def test_guest_wallet(self):
        self.assertEqual(40, self.guest1.wallet)

    def test_guest_cheers_when_fave_song_in_room(self):
        self.room1.add_songs_to_room(self.songs)
        self.assertEqual( "O ya beauty!", self.room1.guest_cheers_when_fave_song_in_room(self.guest1))
