
import unittest

from pycozmo.frame import Frame


class TestFrame(unittest.TestCase):

    def test_from_bytes_multi(self):
        f = Frame.from_bytes(
            b'COZ\x03RE\x01\x07\x9d\n\xa0\n\x8f\x00\x04\x01\x00\x8f\x04\x1d\x00\x97\x1a\x00\x15\xb0\xaa\x9c'
            b'\xac\xb2@\xa8\xba^\xac\xb2@\x02\xb4\xa2\xa0\xb0\xaa@\xac\xb2`\xb0\xaa\x1b\x04 \x00\x03\x1f\x80'
            b'\x1f\x80\t\x00\x00\x00\x00\x00\x1f\x80\x1f\x80\t\x00\x00\x00\x00\x00\x1f\x80\x1f\x80\t\x00\x00'
            b'\x00\x00\x00\x00\x04\x16\x00\x11\x1f\x80\x1f\x80\t\x00\x00\x00\x00\x00\x1f\x80\x1f\x80\t\x00'
            b'\x00\x00\x00\x00\x00')
        self.assertEqual(f.type.value, 7)
        self.assertEqual(f.first_seq, 2717)
        self.assertEqual(f.seq, 2720)
        self.assertEqual(f.ack, 143)
        self.assertEqual(len(f.pkts), 4)

    def test_encode_decode(self):
        expected = \
            b'COZ\x03RE\x01\x07\x9d\n\xa0\n\x8f\x00\x04\x01\x00\x8f\x04\x1d\x00\x97\x1a\x00\x15\xb0\xaa\x9c' \
            b'\xac\xb2@\xa8\xba^\xac\xb2@\x02\xb4\xa2\xa0\xb0\xaa@\xac\xb2`\xb0\xaa\x1b\x04 \x00\x03\x1f\x80' \
            b'\x1f\x80\t\x00\x00\x00\x00\x00\x1f\x80\x1f\x80\t\x00\x00\x00\x00\x00\x1f\x80\x1f\x80\t\x00\x00' \
            b'\x00\x00\x00\x00\x04\x16\x00\x11\x1f\x80\x1f\x80\t\x00\x00\x00\x00\x00\x1f\x80\x1f\x80\t\x00' \
            b'\x00\x00\x00\x00\x00'
        f = Frame.from_bytes(expected)
        actual = f.to_bytes()
        self.assertEqual(expected, actual)
