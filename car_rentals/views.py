from . models import signup
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Car
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Feedback
import datetime



def signup_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email)
        
        if name and email and password:
            rec = signup(name=name, email=email, password=password)
            rec.save()
        
             
    return render(request, "sign_up.html")



def login(request):
    if request.method == "GET":
        # Handle the sign-in form submission
        print("Its a POST request")
        email = request.GET.get("login_email")
        password = request.GET.get("login_password")
        print(email,"its an email")
        print(password,"its a password")

        if email and password:
            user = signup.objects.filter(email=email, password=password).first()
            
            if user:
                print("valid user",email,password)
                request.session['user_id'] = user.user_id
                print(user)

                return HttpResponseRedirect(reverse("homepage"))
            
            else:
                print("Invalid password",email,password)
        else:
            print("user or password is not found.",email,password) 
      
    return render(request, "sign_up.html")


def homepage(request):
    cars = Car.objects.all()
    return render(request, 'homepage.html', {'cars': cars})


"""
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'homepage.html', {'cars': cars})
"""
def car_details(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car_details.html', {'car': car})

def book_car(request, car_id):
    car = get_object_or_404(Car, pk = car_id)
    userId = get_object_or_404(signup, pk = request.session.get('user_id'))
    print(userId)
    print(car)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the booking and save it to the database
            # You can create a Booking model to store booking information
            # Here, we'll assume you have a Booking model
            booking = form.save(commit=False)
            booking.car = car
            #booking.user = userId
            booking.user = userId
            print(booking.user)
            print(booking)
            booking.save()
            #form.save()
            return redirect('booking_success')  # Redirect to a booking success page
    else:
        form = BookingForm()

    return render(request, 'car_details.html', {'car': car, 'form': form})

def bookingsuccess(request):
    return render(request,"booking_success.html")

"""
def feedback_view(request):
    msg={}
    if request.method == "POST":
        print("Entering post request ")
        user_id = request.session.get('user_id')    # Assuming you have a way to get the user ID
        
        rating = request.POST.get("rating")
        feedback_text = request.POST.get("feedback_text")
        date=datetime.date.today()

        Feedback.objects.create(user_id=user_id, rating=rating, feedback_text=feedback_text, date=date)
        print("Data created successfully ")
        feedback_list = Feedback.objects.all()
        print("feedback_list == ", feedback_list)
        for feedbackObj in feedback_list:
            print("feedbackObj 11== ", feedbackObj)
            user = get_object_or_404(signup, pk = feedbackObj.user_id)
            feedbackObj["user"] = user
            print("feedbackObj 22== ", feedbackObj)
            
        msg={"msg":"Feedback submitted"}
        return render(request, "feedback.html", {"feedback_list": feedback_list, 'msg':msg, 'user':user})

    if request.method == "GET":
        #user = get_object_or_404(signup, pk = request.session.get('user_id'))
        feedback_list = Feedback.objects.all()
        for feedbackObj in feedback_list:
            print("feedbackObj 1 == ", feedbackObj)
            user = get_object_or_404(signup, pk = feedbackObj.user_id)
            feedbackObj["user"] = user
            print("feedbackObj 2 == ", feedbackObj)
        return render(request, "feedback.html", {"feedback_list": feedback_list,'user':user})
"""

def feedback_view(request):
    msg = {}
    user = None
    if request.method == "POST":
        user_id = request.session.get('user_id')    # Assuming you have a way to get the user ID
        
        rating = request.POST.get("rating")
        feedback_text = request.POST.get("feedback_text")
        print(feedback_text)
        date = datetime.date.today()

        Feedback.objects.create(user_id=user_id, rating=rating, feedback_text=feedback_text, date=date)
        
        feedback_list = Feedback.objects.all()
        for feedbackObj in feedback_list:
            feedbackObj.user = get_object_or_404(signup, pk=feedbackObj.user_id)
            
        msg = {"msg": "Feedback submitted"}
        return render(request, "feedback.html", {"feedback_list": feedback_list, 'msg': msg, 'user': user})

    if request.method == "GET":
        feedback_list = Feedback.objects.all()
        for feedbackObj in feedback_list:
            feedbackObj.user = get_object_or_404(signup, pk=feedbackObj.user_id)
        return render(request, "feedback.html", {"feedback_list": feedback_list, 'user': user})

