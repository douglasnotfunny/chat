from dotenv import load_dotenv
import os

import mysql.connector

load_dotenv()


def connection():
    mydb = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_DATABASE")
    )
    return mydb

def create():
    mydb = connection()
    cursor = mydb.cursor()
    cursor.execute("CREATE TABLE Conversa (id INT AUTO_INCREMENT PRIMARY KEY, pergunta VARCHAR(1000), resposta VARCHAR(1000), pergunta_raw VARCHAR(1000), resposta_raw VARCHAR(1000))")
    mydb.close()
    return mydb

def save_conversa(val):
    mydb = connection()
    cursor = mydb.cursor()
    
    sql = "INSERT INTO Conversa (pergunta, resposta, pergunta_raw, resposta_raw) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, val)
    
    mydb.commit()
    mydb.close()
    return mydb

def select():
    mydb = connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM conversa")
    result = cursor.fetchall()
    mydb.close()
    return result