from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes
from .forms import NoteForm, NoteSearchForm
from django.db.models import Q


# Create your views here.
def note_list(request):
    notes=Notes.objects.all()
    search_form=NoteSearchForm(request.GET)

    query = request.GET.get('query')
    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))

    return render(request,'note_list.html',{'notes':notes,'search_form':search_form})

def note_detail(request,pk):
    note= get_object_or_404(Notes,pk=pk)
    return render(request,'note_detail.html',{'note':note})

def note_new(request):
    if request.method=='POST':
        form= NoteForm(request.POST)
        if form.is_valid():
            note=form.save(commit=False)
            note.save()
            return redirect('note_detail',pk=note.pk)
    else:
        form=NoteForm()
    return render(request,'note_edit.html',{'form':form})

def note_edit(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_edit.html', {'form': form})


def note_delete(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.delete()
    return redirect('note_list')

