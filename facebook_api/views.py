from json import dumps

from django.shortcuts import render
from django.http import JsonResponse

from API.settings import FACEBOOK_CLIENT_ID
from API.settings import FACEBOOK_CLIENT_SECRET

from flask_oauth import OAuth


oauth = OAuth()

facebook = oauth.remote_app(
    'facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_CLIENT_ID,
    consumer_secret=FACEBOOK_CLIENT_SECRET,
    request_token_params={'scope': ('email, ')}
)


@facebook.authorized_handler
def test(request):
    context = {
        'FACEBOOK_CLIENT_ID': FACEBOOK_CLIENT_ID,
        'FACEBOOK_CLIENT_SECRET': FACEBOOK_CLIENT_SECRET
    }
    me = facebook.get('/me?fields=id,name,email').data

    # authorization_base_url = 'https://www.facebook.com/dialog/oauth'
    # token_url = 'https://graph.facebook.com/oauth/access_token'
    # redirect_uri = 'https://localhost/'  # Should match Site URL
    #
    # from requests_oauthlib import OAuth2Session
    # from requests_oauthlib.compliance_fixes import facebook_compliance_fix
    # facebook = OAuth2Session(FACEBOOK_CLIENT_ID, redirect_uri=redirect_uri)
    # facebook = facebook_compliance_fix(facebook)
    #
    #  # Redirect user to Facebook for authorization
    # authorization_url, state = facebook.authorization_url(
    #     authorization_base_url)
    # print 'Please go here and authorize,', authorization_url
    #
    #  # Get the authorization verifier code from the callback url
    # redirect_response = raw_input('Paste the full redirect URL here:')
    #
    #  # Fetch the access token
    # facebook.fetch_token(token_url, client_secret=FACEBOOK_CLIENT_SECRET,
    #                      authorization_response='https://www.facebook.com/dialog/oauth')
    #
    #  # Fetch a protected resource, i.e. user profile
    # r = facebook.get('https://graph.facebook.com/me?')
    
    return JsonResponse(context)
