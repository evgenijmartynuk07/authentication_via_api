# authentication_via_api

```shell
git clone https://github.com/evgenijmartynuk07/authentication_via_api.git
cd authentication_via_api

python -m venv venv
source venv/bin/activate

create .env based on .env.sample

RUN python manage.py migrate

RUN python manage.py createsuperuser

```

Next You can RUN the server & create application for register:
```shell
visit http://127.0.0.1:8000/admin/oauth2_provider/application/

create new application

*NOTE don`t FORGET copy 'Client secret' it hashed after save!

```

Next You can convert Your google or facebook token to access_token:
```shell
visit http://127.0.0.1:8000/auth/convert-token/

create POST request:

for Google
{
	"client_id": "your django client id",
	"grant_type": "convert_token",
	"client_secret": "your django client secret",
	"backend": "google-oauth2",
	"token": "your Google access_token"
}

for Facebook
{
	"client_id": "your django client id",
	"grant_type": "convert_token",
	"client_secret": "your django client secret",
	"backend": "facebook",
	"token": "your Facebook access_token"
}

You will get Response:

{
    "access_token": "XXXXXXXXXXXXXXXXXXXXXXX",
    "expires_in": 33443.475376,
    "scope": "read write",
    "refresh_token": "XXXXXXXXXXXXXXXXXXXXXXX",
    "token_type": "Bearer"
}

Now You can use access_token as a valid token for Your project!

```

How to create Google App and get ID & Secret:
https://developers.google.com/identity/protocols/oauth2
Google token: https://developers.google.com/oauthplayground/
in the list choice 'Google OAuth2 API v2'

How to crete Facebook App and get ID & Secret:
https://developers.facebook.com/apps/
Facebook token: https://developers.facebook.com/tools/accesstoken/

