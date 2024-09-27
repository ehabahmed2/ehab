from django.shortcuts import render, redirect
from django.core.mail import send_mail
from portfolio_mgmnt import settings

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        msg = request.POST['message']
        
        # Construct the full message to include the sender's details
        full_message = f"Message from {name} ({email}):\n\n{msg}"
        
        try: 
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,  # Your email address (the sender)
                [settings.EMAIL_HOST_USER],  # Your email address (the recipient)
            )
            return render(request, 'contact/thank.html', {'name':name})
        except Exception as e:
            
            print(f'Error receiving an email: {e}')
    return render(request, 'home.html', {})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        msg = request.POST['message']
        
        # Construct the full message to include the sender's details
        full_message = f"Message from {name} ({email}):\n\n{msg}"
        
        try: 
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,  # Your email address (the sender)
                [settings.EMAIL_HOST_USER],  # Your email address (the recipient)
            )
            return render(request, 'contact/thank.html', {'name':name})
        except Exception as e:
            
            print(f'Error receiving an email: {e}')
    return render(request, 'contact/contact_form.html', {})

def questions(request):
    return render(request, 'questions.html', {})