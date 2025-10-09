import os
from .models import TeamMember
from django.shortcuts import render
from .models import Quote, Mission, SideImage
from django import forms
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import FileSystemStorage
from collections import defaultdict
from django.conf import settings
from google.oauth2.service_account import Credentials
import gspread
from google.oauth2 import service_account
from django.shortcuts import render
from googleapiclient.discovery import build
print(os.path.join(settings.BASE_DIR, "credentials.json"))
# Define the scope for Google Sheets API
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def home(request):
    quotes = Quote.objects.all()
    mission = Mission.objects.first()
    left_images = SideImage.objects.filter(position="left")
    right_images = SideImage.objects.filter(position="right")

    return render(request, "main/home.html", {
        "quotes": quotes,
        "mission": mission,
        "left_images": left_images,
        "right_images": right_images,
    })

def contact(request):
    contacts = TeamMember.objects.all()
    return render(request, 'main/contact.html', {'contacts': contacts})

# Form for donor photo upload
class DonorForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    photo = forms.ImageField(required=True)

def donate(request):
    form = DonorForm()
    uploaded = False  

    if request.method == "POST":
        form = DonorForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data["photo"]

            # Save file in MEDIA folder
            fs = FileSystemStorage()
            fs.save(photo.name, photo)  

            uploaded = True  

    return render(request, "main/donate.html", {
        "form": form,
        "uploaded": uploaded,
        # 👇 replace with your real Google Form link
        "form_link": "https://docs.google.com/forms/d/e/1FAIpQLSe_8cStwvpwI4cY6CYVTedISEfkwJIb9zu_d0A2gMDggHM29w/viewform?usp=dialog"
    })

def volunteer(request):
    # Path to credentials.json in project root
    creds_path = os.path.join(settings.BASE_DIR, "credentials.json")

    # Load Google credentials
    creds = service_account.Credentials.from_service_account_file(creds_path)

    # Example: read a Google Sheet
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    SPREADSHEET_ID = "19HRkanx4u1HF4IlAOPhxp8IV60wPZHUgaOBBEIgrCT8"
    RANGE_NAME = "Sheet1!A:F"
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get("values", [])

    return render(request, "main/volunteer.html", {"values": values})

