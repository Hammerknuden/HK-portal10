import streamlit
import streamlit as st
import pandas as pd
import requests
#from onedrive import Onedrive
from datetime import datetime, date
from pathlib import Path
import numpy as np
import gdown
#from django.contrib.sites import requests

from confirmation_email import (admin_email, send_danish_confirmation_email, send_english_confirmation_email,
                                send_german_confirmation_email)
from excel_database import add_data
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64


#df = pd.DataFrame({'Farve': ['R', 'B', 'G', 'F']})
# for at starte:
# tryk ctrl+shift+A for at få action menuen, vælg "terminal"
# skriv `streamlit run streamlit_app.py`

st.subheader("Velkommen til")

st.title("**HAMMERKNUDEN SOMMERPENSION - BOOKING PORTAL**")

st.image("logo2.jpg")

st.subheader("Reservations formular  ")

year = st.selectbox("booking år", options=[ "2024", "2025", "2026"])
bruger = st.selectbox("bruger computer ", options=["finn"])

now = st.date_input("booking dato")

booking_number = st.text_input("booking nummer ")


checkin_date = st.date_input("Checkin dato")
checkout_date = st.date_input("Checkout dato")
single_room = st.checkbox("Enkeltværelse")

days = checkout_date - checkin_date
st.text("Skema viser ikke udchecksdagen da den er irelevant i forbindelse med reservation")
st.markdown(f"**Antal dage denne booking**  {days.days}")


if year == '2024':
    if bruger == "naja":
        file_id = '1-9mALBucV-67ytDpfsWD9vUwXA_-tHOj'
        url = f'https://drive.google.com/uc?id={file_id}'
        df = pd.read_excel(url, sheet_name='book_simp')
        print(df)
        #df = pd.read_excel(r"C:\Users\naja\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\2025_BOOKING_ 2_0.xlsx",
        #                   sheet_name='book_simp')
    if bruger == "finn":

        file_id = '1-9mALBucV-67ytDpfsWD9vUwXA_-tHOj'
        url = f'https://drive.google.com/uc?id={file_id}'
        df = pd.read_excel(url, sheet_name='book_simp')
        print(df)
        #df = pd.read_excel(r'C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\2025_BOOKING_ 2_0.xlsx',
        #                   sheet_name='book_simp')

    else:
        streamlit.markdown("Fil fejl 2025")

    new_data = df[(df['dato'].dt.date >= checkin_date) & (df['dato'].dt.date < checkout_date)]
    unique_values = new_data["1-I"].unique()

    counts_1 = new_data["1-I"].value_counts()
    counts_2 = new_data["2-I"].value_counts()
    counts_3 = new_data["3-I"].value_counts()
    counts_4 = new_data["4-I"].value_counts()
    counts_5 = new_data["5-I"].value_counts()
    #chat
    print(f"Counts 1: {counts_1}")
    print(f"Counts 2: {counts_2}")
    print(f"Counts 3: {counts_3}")
    print(f"Counts 4: {counts_4}")
    print(f"Counts 5: {counts_5}")

    room_1 = (counts_1.get("va", 0))
    room_2 = (counts_2.get("va", 0))
    room_3 = (counts_3.get("va", 0))
    room_4 = (counts_4.get("va", 0))
    room_5 = (counts_5.get("va", 0))
    # chat
    print(f"Room 1: {room_1}")
    print(f"Room 2: {room_2}")
    print(f"Room 3: {room_3}")
    print(f"Room 4: {room_4}")
    print(f"Room 5: {room_5}")

    if room_1 == days.days:
        ledige_rum_1 = 1
    else:
        ledige_rum_1 = 0
    if room_2 == days.days:
        ledige_rum_2 = 1
    else:
        ledige_rum_2 = 0
    if room_3 == days.days:
        ledige_rum_3 = 1
    else:
        ledige_rum_3 = 0
    if room_4 == days.days:
        ledige_rum_4 = 1
    else:
        ledige_rum_4 = 0
    if room_5 == days.days:
        ledige_rum_5 = 1
    else:
        ledige_rum_5 = 0
    ledige_rum = ledige_rum_1 + ledige_rum_2 + ledige_rum_3 + ledige_rum_4 + ledige_rum_5
    print(unique_values)
    st.markdown(f"**Antal ledige rum**  {ledige_rum}")  # "ledige} rum ", {ledige_rum})


if year == '2025':

    if bruger == "naja":
        #df = pd.read_excel(r"C:\Users\naja\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\2025_BOOKING_ 2_0.xlsx",
        #                   sheet_name='book_simp')
        file_id = '1fS2Gs3mOTKGNj0DEQ96Kkahkj7nS_gJW'
        url = f'https://drive.google.com/uc?id={file_id}'
        df = pd.read_excel(url, sheet_name='book_simp')
        print(df)

    if bruger == "finn":
        #df = pd.read_excel(r'C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\2025_BOOKING_ 2_0.xlsx',
        #                   sheet_name='book_simp')
        file_id = '1fS2Gs3mOTKGNj0DEQ96Kkahkj7nS_gJW'
        url = f'https://drive.google.com/uc?id={file_id}'
        df = pd.read_excel(url, sheet_name='book_simp')
        print(df)
    else:
        streamlit.markdown("Fil fejl 2025")

    new_data = df[(df['dato'].dt.date >= checkin_date) & (df['dato'].dt.date < checkout_date)]
    unique_values = new_data["1-I"].unique()

    counts_1 = new_data["1-I"].value_counts()
    counts_2 = new_data["2-I"].value_counts()
    counts_3 = new_data["3-I"].value_counts()
    counts_4 = new_data["4-I"].value_counts()
    counts_5 = new_data["5-I"].value_counts()
    #chat
    print(f"Counts 1: {counts_1}")
    print(f"Counts 2: {counts_2}")
    print(f"Counts 3: {counts_3}")
    print(f"Counts 4: {counts_4}")
    print(f"Counts 5: {counts_5}")

    room_1 = (counts_1.get("va", 0))
    room_2 = (counts_2.get("va", 0))
    room_3 = (counts_3.get("va", 0))
    room_4 = (counts_4.get("va", 0))
    room_5 = (counts_5.get("va", 0))
    # chat
    print(f"Room 1: {room_1}")
    print(f"Room 2: {room_2}")
    print(f"Room 3: {room_3}")
    print(f"Room 4: {room_4}")
    print(f"Room 5: {room_5}")

    if room_1 == days.days:
        ledige_rum_1 = 1
    else:
        ledige_rum_1 = 0
    if room_2 == days.days:
        ledige_rum_2 = 1
    else:
        ledige_rum_2 = 0
    if room_3 == days.days:
        ledige_rum_3 = 1
    else:
        ledige_rum_3 = 0
    if room_4 == days.days:
        ledige_rum_4 = 1
    else:
        ledige_rum_4 = 0
    if room_5 == days.days:
        ledige_rum_5 = 1
    else:
        ledige_rum_5 = 0
    ledige_rum = ledige_rum_1 + ledige_rum_2 + ledige_rum_3 + ledige_rum_4 + ledige_rum_5
    print(unique_values)
    st.markdown(f"**Antal ledige rum**  {ledige_rum}")  # "ledige} rum ", {ledige_rum})

if year == '2026':

    if bruger == "naja":
        df = pd.read_excel(r"C:\Users\naja\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\2025_BOOKING_ 2_0.xlsx",
                           sheet_name='book_simp')
    if bruger == "finn":
        df = pd.read_excel(r'C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\2025_BOOKING_ 2_0.xlsx',
                           sheet_name='book_simp')

    else:
        streamlit.markdown("Fil fejl 2025")

    new_data = df[(df['dato'].dt.date >= checkin_date) & (df['dato'].dt.date < checkout_date)]
    unique_values = new_data["1-I"].unique()

    counts_1 = new_data["1-I"].value_counts()
    counts_2 = new_data["2-I"].value_counts()
    counts_3 = new_data["3-I"].value_counts()
    counts_4 = new_data["4-I"].value_counts()
    counts_5 = new_data["5-I"].value_counts()
    #chat
    print(f"Counts 1: {counts_1}")
    print(f"Counts 2: {counts_2}")
    print(f"Counts 3: {counts_3}")
    print(f"Counts 4: {counts_4}")
    print(f"Counts 5: {counts_5}")

    room_1 = (counts_1.get("va", 0))
    room_2 = (counts_2.get("va", 0))
    room_3 = (counts_3.get("va", 0))
    room_4 = (counts_4.get("va", 0))
    room_5 = (counts_5.get("va", 0))
    # chat
    print(f"Room 1: {room_1}")
    print(f"Room 2: {room_2}")
    print(f"Room 3: {room_3}")
    print(f"Room 4: {room_4}")
    print(f"Room 5: {room_5}")

    if room_1 == days.days:
        ledige_rum_1 = 1
    else:
        ledige_rum_1 = 0
    if room_2 == days.days:
        ledige_rum_2 = 1
    else:
        ledige_rum_2 = 0
    if room_3 == days.days:
        ledige_rum_3 = 1
    else:
        ledige_rum_3 = 0
    if room_4 == days.days:
        ledige_rum_4 = 1
    else:
        ledige_rum_4 = 0
    if room_5 == days.days:
        ledige_rum_5 = 1
    else:
        ledige_rum_5 = 0
    ledige_rum = ledige_rum_1 + ledige_rum_2 + ledige_rum_3 + ledige_rum_4 + ledige_rum_5
    print(unique_values)
    st.markdown(f"**Antal ledige rum**  {ledige_rum}")  # "ledige} rum ", {ledige_rum})

def highlight_cells(val):
#chat

    color = 'background-color: #66FF66' if val == 'va' else ''  # Grøn for 'va'
    return color
# Brug applymap til at anvende funktionen på alle celler i DataFrame
#styled_data = new_data.style.applymap(highlight_cells)
styled_data = new_data[['dato', '1-I', '2-I', '3-I', '4-I', '5-I']].style.applymap(highlight_cells)
# Vis den styliserede DataFrame i Streamlit
st.dataframe(styled_data)

num_guests = st.number_input("Antal gæster", value=2, step=1)
num_rooms = st.number_input("Antal rum", value=1, step=1)
web = st.selectbox("booking via web bc eller FM folkemøde ( ikke mulighed for enk rum)", options=["web", "bc", "FM"])
seng = st.text_input(" type seng DB, ENK, OPCH, OPIN ")
if web == "web":
    rabat = st.number_input(" rabat i procent ", value=10, step=1)
    procent = rabat
if web == "FM":
    FM_add = st.number_input(" Folkemøde tillæg i procent ", value=0, step=5)
    procent = FM_add
else:
    procent = 0

if year == '2024':
    if single_room:
        high_season_price = 925  #2025 950
        low_season_price = 805   #2025 830
        single_room = "Y"
    if web == "FM":
        high_season_price = 1025
        low_season_price = 1025
    else:
        high_season_price = 1025   #2025 1050
        low_season_price = 905     #2025 930
        single_room = "N"
if year == '2025':
    if single_room:
        high_season_price = 950  #2025 950
        low_season_price = 830   #2025 830
        single_room = "Y"
    if web == "FM":
        high_season_price = 1050
        low_season_price = 1050
    else:
        high_season_price = 1050   #2025 1050
        low_season_price = 930     #2025 930
        single_room = "N"
if year == '2026':
    if single_room:
        high_season_price = 985  #2025 950
        low_season_price = 865   #2025 830
        single_room = "Y"
    if web == "FM":
        high_season_price = 1085
        low_season_price = 1085
    else:
        high_season_price = 1085   #2025 1050
        low_season_price = 965     #2025 930
        single_room = "N"

print(low_season_price)
print(high_season_price)
if year == '2024':
    bf_price = 95  #breakfast 2025 100,-
if year == '2025':
    bf_price = 100
if year == '2026':
    bf_price = 110
st.markdown(f"**High season** {high_season_price}")
st.markdown(f"**Low season** {low_season_price}")

Sprog = st.selectbox("Sprog - email confirmation dk uk D", options=["DK", "UK", "D"])

breakfast = st.checkbox("Morgenmad")
if breakfast:
    br_f = int(bf_price * int(num_guests) * int(days.days))
    breakfast = "Y"
else:
    br_f = 0
    breakfast = "N"

if Sprog == "DK":
    if breakfast:
        text_bf = "Morgenmad er inkluderet i prisen"
    else:
        text_bf = "Morgenmas er ikke inkluderet i prisen"

if Sprog == "UK":
    if breakfast:
        text_bf = "Breakfast is included "
    else:
        text_bf = " Breakfast is not included "

if Sprog == "D":
    if breakfast:
        text_bf = "Das Frühstück ist im Preis inbegriffen"
    else:
        text_bf = "Frühstück ist nicht mit enthalten"


if year == '2024':
    high_season_start = datetime.strptime("24-06-24", _format := "%d-%m-%y").date()
    high_season_end = datetime.strptime("19-08-24", _format := "%d-%m-%y").date()
if year == '2025':
    high_season_start = datetime.strptime("29-06-25", _format := "%d-%m-%y").date()
    high_season_end = datetime.strptime("26-08-25", _format := "%d-%m-%y").date()
if year == '2026':
    high_season_start = datetime.strptime("28-06-26", _format := "%d-%m-%y").date()
    high_season_end = datetime.strptime("25-08-26", _format := "%d-%m-%y").date()

days = checkout_date - checkin_date

high_season_days = high_season_end - high_season_start
high_booking = (checkin_date >= high_season_start) and (checkout_date <= high_season_end)
low_booking = ((checkin_date <= high_season_start) and (checkout_date < high_season_start)) or (checkin_date >
                                                                                                    high_season_end)
mixbooking_early = (checkin_date < high_season_start) and (checkout_date > high_season_start)
mixbooking_end = (checkout_date > high_season_end) and (high_season_start < checkin_date) and (checkin_date <
                                                                                                   high_season_end)

high_season_days = high_season_end - high_season_start
mixearly = checkout_date - high_season_start
mixearly_b = high_season_start - checkin_date
mixend = high_season_end - checkin_date
mixend_b = checkout_date - high_season_end
if web == "FM":
    pris = (high_season_price * int(days.days)) * int(num_rooms)
else:
    if high_booking:
        pris = (high_season_price * int(days.days)) * int(num_rooms)
    if low_booking:
        pris = (low_season_price * int(days.days)) * int(num_rooms)
    if mixbooking_early:
        pris = (((int(mixearly.days) * high_season_price) + (int(mixearly_b.days) * low_season_price)) * int(num_rooms))
    if mixbooking_end:
        pris = (high_season_price * (int(mixend.days)) + (int(mixend_b.days) * low_season_price)) * int(num_rooms)

st.markdown(f"**Værelsespris** {pris:.2f}kr")
print(pris)
prismed = pris + br_f
formatted_prismed = f"{prismed:.2f}"
st.markdown(f"**Pris incl breakfast** {formatted_prismed}kr")

if web == "web":
    rabat_a = (int(rabat) / 100)
    rabat_mm = br_f * rabat_a
    rabat_rm = pris * rabat_a
    rabat_t = rabat_mm + rabat_rm
    formatted_rabat_t = f"{rabat_t:.2f}"
    st.markdown(f"**Rabat** {formatted_rabat_t}kr")
    pristotal = prismed - rabat_t
    formatted_pristotal = f"{pristotal:.2f}"
elif web == "FM":
    pris_add_a = (int(FM_add) / 100)
    pris_add_t = (prismed + br_f) * pris_add_a
    formatted_pris_add_t = f"{pris_add_t:.2f}"
    st.markdown(f"**Tiilæg** {formatted_pris_add_t}kr")
    pristotal = prismed + pris_add_t
    formatted_pristotal = f"{pristotal:.2f}"
else:
    formatted_pristotal = formatted_prismed

print(formatted_pristotal)
st.markdown(f"**Den totale pris** {formatted_pristotal}kr")

name = st.text_input("Navn ")
telefon = st.text_input(" Kontakt telefon")
email_address = st.text_input("email")

nationalitet = st.text_input("Nationalitet - DK S N NL etc")

#"D:\Hammerdata\Database hammerknuden.xlsx"
#"Database hammerknuden.xlsx
#https://docs.google.com/spreadsheets/d/1-9Ks0RY1bMlEM0QuYGVv5_VXztI97Yu6/edit?usp=drive_link&ouid=113417285199087461988&rtpof=true&sd=true



#st.subheader("USB database skal være indsat for at bruge known guest checkbox  ")
known_guest = st.checkbox("check for known person")
if known_guest:

    file_id = '1-9Ks0RY1bMlEM0QuYGVv5_VXztI97Yu6'
    url = f'https://drive.google.com/uc?id={file_id}'
    #output = 'database.xlsx'
    #gdown.download(url, output, quiet=False)
    #df = pd.read_excel("D:\Hammerdata\Database hammerknuden.xlsx", sheet_name="Dtb", dtype={"telefon": str})
    #df = pd.read_excel(output, sheet_name='Dtb')
    df = pd.read_excel(url, sheet_name='Dtb')
    search_value = telefon
    pd.set_option("display.max_columns", None)
    rows1 = df[df['telefon'] == search_value]
    #df = pd.read_excel("D:\Hammerdata\Database hammerknuden.xlsx", sheet_name="Dtb", dtype={"email": str})
    search_value = email_address
    df = pd.read_excel(url)
    pd.set_option("display.max_columns", None)
    rows2 = df[df['Email'] == search_value]

    if telefon:
        st.dataframe(rows1)
        known = "Y"
    elif email_address:
        st.dataframe(rows2)
        known = "YY"
else:
    known = "N"

spouse = st.text_input("info for kendt person til Dtb  ")

send_data = st.button("data to excel")
if send_data and year == '2024':
    if bruger == "finn":
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web},{seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {pristotal}, {known})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
                 rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast, pristotal, known,
                 excel_path=r"C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2024 output.xlsx")
    if bruger == "naja":
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web}, {seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {pristotal}, {known})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
                 rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast, pristotal, known,
                 excel_path=r"C:\Users\bonne\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2024 output.xlsx")

    st.markdown("2024 data sendt til excel")

if send_data and year == '2025':
    if bruger == "finn":
        file_id = '1QGGa7LG9OfryfefhJ4QohGYxqjNJ-fPg'
        url = f'https://drive.google.com/uc?id={file_id}'
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web}, {seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {pristotal}, {known})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
                 rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast, pristotal, known,
                 excel_path=url)
                 #excel_path=r"C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2025 output.xlsx")
    if bruger == "naja":
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web}, {seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {pristotal}, {known})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
                 rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast, pristotal, known,
                 excel_path=r"C:\Users\bonne\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2025 output.xlsx")

    st.markdown("2025 data sendt til excel")

if send_data and year == '2026': # husk at indsætte bruger naja / finn
    if bruger == "finn":
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web}, {seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {pristotal}, {known})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
                 rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast, pristotal, known,
                 excel_path=r"C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2026 output.xlsx")
    if bruger == "naja":
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web}, {seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {pristotal}, {known})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
                 rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast, pristotal, known,
                 excel_path=r"C:\Users\bonne\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2026 output.xlsx")

    st.markdown("2026 data sendt til excel")

text_ank = st.checkbox("tekst vedr. ankomsttid  ")
if Sprog == 'DK':
    if text_ank:
        text_ank = ("Da vores reception ikke er bemandet H24, bedes I informere om ankomsts tidspunkt for nøgle "
                    "udlevering")
    else:
        text_ank = " - "

if Sprog == 'UK':
    if text_ank:
        text_ank = ("Since the reception isn´t operative on a 24 hours basis, please inform us on your arrival time, "
                    "to obtain room key")
    else:
        text_ank = " - "

if Sprog == 'D':
    if text_ank:
        text_ank = ("Da die Rezeption nicht rund um die Uhr besetzt ist, informieren Sie uns bitte über Ihre "
                    "Ankunftszeit,um Zimmerschlüssel erhalten.")
    else:
        text_ank = " - "

text_bed = st.checkbox("tekst vedr. valg af seng  ")
if Sprog == 'DK':
    if text_bed:
        text_bed = "Ønske om dobbelt eller enkelseng kan sendes på mail før ankomst"
    else:
        text_bed = " - "

if Sprog == 'UK':
    if text_bed:
        text_bed = "Requests for a double or single bed can be sent by email before arrival"
    else:
        text_bed = " - "

if Sprog == 'D':
    if text_bed:
        text_bed = "Anfragen für ein Doppel- oder Einzelbett können vor der Anreise per E-Mail gesendet werden"
    else:
        text_bed = " - "

text_free = st.checkbox("Skriv ekstra tekst - husk sprog  ")

if text_free:
    text_free = st.text_input("skriv add tekst ")
    print(text_free)
else:
    text_free = " - "

if web == "web" and Sprog == "DK":
    text_web = "Rabat i forbindelse med opholdet er"
    justering = rabat_t
    formatted_justering = f"{justering:.2f}kr"
    print(formatted_justering)
elif web == "FM" and Sprog == "DK":
    text_web = "Evt tillæg i forbindelse med denne booking"
    justering = pris_add_t
    formatted_justering = f"{justering:.2f}kr"
    print(formatted_justering)
    depositum = pristotal * 0.5
    st.markdown(f"** depositum 50% ** {depositum:.2f}")
elif web == "web" and Sprog == "UK":
    text_web = "Any discount in connection with this booking is."
    justering = rabat_t
    formatted_justering = f"{justering:.2f}kr."
elif web == "web" and Sprog == "D":
    text_web = f"Jegliche Ermäßigung im Zusammenhang mit dieser Buchung gilt."
    justering = rabat_t
    formatted_justering = f"{justering:.2f}kr"
else:
    text_web = " - "
    formatted_justering = " - "


guest_email = st.checkbox("send mail direkte til gæst  ")
if guest_email:
    to_addr = [email_address, admin_email]
else:
    to_addr = [admin_email]
#to_addr = "finnjorg@mail.dk"

confirmation_password = st.text_input("Admin kodeord")
booking_submitted = st.button("Bekræft booking")

if Sprog == "DK" and booking_submitted:
    send_danish_confirmation_email(to_addr, confirmation_password, name, num_rooms, num_guests, booking_number,
                                   checkin_date, checkout_date, text_bf, prismed, text_web, formatted_justering,
                                   pristotal, text_ank, text_bed, text_free)
    st.markdown('dansk email er sendt')
elif Sprog == "UK" and booking_submitted:
    send_english_confirmation_email(to_addr, confirmation_password, name, num_rooms, num_guests, booking_number,
                                    checkin_date, checkout_date, text_bf, prismed, text_web, formatted_justering,
                                    pristotal, text_ank, text_bed, text_free)
    st.markdown('engelsk email er sendt')
elif Sprog == "D" and booking_submitted:
    send_german_confirmation_email(to_addr, confirmation_password, name, num_rooms, num_guests, booking_number,
                                   checkin_date, checkout_date, text_bf, prismed, text_web, formatted_justering,
                                   pristotal, text_ank, text_bed, text_free)
    st.markdown('tysk email er sendt')
else:
    st.markdown("mail er ikke sendt ")