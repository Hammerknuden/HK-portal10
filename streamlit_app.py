import streamlit
import streamlit as st
import pandas as pd
import openpyxl
import requests
#from onedrive import Onedrive
from datetime import datetime, date
from pathlib import Path
import numpy as np
#import gdown
#from django.contrib.sites import requests

from confirmation_email import (admin_email, send_danish_confirmation_email, send_english_confirmation_email,
                                send_german_confirmation_email)
from excel_database import add_data
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64
#url for onedrive downloads
#book2025 = 'https://my.microsoftpersonalcontent.com/personal/3be7f4b38f07ed41/_layouts/15/download.aspx?UniqueId=1077df0c-baf7-4a87-ad56-dd626b73020b&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI4MTRkMjJlYi05ZmY2LTRmZWMtYjcxNi04M2VkNWYxODdiNWUiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDYxMTU1MjIifQ.XDYP5wr_tCr-5OvpVO1WpSYKk7dEon2fqECtRqs5i616BqjBeGwD4uUnzYLCnUKgAUp6_34EFLaqZbiJGpN5nul5FMA2TgSnQZXe2QS7MSUbRj7ZZrj9mHsvSXb1cHMAWHV2923s-QGuS7A5bbqmVeNegnm4QA4Mzf4Pp-nv0Ij30-P1yu9qiFhD0fKtxFYDR71UAoVqNok12LT5ZsdkoWfk5glMj4QeBi616Kf7M-9eWjhU529Ctc2sX6PYWOXmuDS6TwkiKNI1a9AjPgqVOes-OiUGyrIQQMBTatLTxAXojTYO5e0diN2gvMi5ltm0DzQeLV5zo8qzqC-2w3BNVHiQFvAZlYMtimjQQUr3LTlA6NOGY4hgnMnRakNU2OYNHSRdRV9AdjHYHepl4tPqZQ.s6G5YYXeoSQQJH9KJ0NH_OCj1wIYQySCKM2M-ZyfANU&ApiVersion=2.0&AVOverride=1'
#book2025 = 'https://my.microsoftpersonalcontent.com/personal/3be7f4b38f07ed41/_layouts/15/download.aspx?UniqueId=1077df0c-baf7-4a87-ad56-dd626b73020b&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI4MTRkMjJlYi05ZmY2LTRmZWMtYjcxNi04M2VkNWYxODdiNWUiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDYzNDc4NTcifQ.Tk4OvX5hMhuoRcjwWBnd6gaw2v2ks6TNzusdATMuf7FJb2EIE8dmJ8jolV1JJ1p7-zErpcNfG6Mtwcbwce1sXTxN8YaLzRTvpiG7ByZB27kUr0KUP8FWJYKqQYpoNSeQcv4e8bLFQzjdzvs7paKJrc3n2fIsFzPNLACHovaZBo6Cx_sPbB9P_Cm8vj4bXNUY07btY8JjCvJDZYdMCDYtVw2InpKz3yiCO3ZFqnUrGwQ08y2y_qjWuDfBjhVpgJ5PCb9-uY_r9RYFW5msUxw-KUwkHgZkwCs6azH94h7CKKDZHmsKlheaCD8TZEwlC1dkV3kWO_Jopxw_gBBISPobc5G5vSaAhq54cbFD-a2yer18SF3wakdhYjBdTLSSTnY_iXYd2zjG7IgljNr31d3hcA.1Vrhcfah7VUD3LJQLAOC1YYk_Ap0Vv6mFDKbLdOCSig&ApiVersion=2.0&AVOverride=1'
#book2026 = ''
#book2026 = 'https://my.microsoftpersonalcontent.com/personal/3be7f4b38f07ed41/_layouts/15/download.aspx?UniqueId=c4800bac-58a6-42a3-9d2a-384fbb61a0d4&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI4MTRkMjJlYi05ZmY2LTRmZWMtYjcxNi04M2VkNWYxODdiNWUiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDU1MDU1MDcifQ.NxDMnsi3Q_68d4L7lJHRmH1OrQxxSIlh9qs76-PVzA1fcc2LmszpG9takY3jpkS8wVA3l0XD_93RImWY3jPGXK4zPtrqsfsRyEMMPhpnC5lCqOp5_bv397vb37sdEQzcyl1jok5_klQH_b2lS5zxNq6Sf6MrFY633V5Y7UFAQObGght0ljo-sTfriY39KO2af9BTspVI4i6-0vK5RFjmztglMO4WszsLQesI3m_-SdjN_pcjekzpQWTRm0E30esBo1poIauU7OK0uSXclFKyb2cKaS0p9JYsi9YhJ0IBDVZWxYu-KdF4qR1V3eNIF93s9od7ItiUC8mq7fVz2xJ8AJ-axIdxmInKI1pNsfpkGDNOuHS6bdFmGx-mxyINZaiulwZAEqWgHsnv8muoyIDQ3A.NzvOL1jtGXrBiVEKmoRAtw91ecCRriSpBqmO2KPMzyA&ApiVersion=2.0&AVOverride=1'
#book2026
#outp2026 = ''
#hk_database = 'https://my.microsoftpersonalcontent.com/personal/3be7f4b38f07ed41/_layouts/15/download.aspx?UniqueId=2bbcff11-e1ae-4318-b932-2b346cafe12a&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI4MTRkMjJlYi05ZmY2LTRmZWMtYjcxNi04M2VkNWYxODdiNWUiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDYwMzY5ODUifQ.He2Qr7MY2AyMb9yEoWoeck7yWLmOjl9GdPN44zyuowTUfj0KNe6ABcWvVwmnQNrHCGvI-5MBse2SCB6f3wwYoeNH4iEXh6NP4gvG4-hVKILSCQyfVIVXQNqVnuLTshWqX4ovZrndxi8fljj6arEnp4WLXW_sgtl1TLycYl5p8ZwGguT4omIHbeMLQp5X1IXO_6AZPb_Q7JxsFu9wPRZNdoIjH-x0TinCcZVvmz3mAQi3_HGD0WuxDvF5JjimPzXSjeqSQWVOB-T5XQ8QNbtal8JQza6iQcaePwiAeCFYRijcl5cvSQS9RKHIUShpH-qGRiJIypoQ_Gfw5ELY5BW7RcB4kT09Jh4fgA-xB_e-yiETJsd4H8efz5vmaDIc864Lj2BacZrApqpjP1ZjOD9XwA.HQskpE4hD4DDnqPpD2D_pTPipf_yDZe194lwXuvW1Bs&ApiVersion=2.0&AVOverride=1'
#hk_database = 'https://my.microsoftpersonalcontent.com/personal/3be7f4b38f07ed41/_layouts/15/download.aspx?UniqueId=2bbcff11-e1ae-4318-b932-2b346cafe12a&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI4MTRkMjJlYi05ZmY2LTRmZWMtYjcxNi04M2VkNWYxODdiNWUiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDYxMTY3NTkifQ.h-ICgWqZbU-O_d85f_XdBry7a4IVbF0wULMPOCd6U7l3CsAtp1Y1R_vY38odp1pUaYqVLxgakM8zY_F_dF4Qji0XsxiVgQkPjBab0J0_rVPMs-3P7M3zNLKbcC8jSBToFbXGqbkHLQ8GBB3WaYiunGtvsJrQl0haYyyfwUDkVM5Z7qsxjqW6ulPwNpc6YL5LYZJnhiU8mUeLd4yiRs44orbXsK2V1rj0BHZsDC5duUvs0NbXayZxD2IpQ0TB6lc_smIi2k7hpcxOc-eJf8bOus62UxBj4sjdx8hetjdHquLVjStg13h3TQWeoTz4GIPrGDXrX6f_MvD9zTsuUjjiUj9NWXiQy5TzhpLxY0kq8y77y2Xw7z9hiHdCsco0XJ9NUrGE6XYRBGrJygpHpEWvVQ._rjBIFq3iFdSvQd1zNyN9Hs10kZ5e9mRONWKbRkennE&ApiVersion=2.0&AVOverride=1'

# for at starte:)
# tryk ctrl+shift+A for at få action menuen, vælg "terminal"
# skriv `streamlit run streamlit_app.py`

st.subheader("Velkommen til")

st.title("**HAMMERKNUDEN SOMMERPENSION - BOOKING PORTAL**")

st.image("logo2.jpg")

st.subheader("Reservations formular  ")

year = st.selectbox("booking år", options=["2025", "2026"])
bruger = st.selectbox("bruger computer ", options=["Finn", "Naja"])
network = st.selectbox("vælg lokal eller web ", options=["local", "URL"])

file_name_1 = r"C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2025_BOOKING_ 2_0.xlsx"

now = st.date_input("booking dato")

booking_number = st.text_input("booking nummer ")


checkin_date = st.date_input("Checkin dato")
checkout_date = st.date_input("Checkout dato")
single_room = st.checkbox("Enkeltværelse")

days = checkout_date - checkin_date
st.text("Skema viser ikke udchecksdagen da den er irelevant i forbindelse med reservation")
st.markdown(f"**Antal dage denne booking**  {days.days}")

if year == '2025':

    if bruger == "naja":
        #url = 'https://my.microsoftpersonalcontent.com/personal/3be7f4b38f07ed41/_layouts/15/download.aspx?UniqueId=1077df0c-baf7-4a87-ad56-dd626b73020b&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI4MTRkMjJlYi05ZmY2LTRmZWMtYjcxNi04M2VkNWYxODdiNWUiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDQyMjI0NjUifQ.KC9jXbujauBxUH6l2xsghR-L_3X_2LaUGcbOTvSIGJJwcYKActkI0tDaHFx3Xilu1kv9fHLI0jLJ9-5fuWGOUbFZvDnmskLBp3kVd-HCS_N-MZIRAGVz1LYrDh4eQMJ7vEZxgHsnVYjh-F28F02zzzd1-tg3dApt8hCTtfJuyxuNqg9bkfDMcJkdpduO44JO69d6GJlOOyCFi6QRGsNad1aDy0sszgRyDbv9t_HITvV4dzBhHRtjRiPj7eNJzGd1fyrPVJREJGl3L-jqKLh0vwaWGoN4qcHL-nEgUmRZWJ4PpTNOdvXSlZ2IKojzBtMB-ZK_G4I4gSX7K7Gr732iBfYDRG711ANop0N-Kg6pBO0EgYhpczkouJCGb-EBlYAdHDx00YCaxMVeTgmXrWlFBw.Sx5UzW5NW5VRE8yivXqnZKw88cSewUT3egnggwwptKU&ApiVersion=2.0&AVOverride=1'
        url = book2025
        df = pd.read_excel(url, sheet_name='book_simp')
        print(df)

    if bruger == "Finn" and network == "URL":
        url = 'https://drive.usercontent.google.com/download?id=1fS2Gs3mOTKGNj0DEQ96Kkahkj7nS_gJW&export=download&authuser=0&confirm=t&uuid=8a74ef99-d891-4950-8622-11ff5c7b5ee4&at=APcmpowsxXunj5Rcd1q_LcxQwLws:1746354248379'
        df = pd.read_excel(url, sheet_name='book_simp')
        new_data = df[(df['dato'].dt.date >= checkin_date) & (df['dato'].dt.date < checkout_date)]
        unique_values = new_data["1-I"].unique()

        counts_1 = new_data["1-I"].value_counts()
        counts_2 = new_data["2-I"].value_counts()
        counts_3 = new_data["3-I"].value_counts()
        counts_4 = new_data["4-I"].value_counts()
        counts_5 = new_data["5-I"].value_counts()
        # chat
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
        print(df)
    if bruger == "Finn" and network == "local":
        #file_name = r"C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2025_BOOKING_ 2_0.xlsx"
        file_name = r"C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2025_BOOKING_ 2_0.xlsx"
        df = pd.read_excel(file_name, sheet_name='book_simp')
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
        url = 'https://drive.usercontent.google.com/download?id=1RM638gexIKWNgr9MklHKUIhkbG04vRoS&export=download&authuser=0&confirm=t&uuid=2155e28f-6119-49d6-902d-064afd303b6a&at=APcmpoxm7SwQpOQkyMWs_vCMRnR5:1746373726707'
        df = pd.read_excel(url, sheet_name='book_simp')
        print(df)
    else:
        streamlit.markdown("Fil fejl 2026")

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


    color = 'background-color: #66FF66' if val == 'va' else ''  # Grøn for 'va'
    return color
styled_data = new_data[['dato', '1-I', '2-I', '3-I', '4-I', '5-I']].style.applymap(highlight_cells) # Vis den styliserede DataFrame i Streamlit
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
    BF = "Y"
    if Sprog == "DK":
        text_bf = "Morgenmad er inkluderet i prisen"
    if Sprog == "UK":
        text_bf = "Breakfast is included "
    if Sprog == "D":
        text_bf = "Das Frühstück ist im Preis inbegriffen"
else:
    br_f = 0
    BF = "N"
    if Sprog == "DK":
        text_bf = "Morgenmad er ikke inkluderet i prisen"
    if Sprog == "UK":
        text_bf = " Breakfast is not included "
    if Sprog == "D":
        text_bf = "Frühstück ist nicht mit enthalten"

#if breakfast and Sprog == "DK":
#    text_bf = "Morgenmad er inkluderet i prisen"
#else:
#    text_bf = "Morgenmad er ikke inkluderet i prisen"

#if breakfast and Sprog == "UK":
#    text_bf = "Breakfast is included "
#else:
#    text_bf = " Breakfast is not included "

#if breakfast and Sprog == "D":
#    text_bf = "Das Frühstück ist im Preis inbegriffen"
#else:
 #   text_bf = "Frühstück ist nicht mit enthalten"


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
fam_name = st.text_input("efternavn  ")
telefon = st.text_input(" Kontakt telefon")
email_address = st.text_input("email")

nationalitet = st.text_input("Nationalitet - DK S N NL etc")

known_guest = st.checkbox("check for known person")
if known_guest:
    #url = 'https://my.microsoftpersonalcontent.com/personal/3be7f4b38f07ed41/_layouts/15/download.aspx?UniqueId=2bbcff11-e1ae-4318-b932-2b346cafe12a&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI4MTRkMjJlYi05ZmY2LTRmZWMtYjcxNi04M2VkNWYxODdiNWUiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDQyMjQzMzIifQ.nyxJ9VDCOEUH1De6k6_WMUeZH7pWDSsbjc4eS4L9JAYNw5sALkGHRgUcgwAypaXa2gRB8aNJOzyPPeNDOGaI4Luoh2H3hMGYsfW4cieH0SLeW-ZrTXFiAxVpBTlx61wEgkVQKIFmnsnmkUi5oszkv01Z7e0_duCIAxh8Angh-6gGwgLGDgazcLyj8uPl-vtSI239C5_ru4h9PtZfrzPptxZkilew5Ezk9B6gXxXXb3UtOemjIFPyx1H2iClPr86fErAE1upM5fIMCfpfqMR7iIcYGpaw2Tp1hEc3FpcrQ6Oyh-jM4TEYXtnstDXQgAO0aXItsYqilQoTiFwWr5a16-GRgRBcpX3oFECsW-HqhKK76UOc0xt-UHvGkAkbh0wcoOW3vf8DKhRn4RFVG_0SDg.4FvHwf39ZNmtPiaSkFxRy0DluCempaNwp2oWI6Zmfs4&ApiVersion=2.0&AVOverride=1'
    #url = hk_database
    #url = 'https://drive.usercontent.google.com/download?id=1-9Ks0RY1bMlEM0QuYGVv5_VXztI97Yu6&export=download&authuser=0&confirm=t&uuid=dfaf9014-eab9-4edd-8563-0ea10daa469a&at=APcmpowChzeTZhFD_oliD1ZjOTed:1746344499202'
    file_id = '1-9Ks0RY1bMlEM0QuYGVv5_VXztI97Yu6'
    url = f'https://drive.google.com/uc?id={file_id}'

    df = pd.read_excel(url, sheet_name='Dtb', dtype={'familienavn': str})
    search_value = fam_name
    pd.set_option("display.max_columns", None, )
    rows1 = df[df['Familienavn'] == search_value]
    df = pd.read_excel(url, sheet_name='Dtb', dtype={'telefon': str})
    search_value = telefon
    pd.set_option("display.max_columns", None,)
    rows2 = df[df['telefon'] == search_value]
    df = pd.read_excel(url, sheet_name="Dtb", dtype={'Email': str})
    search_value = email_address
    pd.set_option("display.max_columns", None)
    rows3 = df[df['Email'] == search_value]

    if fam_name:
        st.dataframe(rows1)
    if telefon:
        st.dataframe(rows2)
        known = "Y"
    elif email_address:
        st.dataframe(rows3)
        known = "YY"
else:
    known = "N"

spouse = st.text_input("Spouce  ")
comments = st.text_input("yderligere info til Dtb  ")
send_data = st.button("data to excel")
if send_data and year == '2024':
    if bruger == "Finn":
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web}, {seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {formatted_pristotal}, {known})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
                 rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast,
                 formatted_pristotal, known, comments,
                 excel_path=r"C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2024 output.xlsx")
    if bruger == "naja":
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web}, {seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {formatted_pristotal}, {known})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
            rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast,
            formatted_pristotal, known, comments,
            excel_path=r"C:\Users\bonne\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2024 output.xlsx")

    st.markdown("2024 data sendt til excel")

if send_data and year == '2025':
    if bruger == "Finn":
        #file_id = '1QGGa7LG9OfryfefhJ4QohGYxqjNJ-fPg'
        #url = f'https://drive.google.com/uc?id={file_id}'
        #url = 'https://drive.usercontent.google.com/download?id=1QGGa7LG9OfryfefhJ4QohGYxqjNJ-fPg&export=download&authuser=0&confirm=t&uuid=4ece34a8-c6d3-4fb2-b14f-d679260a2777&at=APcmpoxYX9pwMTHWhzO7j9CamHva:1746354652387'
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web}, {seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {formatted_pristotal}, {known})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
                 rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast,
                 formatted_pristotal, known, comments,
                 excel_path='output.xlsx')
                 #excel_path=r"C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2025 output.xlsx")
    if bruger == "Naja":
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web}, {seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {formatted_pristotal}, {known})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
                 rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast,
                 formatted_pristotal, known, comments,
                 excel_path="output.xlsx")  #"C:\Users\finnj\-repoHK2\HK-portal10\2025 output.xlsx")
    st.markdown("2025 data sendt til excel")

if send_data and year == '2026': # husk at indsætte bruger naja / finn
    if bruger == "Finn":
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web}, {seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {formatted_pristotal}, {known}, {comments})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
                 rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast,
                 formatted_pristotal, known,
                 excel_path='output.xlsx')#r"C:\Users\finnj\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2026 output.xlsx")
    if bruger == "Naja":
        some_book_data = ({year}, {booking_number}, {name}, {checkin_date}, {checkout_date}, {now}, {nationalitet},
                          {web}, {seng}, {rabat}, {num_rooms}, {num_guests}, {email_address}, {telefon}, {spouse},
                          {single_room}, {breakfast}, {formatted_pristotal}, {known})
        add_data(some_book_data, year, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng,
                 rabat, num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast,
                 formatted_pristotal, known, comments,
                 excel_path='output.xlsx')#r"C:\Users\bonne\OneDrive\DELE MAPPE NAJA\HAMMERKNUDEN\BOOKING\filer\2026 output.xlsx")

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
                                   formatted_pristotal, text_ank, text_bed, text_free)
    st.markdown('dansk email er sendt')
elif Sprog == "UK" and booking_submitted:
    send_english_confirmation_email(to_addr, confirmation_password, name, num_rooms, num_guests, booking_number,
                                    checkin_date, checkout_date, text_bf, prismed, text_web, formatted_justering,
                                    formatted_pristotal, text_ank, text_bed, text_free)
    st.markdown('engelsk email er sendt')
elif Sprog == "D" and booking_submitted:
    send_german_confirmation_email(to_addr, confirmation_password, name, num_rooms, num_guests, booking_number,
                                   checkin_date, checkout_date, text_bf, prismed, text_web, formatted_justering,
                                   formatted_pristotal, text_ank, text_bed, text_free)
    st.markdown('tysk email er sendt')
else:
    st.markdown('mail er ikke sendt ')