import smtplib
import ssl
from email.message import EmailMessage

# Set the subject line that appears in the recipient's inbox
subject = "Email From Python"
# Set the plain-text version of the email content
body = "This is a test email from Python!"
# Prompt the user to enter the sender and recipient email addresses
sender_email = input("Enter the sender's email address: ")
receiver_email = input("Enter the recipient's email address: ")
# Enter your Gmail App Password.
# This 16-character password is generated from your Google Account (under Security > App passwords)
password = input("Enter a password: ")

password = input("Enter a password: ")

import requests

# Latitude and longitude for Victoria, Seychelles
latitude = -4.617
longitude = 55.450

# Request weather data from Open-Meteo API
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"

response = requests.get(url)
data = response.json()

# Extract temperature and wind speed values from the response
temperature = data["current"]["temperature_2m"]
wind_speed = data["current"]["wind_speed_10m"]

# Build an HTML snippet to include in the email body
weather_html = f"""
<ul style="margin:20px 0; padding-left:20px;">
  <li><strong>Current Temperature:</strong> {temperature}°C</li>
  <li><strong>Wind Speed:</strong> {wind_speed} m/s</li>
</ul>
"""

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
#The content of the email
message.set_content(body)

html = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Automated Python Email</title>
  </head>
  <body style="margin:0; padding:0; background-color:#f9f9f9; font-family:Helvetica,Arial,sans-serif;">
    <table width="100%" cellpadding="0" cellspacing="0">
      <tr>
        <td align="center">
          <!-- Main container -->
          <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; margin:30px 0; border-radius:10px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.1);">

            <!-- Header -->
            <tr>
              <td style="background:linear-gradient(90deg,rgba(42, 123, 155, 1) 0%, rgba(87, 199, 133, 1) 50%, rgba(237, 221, 83, 1) 100%); padding:40px; text-align:center;">
                <h1 style="color:#ffffff; margin:0; font-size:28px;">Your Python Email Report</h1>
              </td>
            </tr>

            <!-- Hero image -->
            <tr>
              <td>
                <img
                  src="https://media.istockphoto.com/id/1419410282/photo/silent-forest-in-spring-with-beautiful-bright-sun-rays.jpg?s=612x612&w=0&k=20&c=UHeb1pGOw6ozr6utsenXHhV19vW6oiPIxDqhKCS2Llk="
                  alt="Email Automation"
                  width="600" height="250"
                  style="display:block; border:0; outline:none; text-decoration:none;"
                />
              </td>
            </tr>

            <!-- Body content -->
            <tr>
              <td style="padding:30px; color:#333333; font-size:16px; line-height:1.6;">
                <p>Hi there,</p>

<p>
  Just a quick weather update from paradise 🏝️ — straight from our Python script!
</p>

<p>
  Here's the current temperature in the Seychelles, as retrieved from Open-Meteo's live API:
</p>

{weather_html}

<p>
  Have a sunny day and don’t forget the sunscreen ☀️
</p>


                    <!-- Call-to-action button linking to live weather forecast for Seychelles -->
<p style="text-align:center; margin:30px 0;">
  <a
    href="https://www.meteoblue.com/en/weather/week/victoria_seychelles_241131"
    style="background:linear-gradient(90deg,rgba(42,123,155,1),rgba(87,199,133,1)); color:#ffffff; text-decoration:none; padding:14px 24px; border-radius:5px; font-weight:bold; display:inline-block;"
  >
    See Full Forecast for Seychelles
  </a>
</p>


                <p>
                  Cheers,<br/>
                  <em>The Automation Bot</em>
                </p>
              </td>
            </tr>

            <!-- Footer -->
            <tr>
              <td style="background-color:#ecf0f1; padding:20px; text-align:center; font-size:12px; color:#7f8c8d;">
                <p style="margin:0;">© 2025 Had_R. All rights reserved.</p>
                <p style="margin:5px 0 0;">
                  Don't want these emails? <a href="#" style="color:#1abc9c; text-decoration:none;">Unsubscribe</a>
                </p>
              </td>
            </tr>

          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
"""

#The content
message.add_alternative(html, subtype="html")

#Adds pdf file to the messge.
# Path to the PDF file you want to attach
pdf_path = "/content/loremipsum.pdf"

# Read the PDF file in binary mode
with open(pdf_path, "rb") as f:
    pdf_data = f.read()

# Attach the PDF file to the email message
message.add_attachment(
    pdf_data,
    maintype="application",
    subtype="pdf",
    filename="lorem_Ipsum.pdf"

)

#A secure connection to Gmail. Context for a secure connection which can be use in the ssl library to the Gmail server.
context = ssl.create_default_context()

print("Sending Email!")

#connect with the secure soccet layer. Connectiong to the Gmail server. We need a secure way so we use ssl.
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #Uses the server to log in to our email account so we can send an email.
    server.login(sender_email, password)
    #Sends our email. We convert the message object to a string so we can send it as a string email.
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")
