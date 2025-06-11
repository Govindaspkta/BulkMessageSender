from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio.rest import Client
import sys
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set UTF-8 encoding for Python output
sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Twilio API configuration from environment variables
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_FROM_NUMBER = os.environ.get('TWILIO_FROM_NUMBER')

# Validate environment variables
if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER]):
    raise ValueError("Missing Twilio environment variables. Set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_FROM_NUMBER in .env file.")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send-sms', methods=['POST'])
def send_sms():
    data = request.get_json()
    numbers = data.get('numbers', [])
    message = data.get('message', '')
    
    if not numbers or not message:
        return jsonify({'message': 'Numbers and message are required'}), 400
    
    success_count = 0
    errors = []
    
    # Send SMS using Twilio API
    for number in numbers:
        try:
            message_obj = client.messages.create(
                body=message,
                from_=TWILIO_FROM_NUMBER,
                to=number
            )
            if message_obj.sid:  # Message queued successfully
                success_count += 1
            else:
                errors.append(f"Failed to send to {number}: Unknown error")
        except Exception as e:
            errors.append(f"Error sending to {number}: {str(e)}")
        
        # Rate limit for trial mode
        time.sleep(0.5)
    
    if success_count == len(numbers):
        return jsonify({'message': f'Message sent to {success_count} numbers successfully!'})
    else:
        return jsonify({
            'message': f'Sent to {success_count} numbers. Errors: {", ".join(errors)}'
        }), 500 if not success_count else 200

if __name__ == '__main__':
    app.run(debug=True)