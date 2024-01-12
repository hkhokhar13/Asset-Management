from django.http import HttpResponse
import csv

from django.contrib import admin
from .models import Records


class RecordsAdmin(admin.ModelAdmin):
    list_display = (
        "employee_official_mail",
        "Asset",
        "asset_assign_date",
        "asset_returning_date",
    )
    search_fields = [
        "employee__Official_mail__icontains",
        "Asset__Asset_name__icontains",
        "Asset__Asset_id__icontains",
    ]

    list_filter = [
        "Asset__Asset_name",
    ]

    actions = ["download_records"]

    def employee_official_mail(self, obj):
        return obj.employee.Official_mail

    employee_official_mail.admin_order_field = "employee__Official_mail"

    def download_records(self, request, queryset):
        # Create a CSV response
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="records.csv"'

        # Create a CSV writer and write the header
        writer = csv.writer(response)
        writer.writerow(["Employee", "Asset", "Assign Date", "Returning Date"])

        # Write each record to the CSV
        for record in queryset:
            writer.writerow(
                [
                    record.employee.Official_mail,
                    record.Asset.Asset_name,
                    record.asset_assign_date,
                    record.asset_returning_date,
                ]
            )

        return response

    download_records.short_description = "Download selected records as CSV"


admin.site.register(Records, RecordsAdmin)
