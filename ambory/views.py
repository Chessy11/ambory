
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm



def home_page(request):
    # print(request.session.get("first_name"))
    context = { 
        "title": "Ambory",
        "content": "Welcome to Ambory page",
    }

    if request.user.is_authenticated:
        context["premium_content"] = "AMBORY"
    return render(request, "home_page.html", context)



def about_page(request):
    context = {
        "title":"about_page",
        "content":"This Is About Ambory"
    }
    
    return render(request, "about/about.html", context)





def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":"Welcome to the contact page",
        "form": contact_form,
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("user Logged In")

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user     = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect("/login")
        else:
            print("Error")
    return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email    = form.cleaned_data.get("enail")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
        print(new_user)

    return render(request, "auth/register.html", context)