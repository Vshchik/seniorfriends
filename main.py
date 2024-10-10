import Users
import Groups
import Users

state = {'state': 'Login', 'user': None}


def main():
    ...
    while state['state'] != 'Quit':
        match state['state']:
            case 'Login':
                Login()

            case 'Registration':
                Registration()

            case 'Groups':
                Groups()

            case 'Add_Groups':
                Add_Groups()

            case 'Group':
                Group()

            case 'Members_Of_The_Group':
                Members_Of_The_Group()

            case 'Profile':
                Profile()


def Login():
    ...


def Registration():
    ...


def Groups():
    ...


def Add_Groups():
    ...


def Group():
    ...


def Members_Of_The_Group():
    ...


def Profile():
    ...


if __name__ == '__main__':
    main()
