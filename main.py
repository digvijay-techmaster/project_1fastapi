from fastapi import FastAPI

app=FastAPI(
    title="menu page",
    description="Read only menu API for kiosk display and mobile app"
)
@app.get("/")
def root():
    return {"Message":"Wellcome to my menu API"}
