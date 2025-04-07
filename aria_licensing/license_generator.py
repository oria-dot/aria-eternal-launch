
import uuid
import datetime

def generate_license(client_name):
    license_id = str(uuid.uuid4())
    license_data = {
        "client": client_name,
        "license_key": license_id,
        "issued_on": datetime.date.today().isoformat(),
        "type": "Aria Clone Personal Use",
        "features": ["resume_tool", "freelance_bot", "email_outreach", "basic_dashboard"]
    }
    return license_data

def issue_license(client_name):
    license_info = generate_license(client_name)
    print("License Issued:")
    for key, value in license_info.items():
        print(f" - {key}: {value}")
