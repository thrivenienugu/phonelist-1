'''import sqlite3
conn = sqlite3.connect("phone.db")'''

import psycopg2
conn = psycopg2.connect(
           host="localhost",
           database="phone",
           user="phone",
           password="Dev201801"
       )

def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone,address):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}','{address}');")
    cur.close()
def delete_phone(C, id):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE id = '{id}';")
    cur.close()
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()
string='''Hello and welcome to the phone list, available commands:
    ADD    - add a phone number
    DELETE - delete a contact
    LIST   - list all phone numbers
    SAVE   - save the data
    QUIT   - quit the program
    HELP   - Help'''
print(string)
      
while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        address = input("  Address: ")
        add_phone(conn, name, phone,address)
    elif cmd == "DELETE":
        id = input("id: ")
        delete_phone(conn, id)
    elif cmd == "SAVE":
        save_phonelist(conn)
        
    elif cmd == "QUIT":
        
        exit()
    elif cmd == "HELP":
        print(string)
    else:
        print('Unknown command:',cmd)
