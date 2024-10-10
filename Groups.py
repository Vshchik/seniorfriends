import DataBase
#import Users

# Groups: id, town, age, interests, [users id]
TABLE_NAME = 'DataBases/GroupTable.csv'
KEYS = ['id', 'town', 'age', 'interests', 'users_id']


class Group:
    def __init__(self, town: str, age: str, interests: list, group_id: str = '-1', users_id: list = []):
        self.group_id = group_id
        self.town = town
        self.age = age
        self.interests = interests
        self.users_id = users_id

    def create_new_group(self) -> bool:
        groups = DataBase.reader_nonquery(TABLE_NAME)
        # get the last ID in datatable and add one
        group_id = int(groups[len(groups) - 1][0]) + 1
        group_dict = {'id': str(group_id),
                      'town': self.town,
                      'age': self.age,
                      'interests': self.interests,
                      'users_id': self.users_id}

        if DataBase.writer(TABLE_NAME, group_dict):
            return True
        else:
            return False

    def add_member(self, new_member_id: str) -> bool:
        if not self.check_member_in_group(new_member_id):
            groups = DataBase.reader_nonquery(TABLE_NAME)
            new_table = []
            for index, row in enumerate(groups):
                if row[0] == self.group_id:
                    groups[index][4] = eval(row[4])
                    groups[index][4].append(new_member_id)

                new_table.append(convert_list_to_dict(row))
            return DataBase.change(TABLE_NAME, new_table, KEYS)
        else:
            return False

    def check_member_in_group(self, member_id) -> bool:
        groups = DataBase.reader_query(TABLE_NAME, 'id', self.group_id)
        for index, row in enumerate(groups):
            if str(member_id) in row[4]:
                return True
        return False

    def get_all_members(self):
        group = DataBase.reader_query(TABLE_NAME, 'id', self.group_id)
        return eval(group[0][4])

    def get_all_interests(self):
        group = DataBase.reader_query(TABLE_NAME, 'id', self.group_id)
        return eval(group[0][3])

    def get_messages_in_group(self):
        messages = DataBase.reader_query('DataBases/MessageTable.csv', 'group_id', self.group_id)
        return messages

    def get_group_by_id(self):
        group = DataBase.reader_query(TABLE_NAME, 'interests', str(self.interests))
        return group[0][0]



def convert_list_to_dict(self):
    group_dict = {'id': self[0], 'town': self[1], 'age': self[2], 'interests': self[3],
                  'users_id': self[4]}
    return group_dict


def list_to_str(listt):
    new_string = ""
    for thing in listt:
        new_string += str(thing)
    return new_string


# group = Group('Haifa', '80', ['music', ], users_id=['0', ], group_id='0')
# print(group.get_all_members())
# print(group.get_all_interests())
#print(group.add_member('0'))
# print(group.create_new_group())
# print(group.get_messages_in_group())
# create table
# DataBase.create_table(TABLE_NAME,['id', 'town', 'age', 'interests', 'users_id'], [{'id':'0', 'town':'Haifa', 'age':'60','interests':['music',''], 'users_id':['1','']}])

# group = Group('Tel-Aviv', '70', ['sport'], users_id = ['0'])
# print(group.create_new_group())

# print(group.check_member_in_group(3))
