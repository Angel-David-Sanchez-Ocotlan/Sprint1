#
# FastAPI is a framework and library for implementing REST web services in Python.
# https://fastapi.tiangolo.com/
#
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles
from typing import List, Union

# I like to launch directly and not use the standard FastAPI startup process.
# So, I include uvicorn
import uvicorn


from resources.dining_hall.dining_halls_resource import DiningHallsResource
from resources.dining_hall.dining_halls_data_service import DiningHallsDataService
from resources.dining_hall.dining_hall_models import DiningHallModel, DiningHallRspModel



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


# ******************************
#
# DFF TODO Show the class how to do this with a service factory instead of hard code.


def get_data_service():

    config = {
        "data_directory": "/Users/angelsanchez/Desktop/COMS 6156 - Cloud Computing/Sprint1/e6156-f23-template/data",
        "data_file": "diningHall.json"
    }

    ds = DiningHallsDataService(config)
    return ds


def get_dining_hall_resource():
    ds = get_data_service()
    config = {
        "data_service": ds
    }
    res = DiningHallsResource(config)
    return res


students_resource = get_dining_hall_resource()


#
# END TODO
# **************************************


@app.get("/")
async def root():
    return RedirectResponse("/static/index.html")


@app.get("/api/dining_hall", response_model=str)
async def get_dining_halls():
    #result = students_resource.get_dining_halls()
    return "List of dining halls"


@app.get("/api/dining_hall/staff", response_model=str)
async def get_dining_hall_staff():
    return "All dining hall staff"


@app.get("/api/dining_hall/{name}/staff", response_model=str)
async def get_dining_hall_staff_by_dining_hall(name:str):
    return "All dining hall staff for {}".format(name)

@app.get("/api/dining_hall/{name}", response_model= str)
async def get_dining_hall_staff_by_dining_hall(name:str):
    return "All dining hall reviews for {}".format(name)

@app.get("/api/dining_hall/{name}/{menu_item}", response_model=str)
async def get_dining_hall_staff_by_dining_hall(name:str, menu_item:str):
    return "All dining hall reviews for menu item {} and dining hall {}".format(menu_item, name)

@app.get("/api/dining_hall/{name}/{menu_item}/{review_id}", response_model=str)
async def get_dining_hall_staff_by_dining_hall(name:str,menu_item:str, review_id:str):
    return "Dining Hall review with id {} for menu item {} and dining hall {} ".format(review_id, menu_item, name)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8011)
