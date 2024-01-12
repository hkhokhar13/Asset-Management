from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from datetime import datetime

from .models import Property, AssetProperty, Asset, AssetUploads
from .forms import AssetPropertyForm
import csv
from io import TextIOWrapper
from django.http import HttpResponse


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("property_id", "property_name")


class AssetPropertyInline(admin.TabularInline):
    model = AssetProperty
    form = AssetPropertyForm
    extra = 1


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        "Asset_name",
        "Description",
        "sap_id",
        "Serial_Number",
        "Manufacturer",
        "Model",
        "Purchase_Date",
        "Purchase_Cost",
        "Location",
        "Status",
        "Warranty_Information",
        "License_or_Subscription",
        "Notes",
        "Vendors_Name",
        "Vendors_information",
        "Vendors_location",
        "Vendors_contact_no",
        "Vendors_email_id",
        "Anti_virus_status",
        "display_asset_condition_before",
        "display_asset_condition_after",
        "invoice_details",
    )
    search_fields = [
        "Asset_name",
        "Manufacturer",
        "Status",
        "Serial_Number",
        "sap_id",
    ]

    list_filter = [
        "Asset_name",
    ]

    inlines = [AssetPropertyInline]

    def display_asset_condition_before(self, obj):
        return (
            format_html(
                '<img src="{}" width="50" height="50" />'.format(
                    obj.Asset_Condition_Before.url
                )
            )
            if obj.Asset_Condition_Before
            else None
        )

    def display_asset_condition_after(self, obj):
        return (
            format_html(
                '<img src="{}" width="50" height="50" />'.format(
                    obj.Asset_Condition_After.url
                )
            )
            if obj.Asset_Condition_After
            else None
        )

    display_asset_condition_before.short_description = "Asset Condition Before"
    display_asset_condition_after.short_description = "Asset Condition After"

    actions = ["download_assets"]

    def download_assets(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="assets.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "Asset_name",
                "Description",
                "sap_id",
                "Serial_Number",
                "Manufacturer",
                "Model",
                "Purchase_Date",
                "Purchase_Cost",
                "Location",
                "Status",
                "Warranty_Information",
                "License_or_Subscription",
                "Notes",
                "Vendors_Name",
                "Vendors_information",
                "Vendors_location",
                "Vendors_contact_no",
                "Vendors_email_id",
                "Anti_virus_status",
            ]
        )

        for asset in queryset:
            writer.writerow(
                [
                    asset.Asset_name,
                    asset.Description,
                    asset.sap_id,
                    asset.Serial_Number,
                    asset.Manufacturer,
                    asset.Model,
                    asset.Purchase_Date,
                    asset.Purchase_Cost,
                    asset.Location,
                    asset.Status,
                    asset.Warranty_Information,
                    asset.License_or_Subscription,
                    asset.Notes,
                    asset.Vendors_Name,
                    asset.Vendors_information,
                    asset.Vendors_location,
                    asset.Vendors_contact_no,
                    asset.Vendors_email_id,
                    asset.Anti_virus_status,
                ]
            )

        return response

    download_assets.short_description = "Download selected assets as CSV"


@admin.register(AssetUploads)
class AssetUploadsAdmin(admin.ModelAdmin):
    # ... other configurations ...

    def save_model(self, request, obj, form, change):
        # Save the AssetUploads model
        super().save_model(request, obj, form, change)

        # Process the uploaded CSV file and update Asset table
        csv_file = obj.csv_file
        if csv_file:
            csv_file.seek(0)
            reader = csv.DictReader(TextIOWrapper(csv_file, encoding="utf-8"))

            for row in reader:
                # Format date fields
                for date_field in ["Purchase_Date"]:
                    date_str = row.get(date_field, "")
                    if date_str:
                        # Convert the date string to the "YYYY-MM-DD" format
                        formatted_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                        row[date_field] = formatted_date
                    else:
                        # Handle empty date strings (set to None or remove this field if needed)
                        row[date_field] = None

                # Check if asset with Serial Number already exists
                serial_number = row.get("Serial_Number")
                existing_asset = Asset.objects.filter(
                    Serial_Number=serial_number
                ).first()

                if existing_asset:
                    # Update existing asset
                    for key, value in row.items():
                        setattr(existing_asset, key, value)
                    existing_asset.save()
                else:
                    # Create a new asset
                    Asset.objects.create(**row)
