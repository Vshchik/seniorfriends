import DataBase
import Users

# Groups: id, town, age, interests, [users id]

TABLE_NAME = 'DataBases/GroupTable.csv'


class Group():
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


    def add_member(self):



# group = Group('Haifa', '80', ['music'], users_id=['0'])
# print(group.create_new_group())

# create table
# DataBase.create_table(TABLE_NAME,['id', 'town', 'age', 'interests', 'users_id'], [{'id':'0', 'town':'Haifa', 'age':'60','interests':['music'], 'users_id':['1']}])
