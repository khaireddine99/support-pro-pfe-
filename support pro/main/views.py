from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import *
from .forms import *
import openai
from django.conf import settings
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

openai.api_key = settings.OPEN_AI_KEY

# Create your views here.
line = ['.', 'hello im ai assisstant how may i help you today']
chat = [line]
def index(request):
    # chatbot -----------------------------
    text = ''
    response = '' 

    if request.method == 'POST':
        text = request.POST.get('user')
        result = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(text),
            temperature=1,
            max_tokens = 1000,
        ) 
        response = result.choices[0].text
        line = [text, response]
        chat.append(line)

    context = {'chat':chat}    
    return render(request, 'index.html', context)


def generate_prompt(animal):
    # generate ai response --------------------------------------------------------------
    return """"{}
    """.format(
        animal.capitalize()
    )


def guides(request):
    return render(request, 'guides.html')

def register(request):
    # helps the client create an account -------------------------
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('index')

    context = {'form':form}
    return render(request, 'registration/register.html', context)

@login_required
def new_ticket(request):
    # allow the client to create a ticket then saves it to the db ----
    if request.method != "POST":
        form = ticket_form()
    else:
        form = ticket_form(data=request.POST)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.owner = request.user 
            new_ticket.save()
            return redirect("index")
        
    context = {'form':form}           
    return render(request, 'new.html', context)

@login_required
def my_tickets(request):
    # returns the current users submitted tickets ------
    tickets = Ticket.objects.filter(owner=request.user)
    context = {'tickets': tickets}
    return render(request, 'my_tickets.html', context)


def tickets(request):
    # return all the tickets submitted
    tickets = Ticket.objects.all()
    context = {'tickets':tickets}
    return render(request, 'tickets.html', context)


def ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    comments = Comment.objects.all()

    # write a comment --------------------------------------------
    if request.method != 'POST':
        form = comment_form()
    else:
        form = comment_form(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.owner = request.user
            new_comment.ticket = ticket
            new_comment.save()  
            form = comment_form()         
        
    context = {'ticket':ticket, 'comments':comments, 'form':form}
    return render(request, 'ticket.html', context)

def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    ticket = comment.ticket
    
    if request.method != 'POST':
        form = comment_form(instance=comment)
    else:
        form = comment_form(instance=comment, data=request.POST)   
        if form.is_valid():
            form.save()
            return redirect('ticket', ticket_id=ticket.id) 
        
    context = {'form':form}
    return render(request, 'edit_comment.html', context)    


def edit_ticket(request, ticket_id):
    # helps the client edit a ticket -----------------
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method != 'POST':
        form = ticket_form(instance=ticket)
    else:
        form = ticket_form(instance=ticket, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket', ticket_id=ticket.id)

    context = {'ticket':ticket, 'form':form}
    return render(request, 'edit_ticket.html', context)


















