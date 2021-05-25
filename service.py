from products_model import PModel

class ProductService:
    def __init__(self):
        self.model = PModel()
    
    def get_all(self):
        return self.model.get_all_products()

    def get_by_id(self,_id):
        return self.model.get_productbyid(_id)

    def create(self,params):
        return self.model.create_product(params)
    
    def update(self,_id,params):
        return self.model.update_product(_id,params)

    def delete(self,_id):
        return self.model.delete_product(_id)