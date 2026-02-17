from django.shortcuts import redirect, render
from .models import Note
from .forms import NoteForm
from django.contrib import messages

def index(request):
    notes = Note.objects.all().order_by('-id')
    return render(request, "notes/index.html",{
        'notes': notes


    })
def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.create(form.cleaned_data)
            messages.success(request,'data added successfully!')
            return redirect("notes:index")
    else:
        form = NoteForm()
        form = NoteForm
        return render(request,"notes/add.html",{
            'form':form
    })

