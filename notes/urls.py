from django.contrib import admin
from django.urls import path, include
from .views import home_view, notes_view, delete_view, note_view

urlpatterns = [
    path("", notes_view, name="home"),
    path("delete_note/<note_id>", delete_view, name="delete_note"),
    path("expand/<note_id>", note_view, name="note_view"),
]
