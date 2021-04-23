from django.db import models

# Create your models here.

class Date(models.Model):
    """Model representing availability date."""
    date_of_work = models.DateField(null=True, blank=True)
    
    day = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.day
        

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Availability(models.Model):
    """Model representing an availability."""

    # Foreign Key used because availability can only have one employee, but employees can have multiple availabilitys
    # Employee as a string rather than object because it hasn't been declared yet in the file
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)

    hours = models.TextField(max_length=200, help_text='Enter hours of availability')


    # ManyToManyField used because date can contain many availabilitys. availabilitys can cover many dates.
    # Date class has already been defined so we can specify the object above.
    date = models.ManyToManyField(Date, help_text='Select a date for work')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.date}, {self.hours}'
        
    def get_absolute_url(self):
        """Returns the url to access a detail record for this availability."""
        return reverse('availability-detail', args=[str(self.id)])
        
        


        
  ##############
class Employee(models.Model):
    """Model representing an employee."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    



    def get_absolute_url(self):
        """Returns the url to access a particular employee instance."""
        return reverse('employee-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
