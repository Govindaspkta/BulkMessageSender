Bulk SMS Sender
A web app to send bulk SMS to verified numbers globally, including Nepal (+977), using Twilio’s free trial. Built with React, Flask, and a secure venv. Supports multilingual messages (e.g., Nepali: नमस्ते). Test ~300 SMS with Twilio’s $15 credit!
Features

Send SMS to multiple verified numbers.
E.164 format validation (e.g., +9779812345678).
UTF-8 for multilingual texts (Nepali, Arabic, etc.).
Secure credentials via .env.
Isolated dependencies in Python venv.

Prerequisites

Python 3.8+
Twilio account (twilio.com/try-twilio)
Git

Setup

Clone the repo:
<<<<<<< HEAD
git clone https://github.com/your-username/your-repo.git
cd your-repo
=======
git clone https://github.com/Govindaspkta/BulkMessageSender.git
cd BulkMessageSender
>>>>>>> 533a848 (added readme)


Set up virtual environment:
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux


Install dependencies:
<<<<<<< HEAD
pip install flask flask-cors twilio requests python-dotenv
=======
pip install -r requirements.txt
>>>>>>> 533a848 (added readme)


Configure Twilio:

Sign up at twilio.com/try-twilio.
Get Account SID, Auth Token, and a Phone Number from Twilio Console.
Verify recipient numbers (e.g., +9779812345678) in Twilio Console > Phone Numbers > Manage > Verified Caller IDs.
Create .env in the project root:TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_FROM_NUMBER=+12025550123




Run the backend:
python app.py


Run the frontend:
python -m http.server 8000

Visit http://localhost:8000.

Test:

Enter verified numbers (e.g., +9779812345678,+9779823456789).
Add a message (e.g., नमस्ते! Test).
Click "Send SMS" and check delivery.



Notes

Trial Mode: Only verified numbers work (~$0.045/SMS for Nepal, ~300 messages with $15 credit).
Compliance: Ensure recipient consent for Nepal’s telecom laws.
Production: Upgrade Twilio for unrestricted bulk sending.

Contributing
<<<<<<< HEAD
🚀 Add features (e.g., paid Twilio support, CSV upload)? Fork, create a branch, and submit a PR!
License
MIT License
=======
🚀 Add features (e.g., CSV upload, paid Twilio support)? Fork, create a branch, and submit a PR!
License
This project is licensed under the MIT License - see the LICENSE file for details.
>>>>>>> 533a848 (added readme)
