# Dynamic Payment QR Generator

A Django-based web application that generates **UPI payment QR codes** dynamically.  
Users can enter their UPI ID, name, amount, and note in the frontend, and the backend generates a QR code that can be scanned in apps like Google Pay, PhonePe, Paytm, or BHIM to initiate payments.

---

## 🚀 Features
- Generate UPI QR codes dynamically from user input.
- Pre-filled payment details (UPI ID, name, amount, note).
- Scan QR with any UPI-enabled app to pay instantly.
- Simple, responsive frontend design with a styled card layout.
- “Pay Now” button that opens UPI apps directly on mobile.

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Django templates)
- **QR Generation:** [qrcode](https://pypi.org/project/qrcode/) Python library
- **Database:** SQLite (default Django setup, can be swapped)

---
## LIVE LINK  
 -**https://dynamic-payment-qr-generator.onrender.com
## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Dynamic_Payment_QR_generator.git
   cd Dynamic_Payment_QR_generator
