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
@app.get("/menu",response_model=MenuResponse)
def get_menu(categoary: str | None = Query(None, description="Filters according to drink categoary")):
    '''categoary	The name of the input. It becomes the name in the URL.
    : str | None	The type. It can be text (str) or nothing (None).
    = Query(...)	Tells FastAPI: "read this from the query string in the URL."
    None (first value in Query)	The default value. If the user does not send it, it is None.
    description=...	Help text shown in the auto docs (/docs). It does not change how the code works.'''
    if categoary:
        filtered = [item for item in menu_items if item["categoary"] == categoary.lower()]
        if not filtered:
            raise HTTPException(status_code=404,detail=f"No iteam found in categoary={categoary}")
        return MenuResponse(count=len(filtered), iteams=filtered)
    #as filtered is an list of doc filtered by categoary
    return MenuResponse(count=len(menu_items),iteams=menu_items)


