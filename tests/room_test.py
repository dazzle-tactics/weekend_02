import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Venice Suite", 7, 5)
        self.room2 = Room("Cosy Wee Thing", 2, 15)
        self.room3 = Room("Cybernautic Highway", 9, 4)
        self.rooms = [self.room1, self.room2, self.room3]
        self.song1 = Song("The Love Shack", "The B52's")
        self.song2 = Song("Africa", "Toto")
        self.song3 = Song("Burning Down the House", "Talking Heads")
        self.songs = [self.song1, self.song2, self.song3]
        self.guest1 = Guest("Rabbie Burns", 40, self.song2)
        self.guest2 = Guest("Christina Rossetti", 30, self.song3)
        self.guest3 = Guest("Lord Byron", 10, self.song3)
        self.guest_group1 = [self.guest1, self.guest2, self.guest3]


    def test_guests_checked_into_room(self):
        self.room1.check_guests_in(self.guest_group1)
        self.assertEqual(3, len(self.room1.guests_checked_in))

    def test_guests_checked_out_of_room(self):
        self.room1.check_guests_out()
        self.assertEqual(0, len(self.room1.guests_checked_in))

    def test_add_songs_to_rooms(self):
        self.room1.add_songs_to_room(self.songs)
        self.room2.add_songs_to_room(self.songs)
        self.room3.add_songs_to_room(self.songs)
        self.assertEqual(9, len(self.room1.song_list) + len(self.room2.song_list) + len(self.room3.song_list))

    def test_more_guests_checked_in_than_capacity(self):
        self.assertEqual("Too many guests", self.room2.check_guests_in(self.guest_group1))

    def test_guests_pay_entry(self):
        self.room1.payment(self.guest1)
        self.assertEqual(35, self.guest1.wallet)
        self.assertEqual(5, self.room1.till)

    # def test_guests_pay_entry_when_checking_in(self):
    #     self.room1.check_guests_in(self.guest1)
    #     self.assertEqual(35, self.guest1.wallet)     