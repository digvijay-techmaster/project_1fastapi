# project_1fastapi
FastAPI Menu API

A small FastAPI project built to learn the basics of backend API
development with FastAPI, Pydantic, query parameters, path parameters,
response models, error handling, and separation of data from application
code.

What I Learned

1. Creating a FastAPI application

I learned how to create a FastAPI application:

from fastapi import FastAPI

app = FastAPI()

app is the FastAPI application object used to create API routes.

2. Creating API routes

I learned how @app.get() connects a URL and HTTP GET method to a
Python function.

Examples:

@app.get("/")
@app.get("/menu")
@app.get("/menu/{item_id}")

/ is the root endpoint.

/menu returns the menu.

/menu/{item_id} gets one menu item by its ID.

3. GET requests

I learned that GET endpoints are used to retrieve data.

GET /menu
GET /menu/4

The first gets the menu, while the second gets the item with ID 4.

4. Path parameters

I learned how {item_id} becomes a path parameter.

@app.get("/menu/{item_id}")
def get_item(item_id: int):

For /menu/4, FastAPI passes 4 to item_id.

5. Query parameters

I learned that query parameters are written after ?.

Example:

/menu?categoary=hot drink

I learned how Query() defines an optional query parameter and adds a
description to the automatic API documentation.

categoary: str | None = Query(
    None,
    description="Filters according to drink categoary"
)

I also learned that str | None means the value can be a string or
None.

6. Filtering with list comprehension

I learned how to filter menu items:

filtered = [
    item for item in menu_items
    if item["categoary"] == categoary.lower()
]

I learned that item for item in menu_items goes through each item,
while the if condition decides which items are included.

I also learned that .lower() converts a string to lowercase.

7. Pydantic and BaseModel

I learned how Pydantic models define the expected structure and data
types of API data.

class MenuIteam(BaseModel):
    id: int
    name: str
    categoary: str
    price: float | None = None
    description: str
    available: bool

Pydantic checks whether the data follows these rules.

8. Optional fields

I learned that:

price: float | None = None

means price can contain a float or None, and its default value is
None.

9. Response models

I learned how response_model tells FastAPI what structure an endpoint
should return.

@app.get("/menu", response_model=MenuResponse)

For an endpoint that returns one item, the response model should match
what the function returns:

@app.get("/menu/{item_id}", response_model=MenuIteam)

10. Nested Pydantic models

I learned how one Pydantic model can be used inside another:

class MenuResponse(BaseModel):
    status: str = "success"
    count: int
    iteams: list[MenuIteam]

iteams is a list of MenuIteam objects, and Pydantic checks the items
in that list.

11. HTTPException and 404 errors

I learned how to raise an HTTP error when something cannot be found:

raise HTTPException(
    status_code=404,
    detail="Menu item not found"
)

I used this when no category matched or when a menu item ID did not
exist.

12. Separating data from application code

I learned the basic idea of separation of concerns.

data.py contains the menu data.

models.py contains the Pydantic models.

main.py contains the FastAPI application and API logic.

This makes the project easier to organize and maintain.

13. Automatic API documentation

I learned that FastAPI automatically creates API documentation.

Swagger UI can be opened at:

http://127.0.0.1:8000/docs

It can be used to view and test the API endpoints.

14. Running the FastAPI server

I learned how to run the project using Uvicorn:

uvicorn main:app --reload

uvicorn starts the server.

main refers to main.py.

app refers to the FastAPI object named app.

--reload reloads the server when the code changes.

15. Debugging FastAPI and Pydantic errors

I learned how to read validation errors from the terminal.

For example, if the response data does not contain a required field such
as price, Pydantic produces a validation error.

I also learned that the response_model must match the data returned by
the endpoint.

For example, returning one menu item while using
response_model=MenuResponse caused a response validation error because
MenuResponse expected fields such as count and iteams.

Project Structure

project_1fastapi/
│
├── main.py
├── models.py
├── data.py
├── requirements.txt
├── .gitignore
└── README.md

main.py

Contains the FastAPI application, routes, query parameter handling,
filtering, and error handling.

models.py

Contains the Pydantic models used to define and validate the API
response structure.

data.py

Contains the menu data separately from the API logic.

requirements.txt

Contains the Python packages required by the project, including FastAPI,
Pydantic, and Uvicorn.

Endpoints

Root

GET /

Returns a welcome message.

Get all menu items

GET /menu

Returns all menu items.

Filter menu by category

GET /menu?categoary=hot drink

Returns menu items belonging to the requested category.

Get one menu item

GET /menu/{item_id}

Example:

GET /menu/4

Returns the menu item with ID 4.

Main Concepts Learned

FastAPI application

GET endpoints

Route decorators

Path parameters

Query parameters

Query()

Type hints

str | None

Pydantic BaseModel

Response models

Nested Pydantic models

List comprehensions

Dictionary access

.lower()

HTTPException

HTTP 404 errors

Automatic Swagger documentation

Uvicorn

--reload

Separating data, models, and application logic

Reading and debugging Pydantic validation errors