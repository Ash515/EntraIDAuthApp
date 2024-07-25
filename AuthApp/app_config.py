import os

CLIENT_ID = ""
CLIENT_SECRET = ""
AUTHORITY = f"https://login.microsoftonline.com/<tenant id>"
REDIRECT_PATH = "/getAToken"  
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
SCOPE = ["User.ReadBasic.All"]
SESSION_TYPE = "filesystem"
