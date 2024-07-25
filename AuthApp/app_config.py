import os

CLIENT_ID = "b86de486-d396-4195-82b9-18900fd4c329"
CLIENT_SECRET = "Yts8Q~w29yBlp6rZdoG3gs_waVFfusoK3hSEqcc4"
AUTHORITY = f"https://login.microsoftonline.com/178e4ea3-2e59-4270-b014-2d41ac841c15"
REDIRECT_PATH = "/getAToken"  
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
SCOPE = ["User.ReadBasic.All"]
SESSION_TYPE = "filesystem"
