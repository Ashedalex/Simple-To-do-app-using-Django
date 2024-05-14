
from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django import forms
from django.urls import reverse
tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    due_date = forms.DateTimeField(label="Due-Date")

def home(request):
    if request.method == "GET":
        form = NewTaskForm(request.GET)
        if form.is_valid():
            task_text = form.cleaned_data["task"]
            due_date = form.cleaned_data["due_date"]
            tasks.append([task_text, due_date])
            return HttpResponseRedirect(reverse('home'))
    else:
        form = NewTaskForm()
    
    return render(request, 'to_do/home.html', {"form": form, "tasks": tasks})
