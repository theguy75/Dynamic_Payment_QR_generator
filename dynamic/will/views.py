import qrcode
from django.shortcuts import render
from io import BytesIO
import base64

def generate_qr(request):
    qr_image = None
    if request.method == "POST":
        upi_id = request.POST.get("upi_id")
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        note = request.POST.get("note")

        # Build UPI URL dynamically
        upi_uri = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn={note}"

        # Generate QR code
        qr = qrcode.make(upi_uri)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        qr_image = base64.b64encode(buffer.getvalue()).decode()

    return render(
        request,
        "qrcode.html",
        {
            "qr_image": qr_image,
            "upi_id": upi_id,
            "name": name,
            "amount": amount,
            "note": note,
        },
    )
