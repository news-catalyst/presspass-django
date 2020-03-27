# PressPass Login Example - Django

This is an example of how to implement "Login with PressPass" functionality in a Django app.

## Setup this demo

For now this assumes you have PressPass running locally. These instructions will change a bit once it's all up and running.

```
git clone git@github.com:news-catalyst/presspass-django.git
cd presspass-django
pipenv install
pipenv shell
python manage.py migrate
```

Provided you have [the Squarelet API](https://github.com/muckrock/squarelet) running locally at "dev.presspass.com", set the following env var to point to the OIDC endpoint:

```
export PRESSPASS_BACKEND_URL=http://dev.presspass.com/openid
```

Setup a client in PressPass:

- the response type should be "code (Authorization Code Flow)"
- the client type should be "public"
- set the redirect URI, which should point to this sample app, for instance: `http://127.0.0.1:8000/complete/presspass/`

A quick note about redirect URIs: these should be set for all your different environments, so your development, staging and production sites all get a mention (eventually).

Copy the `client id` from your newly setup presspass client and:

```
export PRESSPASS_CLIENT_ID=036592
```

Then start this app:

```
python manage.py runserver
```

You should be able to navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/), click on the "Login with PressPass" link in the nav, and get an authorization screen displaying the name of your PressPass client. Once you click "Authorize" you should return to this sample app and see a greeting that you're logged in.

## TODO

This will need instructions more geared towards someone who possibly doesn't already have the social auth stuff setup in their app. I did keep notes on how I got all of it up and running just in case.
