from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()


your_email = os.getenv('your_email')
your_password = os.getenv('your_password')
mail_server = os.getenv('mail_server')

app = Flask(__name__)
app.config['MAIL_SERVER'] = mail_server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = your_email
app.config['MAIL_PASSWORD'] = your_password
app.config['SECRET_KEY'] = 'qyurnhykslpjdjsyskdwe'

mail = Mail(app)
CORS(app)


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    form_data = request.get_json()

    # Get the form data
    name = form_data['name']
    email = form_data['email']
    subject = form_data['subject']
    phone = form_data['phone']
    message = form_data['message']

    # Send the email 
    msg = Message('Contact Form Submission', sender=your_email, recipients=[your_email])
    msg.body = 'Name: {}\nEmail: {}\nSubject: {}\nPhone: {}\nMessage: {}'.format(name, email, subject, phone, message)

    # msg.body = f'Name: {name}\nEmail: {email}\nSubject: {subject}\nPhone: {phone}\n message: {message}'
    mail.send(msg)

    response_data = {'message': 'Form submitted successfully'}
    return jsonify(response_data), 200


@app.route('/newsletter', methods=['GET', 'POST'])
def newsletter():
    form_data = request.json

    # Subscribing for Newsletter
    email = form_data['email']

    # Send the email 
    msg = Message('Newsletter Subscription', sender=your_email, recipients=[your_email])
    msg.body = 'Email: {}'.format(email)
    mail.send(msg)

    response_data = {'message': 'Form submitted successfully'}
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True, port=3001)