import unittest

from classes.room import Room
from classes.guest import Guest
from classes.bar import Bar
from classes.song import Song

class TestBar(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Venice Suite", 7, 5)
        self.room2 = Room("Cosy Wee Thing", 2, 15)
        self.room3 = Room("Cybernautic Highway", 9, 4)
        self.rooms = [self.room1, self.room2, self.room3]
        self.song1 = Song("The Love Shack", "The B52's")
        self.song2 = Song("Africa", "Toto")
        self.song3 = Song("Burning Down the House", "Talking Heads")
        self.guest1 = Guest("Rabbie Burns", 40, self.song1)
        self.guest2 = Guest("Christina Rossetti", 30, self.song3)
        self.guest3 = Guest("Lord Byron", 10, self.song3)

        self.bar = Bar(0)

    def test_collect_payment_from_rooms(self):
        self.room1.payment(self.guest1)
        self.room2.payment(self.guest2)
        self.room3.payment(self.guest3)
        self.assertEqual(35, self.guest1.wallet)
        self.assertEqual(15, self.guest2.wallet)
        self.assertEqual(6, self.guest3.wallet)
        self.assertEqual(5, self.room1.till)
        self.assertEqual(15, self.room2.till)
        self.assertEqual(4, self.room3.till)
        self.bar.collect_payment_from_rooms(self.rooms)
        self.assertEqual(24, self.bar.till)
        self.assertEqual(0, self.room1.till + self.room1.till + self.room1.till)