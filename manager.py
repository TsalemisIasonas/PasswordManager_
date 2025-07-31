import random
import string , sqlite3

class PasswordCreator:

    query1 = "CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, site TEXT, password TEXT)"
    query2 = "INSERT INTO passwords (site, password) VALUES (?, ?)"
    query3 = "SELECT * FROM passwords WHERE site = ?"
    query4 = "DELETE FROM passwords WHERE site = ?"
    query5 = "UPDATE passwords SET password = ? WHERE site = ?"



    def __init__(self, length):
        self.length = length
        self.conn = sqlite3.connect('passwords.db')
        self.cursor = self.conn.cursor()

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(self.length))
        return password

    def store_password(self, site, password):
        self.cursor.execute(self.query1)
        self.cursor.execute(self.query2, (site, password))
        print(f"Password for {site} stored successfully: {password}")

    def retrieve_password(self, site):
        self.cursor.execute(self.query3, (site,))
        result = self.cursor.fetchone()
        if result:
            print(f"Password for {site}: {result[2]}")
        else:
            print(f"No password found for {site}")

    def update_password(self, site, new_password):
        self.cursor.execute(self.query4, (site,))
        if self.cursor.fetchone():
            self.cursor.execute(self.query5, (new_password, site))
            print(f"Password for {site} updated successfully.")
        else:
            print(f"No password found for {site}")

if __name__ == "__main__":
    site = input("Enter the site name: ")
    length = random.randint(12, 16)
    password_creator = PasswordCreator(length)
    password = password_creator.generate_password()
    password_creator.store_password(site, password)
    