"""
File containing all of our API route endpoints.
"""
import requests
from flask import request, make_response, jsonify
from os import environ
from dotenv import load_dotenv

load_dotenv(".env")
ACCOUNT_API_KEY = environ.get('BUNNY_ACCOUNT_KEY')
if ACCOUNT_API_KEY is None:
    raise ValueError("No BUNNY_ACCOUNT_KEY environment variable was set!")

method_map = {
    "GET": requests.get,
    "HEAD": requests.head,
    "OPTIONS": requests.options,
    "PUT": requests.put,
    "DELETE": requests.delete,
    "POST": requests.post,
    "PATCH": requests.patch
}

class RESPONSEDATA:
    def __init__(self) -> None:
        return None


def retrieve_library_api_key(libraryId: str):
    '''Retrieves the API key specific to the given Library'''
    bunny_api_response = make_api_request(
        url = f"https://api.bunny.net/videolibrary/{libraryId}?includeAccessKey=true",
        method = "GET"
    )
    bunny_api_response = bunny_api_response.json()

    api_key = bunny_api_response.get("ApiKey")
    if api_key is not None:
        return api_key
    else:
        return None

def require_library_api_key(func):
    '''
    Function decorator to append `_library_api_key` as a kwarg to a function call.
    Retrieves the API key for the given `libraryId` func kwarg.
    '''
    def wrapper(*args, **kwargs):
        kwargs['_library_api_key'] = retrieve_library_api_key(kwargs['libraryId'])
        result = func(
            *args, **kwargs
        )
        return result
    wrapper.__name__ = func.__name__
    return wrapper

def make_api_request(url: str, method: str, data = None, json = None, headers = None):
    request_headers = {
        "AccessKey": ACCOUNT_API_KEY,
        "accept": "application/json"
    }
    if headers is not None:
        for key in headers:
            request_headers[key] = headers[key]
    
    call = method_map[method]
    response = call(
        url, headers=request_headers, data=data, json=json
    )
    return response

def make_api_response(bunny_response: requests.Response, metadata: dict):
    route_response = metadata['responses'].get(
        bunny_response.status_code, "Unknown response code."
    )

    if route_response is RESPONSEDATA:
        api_response = make_response(
            jsonify(bunny_response.json())
        )
    else:
        api_response = make_response(
            jsonify(route_response)
        )
    api_response.status_code = bunny_response.status_code

    return api_response
    

def GetCountryList():
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/country",
        method = str(request.method),
        data = request.data
    )
    return make_api_response(bunny_api_response, request.metadata)

def ListAPIKeys():
    if request.query_string.decode() != "":
        query_string = f"?{request.query_string.decode()}"
    else:
        query_string = ""
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/apikey" + query_string,
        method = str(request.method),
        data = request.data
    )
    return make_api_response(bunny_api_response, request.metadata)

def ListRegions():
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/region",
        method = str(request.method),
        data = request.data
    )
    return make_api_response(bunny_api_response, request.metadata)

def ListVideoLibraries():
    if request.query_string.decode() != "":
        query_string = f"?{request.query_string.decode()}"
    else:
        query_string = ""
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/videolibrary" + query_string,
        method = str(request.method),
        data = request.data
    )
    return make_api_response(bunny_api_response, request.metadata)

def AddVideoLibrary():
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/videolibrary",
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def GetVideoLibrary(libraryId):
    if request.query_string.decode() != "":
        query_string = f"?{request.query_string.decode()}"
    else:
        query_string = ""
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/videolibrary/" + libraryId + query_string,
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def UpdateVideoLibrary(libraryId):
    if request.query_string.decode() != "":
        query_string = f"?{request.query_string.decode()}"
    else:
        query_string = ""
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/videolibrary/" + libraryId + query_string,
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def DeleteVideoLibrary(libraryId):
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/videolibrary/" + libraryId,
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def GetLanguages():
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/videolibrary/languages",
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def ResetVideoLibraryApiKey(libraryId):
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/videolibrary/" + libraryId + "/resetApiKey",
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def Purge():
    if request.query_string.decode() != "":
        query_string = f"?{request.query_string.decode()}"
    else:
        query_string = ""
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/purge" + query_string,
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def ListStorageZones():
    if request.query_string.decode() != "":
        query_string = f"?{request.query_string.decode()}"
    else:
        query_string = ""
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/storagezone" + query_string,
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def AddStorageZone():
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/storagezone",
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def CheckStorageZoneAvailability():
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/storagezone/checkavailability",
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def GetStorageZone(storageZoneId):
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/storagezone/" + storageZoneId,
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def UpdateStorageZone(storageZoneId):
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/storagezone/" + storageZoneId,
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def DeleteStorageZone(storageZoneId):
    bunny_api_response = make_api_request(
        url = "https://api.bunny.net/storagezone/" + storageZoneId,
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

def GetStorageZoneStatistics(storageZoneId):
    if request.query_string.decode() != "":
        query_string = f"?{request.query_string.decode()}"
    else:
        query_string = ""

    bunny_api_response = make_api_request(
        url = f"https://api.bunny.net/storagezone/{storageZoneId}/statistics" + query_string,
        method = str(request.method),
        json = request.json
    )
    return make_api_response(bunny_api_response, request.metadata)

@require_library_api_key
def GetCollection(libraryId, collectionId, _library_api_key):
    if request.query_string.decode() != "":
        query_string = f"?{request.query_string.decode()}"
    else:
        query_string = ""
    
    bunny_api_response = make_api_request(
        url = f"https://video.bunnycdn.com/library/{libraryId}/collections/{collectionId}" + query_string,
        method = str(request.method),
        json = request.json,
        headers = {
            "AccessKey": _library_api_key
        }
    )
    return make_api_response(bunny_api_response, request.metadata)


@require_library_api_key
def UpdateCollection(libraryId, collectionId, _library_api_key):
    bunny_api_response = make_api_request(
        url = f"https://video.bunnycdn.com/library/{libraryId}/collections/{collectionId}",
        method = str(request.method),
        json = request.json,
        headers = {
            "AccessKey": _library_api_key
        }
    )
    return make_api_response(bunny_api_response, request.metadata)

@require_library_api_key
def DeleteCollection(libraryId, collectionId, _library_api_key):
    bunny_api_response = make_api_request(
        url = f"https://video.bunnycdn.com/library/{libraryId}/collections/{collectionId}",
        method = str(request.method),
        json = request.json,
        headers = {
            "AccessKey": _library_api_key
        }
    )
    return make_api_response(bunny_api_response, request.metadata)

@require_library_api_key
def ListCollections(libraryId, _library_api_key):
    if request.query_string.decode() != "":
        query_string = f"?{request.query_string.decode()}"
    else:
        query_string = ""

    bunny_api_response = make_api_request(
        url = f"https://video.bunnycdn.com/library/{libraryId}/collections" + query_string,
        method = str(request.method),
        json = request.json,
        headers = {
            "AccessKey": _library_api_key
        }
    )
    return make_api_response(bunny_api_response, request.metadata)

@require_library_api_key
def CreateCollection(libraryId, _library_api_key):
    bunny_api_response = make_api_request(
        url = f"https://video.bunnycdn.com/library/{libraryId}/collections",
        method = str(request.method),
        json = request.json,
        headers = {
            "AccessKey": _library_api_key
        }
    )
    return make_api_response(bunny_api_response, request.metadata)