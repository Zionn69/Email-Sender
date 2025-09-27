import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

# Gmail credentials (replace with your actual email and App Password)
gmail_user = 'your_email@gmail.com'
app_password = 'your_app_password'

# Set up the SMTP server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(gmail_user, app_password)

# Read the CSV file
with open('emails.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        email = row['Email']
        subject = row['Subject']
        message = row['Message']

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = email
        msg['Subject'] = subject

        # Personalize the body
        body = f"Hello {name},\n\n{message}\n\nBest regards,\nYour Team"
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            server.sendmail(gmail_user, email, msg.as_string())
            print(f"Email sent successfully to {email}")
        except Exception as e:
            print(f"Failed to send email to {email}: {e}")

# Close the server connection
server.quit()
