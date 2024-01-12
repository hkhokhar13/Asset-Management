from django.db import models


# Create your models here.
class Employee(models.Model):
    Employee_name = models.CharField(max_length=100, blank=True)
    Employee_id = models.CharField(max_length=100, blank=False, unique=True)
    Official_mail = models.CharField(max_length=100, blank=True)
    # Personal_mail = models.CharField(max_length=100, blank=True)
    Employee_contact_info = models.CharField(max_length=100, blank=True)
    Reporting_manager = models.CharField(max_length=100, blank=True)
    Data_security = models.CharField(max_length=100, blank=True)
    # Asset_assign_date = models.DateField(blank=True, null=True)
    # Asset_returning_date = models.DateField(blank=True, null=True)
    Accessories_Given = models.CharField(max_length=100, blank=True)
    Notes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.Employee_name}:{self.Employee_id}"
