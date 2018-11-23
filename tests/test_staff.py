from unittest import TestCase

from staff import Staff


class TestStaff(TestCase):

    """
    For simplicity I'm using here a real input file that is included
    """
    def test_parse_hierarchy(self):
        expected = {
            'Adam': 'Bob',
            'Andrea': 'Bob',
            'Aaron': 'Brenda',
            'Aisha': 'Brenda',
            'Brenda': 'Chris',
            'Bob': 'Chris',
        }

        staff = Staff()
        staff.parse_input('test_staff.input')

        self.assertDictEqual(staff.hierarchy, expected)

    def test_get_managers(self):
        expected = ['Adam', 'Bob', 'Chris']
        hierarchy = {
            'Adam': 'Bob',
            'Andrea': 'Bob',
            'Xavier': 'Adam',
            'Aaron': 'Brenda',
            'Aisha': 'Brenda',
            'Brenda': 'Chris',
            'Bob': 'Chris',
        }

        staff = Staff()
        staff.hierarchy = hierarchy
        actual = list(staff.get_all_managers('Xavier'))

        self.assertEqual(actual, expected)

    def test_find_closest_manager(self):
        '''
        ./staff staff.input Adam Andrea
        Bob
        '''

        '''
        ./staff staff.input Adam Aisha
        Chris
        '''

        '''
        ./staff staff.input Brenda Andrea
        Chris
        '''
        hierarchy = {
            'Adam': 'Bob',
            'Andrea': 'Bob',
            'Xavier': 'Adam',
            'Aaron': 'Brenda',
            'Aisha': 'Brenda',
            'Brenda': 'Chris',
            'Bob': 'Chris',
        }

        staff = Staff()
        staff.hierarchy = hierarchy

        self.assertEqual(staff.find_closest_manager('Adam', 'Andrea'), 'Bob')
        self.assertEqual(staff.find_closest_manager('Adam', 'Aisha'), 'Chris')
        self.assertEqual(staff.find_closest_manager('Brenda', 'Andrea'), 'Chris')

    def test_not_found(self):
        hierarchy = {
            'Adam': 'Bob',
            'Andrea': 'Bob',
            'Aaron': 'Brenda',
            'Aisha': 'Brenda',
            'Brenda': 'Chris',
        }

        staff = Staff()
        staff.hierarchy = hierarchy

        self.assertEqual(staff.find_closest_manager('Adam', 'Aaron'), None)

