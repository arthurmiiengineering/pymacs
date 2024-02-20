'''Test for plugin loading and initialization.'''
# Standard library imports.
import unittest

# Project imports.
import src.loader

# Class definitions.

class TestLoader(unittest.TestCase):
    def setUp(self):
        pass

    def test_loader(self):
        '''Testing .'''
        with self.subTest('uppercase option'):
            self.assertEqual(
                goodbye_world(upper=True),
                'GOODBYE WORLD'
            )

# Function definitons.

def main() -> None:
    '''Run all tests.'''
    unittest.main()

# Main function guard.

if __name__ == '__main__':
    main()