from django.shortcuts import render, redirect
from .models import RegisterData, Image
from .forms import Getform, Imageform
from django.contrib.auth.models import User, auth     # it is use for
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


class UserData(User):

    def register(request):
        if request.method == 'POST':
            form = Getform(request.POST)
            if form.is_valid():
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                re_password = request.POST['re_password']
                messages.success(request, 'The New User :' + " " + request.POST['username'] + " " + "Is Saved Successfully..!!")

                if RegisterData.objects.filter(username = username).exists():
                    ctx = {'error':'username must be different'}
                    return render(request, 'register.html', ctx)

                elif RegisterData.objects.filter(email = email).exists():
                    ctx1 = {'error1': ' Email is exists\nPlease enter another email '}
                    return render(request, 'register.html', ctx1)

                elif password != re_password:  # it is use for password condition
                    ctx2 = {'form': form, 'error2': ' both password must be same '}
                    return render(request, 'register.html', ctx2)

                else:
                    form.save()
                    return render(request, 'success.html')

        return render(request, 'register.html')


def success(request):
    employees = RegisterData.objects.all()
    return render(request, 'success.html', {'employees':employees})

def show(request):
    employees = RegisterData.objects.all()
    return render(request, 'show.html', {'employees':employees})

def edit(request, id):
    employee = RegisterData.objects.get(id=id)
    return render(request, 'edit.html', {'employee':employee})

def update(request, id):
    employee = RegisterData.objects.get(id=id)
    form = Getform(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'employee':employee})

def destroy(request, id):
    employee = RegisterData.objects.get(id=id)
    employee.delete()
    return redirect('/show')

def logindata(request):
    if request.method == 'POST':
        try:
            userdetail = RegisterData.objects.get(email = request.POST['email'], password = request.POST['password'])
            request.session['email']=userdetail.email
            return render(request, 'success.html')
        except RegisterData.DoesNotExist as e:
            messages.success(request, 'Username / Pasword is Invalid..!')
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['email']
    except:
        return render(request, 'success.html')
    return render(request, 'success.html')


# """ -------- Reset Password ------- """
def change(request, id):
    employee = RegisterData.objects.get(id=id)
    return render(request, 'change.html', {'employee': employee})

def reset(request, id):
    employee = RegisterData.objects.get(id=id)
    return render(request, 'reset.html', {'employee': employee})


# """ ---------- User Profile function ---------- """
def profshow(request):
    user = request.session.get('user')
    return render(request, 'profshow.html', {'user': user})

def profile(request):
    employee = RegisterData.objects.all()
    return render(request, 'profile.html', {'epmloyee': employee})

def save(request, id):
    employee = RegisterData.objects.get(id=id)
    form = Getform(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/prof')
    return render(request, 'success.html', {'employee':employee})

# """ ------------- Gallery functions ------------- """

def photos(request, id):
    form = RegisterData.objects.get(id=id)
    if request.method == 'POST':
        form = Imageform(request.POST, instance=request.session['email'])
        if form.is_valid():
            email = request.POST['email']
            if Image.objects.filter(email=email).exists():
                form.save()
            return redirect('/gallery')
    return render(request, 'gallery/home.html', {'form':form})


def photoshow(request):
    form = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'form':form})

def editphoto(request, id):
    employee = Image.objects.get(id=id)
    return render(request, 'edit.html', {'employee':employee})

def upload(request, id):
    employee = Image.objects.get(id=id)
    form = Imageform(request.POST, instance=employee)
    if request.method == 'POST':
        form = Imageform()
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request, 'success.html', {'form':form})