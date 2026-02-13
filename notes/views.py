from django.shortcuts import render

def index(request):
    return render(request, "notes/index.html")

def add_notes(request):
    return render (request,"notes/add.html")