import requests
Base_URL = "https://jerp.aroundstore.net/onlineBookingApis/"

def callApi(method, path, payload=None, params={}, token = False):
    headers = {}


    if token:
        headers["Authorrization"] = f"Bearer{token}"

    params["dbName"] = "FisioArmonia"

    output = requests.request(
        method=method,
        params= params,
        url=Base_URL,
        json=payload,
        headers=headers
        )
    if output.ok:
        return output.json()["return"]
    else:
        output.reason_for_status()

def auth(username, password):
    return callApi("POST", "auth", {"username": username, "pasword": password} )

def getLocations(token):
    return callApi("GET", "getLocations", None, token=token)

def getProfessionals(toke, locationId=None):
    return callApi("GET", {"getResources", locationId}, token=token )

def getPerformances(token):
    return callApi("GET","getItems", None, token=token)

def searchAvailabilities(token, performanceId=None,ProfessionalId=None, startDate=None):
    return callApi("GET", "searchAvailabilities", params={"item_id": performanceId, "agenda_id": ProfessionalId, "start_date": startDate}, token=token)

"""
output = auth("*********", "***************")
token = output["token"]

locations = getLocations(token)

for location in locations:
    print(location["descrition"])

    performance = getPerformances(token)[0]
    print(searchAvailabilities(token, performanceId=performance["id"][0]))"
"""
