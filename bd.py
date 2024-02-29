import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hNYALikah3&!",
    database="deals_db"
)


def get_all_deal():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM deals")
    deals = cursor.fetchall()
    cursor.close()

    return deals


def create_entry(fio, phone, comment):
    cursor = mydb.cursor()
    sql = "INSERT INTO deals (full_name, phone_number, comment) VALUES (%s, %s, %s)"
    val = (fio, phone, comment)

    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

    return True