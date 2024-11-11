from flask import Flask, request, jsonify
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
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>",
        "methods": ["GET"],
        "view_func": Routes.GetVideo,
        "metadata": {
            "description": "Get Video",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>",
        "methods": ["POST"],
        "view_func": Routes.UpdateVideo,
        "metadata": {
            "description": "Update Video",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>",
        "methods": ["DELETE"],
        "view_func": Routes.DeleteVideo,
        "metadata": {
            "description": "Delete Video",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>/heatmap",
        "methods": ["GET"],
        "view_func": Routes.GetVideoHeatmap,
        "metadata": {
            "description": "Get Video Heatmap",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>/play",
        "methods": ["GET"],
        "view_func": Routes.GetVideoPlayData,
        "metadata": {
            "description": "Get Video play data",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/statistics",
        "methods": ["GET"],
        "view_func": Routes.GetVideoPlayData,
        "metadata": {
            "description": "Get Video play data",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video does not exist",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>/reencode",
        "methods": ["POST"],
        "view_func": Routes.ReencodeVideo,
        "metadata": {
            "description": "Reencode Video",
            "responses": {
                200: Routes.RESPONSEDATA,
                400: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video was not found",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>/repackage",
        "methods": ["POST"],
        "view_func": Routes.RepackageVideo,
        "metadata": {
            "description": "Repackage Video",
            "responses": {
                200: Routes.RESPONSEDATA,
                400: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video was not found",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos",
        "methods": ["GET"],
        "view_func": Routes.ListVideos,
        "metadata": {
            "description": "List Videos",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos",
        "methods": ["POST"],
        "view_func": Routes.CreateVideo,
        "metadata": {
            "description": "Create Video",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>/thumbnail",
        "methods": ['POST'],
        "view_func": Routes.SetThumbnail,
        "metadata": {
            "description": "Set Thumbnail",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video was not found",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/fetch",
        "methods": ["POST"],
        "view_func": Routes.FetchVideo,
        "metadata": {
            "description": "Fetch Video",
            "responses": {
                200: Routes.RESPONSEDATA,
                400: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video was not found",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>/captions/<sourceLang>",
        "methods": ["POST"],
        "view_func": Routes.AddCaption,
        "metadata": {
            "description": "Add Caption",
            "responses": {
                200: Routes.RESPONSEDATA,
                400: "Failed adding captions",
                401: "The request authorization failed",
                404: "The requested video was not found",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>/captions/<sourceLang>",
        "methods": ["DELETE"],
        "view_func": Routes.DeleteCaption,
        "metadata": {
            "description": "Delete Caption",
            "responses": {
                200: Routes.RESPONSEDATA,
                400: "Failed deleting captions",
                401: "The request authorization failed",
                404: "The requested video was not found",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>/transcribe",
        "methods": ["POST"],
        "view_func": Routes.TranscribeVideo,
        "metadata": {
            "description": "Transcribe Video",
            "responses": {
                200: Routes.RESPONSEDATA,
                400: "Invalid request for transcription queue",
                401: "The request authorization failed",
                404: "The requested video was not found",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>/resolutions",
        "methods": ["GET"],
        "view_func": Routes.VideoResolutionInfo,
        "metadata": {
            "description": "Video resolutions info",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video was not found",
                500: "Internal Server Error"
            }
        }
    },
    {
        "rule": "/library/<libraryId>/videos/<videoId>/resolutions/cleanup",
        "methods": ["POST"],
        "view_func": Routes.CleanupUnconfiguredResolutions,
        "metadata": {
            "description": "Cleanup unconfigured resolutions",
            "responses": {
                200: Routes.RESPONSEDATA,
                401: "The request authorization failed",
                404: "The requested video was not found",
                500: "Internal Server Error"
            }
        }
    }
]

@api.route('/status', endpoint='application_status')
@api.route('/', endpoint='application_status')
def application_status():
    '''
    Route for application status checks. 
    This is here instead of `Routes.py` as it's not a route linked to a Bunny API function.
    '''
    return jsonify({
        "service_status": 200,
        "bunny_status": Routes.get_bunny_api_status()
    })

@api.before_request
def apply_request_metadata_context():
    path_routes = [route for route in api_routes if route['rule'] == str(request.url_rule)]
    route = [route for route in path_routes if request.method in route['methods']]
    
    if len(route) > 1:
        raise Exception("Multiple routes found in api_routes for given rule and method")
    elif len(route) == 1:
        route = route[0]
        request.metadata = route.get('metadata')

for route in api_routes:
    rule = route.copy() # This is *not* a reference to the item in api_routes.
    rule.pop("metadata") # Do not include the metadata as a kwarg.
    api.add_url_rule(**rule)

if __name__ == "__main__":
    api.run('127.0.0.1', 5001, debug = True)















