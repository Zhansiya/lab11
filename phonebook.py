import psycopg2

# -----------------------------
# 1) CONNECT TO DATABASE
# -----------------------------
def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="12369874"   # ← мұнда өз пароліңді жаз!
    )


# -----------------------------
# 2) CREATE TABLE IF NOT EXISTS
# -----------------------------
def create_table():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(20)
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()
    print("✔ Table is ready!")


# -----------------------------
# 3) INSERT USER
# -----------------------------
def add_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("INSERT INTO phonebook(name, phone) VALUES (%s, %s);", (name, phone))
    
    conn.commit()
    cur.close()
    conn.close()
    print("✔ User added!")


# -----------------------------
# 4) UPDATE USER
# -----------------------------
def update_user():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone: ")
    
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s;", (new_phone, name))
    
    conn.commit()
    cur.close()
    conn.close()
    print("✔ User updated!")


# -----------------------------
# 5) DELETE USER
# -----------------------------
def delete_user():
    name = input("Enter name to delete: ")
    
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("DELETE FROM phonebook WHERE name=%s;", (name,))
    
    conn.commit()
    cur.close()
    conn.close()
    print("✔ User deleted!")


# -----------------------------
# 6) SHOW ALL USERS
# -----------------------------
def show_all():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()
    
    for r in rows:
        print(r)
    
    cur.close()
    conn.close()


# -----------------------------
# 7) MAIN MENU
# -----------------------------
def menu():
    create_table()  # first time run, creates table automatically
    
    while True:
        print("\n------ PHONEBOOK MENU ------")
        print("1. Add user")
        print("2. Update user")
        print("3. Delete user")
        print("4. Show all users")
        print("5. Exit")

        choice = input("Choose option: ")
        
        if choice == "1":
            add_user()
        elif choice == "2":
            update_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            show_all()
        elif choice == "5":
            print("Exit...")
            break
        else:
            print("Invalid option!")


menu()
