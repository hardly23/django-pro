from django.shortcuts import render
from .forms import UserForm,userProfileInfo
from django.core.mail import send_mail


from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')
def special():
    return HttpResponse("you are Login")


@login_required()
def other(request):
    return render(request,'index.html')

def username_logout(request):
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered= False

    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form = userProfileInfo(data=request.POST)



        if user_form.is_valid() and profile_form.is_valid():

            user= user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user



            if 'profile_form' in request.FILES:
                profile.name_id = request.FILES['name_id']
                profile.mobile = request.FILES['mobile']
                profile.City = request.FILES['City']
                profile.State = request.FILES['State']
                profile.Country = request.FILES['Country']
                profile.Address_line1 = request.FILES['Address_line1']
                profile.Zipcode = request.FILES['Zipcode']
                profile.Country = request.FILES['Country']



            profile.save()



            registered = True
        else:
            print(user_form.errors,profile_form)

    else:
        user_form = UserForm()
        profile_form =userProfileInfo()
    return render(request,'form.html',{'user_form':user_form
                                                         ,'profile_form':profile_form
                                                         ,'registered' :registered})

def user_login(request):
    if request == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if  user.is_active:
                login(request,user)
                return reverse('index')

            else:
                return HttpResponse("not active ")

        else:
            print("Some one tried to log in failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid Login details supplied ! ")

    else:

        return render(request,'login.html',{})



























# def form_name_view(request):
#     form = NewUser()

    # if request.method == 'POST':
    #     form = NewUser(request.POST)
    #
    #
    #
    #     if form.is_valid():
    #         form.save(commit=True)
    #         return index(request)
    #
    #     else:
    #         print("ERROR FROM INVALID")
    #
    # return render(request,'form.html',{'form':form})