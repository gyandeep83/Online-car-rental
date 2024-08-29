from django.db import models

class signup(models.Model):
    user_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    class Meta:
        db_table="signup"
        
class Car(models.Model):
    car_id=models.IntegerField(primary_key=True)
    car_name = models.CharField(max_length=100)
    seating_capacity = models.IntegerField()
    max_horsepower = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    rent=models.IntegerField()
    Mileage=models.IntegerField()
    Top_speed=models.IntegerField()
    imagepath=models.CharField(max_length=200)
    
    class Meta:
        db_table="Car"
    

    def __str__(self):
        return self.car_name
    


class Booking(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)  # Link each booking to a car
    user = models.ForeignKey('signup', on_delete=models.CASCADE)  # Link each booking to a user_id
    start_date = models.DateField()
    end_date = models.DateField()
    
    class Meta:
        db_table = "Booking"


    # You can add more fields like total_price, status, etc. based on your requirements

    def __str__(self):
        return f"Booking for {self.car.car_name} by {self.user.name}"
        #return f"Booking for {self.car.car_name}"





class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(signup, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback_text = models.TextField()
    date=models.DateField()
    
    class Meta:
        db_table = "Feedback"


    def __str__(self):
        return f"Feedback from User ID {self.user.user_id}"
    
    

