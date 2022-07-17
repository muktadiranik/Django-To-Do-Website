from django import forms
from django.forms import ModelForm
from .models import ToDoList


class ToDoListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ["name", "description", "date_end", "status"]
        labels = {
            "name": "",
            "description": "",
            "date_end": "",
            "status": ""
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Description"}),
            "date_end": forms.DateInput(attrs={"class": "form-control", "placeholder": "Date End", "type": "date"}),
            "status": forms.Select(attrs={"class": "form-control"})
        }
