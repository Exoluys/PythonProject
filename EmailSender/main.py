import smtplib
import ssl

# SMTP server and port for Gmail
host = "smtp.gmail.com"
port = 465  # Port 465 is for SSL connection

# Email details
username = input("Enter your email address: ")
password = input("Enter your password: ")
receiver = input("Enter receiver email: ")

# Set up the message
subject = input("Subject: ")
body = input("Enter your message: ")

message = f"Subject: {subject}\n\n{body}"

try:
    # Establish a secure connection with the SMTP server using SSL encryption
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password) # Log in using secure credentials
        server.sendmail(username, receiver, message) # Send the email

# Handle authentication errors specifically
except smtplib.SMTPAuthenticationError:
    print("Error: Authentication failed. Check your credentials.")

# Catch any other exceptions that may occur and print the error details
except Exception as e:
    print(f"An error occurred: {e}")

# Confirmation message, though it will print regardless of success or failure
finally:
    print("Mail Sent")
