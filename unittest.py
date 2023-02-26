import unittest
from io import StringIO
from unittest.mock import patch
from pynput.keyboard import Key
from my_module import on_press, write_file

class TestOnPress(unittest.TestCase):
    
    def test_on_press(self):
        
        expected_output = 'a pressed\n'
        expected_keys = [Key.a]
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
           
            on_press(Key.a)
            
            self.assertEqual(fake_out.getvalue(), expected_output)
            
            self.assertEqual(keys, expected_keys)
