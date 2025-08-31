import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Patient

def generate_qr(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    detail_url = request.build_absolute_uri(
        reverse('patient_detail', args=[patient.id])
    )
    img = qrcode.make(detail_url)
    buf = BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/png")

def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'patient_detail.html', {'patient': patient})

# Create your views here.
