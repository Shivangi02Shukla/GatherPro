from django.db import models

# Create your models here.

Year =[
    ("Sabrang 2018", "Sabrang 2018"),
    ("Sabrang 2019", "Sabrang 2019"),
    ("Sabrang 2022", "Sabrang 2022"),
]

Club =[
    ("Drama Club", "Drama Club"),
    ("Dance Club", "Dance Club"),
    ("Business & Finance Club", "Business & Finance Club"),
    ("Robotics Club", "Robotics Club"),
    ("Music Club", "Music Club"),
    ("Quiz Club", "Quiz Club"),
]

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    club_name = models.CharField(max_length=30, choices=Club, default= "Drama Club")
    fee = models.CharField(max_length=100)
    prize = models.CharField(max_length=100, default="")
    coordinator_name_1 = models.CharField(max_length=100)
    coordinator_no_1 = models.CharField(max_length=10, default="")
    coordinator_name_2 = models.CharField(max_length=100,default="")
    coordinator_no_2 = models.CharField(max_length=10, default="")
    year = models.CharField(max_length=30, choices=Year, default=1)
    image = models.ImageField(upload_to='pics')
    

    def __str__(self):
        return self.name

Team =[
    ("Dignitaries", "Dignitaries"),
    ("Organizing Committee", "Organizing Committee"),
    ("Core Committee", "Core Committee"),
]

class Ourteam(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=1000, default="")
    post = models.CharField(max_length=30, choices=Team, default=1)
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

Type =[
    ("Gold Sponsor", "Gold Sponsor"),
    ("Event Sponsors", "Event Sponsors"),
    ("Stall Sponsors", "Stall Sponsors"),
    ("Printing Partner", "Printing Partner"),
]
class Sponsor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sponsorstype = models.CharField(max_length=30, choices=Type, default=1)
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Winner(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
