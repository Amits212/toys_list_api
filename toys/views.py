from django.shortcuts import render
from .models import Toy

def get_all_toys(request):
    toys = Toy.objects.all()
    return render(request, "index.html", {"toys":toys})