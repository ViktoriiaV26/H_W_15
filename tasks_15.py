import json


class WriteJsonFile:

    def __init__(self, *args):
        self.start_json_file = "./my.json"
        self.result_json_file = "./HW_result.json"
        self.start_dict = {}

    def make_dict(self):
        """Return dictionary from json-file"""
        with open(self.start_json_file, 'r') as json_file:
            self.start_dict = json.load(json_file)
            return self.start_dict

    def dict_sort_by_type(self, some_func):
        """Return dictionary with sorted types of values"""
        employee = self.start_dict['employee']
        my_dict_ = {}
        for person in employee:
            first_name = person.get('firstName')
            last_name = person.get('lastName')
            fio = f"{first_name} {last_name}"
            ints = []
            strings = []
            floats = []
            nons = []
            bools = []
            for pers_key, pers_value in person.items():
                if type(pers_value) == int:
                    ints.append(pers_value)
                elif type(pers_value) == str:
                    strings.append(pers_value)
                elif type(pers_value) == float:
                    floats.append(pers_value)
                elif type(pers_value) is None:
                    nons.append(pers_value)
                elif type(pers_value) == bool:
                    bools.append(pers_value)
            my_dict2 = {'int': ints, 'string': strings, 'float': floats, 'None': nons, 'bool': bools}
            my_dict3 = {fio: my_dict2}
            my_dict_.update(my_dict3)
            self.start_dict.update({'employee': my_dict_})
        return self.start_dict

    def save_sorted_dict(self, func):
        """Return new json-file"""
        with open(self.result_json_file, 'w') as file:
            json.dump(self.start_dict, file, indent=3)

    def main(self):
        """Return function which start run code"""
        self.save_sorted_dict(self.dict_sort_by_type(self.make_dict()))


some_file = WriteJsonFile()

if __name__ == "__main__":
    some_file.main()