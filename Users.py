import DataBase

TABLE_NAME = 'DataBases/UserTable.csv'


class User:
    def __init__(self, name: str, age: str, password: str, town: str, interests: list, user_id: str = '-1'):
        self.user_id = str(user_id)
        self.name = name
        self.age = age
        self.password = password
        self.town = town
        self.interests = interests

    def add_new_user(self) -> bool:
        users = DataBase.reader_nonquery(TABLE_NAME)
        # get the last ID in datatable and add one
        user_id = int(users[len(users) - 1][0]) + 1
        user_dict = {'id': str(user_id),
                     'name': self.name,
                     'age': self.age,
                     'password': self.password,
                     'town': self.town,
                     'interests': self.interests}

        if DataBase.writer(TABLE_NAME, user_dict):
            return True
        else:
            return False

    def login(self) -> bool:
        user_password = DataBase.reader_query(TABLE_NAME, 'name', self.name)[0][3]
        if self.password == user_password:
            return True
        else:
            return False

    def get_user_by_id(self):
        user_list = DataBase.reader_query(TABLE_NAME, 'id', self.user_id)[0]
        user = User(user_list[1], user_list[2], user_list[3], user_list[4], user_list[5], user_id=user_list[0])
        return user

    def __str__(self):
        return f"Name: {self.name}, password: {self.password}, age: {self.age}, town: {self.town}"


# create table
# DataBase.create_table(TABLE_NAME,['id', 'name', 'age', 'password', 'town', 'interests'], [{'id':'0', 'name':'tester', 'age':'62', 'password':'test','town':'Haifa' ,'interests':['music', 'sport']}])

# user = User('ana','0','test', '',[])
# print(user.login())

# user = User('', '', '', '', [], user_id='1')
# print(user.get_user_by_id())
