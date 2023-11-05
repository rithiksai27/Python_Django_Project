from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Events, Admin, ServiceProvider,Booking
from .forms import UserRegisterForm, LoginForm, AddServiceProviderForm, DeleteServiceProviderForm, BookingForm, \
    SPLoginForm
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver


def Homepage(request):

    events = []
    return render(request, 'events/Homepage.html', {'events': events})

def events_list(request):
    event = Events.objects.all()
    paginator = Paginator(event, 4)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'events/events_list.html', {'page': page})

def AdminHome(request):
    return render(request, 'events/AdminHome.html')
def ServiceProviderHome(request):
    return render(request, 'events/ServiceProviderHome.html')
def UserHome(request):
    return render(request, 'events/UserHome.html')
def eventsAvailable(request):
    return render(request, 'events/eventsAvailable.html')

def index(request):
    return render(request, 'events/index.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created Successfully')
            return redirect('events/Homepage')
    else:
        form = UserRegisterForm()
    return render(request, 'events/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'events/profile.html')
def createevent(request):
    if request.method == 'POST':

        event_name = request.POST.get('eventName')
        event_date = request.POST.get('eventDate')
        event_time = request.POST.get('eventTime')
        event_description = request.POST.get('eventDescription')


        event = Events( name=event_name, date=event_date, time=event_time, description=event_description)
        event.save()

    return render(request, 'events/createevent.html')

def payment(request):
    payment_successful = False  # Initialize as False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        event_type = request.POST.get('event_type')

        # Create a new Booking object with the submitted data
        booking = Booking(name=name, email=email, event_type=event_type)

        # Perform any additional validation or data processing as needed

        # Simulate a successful payment by setting payment_successful to True
        payment_successful = True

        # Save the booking to the database
        booking.save()

        # Redirect to the payment page after the booking is saved
        return redirect('events/payment')

    return render(request, 'events/payment.html', {'payment_successful': payment_successful})


def adminlogin(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # Verify the user's credentials (assuming Admin is your custom model)
                try:
                    admin = Admin.objects.get(username=username)
                    if admin.password == password:  # Replace with your custom password hashing logic
                        # Password matches
                        # Log in the user or set a session variable
                        # Redirect to the admin profile page
                        return redirect('events/AdminHome')
                    else:
                        return render(request, 'events/adminlogin.html',
                                      {'form': form, 'error_message': 'Invalid login credentials'})
                except Admin.DoesNotExist:
                    return render(request, 'events/adminlogin.html',
                                  {'form': form, 'error_message': 'Invalid login credentials'})
        else:
            form = LoginForm()

        return render(request, 'events/adminlogin.html', {'form': form})

def adminlogout(request):
    return render(request, 'events/adminlogout.html')
def ContactUs(request):
    return render(request, 'events/ContactUs.html')


def AboutUs(request):
    return render(request, 'events/AboutUs.html')


def booking(request, event_type):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a confirmation page or a thank you page
        # If the form is not valid, stay on the same page and display errors
    else:
        form = BookingForm(initial={'event_type': event_type})

    return render(request, 'events/booking.html', {'form': form})

def serviceproviderlogin(request):
    if request.method == 'POST':
        form = SPLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verify the user's credentials (assuming ServiceProvider is your custom model)
            try:
                dmin = ServiceProvider.objects.get(username=username)
                if dmin.password == password:  # Replace with your custom password hashing logic
                    # Password matches
                    # Log in the user or set a session variable
                    # Redirect to the admin profile page
                    return redirect('events/ServiceProviderHome')
                else:
                    return render(request, 'events/serviceproviderlogin.html',
                                  {'form': form, 'error_message': 'Invalid login credentials'})
            except ServiceProvider.DoesNotExist:
                return render(request, 'events/serviceproviderlogin.html',
                              {'form': form, 'error_message': 'Invalid login credentials'})
    else:
        form = SPLoginForm()

    return render(request, 'events/serviceproviderlogin.html', {'form': form})


def serviceproviderlogout(request):
    return render(request, 'events/serviceproviderlogout.html')


def addserviceprovider(request):
    if request.method == 'POST':
        form = AddServiceProviderForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AddServiceProviderForm()

    return render(request, 'events/addserviceprovider.html', {'form': form})


def removeserviceprovider(request):
    if request.method == 'POST':
        form = DeleteServiceProviderForm(request.POST)
        if form.is_valid():
            # Get the selected service provider's username to delete
            username = form.cleaned_data['delete_provider']
            if username:
                try:
                    provider = ServiceProvider.objects.get(username=username)
                    provider.delete()
                except ServiceProvider.DoesNotExist:
                    # Handle the case where the specified username is not found
                    pass

    form = DeleteServiceProviderForm()


    return render(request, 'events/removeserviceprovider.html', {'form': form})
# views.py



def myview(request):

    if request.user.is_authenticated:
        username = request.user.username

        request.session['username'] = username

    return render(request, 'events/template.html')

def anotherview(request):
    if 'username' in request.session:

        username = request.session['username']

    return render(request, 'events/anothertemplate.html')
@receiver(user_logged_out)
def clear_custom_session_data(sender, user, request, **kwargs):
    # Check and delete your additional session data upon user logout
    if 'user_id' in request.session:
        del request.session['user_id']