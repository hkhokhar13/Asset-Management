from django.db import models
from jsonfield import JSONField
import uuid


class Asset(models.Model):
    Asset_name = models.CharField(max_length=100, blank=True)
    Asset_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )

    Description = models.CharField(max_length=100, blank=True)
    sap_id = models.CharField(max_length=100, blank=True)
    Serial_Number = models.CharField(max_length=100, blank=False, unique=True)
    Manufacturer = models.CharField(max_length=100, blank=True)
    Model = models.CharField(max_length=100, blank=True)
    Purchase_Date = models.DateField(blank=True, null=True)
    Purchase_Cost = models.CharField(max_length=100, blank=True)
    Location = models.CharField(max_length=100, blank=True)
    Status = models.CharField(max_length=100, blank=True)
    Anti_virus_status = models.CharField(max_length=100, blank=True)
    Warranty_Information = models.CharField(max_length=100, blank=True)
    License_or_Subscription = models.CharField(max_length=100, blank=True)
    Notes = models.CharField(max_length=100, blank=True)
    Vendors_Name = models.CharField(max_length=100, blank=True)
    Vendors_information = models.CharField(max_length=100, blank=True)
    Vendors_location = models.CharField(max_length=100, blank=True)
    Vendors_contact_no = models.CharField(max_length=100, blank=True)
    Vendors_email_id = models.CharField(max_length=100, blank=True)
    display_asset_condition_before = models.ImageField(
        upload_to="", blank=True, null=True
    )
    display_asset_condition_after = models.ImageField(
        upload_to="", blank=True, null=True
    )
    invoice_details = models.FileField(upload_to="", blank=True, null=True)

    def __str__(self):
        return f"{self.Asset_name}:{self.Serial_Number}"


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    property_name = models.CharField(max_length=100)

    def __str__(self):
        return self.property_name


class AssetProperty(models.Model):
    asset = models.ForeignKey("Asset", on_delete=models.CASCADE)
    property = models.ForeignKey("Property", on_delete=models.CASCADE)
    property_value = models.CharField(max_length=100)


# def __str__(self):
#     return f"{self.asset.Asset_name} + {self.property.property_name}"


class AssetUploads(models.Model):
    csv_file = models.FileField(upload_to="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.csv_file.name} - {self.uploaded_at}"
