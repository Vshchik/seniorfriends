import DataBase

TABLE_NAME = 'UserTable.csv'


class User:
    def __init__(self, name: str, age: str, password: str, town: str, interests: list, user_id: int = -1):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.password = password
        self.town = town
        self.interests = interests

    def add_new_user(self):
        users = DataBase.reader_nonquery(TABLE_NAME)
        # get the last ID in datatable and add one
        user_id = int(users[len(users) - 1][0]) + 1
        user_dict = {'id': str(user_id),
                     'name': self.name,
                     'age': self.age,
                     'password': self.password,
                     'town': self.town,
                     'interests': self.interests}

        DataBase.writer(TABLE_NAME, user_dict)



# create table
# DataBase.create_table(TABLE_NAME,['id', 'name', 'age', 'password', 'town', 'interests'], [{'id':'0', 'name':'tester', 'age':'62', 'password':'test','town':'Haifa' ,'interests':['music', 'sport']}])

