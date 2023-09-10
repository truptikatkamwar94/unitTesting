from typing import List

class ShoppingCart:
    def __init__(self,max_size:int)->None:
        self.itemsL:List[str]=[]
        self.max_size=max_size
        

    def add(self,item :str):
        if self.size()==self.max_size:
            raise OverflowError("canNOT ADD MORE than 5 items ERROR")
        self.itemsL.append(item)
        print("updated list",self.itemsL)

    def size(self)->int:
        return len(self.itemsL)
    
    def get_items(self):
        return self.itemsL

    def get_total_price(self,price_map):
        total_price=0
        for i in self.itemsL:
            print("-----",price_map.get(i))
            total_price+=price_map.get(i)
        return total_price