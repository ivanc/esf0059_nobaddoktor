import requests
from dotenv import load_dotenv
import os

BASE_URL = "https://jerp.aroundstore.net/onlineBookingApis/"

def callApi(method, path, payload=None, params={}, token = False):
    headers = {}
    


    if token:
        headers["Authorization"] = f"Bearer {token}"

    params["dbName"] = "FisioArmonia"

    output = requests.request(
        method=method,
        params= params,
        url=BASE_URL+path,
        json=payload,
        headers=headers
        )
    if output.ok:
        return output.json()["return"]
    else:
        output.raise_for_status()

def auth(username, password):
    return callApi("POST", "auth", {"username": username, "password": password} )

def getLocations(token):
    return callApi("GET", "getLocations", None, token=token)

def getProfessionals(token, locationId=None):
    return callApi("GET", {"getResources", locationId}, token=token )

def getPerformances(token):
    return callApi("GET","getItems", None, token=token)

def searchAvailabilities(token, performanceId=None,professionalId=None, startDate=None):
    return callApi("GET", "searchAvailabilities", token=token,
                   params={
                       "item_id": performanceId, 
                       "agenda_id": professionalId, 
                       "start_date": startDate
                       })

if __name__ == "__main__":
    load_dotenv()

    output = auth(os.getenv('API_WRAPPER_USER'), os.getenv('API_WRAPPER_PASSWORD'))
    print(os.getenv('API_WRAPPER_USER'))
    print(os.getenv('API_WRAPPER_PASSWORD'))
    token = output["token"]

    locations = getLocations(token)

    for location in locations:
        print(location["description"])

    performance = getPerformances(token)[0]
    print(searchAvailabilities(token, performanceId=performance["id"])[0])
#
#output = auth("*********", "***************")
#token = output["token"]

#locations = getLocations(token)

#for location in locations:
#    print(location["descrition"])

#    performance = getPerformances(token)[0]
#    print(searchAvailabilities(token, performanceId=performance["id"][0]))"