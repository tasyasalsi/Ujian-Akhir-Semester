import pymysql


def create_table():
    connection = pymysql.connect(
        host="localhost",
        user="user",
        password="passworddd",
        db="mydatabase"
    )

    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255)
        )
    """)

    connection.commit()

    connection.close()
    print("Berhasil membuat tabel!")

def create_user(name, email):
    connection = pymysql.connect(
        host="localhost",
        user="user",
        password="passworddd",
        db="mydatabase"
    )

    cursor = connection.cursor()

    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    value = (name, email)
    cursor.execute(sql, value)

    connection.commit()

    connection.close()
    print("Berhasil memasukan data!")


def read_users():
    connection = pymysql.connect(
        host="localhost",
        user="user",
        password="passworddd",
        db="mydatabase"
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()

    connection.close()
    print("Data : " + str(rows))


def update_user(id, name, email):
    connection = pymysql.connect(
        host="localhost",
        user="user",
        password="passworddd",
        db="mydatabase"
    )

    cursor = connection.cursor()

    sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
    value = (name, email, id)
    cursor.execute(sql, value)

    connection.commit()

    connection.close()
    print("Berhasil update user dengan id " + str(id))



def delete_user(id):
    connection = pymysql.connect(
        host="localhost",
        user="user",
        password="passworddd",
        db="mydatabase"
    )

    cursor = connection.cursor()

    sql = "DELETE FROM users WHERE id=%s"
    value = (id)
    cursor.execute(sql, value)

    connection.commit()

    connection.close()
    print("Berhasil menghapus user dengan id " + str(id))


create_table()
create_user("caci", "caci@example.com")
read_users()
update_user(1, "caci", "caci@example.com")
delete_user(1)
