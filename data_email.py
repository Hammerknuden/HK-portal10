import smtplib
from email.message import EmailMessage
import ssl
from email.utils import make_msgid
from pathlib import Path

port = 587
smtp_server = 'send.one.com'
Subject = "Hammerknuden reservations data"
sender_email = 'reservation@hammerknuden.dk'
admin_email = 'reservation@hammerknuden.dk'
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
        now,
        nationalitet,
        web,
        num_rooms,
        num_guests,
        email_address,
        telefon,
        formatted_pristotal):
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif;">

            <hr>
            <h2>Reservation Data</h2>
            <hr>

            <img src="cid:{logo_cid}" alt="logo" width="300"/>

            <p>
                Reservations Data mail for reservation </b><br>
                Booknr: {booking_number} <br>
                {name},{checkin_date},{checkout_date},{now},{nationalitet},{web}<br>
            </p>

            <p>
                <b>Antal værelser og gæster:</b><br>
                Antal værelser: {num_rooms}, {num_guests}<br>
            </p>

            <p>
                <b>Kontaktoplysninger:</b><br>
                Email: {email_address}, {telefon}<br>
            </p>
            <p>
                <b>Total pris:</b> {formatted_pristotal}
            </p>

        </body>
    </html>
    """


def send_data_email(to_addr_1, confirmation_password, booking_number, name, checkin_date, checkout_date, num_rooms,
                    now, nationalitet, web, num_guests, email_address, telefon, formatted_pristotal):

    logo_cid = make_msgid()
    html_content = data_email_html_template(logo_cid[1:-1], booking_number, name, checkin_date, checkout_date,
                                            now, nationalitet, web, num_rooms, num_guests, email_address, telefon,
                                            formatted_pristotal)

    # construct email
    email = EmailMessage()

    email['Subject'] = Subject + f" #{booking_number}"
    email['From'] = sender_email
    email['To'] = to_addr_1
    email.set_content("Email client does not support html content")
    email.add_alternative(html_content, subtype='html')

    with open(logo_path, 'rb') as img:
        email.get_payload()[1].add_related(img.read(), maintype='image', subtype='jpeg', cid=logo_cid)

    send_email(confirmation_password, email)