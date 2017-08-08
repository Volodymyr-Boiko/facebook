import requests
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.shortcuts import render

from url_worker.url_worker import URL_WORKER

from .forms import UserForm
from .forms import UserProfileForm
from .models import UserProfile


@login_required
def test(request):
    url = URL_WORKER()
    result = requests.get(url.url).json()

    return JsonResponse(result)


def main(request):
    user = UserProfile.objects.all()
    context = {}
    if user:
        context['user'] = user[0]
    response = render(request, 'main.html', context)
    response.set_cookie('fbsr_132816840603239', '132816840603239')

    return response


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context = {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'register.html', context)


@login_required
def home(request):
    # import facebook
    # result = facebook.get_user_from_cookie(
    #     cookies=request.COOKIES,
    #     app_id='132816840603239',
    #     app_secret='91ae669a2520d2270c98f2a874bf1ea0')

    return render(request, 'home.html')
