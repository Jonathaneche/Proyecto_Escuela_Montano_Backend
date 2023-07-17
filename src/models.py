from flask import jsonify, request
from database.db import connectdb

# Obtain all categories

def get_categories():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM categorias')
    categorias = cur.fetchall()
    data = [{'idcat': dato[0], 'descripcion': dato[1]} for dato in categorias]
    conn.close()
    return jsonify(data)

#Agregar una categoria
def add_categoria():
    conn = connectdb()
    cur = conn.cursor()
    data = request.get_json()

    idcat = data['idcat']
    descripcion = data['descripcion']

    cur.execute('INSERT INTO categorias (idcat, descripcion) VALUES (%s, %s)', (idcat, descripcion))
    conn.commit()
    conn.close()                                                            
    print('Categoria agregada')                                 
    return "Categoria agregada"

#Delete one category by its id
def delete_category_by_id(idcat):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('DELETE FROM categorias WHERE idcat = %s', (idcat,))
    conn.commit()
    conn.close()
    print("The category was deleted !!")
    return ""

#########Funciones para tabla productos##############

#Get one product by id
def get_product_by_id(id):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s', (id,))
    dato_producto = cur.fetchone()
    conn.close()
    
    if dato_producto:
        producto = {
            'nombre': dato_producto[1],
            'precio': dato_producto[2],
            'img': dato_producto[3]
        }
        return jsonify(producto)
    else:
        return 'El producto no fue encontrado'
    
#Agregar un producto
def add_producto():
    conn = connectdb()
    cur = conn.cursor()
    data = request.get_json()

    nombre = data['nombre']
    precio = data['precio']
    img = data['img']
    idcat = data['idcat']

    cur.execute('INSERT INTO productos (nombre, precio, img, idcat) VALUES (%s, %s, %s, %s)', (nombre, precio, img, idcat))
    conn.commit()
    conn.close()                                                            
    print('Producto agregado ')                                 
    return "Producto agregado"

#Update un producto

def update_producto(id):
    conn = connectdb()
    cur = conn.cursor()

    data = request.get_json()

    if "nombre" in data:
        nombre = data["nombre"]
        cur.execute('UPDATE productos SET nombre = %s WHERE id = %s', (nombre, id))

    if "precio" in data:
        precio = data["precio"]
        cur.execute('UPDATE productos SET precio = %s WHERE id = %s', (precio, id))

    if "img" in data:
        img = data["img"]
        cur.execute('UPDATE productos SET img = %s WHERE id = %s', (img, id))

    if "idcat" in data:
        idcat = data["idcat"]
        cur.execute('UPDATE productos SET idcat = %s WHERE id = %s', (idcat, id))
      
    conn.commit()
    conn.close()

    return 'Producto modified'


#Delete one product by its id
def delete_producto_by_id(id):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('DELETE FROM productos WHERE id = %s', (id,))
    conn.commit()
    conn.close()
    print("The prodcut was deleted !!")
    return "The product was deleted !!"



#Get all products grouped by category
def get_products_by_category(idcat):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM productos where idcat = %s', (idcat,))
    productos = cur.fetchall()
    data = [{'nombre': dato[1], 'precio': dato[2], 'img': dato[3]} for dato in productos]
    conn.close()
    return jsonify(data)