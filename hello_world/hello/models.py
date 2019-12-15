from django.db import models

class Students(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	StudentID = models.IntegerField()
	major = models.CharField(max_length=50)
	year = models.CharField(max_length=50)
	GPA = models.DecimalField(max_digits = 5, decimal_places=2)

class CourseDetails(models.Model):
	CourseID = models.IntegerField() #3903/107349
	CourseTitle = models.CharField(max_length=100) #Econ 3903
	CourseName = models.CharField(max_length=100) #Faculty Seminar Topics
	SectionCode = models.IntegerField() #1
	Department = models.CharField(max_length=100) #Economics
	Instructor = models.CharField(max_length=100) #Lerner,Josh

class GraduationRate(models.Model):
	Campus = models.CharField(max_length=100) #"Brockport"
	GradYear = models.DateField() #Fall 2017
	FourYrGradRate = models.DecimalField(max_digits = 5, decimal_places=2) #48.19
	FiveYrGradRate = models.DecimalField(max_digits = 5, decimal_places=2) #64.29
	SixYrGradRate = models.DecimalField(max_digits = 5, decimal_places=2) #65.9


# Create your models here.
