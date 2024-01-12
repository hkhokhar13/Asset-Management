from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponse
from .models import Employee
import csv


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "Employee_name",
        "Official_mail",
        "Employee_id",
        "Employee_contact_info",
        "Reporting_manager",
        "Data_security",
        "Accessories_Given",
        "Notes",
    )
    search_fields = [
        "Employee_name",
    ]

    actions = ["download_employees"]

    def download_employees(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="employees.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "Employee_name",
                "Official_mail",
                "Employee_id",
                "Employee_contact_info",
                "Reporting_manager",
                "Data_security",
                "Accessories_Given",
                "Notes",
            ]
        )

        for employee in queryset:
            writer.writerow(
                [
                    employee.Employee_name,
                    employee.Official_mail,
                    employee.Employee_id,
                    employee.Employee_contact_info,
                    employee.Reporting_manager,
                    employee.Data_security,
                    employee.Accessories_Given,
                    employee.Notes,
                ]
            )

        return response

    download_employees.short_description = "Download selected employees as CSV"


admin.site.register(Employee, EmployeeAdmin)
