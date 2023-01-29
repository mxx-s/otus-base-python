from django.shortcuts import render
from users.models import User


# Create your views here.


def main_user_page(request):
    users=User.objects.all()

    context = {
        'users': users
    }
    return render(request, "users/index.html", context=context)
