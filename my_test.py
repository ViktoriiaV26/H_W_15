import unittest
import os.path
from tasks_15 import WriteJsonFile


class TestWriteJsonFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.write_json_file = WriteJsonFile()

    def test_deserialize(self):
        self.assertEqual(type(self.write_json_file.make_dict()), type({1: 1, }))

    def test_serialize(self):
        self.assertEqual(True, os.path.exists("./HW_result.json"))

    def test_dict_sort_by_type(self):
        test_dict = {"employee": [
            {
                "id": 33,
                "firstName": "Tom",
                "lastName": "Cruise",
                "salary": 1.3
            },
        ]
        }
        self.assertEqual(self.write_json_file.dict_sort_by_type(test_dict)["employee"]["Tom Cruise"]["float"], [1.3])

    @classmethod
    def tearDownClass(cls):
        print("Testing done")


if __name__ == "__main__":
    TestWriteJsonFile()
