from fastapi import FastAPI,Query,HTTPException
from models import MenuIteam,MenuResponse
from data import menu_items

app=FastAPI(
    title="menu page",
    description="Read only menu API for kiosk display and mobile app"
)
@app.get("/")
def root():
    return {"Message":"Wellcome to my menu API"}

#/menu->path
#/menu?cateory=drink->path with query and query always starts with ?
@app.get("/menu",response_model=MenuResponse) #using response_model as MenuResponse is called dependancy injection 
def get_menu(categoary: str | None = Query(None, description="Filters according to drink categoary")):
    '''categoary	The name of the input. It becomes the name in the URL.
    : str | None	The type. It can be text (str) or nothing (None).
    if code is -def get_menu(categoary: str | None = None):
    this means -categoary → can be a string or None
           ↓
        default = None
    = Query(none)-This parameter is an optional query parameter. If the user doesn't provide it, its value is None
    description=...	Help text shown in the auto docs (/docs). It does not change how the code works.'''
    if categoary:
        filtered = [item for item in menu_items if item["categoary"] == categoary.lower()]
        '''this how list comprehension works-
        [item       for item in menu_items]
        ↑                 ↑
        what to put       where to get it from'''
        if not filtered:
            raise HTTPException(status_code=404,detail=f"No iteam found in categoary={categoary}")
        return MenuResponse(count=len(filtered), iteams=filtered)
    #as filtered is an list of doc filtered by categoary
    return MenuResponse(count=len(menu_items),iteams=menu_items)
@app.get("/menu/{item_id}",response_model=MenuIteam)
def get_item(item_id:int):
    for item in menu_items:
        if item["id"]== item_id:
            return item
    raise HTTPException(status_code=404,detail=f"Menu item with id {item_id} not found")
   