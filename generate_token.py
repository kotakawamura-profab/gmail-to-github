from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret_621445063362-93960bk34p435ras02l46iaqnp31269a.apps.googleusercontent.com.json",
        SCOPES
    )
    creds = flow.run_local_server(port=0)

    print("==== COPY BELOW ====")
    print(creds.to_json())
    print("==== COPY ABOVE ====")

if __name__ == "__main__":
    main()