import requests
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.shortcuts import render

from url_worker.url_worker import URL_WORKER
from services.unicode_worker import convert_object

from .forms import UserForm
from .forms import UserProfileForm
from .models import UserProfile


def test(request):
    url = URL_WORKER()
    result = requests.get(url.url).json()

    return JsonResponse(result)


def main(request):
    user = UserProfile.objects.all()
    context = {}
    if user:
        context['user'] = user[0]

    return render(request, 'main.html', context)


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
    return render(request, 'home.html')
