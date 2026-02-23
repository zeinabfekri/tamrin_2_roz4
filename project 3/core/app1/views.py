from django.shortcuts import render

def index(request):
    love = {
        'Real Madrid':'https://www.realmadrid.com/en-US' ,
        'Barcelona': 'https://www.fcbarcelona.com/en/',
    }
    return render(request , 'app1/index.html' , {'links':love})