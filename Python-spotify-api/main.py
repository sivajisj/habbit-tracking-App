import base64
import json
import os
import requests

client_id = os.environ.get("CLIENT_ID" )
client_secret = os.environ.get("CLIENT_SECRET" )

print( f"{client_id}   {client_secret}" )


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8" )
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token/"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}

    result = requests.post( url, headers=headers, data=data )
    # print(result)
    json_res = json.loads( result.content )
    # print(json_res)
    token = json_res["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header( token )
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    res = requests.get( query_url, headers=headers )
    json_res = json.loads( res.content)['artists']["items"]
    if len(json_res) == 0:
        print("No artist with this name exists...!")
        return None
    else:
        return json_res[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    res = requests.get(url, headers=headers)
    # print(res)
    json_result = json.loads(res.content)["tracks"]
    return json_result


token = get_token()
result= search_for_artist( token, "weekend")
artist_id = result["id"]
songs = get_songs_by_artist(token, artist_id)

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}")
