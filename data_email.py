import smtplib
from email.message import EmailMessage
import ssl
from email.utils import make_msgid
from pathlib import Path

port = 587 #587
smtp_server = 'send.one.com'  #'asmtp.yousee.dk'
Subject = "Hammerknuden Reservation"
sender_email = 'reservation@hammerknuden.dk' #'Hkreservation@mail.dk'
admin_email = 'reservation@hammerknuden.dk' #'Hkreservation@mail.dk'  #'reservation@hammerknuden.dk'
logo_path = Path("logo2.jpg")

def send_email(confirmation_password, email):
    context = ssl.create_default_context()
    # Send the message via local SMTP server.
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(admin_email, confirmation_password)
        server.send_message(email)

def data_email_html_template(
        logo_cid,
        booking_number,
        name,
        checkin_date,
        checkout_date,
        num_rooms,
        num_guests,
        email_address,
        telefon,
        formatted_pristotal):
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif;">

            <hr>
            <h2>Reservation</h2>
            <hr>

            <img src="cid:{logo_cid}" alt="logo" width="300"/>

            <p>
                Data mail for reservation <b>{booking_number}</b><br>
                Navn: <b>{name}</b>
            </p>

            <p>
                <b>Ophold:</b><br>
                Check-in: {checkin_date}<br>
                Check-out: {checkout_date}<br>
                Antal værelser: {num_rooms}<br>
                Antal gæster: {num_guests}
            </p>

            <p>
                <b>Kontaktoplysninger:</b><br>
                Email: {email_address}<br>
                Telefon: {telefon}
            </p>

            <p>
                <b>Total pris:</b> {formatted_pristotal}
            </p>

        </body>
    </html>
    """


def send_data_email(to_addr, confirmation_password, booking_number, name, checkin_date, checkout_date, num_rooms,
                    num_guests, email_address, telefon, formatted_pristotal):

    logo_cid = make_msgid()
    html_content = data_email_html_template(logo_cid[1:-1], booking_number, name, checkin_date, checkout_date,
                                            num_rooms, num_guests, email_address, telefon, formatted_pristotal)

    # construct email
    email = EmailMessage()

    email['Subject'] = Subject + f" #{booking_number}"
    email['From'] = sender_email
    email['To'] = to_addr
    email.set_content("Email client does not support html content")
    email.add_alternative(html_content, subtype='html')

    with open(logo_path, 'rb') as img:
        email.get_payload()[0].add_related(img.read(), 'image', 'jpeg', cid=logo_cid)

    send_email(confirmation_password, email)