#!/usr/bin/python3
# models/base.py

import json
import csv


class Base:
    """
    Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize id, increment class attribute if no id is provided and set as id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a Python object from its JSON string representation.
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the JSON string representation of a list of instances to a file.
        """
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(o.to_dictionary())
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with attributes already set.
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = None
        if dummy:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.
        """
        filename = cls.__name__ + ".json"
        instances = []
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
        except FileNotFoundError:
            pass
        return [cls.create(**instance) for instance in instances]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save the instances to a CSV file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances from a CSV file.
        """
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    instance = {}
                    keys = cls.get_csv_attributes()
                    for i, value in enumerate(row):
                        instance[keys[i]] = int(value)
                    instances.append(cls.create(**instance))
        except FileNotFoundError:
            pass
        return instances

    @staticmethod
    def get_csv_attributes():
        """
        Returns a list of attribute names to use for CSV serialization.
        """
        return []

    def to_dictionary(self):
        """
        Returns a dictionary representation of the instance.
        This method should be overridden in child classes.
        """
        return {}

    def to_csv_row(self):
        """
        Returns a list of attribute values to use for CSV serialization.
        This method should be overridden in child classes.
        """
        return []
