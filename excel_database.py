import pandas as pd
from pathlib import Path
import streamlit
import openpyxl
from io import BytesIO

excel_buffer = BytesIO

#if year == '2026':

def add_data(year, book_data, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, ankomst, seng,
             procent, num_rooms, num_guests, email_address, telefon, spouse, single_room, BF, pristotal, known,
             comments, excel_output=None, sheet_name='book'):

    book_data = {'book nr': [booking_number], 'navn': [name], 'Checkin': [checkin_date],
                 'checkout': [checkout_date], 'booking dato': [now], 'nation': [nationalitet], 'web': [web],
                 'ankomst': {ankomst}, 'bed': [seng], 'rabat': [procent], 'antal værelser': [num_rooms],
                 'nr gæst': [num_guests], 'Email': [email_address], 'telefon': [telefon], 'Spouse': [spouse],
                 'enkelt': [single_room], 'morgenmad': [BF], 'pris ialt': [pristotal], 'known': [known], 'Comments':
                 [comments]}
    df1 = pd.DataFrame(book_data)
    print(df1)
    rek = int(booking_number)
    print(rek)
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        df1.to_excel(writer, sheet_name='book', index=False) #pd.DataFrame(book_data).to_excel(writer, sheet_name='book', startrow=rek, startcol=0, index=False, header=False)
        book_data = {'book nr': [booking_number], 'navn': [name], 'Checkin': [checkin_date],
                     'checkout': [checkout_date], 'booking dato': [now], 'nation': [nationalitet], 'web': [web],
                     'ankomst': {ankomst}, 'bed': [seng], 'rabat': [procent], 'antal værelser': [num_rooms],
                     'nr gæst': [num_guests], 'Email': [email_address], 'telefon': [telefon], 'Spouse': [spouse],
                     'enkelt': [single_room], 'morgenmad': [BF], 'pris ialt': [pristotal], 'known': [known]}

    print("data sendt to excel")




