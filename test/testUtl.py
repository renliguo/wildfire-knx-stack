#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ctypes import create_string_buffer
import unittest

from common import ModuleIDs, BaseTest
from msg import Messaging

class TestUtlStringFunctions(BaseTest):

    CLASS = Messaging
    DLL = "messaging"

    def testStrCpyEmptyStringDoesNothing(self):
        dest = create_string_buffer(120)
        src = create_string_buffer(b"")
        self.obj.utl.strCpy(dest, src)
        self.assertEqual(dest.value, "")

    def testStrCpyReallyCopies(self):
        dest = create_string_buffer(120)
        src = create_string_buffer(b"Hello, world!!!")
        self.obj.utl.strCpy(dest, src)
        self.assertEqual(dest.value, "Hello, world!!!")

    def testStrRevEmptyStringDoesNothing(self):
        src = create_string_buffer(b"")
        self.obj.utl.strRev(src)
        self.assertEqual(src.value, "")

    def testStrRevReallyWorks(self):
        src = create_string_buffer(b"Hello, world!!!")
        self.obj.utl.strRev(src)
        self.assertEqual(src.value, "Hello, world!!!"[::-1])

    def testStrRevMinimalReversal(self):
        src = create_string_buffer(b"AB")
        self.obj.utl.strRev(src)
        self.assertEqual(src.value, "BA")

    def testItoa1(self):
        result = self.obj.utl.itoa(0, 2)
        self.assertEqual(result, "0")

    def testItoa2(self):
        result = self.obj.utl.itoa(0xDEADBEEF, 16)
        self.assertEqual(result, "DEADBEEF")

    def testItoa3(self):
        result = self.obj.utl.itoa(4711, 10)
        self.assertEqual(result, "4711")

    def testItoa4(self):
        result = self.obj.utl.itoa(0xAA55, 2)
        self.assertEqual(result, "1010101001010101")

    def testItoa5(self):
        result = self.obj.utl.itoa(0xABBA, 16)
        self.assertEqual(result, "ABBA")

    def testRandom(self):
        self.obj.utl.randomize(4711)
        result = [self.obj.utl.random() for _ in range(32)]
        self.assertEqual(result, [26701, 4643, 12511, 4081, 12962, 32246, 28920, 2322, 12805, 21482,
                                  27822, 4008, 16381, 9415, 30906, 32284, 17572, 27729, 11141, 409,
                                  27925, 9538, 10099, 25706, 23699, 8457, 15859, 8721, 17530, 8005,
                                  14151, 8486]
        )

class TestUtlBitFunctions(BaseTest):

    CLASS = Messaging
    DLL = "messaging"

    """
        ("Utl_BitReset", c_uint16, [c_uint16, c_uint8]),
        ("Utl_BitToggle", c_uint16, [c_uint16, c_uint8]),
        ("Utl_BitGetHighest", c_uint16, [c_uint16]),
        ("Utl_BitGetLowest", c_uint16, [c_uint16]),
        ("Utl_BitSetLowest", c_uint16, [c_uint16]),
        ("Utl_BitResetLowest", c_uint16, [c_uint16]),

        self.obj.utl.
    """
    def testBitGetFalse(self):
        self.assertFalse(self.obj.utl.bitGet(0x0000, 3))

    def testBitGetTrue(self):
        self.assertTrue(self.obj.utl.bitGet(0x0008, 3))

    def testBitGetAllSet(self):
        self.assertTrue(self.obj.utl.bitGet(0xffff, 5))

    def testBitSetLowest(self):
        self.assertEqual(self.obj.utl.bitSet(0x0000, 0), 0x00001)

    def testBitSetHighest(self):
        self.assertEqual(self.obj.utl.bitSet(0x0000, 15), 0x8000)

    def testBitSetOutOfRange(self):
        self.assertEqual(self.obj.utl.bitSet(0x0000, 16), 0x0000)

def main():
    unittest.main()

if __name__ == '__main__':
    main()

