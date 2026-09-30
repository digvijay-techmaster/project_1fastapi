from pydantic import BaseModel

class MenuIteam(BaseModel):
    id:int
    name:str
    categoary:str
    price:float
    description:str
    avilable:bool

class MenuResponse(BaseModel):
    status:str="success"
    count:int
    iteams:list[MenuIteam]

# status: str = "success": The = "success" is a default value. If you do not give a status and you give status value when 
# you create a object , it becomes "success" automatically.
# count: int: How many items are in the list.
# iteams: list[MenuIteam]: A list of MenuIteam objects. Pydantic checks that every item in the list follows the MenuIteam rules.
    
