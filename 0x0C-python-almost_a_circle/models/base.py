#!/usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""
import json
import os


class Base:
    """[summary]

    Returns:
        [type]: [description]
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """[summary]

        Args:
            id ([type], optional): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """[summary]

        Args:
            list_dictionaries ([type]): [description]

        Returns:
            [type]: [description]
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """[summary]

        Args:
            list_objs ([type]): [description]
        """
        list_ob = []
        if list_objs is None:
            list_ob = []
        else:
            for i in list_objs:
                list_ob.append(i.to_dictionary())

        json_object = Base.to_json_string(list_ob)

        with open('{}.json'.format(cls.__name__),
                  mode='w', encoding='utf-8') as f:
            f.write(json_object)

    @staticmethod
    def from_json_string(json_string):
        """[summary]

        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        lists = []
        if json_string is None:
            return lists
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """[summary]

        Returns:
            [type]: [description]
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            instance = cls(1, 1)
        elif cls == Square:
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """[summary]

        Returns:
            [type]: [description]
        """
        instance = []
        if os.path.isfile('{}.json'.format(cls.__name__)):
            with open('{}.json'.format(cls.__name__),
                      mode='r', encoding='utf-8') as f:
                obj = f.read()
            list_output = cls.from_json_string(obj)
            for i_dict in list_output:
                instance.append(cls.create(**i_dict))
            return instance
        else:
            return instance
