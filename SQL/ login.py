import sqlite3

# Function to create a new user
def create_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()


# Function to check if the username and password are correct
def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None


# Example usage
create_user("user1", "password1")
create_user("user2", "password2")


username = input("Enter your username: ")
password = input("Enter your password: ")
