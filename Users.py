import DataBase
import Groups

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
        user = User(user_list[1], user_list[2], user_list[3], user_list[4], eval(user_list[5]), user_id=user_list[0])
        return user

    def get_user_id(self):
        users = DataBase.reader_nonquery(TABLE_NAME)
        for row in users:
            if row[1] == self.name and row[3] == self.password:
                return row[0]

    def get_users_interest(self):
        user = DataBase.reader_query(TABLE_NAME, 'id', self.user_id)
        return eval(user[0][5])

    def get_users_groups(self):
        groups = DataBase.reader_nonquery('DataBases/GroupTable.csv')
        users_groups = []
        for row in groups:
            if self.user_id in row[4]:
                users_groups.append(row)
        return users_groups

    def find_groups(self):
        group_list = []
        groups = DataBase.reader_query('DataBases/GroupTable.csv', 'town', self.town)
        for row in groups:
            group = Groups.Group(row[1], row[2], row[3], eval(row[4]))
            group.group_id = row[0]
            if not group.check_member_in_group(self.user_id):
                if int(self.age) >= 90:
                    if int(group.age) == 90:
                        group_list.append(group)
                else:
                    if int(group.age) + 10 > int(self.age) >= int(group.age):
                        group_list.append(group)
        return group_list

    def find_perfect_group(self):
        if len(self.interests) >= 3:
            perfect_groups_exist = []
            perfect_groups_notexist = []
            groups = DataBase.reader_query('DataBases/GroupTable.csv', 'town', self.town)
            users = DataBase.reader_query(TABLE_NAME, 'town', self.town)
            filtred_users = []
            for user in users:
                if int(self.age) + 10 >= int(user[2]) >= int(self.age) - 10 and user[1] != self.name:
                    filtred_users.append(user)
            for group in groups:
                interests = (e in self.interests for e in eval(group[3]))
                summ = sum(1 for _ in interests)
                if summ == 3:
                    perfect_groups_exist.append(group)

            # take two any users and check if them have 3+ same interests
            if len(filtred_users) >= 2:
                for index in range(len(filtred_users) - 2):
                    for jindex in range(1, len(filtred_users) - 1):
                        interests1 = []
                        interests2 = []
                        for i in eval(filtred_users[index][5]):
                            if i in self.interests:
                                interests1.append(i)
                        for i in eval(filtred_users[jindex][5]):
                            if i in self.interests:
                                interests2.append(i)

                        summ = []
                        for i in interests1:
                            if i in interests2:
                                summ.append(i)

                        if len(summ) >= 3:
                            temp_list = []
                            for x in summ:
                                temp_list.append(x)
                            group = Groups.Group(self.town, self.age, [temp_list[0], temp_list[1], temp_list[2]])
                            perfect_groups_notexist.append(group)

            return perfect_groups_exist, perfect_groups_notexist




    def __str__(self):
        return f"Name: {self.name}, password: {self.password}, age: {self.age}, town: {self.town}"


def get_all_users(self):
    users = DataBase.reader_nonquery(TABLE_NAME)
    users2 = []
    for user in users:
        users2.append(user)

    return users2


# create table
# DataBase.create_table(TABLE_NAME,['id', 'name', 'age', 'password', 'town', 'interests'], [{'id':'0', 'name':'tester', 'age':'62', 'password':'test','town':'Haifa' ,'interests':['music', 'sport']}])

# user = User('ana','0','test', '',[])
# print(user.login())

# user = User('', '', '', '', [], user_id='1')
# print(user.get_user_by_id())
# print(user.get_users_interest())
# print(user.get_users_groups())

# user = User("", "", "", "", [], 1)
# user = user.get_user_by_id()
#
# groups = user.find_groups()
# for row in groups:
#     print(row.town, row.age, row.interests)
#
# user = User('', '', '', '', [], user_id='1')
# user = user.get_user_by_id()
#
# tab1, tab2 = user.find_perfect_group()
# print(tab1)
# print(tab2[0].interests)

