import mysql.connector

class SQLHandler:
    def __init__(self, host, port, username, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        

    def __del__(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            

    def insert(self, value1, value2, value3, column1='user_phone_number', column2='user_name', column3='user_id'):
        self.cursor.execute(f'INSERT INTO credentials ({column1}, {column2}, {column3}) VALUES ("{value1}", "{value2}", "{value3}")')
        self.connection.commit()

    def update_changed_name(self, user_id, new_first_last_name, column1='user_id', column2='user_name'):
        self.cursor.execute(f'UPDATE credentials SET {column2} = "{new_first_last_name}" WHERE {column1} = "{user_id}"')
        self.connection.commit()

    def update_changed_phone_number(self, user_id, new_phone_number, column1='user_id', column2='user_phone_number'):
        self.cursor.execute(f'UPDATE credentials SET {column2} = "{new_phone_number}" WHERE {column1} = "{user_id}"')
        self.connection.commit()
    
    def select(self, user_name):
        self.cursor.execute(f'SELECT user_phone_number, user_name FROM credentials WHERE user_name = "{user_name}"')
        result = list(self.cursor.fetchone())
        return result[0], result[1]
        

    



