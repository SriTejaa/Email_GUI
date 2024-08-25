import smtplib

# Set up the SMTP server and port
s = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS for security
s.starttls()

# Use your email and the app-specific password
email = '20u41a0553@diet.edu.in'
app_password = '20U41A0553'  # Replace with the app-specific password

# Login to the SMTP server
try:
    s.login(email, app_password)
except smtplib.SMTPAuthenticationError as e:
    print(f"Failed to login: {e}")
    s.quit()
    exit()

# Define the message
message = "Hi, I'm Cyber Trainer"

# Send the email
try:
    s.sendmail(email, 'sriteja2003@gmail.com', message)
    print("Email sent successfully!")
except smtplib.SMTPException as e:
    print(f"Failed to send email: {e}")

# Quit the SMTP server
s.quit()