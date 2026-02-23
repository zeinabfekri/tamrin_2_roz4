from django.shortcuts import render



def index1(request):
    zibayee = {
        'Canada hockey':'https://www.hockeycanada.ca/en-ca/team-canada' ,
        'America hockey': 'https://teamusa.usahockey.com/',
    }
    return render(request , 'app1/index.html' , {'links':zibayee})