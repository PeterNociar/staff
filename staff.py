#!/usr/bin/env python
import argparse
from itertools import zip_longest


class Staff:

    def __init__(self):
        self.hierarchy = {}

    def parse_input(self, input_file):
        """
        Parse the input file into hierarchy structure.
        For speed I choose flat structure with reference from child to parent

        :param input_file: path to the input file
        :return: None
        """
        with open(input_file) as input:
            for line in input:
                managee, manager = line.strip().split(' ')
                self.hierarchy[managee] = manager

    def get_all_managers(self, managee):
        """
        Generator of managers for an employee
        :param managee: The employee name for whom we want to get the managers hierarchy
        :return: generator
        """
        while True:
            if managee in self.hierarchy:
                yield self.hierarchy[managee]
                managee = self.hierarchy[managee]
            else:
                return

    def find_closest_manager(self, name_one, name_two):
        """
        Iterates the 2 generators simultaneously and finds the first same manager in hierarchy
        :param name_one: first employee
        :param name_two: second employee
        :return: closest managers name or None
        """
        all_managers = set()
        for manager_one, manager_two in zip_longest(self.get_all_managers(name_one), self.get_all_managers(name_two)):
            if manager_one is not None and  manager_one in all_managers:
                return manager_one
            else:
                all_managers.add(manager_one)

            if manager_two is not None and manager_two in all_managers:
                return manager_two
            else:
                all_managers.add(manager_two)


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input_file', type=str, help='File containing managee-manager pairs')
    parser.add_argument('first_name', type=str, help='First employee')
    parser.add_argument('second_name', type=str, help='Second employee')

    args = parser.parse_args()
    staff = Staff()
    staff.parse_input(input_file=args.input_file)
    closest = staff.find_closest_manager(args.first_name, args.second_name)

    if closest is None:
        print(f"Couldn't find manager for {args.first_name} and {args.second_name}")
    else:
        print(closest)


if __name__ == "__main__":
    main()
