from django.db import models

class Item(models.Model):
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    civil_status = models.CharField(max_length=20)
    height = models.FloatField()  # Assuming height is in meters
    weight = models.FloatField()  # Assuming weight is in kilograms
    blood_type = models.CharField(max_length=3)
    gsis_id_no = models.CharField(max_length=20)
    pagibig_id_no = models.CharField(max_length=20)
    philhealth_no = models.CharField(max_length=20)
    sss_no = models.CharField(max_length=20)
    tin_no = models.CharField(max_length=20)
    agency_employee_no = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=100)
    residential_address = models.TextField()
    residential_zip_code = models.CharField(max_length=10)
    residential_telephone_no = models.CharField(max_length=20, blank=True)
    permanent_address = models.TextField()
    permanent_zip_code = models.CharField(max_length=10)
    permanent_telephone_no = models.CharField(max_length=20, blank=True)
    email_address = models.EmailField()
    cell_phone_no = models.CharField(max_length=20)
    agency_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.surname}, {self.first_name} {self.middle_name if self.middle_name else ''}"
