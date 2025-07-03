import mysql.connector


def inicializar_bd():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yzma@2019"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS academias_db")
    cursor.execute("USE academias_db")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS academias (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            direccion VARCHAR(200),
            telefono VARCHAR(20)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            apellidos VARCHAR(100),
            dni VARCHAR(20),
            telefono VARCHAR(20),
            email VARCHAR(100),
            ref_curso VARCHAR(100),
            nombre_curso VARCHAR(100),
            fecha_fin_curso DATE NOT NULL,
            academia_id INT,
            FOREIGN KEY (academia_id) REFERENCES academias(id)
        )
    """)
    conn.close()

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yzma@2019",
        database="academias_db"
    )

def crear_usuario(username, password):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    conn.close()

def verificar_usuario(username, password):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None
