from django.shortcuts import render
from .models import Message
from django.contrib.auth.decorators import login_required
from pickle import loads, dumps
import base64
import ast


class Counter(object):
    def __init__(self, count):
        self.count = count

@login_required
def Messageboard(request): 
    # Get pickle shit
    userdata = request.COOKIES.get("num_messages")
    if userdata == None:
        user_messages = Counter(0)
        print(user_messages.count)
    else:
        userdata = ast.literal_eval(userdata)
        user_messages = loads(base64.b64decode(userdata))
        print(user_messages.count)

    if 'q' in request.POST:
        name = "Anonymous"
        q = request.POST['q']
        if 'name' in request.POST and request.POST['name'] != "":
            name = request.POST['name']
        Message.objects.create(name=name,message=q)
        message_list = Message.objects.all()
        user_messages.count = user_messages.count + 1
        context = {'message_list': message_list, 'total_messages': user_messages.count}
        
        # Pickle shit
        response = render(request, 'messageboard.html', context)
        user_messages= base64.b64encode(dumps(user_messages))
        response.set_cookie(key='num_messages', value=user_messages)
        
        return response

    elif 'clearall' in request.GET:
        Message.objects.all().delete()

        # Pickle shit
        user_messages.count = 0
        message_list = Message.objects.all()
        context = {'message_list': message_list, 'total_messages': user_messages.count}
        user_messages = base64.b64encode(dumps(user_messages))
        response = render(request, 'messageboard.html', context)
        response.set_cookie(key='num_messages', value=user_messages)

        return response

    message_list = Message.objects.all()
    context = {'message_list': message_list, 'total_messages': user_messages.count}
    
    response = render(request, 'messageboard.html', context)
    user_messages = base64.b64encode(dumps(user_messages))
    response.set_cookie(key='num_messages', value=user_messages)
    return response


def index(request):
    return render(request, 'index.html')

