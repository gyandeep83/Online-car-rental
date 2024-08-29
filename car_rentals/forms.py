# forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking  # Assuming you have a Booking model
        fields = ['start_date', 'end_date']
