from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        'He2lo_1',
        'Hello_2',
        'Hello_3'
    ]
    return JsonResponse(friends,safe=False)