import DataBase
import Users
import Groups

TABLE_NAME = 'DataBases/MessageTable.csv'
KEYS = ['id', 'user_id', 'group_id', 'text']

class Messages():
    def __init__(self, user_id, group_id, text, mess_id='-1'):
        self.mess_id = mess_id
        self.user_id = user_id
        self.group_id = group_id
        self.text = text

    def create_message(self):
        messages = DataBase.reader_nonquery(TABLE_NAME)
        # get the last ID in datatable and add one
        mess_id = int(messages[len(messages) - 1][0]) + 1
        mess_dict = {'id': str(mess_id),
                      'user_id': self.user_id,
                      'group_id': self.group_id,
                      'text': self.text}

        if DataBase.writer(TABLE_NAME, mess_dict):
            return True
        else:
            return False

    def message_to_list(self):
        message_list = []
        message_list.append(self.mess_id)
        message_list.append(self.user_id)
        message_list.append(self.group_id)
        return message_list

# create table
# DataBase.create_table(TABLE_NAME,KEYS, [{'id':'0', 'user_id':'0', 'group_id':'0', 'text':'test'}])
