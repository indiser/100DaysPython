import os
import google_auth_oauthlib.flow
import google_auth_httplib2
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.http

script_dir=os.path.dirname(os.path.abspath(__file__))
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate_youtube():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    client_secret = os.path.join(script_dir, "client.json")

    flow=google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secret,SCOPES
    )

    credentials=flow.run_local_server(port=8080, prompt='consent')

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", credentials=credentials
    )

    return youtube

def upload_video(youtube):
    request_body={
        "snippet":{
            "categoryId":"22",
            "title": "test",
            "description":"test description",
            "tags":["test","python"]
        },
        "status":{
            "privacyStatus": "private"
        }
    }

    media_file = os.path.join(script_dir, "ready_to_upload/I_Didn't_Cry_1rfdiio.mp4")

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=googleapiclient.http.MediaFileUpload(media_file,chunksize=-1,resumable=True)
    )

    response=None

    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload {int(status.progress()*100)}%")
    print(f"Video Uploaded with Id: {response['id']}")

if __name__=="__main__":
    youtube=authenticate_youtube()
    upload_video(youtube=youtube)