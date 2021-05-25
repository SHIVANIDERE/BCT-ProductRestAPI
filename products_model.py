import sqlite3

class PModel:
    def __init__(self):
        self.conn = sqlite3.connect('bct.db',check_same_thread=False)
        self.create_table()
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        self.conn.commit()
        self.conn.close()
    
    def get_all_products(self):
    
        query = 'SELECT ID, Name, Category, Image, price, Quantity FROM product'

        result_set = self.conn.execute(query).fetchall()

        result = [
            {column:row[i] for i,column in enumerate(result_set[0].keys())}
        for row in result_set
        ]
        return result
        
    def create_product(self,params):
        query = "INSERT INTO product(Name,Category,Image,price,Quantity) VALUES('{0}','{1}','{2}','{3}','{4}')".format(
            params.get('Name'),
            params.get('Category'),
            params.get('price'),
            params.get('Image'),
            params.get('Quantity')
        )

        result = self.conn.execute(query)
        return self.get_productbyid(result.lastrowid)


    def get_productbyid(self,_id):
    
        query = 'SELECT ID,Name,Category,Image,price,Quantity FROM product WHERE id={0}'.format(_id)

        result_set = self.conn.execute(query).fetchall()

        result = [{
            column:row[i] for i,column in enumerate(result_set[0].keys())}
            for row in result_set
            ]
        return result
    
    def update_product(self,_id,params):
        query = 'UPDATE product SET Name="{0}", Category = "{1}", Image = "{2}", price = "{3}", Quantity = "{4}" WHERE ID = {5} '.format(
            params.get('Name'),
            params.get('Category'),
            params.get('price'),
            params.get('Image'),
            params.get('Quantity'),
            _id
        )
        print("Product details updated")
        self.conn.execute(query)
        return self.get_productbyid(_id)

    def delete_product(self,_id):
        query = 'DELETE from product WHERE id={0}'.format(_id)
        result = self.conn.execute(query)
        status = 200 if result.rowcount == 1 else 404
        return{"status":status, "affected_rows": result.rowcount} 

    def create_table(self):
        query="""
        CREATE TABLE IF NOT EXISTS "product"(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Category TEXT,
            price REAL NOT NULL,
            Quantity INTEGER NOT NULL
        );
        """
        self.conn.execute(query)
