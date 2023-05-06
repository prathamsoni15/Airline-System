# Generated by Django 4.1 on 2022-10-09 17:08

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirlineModel',
            fields=[
                ('Airline_id', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('From', models.CharField(choices=[('Ahemdabad', 'Ahemdabad'), ('Goa', 'Goa'), ('Mumbai', 'Mumbai'), ('Darjeeling', 'Darjeeling'), ('Gangtok', 'Gangtok'), ('Delhi', 'Delhi'), ('Nagpur', 'Nagpur'), ('kolkata', 'kolkata'), ('Manali', 'Manali'), ('Kerala', 'Kerala')], default='Mumbai', max_length=15)),
                ('To', models.CharField(choices=[('Ahemdabad', 'Ahemdabad'), ('Goa', 'Goa'), ('Mumbai', 'Mumbai'), ('Darjeeling', 'Darjeeling'), ('Gangtok', 'Gangtok'), ('Delhi', 'Delhi'), ('Nagpur', 'Nagpur'), ('kolkata', 'kolkata'), ('Manali', 'Manali'), ('Kerala', 'Kerala')], default='Delhi', max_length=15)),
                ('Departing_Date', models.DateField()),
                ('Returning_Date', models.DateField()),
                ('Class', models.CharField(choices=[('Economy', 'Economy'), ('First', 'First'), ('Buisness', 'Buisness')], default='Economy', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('Booking_id', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('Firstname', models.CharField(max_length=25)),
                ('Lastname', models.CharField(max_length=10)),
                ('Mobile_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='BranchModel',
            fields=[
                ('Branch_code', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('Add1', models.TextField(max_length=100)),
                ('Add2', models.TextField(max_length=100)),
                ('City', models.CharField(max_length=20)),
                ('Telephone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Carname', models.CharField(choices=[('Mini', 'Mini'), ('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Premiere', 'Premiere')], default='Mini', max_length=20)),
                ('Pickup', models.CharField(max_length=20)),
                ('Dropoff', models.CharField(max_length=20)),
                ('PickupDate', models.DateField()),
                ('PickupTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FareModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Route_No', models.IntegerField()),
                ('AIR_Bus_No', models.TextField(max_length=10)),
                ('First_Fare', models.IntegerField()),
                ('Business_Fare', models.IntegerField()),
                ('Economy_Fare', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quality_Score', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2')], default='Feedback score', max_length=200)),
                ('Message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PassengerModel',
            fields=[
                ('Reg_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('passport_no', models.CharField(max_length=20)),
                ('f_name', models.CharField(max_length=10)),
                ('l_name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RouteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Route_No', models.CharField(max_length=5)),
                ('Description', models.CharField(max_length=25)),
                ('From', models.TextField(choices=[('Ahemdabad', 'Ahemdabad'), ('Goa', 'Goa'), ('Mumbai', 'Mumbai'), ('Darjeeling', 'Darjeeling'), ('Gangtok', 'Gangtok'), ('Delhi', 'Delhi'), ('Nagpur', 'Nagpur'), ('kolkata', 'kolkata'), ('Manali', 'Manali'), ('Kerala', 'Kerala')], default='Mumbai', max_length=25)),
                ('To', models.TextField(choices=[('Ahemdabad', 'Ahemdabad'), ('Goa', 'Goa'), ('Mumbai', 'Mumbai'), ('Darjeeling', 'Darjeeling'), ('Gangtok', 'Gangtok'), ('Delhi', 'Delhi'), ('Nagpur', 'Nagpur'), ('kolkata', 'kolkata'), ('Manali', 'Manali'), ('Kerala', 'Kerala')], default='Ahmedabad', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='StatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flightno', models.CharField(max_length=10)),
                ('DepartureDate', models.DateField()),
                ('Origin', models.CharField(max_length=20)),
                ('Destination', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TicketModel',
            fields=[
                ('ticket_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('destination_id', models.CharField(max_length=20)),
                ('depart_date', models.DateField()),
                ('return_date', models.DateField()),
                ('Booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theme.bookingmodel')),
                ('Reg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theme.passengermodel')),
            ],
        ),
        migrations.CreateModel(
            name='concessionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Extra_Baggage_Allowance', models.CharField(max_length=50)),
                ('Fare', models.CharField(max_length=12)),
                ('Booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theme.bookingmodel')),
                ('Flightno', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to='theme.statusmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CargoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Origin', models.CharField(choices=[('Ahemdabad', 'Ahemdabad'), ('Goa', 'Goa'), ('Mumbai', 'Mumbai'), ('Darjeeling', 'Darjeeling'), ('Gangtok', 'Gangtok'), ('Delhi', 'Delhi'), ('Nagpur', 'Nagpur'), ('kolkata', 'kolkata'), ('Manali', 'Manali'), ('Kerala', 'Kerala')], default='Mumbai', max_length=20)),
                ('Destination', models.CharField(choices=[('Ahemdabad', 'Ahemdabad'), ('Goa', 'Goa'), ('Mumbai', 'Mumbai'), ('Darjeeling', 'Darjeeling'), ('Gangtok', 'Gangtok'), ('Delhi', 'Delhi'), ('Nagpur', 'Nagpur'), ('kolkata', 'kolkata'), ('Manali', 'Manali'), ('Kerala', 'Kerala')], default='Mumbai', max_length=100)),
                ('Date', models.DateField()),
                ('Goods_Description', models.TextField()),
                ('Weight', models.IntegerField()),
                ('Product', models.CharField(max_length=30)),
                ('Airline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theme.airlinemodel')),
            ],
        ),
        migrations.CreateModel(
            name='CancellationModel',
            fields=[
                ('Cancel_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('Cancel_Date', models.DateField()),
                ('Refund_Money', models.CharField(max_length=20)),
                ('Booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theme.bookingmodel')),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userProfile', models.ImageField(upload_to='userProfile')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]