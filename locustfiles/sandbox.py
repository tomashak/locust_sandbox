import mysql.connector
from mysql.connector.constants import ClientFlag

conn = mysql.connector.connect(user='root', password='admin', host="127.0.0.1", port=3307, database='prestashop', ssl_disabled = True)
cursor = conn.cursor()
sql = '''select * from ps_cart order by id_cart desc'''
cursor.execute(sql)
result = cursor.fetchall()
print(result[0])
print("ID cart:" + str(result[0][0]))


sql = """
    select ps_product_lang.name,ps_product_lang.description_short,ps_cart_product.*,ps_product.price 
    from ps_cart_product 
    join ps_product ON ps_cart_product.id_product=ps_product.id_product
    join ps_product_lang ON ps_cart_product.id_product=ps_product_lang.id_product
    where ps_cart_product.id_cart=""" + str(result[0][0])
print(sql)
cursor2 = conn.cursor()
cursor2.execute(sql)
result = cursor2.fetchone()
print(result)
print("Name product: " + result[0])


conn.close()

#root@127.0.0.1:3307
#jdbc:mysql://127.0.0.1:3307/?user=root