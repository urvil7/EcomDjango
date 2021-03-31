from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,ContactAddForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.is_active = False
            # user.save()
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            htmly = get_template('Users/Email.html')
            user_name = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(user_name)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, f'Your account has been created!You are now able to log in')
            return redirect('login')
    else:    
        form = UserRegisterForm()
    return render(request, 'Users/register.html',{'form':form})

def activateEmail(request,username):
    if request.method == 'GET':
        userData = User.objects.filter(username=username).first()
        if userData is not None:
            userData.profile.is_email = True
            userData.save()
            return redirect('redirect_to_login')
        else:
            messages.info(request, f'User is not found')
    return render(request, 'Users/Email.html')

def redirect_to_login(request):
    return render(request, 'Users/ActivateEmail.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            is_email_confirm = user.profile.is_email
            if  is_email_confirm is True:
                request.session['user_id'] = user.id
                form = login(request, user)
                # messages.success(request, f' welcome {username}!!')
                return redirect('home')
            else:
                messages.info(request, f'Please Activate Your Account')
        else:
            messages.info(request, f'Login details invalid!')
    form = AuthenticationForm()
    return render(request, 'Users/login.html', {'form':form, 'title':'log in'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
  
    return render(request,'Users/profile.html',context)

def ContactUs(request):
    if request.method == 'GET':
        return render(request,'Users/contactus.html')
    else:
        contact_form = ContactAddForm(request.POST)
        contact_form.save()
        Name = contact_form.cleaned_data.get('Name')
        Email = contact_form.cleaned_data.get('Email')
        Subject = contact_form.cleaned_data.get('Subject')
        Message = contact_form.cleaned_data.get('Message')
        htmly = get_template('Users/queryEmail.html')
        user_name = { 'Name': Name ,'Message': Message}
        subject, from_email, to = Subject, 'your_email@gmail.com', Email
        html_content = htmly.render(user_name)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        messages.success(request,f"We got your Query,after some time our team will contact you!")
        return render(request,'Users/contactus.html')