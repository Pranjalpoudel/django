from django.shortcuts import render
from .models import Note

def index(request):
    notes = Note.objects.all().order_by('_id')
    return render(request, "notes/index.html",{
        'notes': notes


    })

def add_notes(request):
    return render (request,"notes/add.html")