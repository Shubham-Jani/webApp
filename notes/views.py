from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Note
# Create your views here.


def home_view(request):
    return render(request, "home.html", {})

# in notes view there are two main views notes view, note view


def notes_view(request):
    if request.method == 'POST':
        title = request.POST.get('note_title')
        description = request.POST.get('note_description')
        if "shubham" in title.lower() or "shubham" in description.lower():
            messages.warning(request, "Goli beta masti nahi ! 🙂")
            return redirect("home")
        new_note = Note(title=title, description=description)
        new_note.save()
        return redirect("home")
    if request.method == 'GET' and request.GET.get('search_notes') != None:
        search_field = request.GET.get('search_notes')
        notes = Note.objects.filter(
            Q(title__contains=search_field) | Q(description__contains=search_field))
        context = {"all_notes": notes}
        return render(request, "notes.html", context)

    if Note.objects.count() == 0:
        return render(request, "no_notes.html", {})
    all_notes = Note.objects.all()
    context = {"all_notes": all_notes}
    return render(request, "notes.html", context)


def delete_view(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    messages.success(
        request, f"Note Deleted ! ( the note was yours right ? 🧐 )")
    return redirect("home")


def note_view(request):
    note = Note.objects.get(pk=note.id)
    context = {"note": note}
    return render(request, "partials/note_view.html", context)
