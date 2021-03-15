from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.labels",
]


def make_label(name, mlv="show", llv="labelShow"):
    label = {"messageListVisibility": mlv, "labelListVisibility": llv, "name": name}
    return label


def main():
    # Create or Check Authorisation
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    # API Request
    service = build("gmail", "v1", credentials=creds)
    label = make_label("Choco")

    try:
        created_label = (
            service.users().labels().create(userId="me", body=label).execute()
        )
        print("Label Created")

    except Exception as e:
        print(f"Error occured: {e}")


if __name__ == "__main__":
    main()
