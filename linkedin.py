import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session

# Load from .env file
load_dotenv()
client_id = os.getenv('86buz8q7nvm3ki')
client_secret = os.getenv('WPL_AP1.pDlT2DEV2SkjdODh.E+vT0g==')
redirect_uri = os.getenv('https://www.linkedin.com/in/bhanupriya-sharma-670b22231')

# LinkedIn OAuth endpoints
authorization_base_url = 'https://www.linkedin.com/in/bhanupriya-sharma-670b22231'
token_url = 'https://https://www.linkedin.com/in/bhanupriya-sharma-670b22231'

# Define scope (permissions)
scope = ['r_liteprofile', 'w_member_social']

# Start the OAuth session
linkedin = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

# Step 1: Redirect user to LinkedIn for authorization
authorization_url, state = linkedin.authorization_url(authorization_base_url)
print("Go to this URL and authorize the app:")
print(authorization_url)

# Step 2: After redirect, get response URL with code
redirect_response = input("Paste the full redirect URL here: ")

# Step 3: Fetch the access token
token = linkedin.fetch_token(token_url,
                             client_secret=client_secret,
                             authorization_response=redirect_response)

print("✅ Access Token:")
print(token['access_token'])

