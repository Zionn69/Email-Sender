# Email Sender

A Python script to automatically send personalized emails using data from a CSV file via Gmail SMTP.

## Features

- Reads CSV file with columns: Name, Email, Subject, Message
- Sends emails row by row using Gmail SMTP (smtp.gmail.com, port 465)
- Personalizes email body with recipient's name
- Uses Gmail App Password for authentication (requires 2FA enabled)
- Prints success or error messages for each email
- Uses only standard libraries: smtplib and email.mime

## Prerequisites

- Python 3.x
- Gmail account with 2FA enabled
- App Password generated from Google Account settings

## Installation

1. Clone or download the repository.
2. Ensure Python 3.x is installed.

## Setup

1. Enable 2FA on your Gmail account.
2. Generate an App Password: Go to Google Account > Security > App passwords > Generate.
3. Create a CSV file named `emails.csv` with the following columns:
   ```
   Name,Email,Subject,Message
   John Doe,john@example.com,Welcome,Thank you for joining.
   ```
4. Edit `email_sender.py` and replace placeholders:
   - `gmail_user = 'your_email@gmail.com'`
   - `app_password = 'your_app_password'`

## Usage

```bash
python email_sender.py
```

The script will read the CSV file and send emails to each recipient, printing the status for each.

## Example CSV Content

```
Name,Email,Subject,Message
Alice Johnson,alice@example.com,Newsletter,Here's the latest update.
Bob Smith,bob@example.com,Reminder,Don't forget our meeting tomorrow.
```

## Notes

- Ensure the CSV file is in the same directory as the script.
- The email body format is: "Hello {Name},\n\n{Message}\n\nBest regards,\nYour Team"
- Handle errors gracefully; check console output for issues.

## License

This project is licensed under the MIT License.
