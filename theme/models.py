from distutils.text_file import TextFile
from django.db import models
from django.contrib.auth.models import AbstractUser
#Create your models here

JT = (
    ('0','0'),
    ('1','1'),
    ('2','2')
)

cars = (
    ('Mini','Mini'),
    ('Sedan','Sedan'),
    ('SUV','SUV'),
    ('Premiere','Premiere')
)
route = (
    ('Ahemdabad','Ahemdabad'),
    ('Goa','Goa'),
    ('Mumbai','Mumbai'),
    ('Darjeeling','Darjeeling'),
    ('Gangtok','Gangtok'),
    ('Delhi','Delhi'),
    ('Nagpur','Nagpur'),
    ('kolkata','kolkata'),
    ('Manali','Manali'),
    ('Kerala','Kerala'),
)

class1 = (
    ('Economy','Economy'),
    ('First','First'),
    ('Buisness','Buisness')
)
pickup = (
    ('Dubai Airport','Dubai Airport'),
    ('Mumbai Airport','Mumbai Airport'),
    ('Kolkata Airport','Kolata Airport'),
    ('Delhi Airport','Delhi Airport'),
    ('Ahmedabad Airport','Ahmedabad Airport')
)

# class UserModel(AbstractUser):
#     userProfile=models.ImageField(upload_to="userProfile")
class SignUp(models.Model):
    username = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50)
    phone = models.TextField(max_length = 10)
    password = models.TextField(max_length = 50)
    def __str__(self):
        return self.username

class CategoryModel(models.Model):
    title=models.CharField(max_length=200)  
    description= models.TextField()

class AirlineModel(models.Model):
    Airline_id=models.CharField(max_length=8,unique=True,primary_key=True)
    From=models.CharField(max_length=15,null=False,blank=False,choices=route,default="Mumbai")
    To=models.CharField(max_length=15,null=False,blank=False,choices=route,default="Delhi")
    Departing_Date=models.DateField()
    Returning_Date=models.DateField()
    Class=models.CharField(max_length=15,null=False,blank=False,choices=class1,default='Economy')

class StatusModel(models.Model):
    Flightno=models.CharField(max_length=10,null=False,blank=False)
    DepartureDate=models.DateField()
    Origin=models.CharField(max_length=20)
    Destination=models.CharField(max_length=20)

class CargoModel(models.Model):
    Airline_id=models.ForeignKey("AirlineModel",on_delete=models.CASCADE)
    Origin=models.CharField(max_length=20,choices=route,default="Mumbai")
    Destination=models.CharField(max_length=100,choices=route,default="Mumbai")
    Date=models.DateField()
    Goods_Description=models.TextField(null=False,blank=False)
    Weight=models.IntegerField(null=False,blank=False)
    Product=models.CharField(max_length=30)

class BookingModel(models.Model):
    Booking_id=models.CharField(max_length=8,null=False,blank=False,unique=True,primary_key=True)
    Firstname=models.CharField(max_length=25)
    Lastname=models.CharField(max_length=10)
    Mobile_number=models.CharField(max_length=12,null=False,blank=False)

class CarModel(models.Model):
    Carname=models.CharField(max_length=20,choices=cars,default='Mini')
    Pickup=models.CharField(max_length=20,null=False,blank=False,choices=pickup,default='Dubai Airport')
    Dropoff=models.CharField(max_length=20)
    PickupDate=models.DateField()
    PickupTime=models.TimeField()

class CancellationModel(models.Model):
    Cancel_id=models.CharField(max_length=10,unique=True,primary_key=True)
    Booking_id=models.ForeignKey("BookingModel",on_delete=models.CASCADE)
    Cancel_Date=models.DateField()
    Refund_Money=models.CharField(max_length=20)
    
class BranchModel(models.Model):
    Branch_code=models.CharField(max_length=10,unique=True,null=False,primary_key=True)
    Add1=models.TextField(max_length=100)
    Add2=models.TextField(max_length=100)
    City=models.CharField(max_length=20)
    Telephone=models.CharField(max_length=10)

class PassengerModel(models.Model):
    Reg_id=models.CharField(max_length=10,unique=True,primary_key=True)
    passport_no=models.CharField(max_length=20)
    f_name=models.CharField(max_length=10)
    l_name=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)

class TicketModel(models.Model):
    ticket_id=models.CharField(max_length=10,unique=True,primary_key=True)
    Booking_id=models.ForeignKey("BookingModel",on_delete=models.CASCADE)
    Reg_id=models.ForeignKey("PassengerModel",on_delete=models.CASCADE)
    destination_id=models.CharField(max_length=20)
    depart_date=models.DateField()
    return_date=models.DateField()

class RouteModel(models.Model):
    Route_No=models.CharField(max_length=5)
    Description=models.CharField(max_length=25)
    From=models.TextField(max_length=25,choices=route,default="Mumbai")
    To=models.TextField(max_length=25,choices=route,default="Ahmedabad")

class FareModel(models.Model):
    Route_No=models.IntegerField()
    AIR_Bus_No=models.TextField(max_length=10)
    First_Fare=models.IntegerField()
    Business_Fare=models.IntegerField()
    Economy_Fare=models.IntegerField()

class concessionModel(models.Model):
    Booking_id=models.ForeignKey("BookingModel",on_delete=models.CASCADE)
    Flightno=models.ForeignKey("StatusModel",on_delete=models.CASCADE,max_length=10)
    Extra_Baggage_Allowance=models.CharField(max_length=50)
    Fare=models.CharField(max_length=12,null=False,blank=False)
	
class FeedbackModel(models.Model):
    Quality_Score=models.CharField(max_length=200,choices=JT,default='Feedback score')  
    Message= models.TextField(max_length=500)

    
def __str__(self):
    return self.title

class Meta:
    db_table="dashboard_user"