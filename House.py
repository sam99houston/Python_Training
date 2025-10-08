# step 1 define class
class House:
    house_type = "residential"
# step 2 define constructor  
    def __init__(self,adress,size):
         self.adress = adress
         self.size = size
# step 3 methods      
    def describe(self):
        return f"Address {self.adress}\nsize: {self.size} sqft"

# step 4 create objects
house1= House("123 Main street", "125")
house2 = House("Honeyberry","250")

# step 5 perform operations
h1_info1 = house1.describe()
h2_info2 = house2.describe()

# step 6 output

print(h1_info1)
print(h2_info2)