from msilib.schema import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Majdoor_login, Majdoor_signup_form, Customer_login, Customer_signup_form
from .models import Majdoor_db, Users_db



def index(request):
    return render(request, 'index.html')


def customer_afterlogin(request):
      products =Majdoor_db.objects.all()
      context = {
        'products':products
    }
      return render(request, 'customer_afterlogin.html',context)


def guide(request):
    return render(request, 'guide.html')
def call_support(request, mobile_number):
    contact = Majdoor_db.objects.mobile_number()  # Assuming you want to fetch the first contact
    return render(request, 'customer_afterlogin.html', {'mobile_number': contact.mobile_number})




def about(request):
    return render(request, 'about.html')


def feedback(request):
    return render(request, 'feedback.html')


def majdoor_login(request):
    if request.method == 'POST':
        form = Majdoor_login(request.POST)
        if form.is_valid():
            m_id = form.cleaned_data['m_id']
            password = form.cleaned_data['password']
            try:
                user = Majdoor_db.objects.get(m_id=m_id)
                # Verify the password using the check_password method
                if user.password == password:
                    # Log the user in using Django's built-in authentication system
                    # You may need to import the necessary modules for authentication
                    # Example: from django.contrib.auth import authenticate, login
                    # Then use authenticate() and login() functions to log in the user
                    # Example: authenticated_user = authenticate(request, username=m_id, password=password)
                    #          if authenticated_user is not None:
                    #              login(request, authenticated_user)
                    return redirect('majdoor_afterlogin', m_id=m_id)
                else:
                    # If password is incorrect, return an error
                    return render(request, 'majdoor_login.html', {'form': form, 'error_message': 'Invalid username or password'})
            except Majdoor_db.DoesNotExist:
                # If no user is found with the provided m_id, return an error
                return render(request, 'majdoor_login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = Majdoor_login()
    return render(request, 'majdoor_login.html', {'form': form})

def majdoor_afterlogin(request, m_id):
    return render(request, 'majdoor_afterlogin.html', {'m_id': m_id})


def customer_login(request):
    if request.method == 'POST':
        form = Customer_login(request.POST)
        if form.is_valid():
            c_id = form.cleaned_data['c_id']
            password = form.cleaned_data['password']
            try:
                user = Users_db.objects.get(c_id=c_id)
                # Verify the password using the check_password method
                if user.password == password:
                    # Log the user in using Django's built-in authentication system
                    # You may need to import the necessary modules for authentication
                    # Example: from django.contrib.auth import authenticate, login
                    # Then use authenticate() and login() functions to log in the user
                    # Example: authenticated_user = authenticate(request, username=m_id, password=password)
                    #          if authenticated_user is not None:
                    #              login(request, authenticated_user)
                    return redirect('customer_afterlogin')
                else:
                    # If password is incorrect, return an error
                    return render(request, 'customer_login.html', {'form': form, 'error_message': 'Invalid username or password'})
            except Users_db.DoesNotExist:
                # If no user is found with the provided m_id, return an error
                return render(request, 'customer_login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = Customer_login()
    return render(request, 'customer_login.html', {'form': form})


def customer_sign_up(request):
    if request.method == 'POST':
        form = Customer_signup_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer_login')
    else:
        form = Customer_signup_form()
    return render(request, 'customer_sign_up.html', {'form': form})


def forget(request):
    return render(request, 'forget.html')



def majdoor_signup(request):
    if request.method == 'POST':
        form = Majdoor_signup_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thank')
    else:
        form = Majdoor_signup_form()
    return render(request, 'majdoor-signup.html', {'form': form})


def thank(request):
    return render(request, 'thank.html')




def contact(request):
    return render(request, 'contact.html')
