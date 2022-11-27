from django.shortcuts import render
from home.models import YoutubeLink, Defence
# Create your views here.


def home(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/cause/cause_1_1.html', )
    else:
        return render(request, 'home/cause/cause_1_1.html', )


def cause(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/cause/cause_1_1.html', )
    else:
        return render(request, 'home/cause/cause_1_1.html', )


def cause_1(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/cause/cause_1_2.html', )
    else:
        return render(request, 'home/cause/cause_1_2.html', )


def cause_2_0(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/cause/cause_2_0.html', )
    else:
        return render(request, 'home/cause/cause_2_0.html', )


def cause_2_1(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/cause/cause_2_1.html', )
    else:
        return render(request, 'home/cause/cause_2_1.html', )


def cause_2_2(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/cause/cause_2_2.html', )
    else:
        return render(request, 'home/cause/cause_2_2.html', )


def cause_2_3(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/cause/cause_2_3.html', )
    else:
        return render(request, 'home/cause/cause_2_3.html', )


def cause_2_4(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/cause/cause_2_4.html', )
    else:
        return render(request, 'home/cause/cause_2_4.html', )


def cause_2_5(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/cause/cause_2_5.html', )
    else:
        return render(request, 'home/cause/cause_2_5.html', )


def cause_2_6(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/cause/cause_2_6.html', )
    else:
        return render(request, 'home/cause/cause_2_6.html', )


def plaintiff(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/plaintiff.html', )
    else:
        return render(request, 'home/plaintiff.html', )


def defendant(request):
    user_agent = request.META['HTTP_USER_AGENT']

    listed_out_defence = Defence.objects.all()

    if 'Mobile' in user_agent:
        return render(request, 'home/defence.html', context={'listed_out_defence': listed_out_defence})
    else:
        return render(request, 'home/defence.html', context={'listed_out_defence': listed_out_defence})


def court_hearing(request):
    user_agent = request.META['HTTP_USER_AGENT']

    if 'Mobile' in user_agent:
        return render(request, 'home/court_hearing.html', )
    else:
        return render(request, 'home/court_hearing.html', )