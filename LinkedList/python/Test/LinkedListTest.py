import unittest
from Main.LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_insert(self):
        linkedList = LinkedList()
        linkedList.insert(10)
        linkedList.insert(12)
        linkedList.insert(13)

        self.assertEqual(linkedList.size(), 3)


    def test_insert_and_remove(self):
        linkedList = LinkedList()
        linkedList.insert(10)
        linkedList.remove(10)

        self.assertEqual(linkedList.size(),0)