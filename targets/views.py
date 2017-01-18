import json
from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.core import serializers

from models import Counter

def home(request):
    return render(request, "targets/home.html", dict())

def get_counter(request):
    counter,c = Counter.objects.get_or_create(name="main")
    c_dict = dict(counter=counter)
    if request.method == "POST":
        counter.value += 1
        counter.save()
    return render(request, "targets/counter.html", c_dict)

def get_counter_ajax(request):
    counter,c = Counter.objects.get_or_create(name="main")
    # make it serializer in the response by serializing and deserializing
    c_j = json.loads(serializers.serialize('json', [counter]))[0]['fields']
    c_dict = dict(counter=c_j)
    return HttpResponse(json.dumps(c_dict), content_type="application/json")

def incr_counter_ajax(request):
    counter,c = Counter.objects.get_or_create(name="main")
    counter.value += 1
    counter.save()
    c_j = json.loads(serializers.serialize('json', [counter]))[0]['fields']
    c_dict = dict(counter=c_j)
    return HttpResponse(json.dumps(c_dict), content_type="application/json")
