from flask import Flask, request
import Routes

api = Flask(__name__)

api_routes = [
    {
        "rule": "/country",
        "methods": ["GET"],
        "view_func": Routes.GetCountryList,
        "metadata": {
            "description": "Get Country List",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                403: "Forbidden",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/apikey",
        "methods": ["GET"],
        "view_func": Routes.ListAPIKeys,
        "metadata": {
            "description": "List API Keys",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                403: "Forbidden",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/region",
        "methods": ["GET"],
        "view_func": Routes.ListRegions,
        "metadata": {
            "description": "List Regions",
            "responses": {
                200: Routes.RESPONSEDATA,
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/videolibrary",
        "methods": ["GET"],
        "view_func": Routes.ListVideoLibraries,
        "metadata": {
            "description": "List Video Libraries",
            "responses": {
                200: Routes.RESPONSEDATA,
                201: Routes.RESPONSEDATA,
                202: Routes.RESPONSEDATA,
                203: Routes.RESPONSEDATA,
                204: Routes.RESPONSEDATA,

                401: "The request authorization failed",
                403: "Forbidden",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/videolibrary",
        "methods": ["POST"],
        "view_func": Routes.AddVideoLibrary,
        "metadata": {
            "description": "Add Video Library",
            "responses": {
                200: Routes.RESPONSEDATA,
                201: Routes.RESPONSEDATA,
                202: Routes.RESPONSEDATA,
                203: Routes.RESPONSEDATA,
                204: Routes.RESPONSEDATA,

                401: "The request authorization failed",
                403: "Forbidden",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/videolibrary/<libraryId>",
        "methods": ["GET"],
        "view_func": Routes.GetVideoLibrary,
        "metadata": {
            "description": "Get Video Library",
            "responses": {
                200: Routes.RESPONSEDATA,
                201: Routes.RESPONSEDATA,
                202: Routes.RESPONSEDATA,
                203: Routes.RESPONSEDATA,
                204: Routes.RESPONSEDATA,

                401: "The request authorization failed",
                404: "A Video Library with the requested ID does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/videolibrary/<libraryId>",
        "methods": ["POST"],
        "view_func": Routes.UpdateVideoLibrary,
        "metadata": {
            "description": "Update Video Library",
            "responses": {
                200: Routes.RESPONSEDATA,
                201: Routes.RESPONSEDATA,
                202: Routes.RESPONSEDATA,
                203: Routes.RESPONSEDATA,
                204: Routes.RESPONSEDATA,

                401: "The request authorization failed",
                404: "A Video Library with the requested ID does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/videolibrary/<libraryId>",
        "methods": ["DELETE"],
        "view_func": Routes.DeleteVideoLibrary,
        "metadata": {
            "description": "Delete Video Library",
            "responses": {
                200: Routes.RESPONSEDATA,
                201: Routes.RESPONSEDATA,
                202: Routes.RESPONSEDATA,
                203: Routes.RESPONSEDATA,
                204: Routes.RESPONSEDATA,

                401: "The request authorization failed",
                404: "A Video Library with the requested ID does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/videolibrary/languages",
        "methods": ["GET"],
        "view_func": Routes.GetLanguages,
        "metadata": {
            "description": "Get Languages",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/videolibrary/<libraryId>/resetApiKey",
        "methods": ["POST"],
        "view_func": Routes.ResetVideoLibraryApiKey,
        "metadata": {
            "description": "Reset Video Library API Key",
            "responses": {
                200: Routes.RESPONSEDATA,
                201: Routes.RESPONSEDATA,
                202: Routes.RESPONSEDATA,
                203: Routes.RESPONSEDATA,
                204: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The Video Library with the requested ID does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/purge",
        "methods": ["GET", "POST"], # Functionally the GET and POST can work identically.
        "view_func": Routes.Purge,
        "metadata": {
            "description": "Purge URL Cache",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/storagezone",
        "methods": ["GET"],
        "view_func": Routes.ListStorageZones,
        "metadata": {
            "description": "List Storage Zones",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/storagezone",
        "methods": ["POST"],
        "view_func": Routes.AddStorageZone,
        "metadata": {
            "description": "Add Storage Zone",
            "responses": {
                200: Routes.RESPONSEDATA,
                400: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/storagezone/checkavailability",
        "methods": ["POST"],
        "view_func": Routes.CheckStorageZoneAvailability,
        "metadata": {
            "description": "Check Storage Zone Availability",
            "responses": {
                200: Routes.RESPONSEDATA,
                400: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/storagezone/<storageZoneId>",
        "methods": ["GET"],
        "view_func": Routes.GetStorageZone,
        "metadata": {
            "description": "Get Storage Zone",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested storage zone does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/storagezone/<storageZoneId>",
        "methods": ["POST"],
        "view_func": Routes.UpdateStorageZone,
        "metadata": {
            "description": "Update Storage Zone",
            "responses": {
                200: Routes.RESPONSEDATA,
                400: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested storage zone does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/storagezone/<storageZoneId>",
        "methods": ["DELETE"],
        "view_func": Routes.DeleteStorageZone,
        "metadata": {
            "description": "Delete Storage Zone",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested storage zone does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/storagezone/<storageZoneId>/statistics",
        "methods": ["GET"],
        "view_func": Routes.GetStorageZoneStatistics,
        "metadata": {
            "description": "Get Storage Zone Statistics",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested storage zone does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/collections/<collectionId>",
        "methods": ["GET"],
        "view_func": Routes.GetCollection,
        "metadata": {
            "description": "Get Collection",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested storage zone does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/collections/<collectionId>",
        "methods": ["POST"],
        "view_func": Routes.UpdateCollection,
        "metadata": {
            "description": "Update Collection",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested storage zone does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/collections/<collectionId>",
        "methods": ["DELETE"],
        "view_func": Routes.DeleteCollection,
        "metadata": {
            "description": "Delete Collection",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested storage zone does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/collections",
        "methods": ["GET"],
        "view_func": Routes.ListCollections,
        "metadata": {
            "description": "List Collections",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested storage zone does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/collections",
        "methods": ["POST"],
        "view_func": Routes.CreateCollection,
        "metadata": {
            "description": "Create Collection",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested storage zone does not exist",
                500: "Internal Server Error"
            }
        }
    }
]

@api.before_request
def apply_request_metadata_context():
    path_routes = [route for route in api_routes if route['rule'] == str(request.url_rule)]
    route = [route for route in path_routes if request.method in route['methods']]
    
    if len(route) != 1: 
        raise Exception("Multiple routes found in api_routes for given rule and method")
    route = route[0]

    request.metadata = route['metadata']

for route in api_routes:
    rule = route.copy() # This is *not* a reference to the item in api_routes.
    rule.pop("metadata") # Do not include the metadata as a kwarg.
    api.add_url_rule(**rule)

if __name__ == "__main__":
    api.run('127.0.0.1', 5001, debug = True)















