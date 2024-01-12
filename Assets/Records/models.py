from django.db import models
from Employee.models import Employee
from category.models import Asset


class Records(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    asset_assign_date = models.DateField(blank=True, null=True)
    asset_returning_date = models.DateField(blank=True, null=True)

    # def __str__(self):
    #     return f"{self.employee.Employee_name} - {self.Asset.Asset_name}"
