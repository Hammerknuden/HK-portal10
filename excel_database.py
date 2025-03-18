import pandas as pd
from pathlib import Path
import streamlit


def add_data(year, book_data, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng, procent,
             num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast, pristotal, known,
             excel_path='2024 output.xlsx'):

    book_data = {'book nr': [booking_number], 'navn': [name], 'Checkin': [checkin_date],
                 'checkout': [checkout_date], 'booking dato': [now], 'nation': [nationalitet], 'web': [web],
                 'ankomst': '', 'bed': [seng], 'rabat': [procent], 'antal værelser': [num_rooms],
                 'nr gæst': [num_guests], 'Email': [email_address], 'telefon': [telefon], 'Spouse': [spouse],
                 'enkelt': [single_room], 'morgenmad': [breakfast], 'pris ialt': [pristotal], 'known': [known]}

    df1 = pd.DataFrame(book_data)
    print(df1)
    rek = int(booking_number)
    print(rek)
    with pd.ExcelWriter(excel_path, mode='a', if_sheet_exists="overlay") as writer:
        pd.DataFrame(book_data).to_excel(writer, sheet_name='book', startrow=rek, startcol=0, index=False, header=False)
        book_data = {'book nr': [booking_number], 'navn': [name], 'Checkin': [checkin_date],
                     'checkout': [checkout_date], 'booking dato': [now], 'nation': [nationalitet], 'web': [web],
                     'ankomst': '', 'bed': [seng], 'rabat': [procent], 'antal værelser': [num_rooms],
                     'nr gæst': [num_guests], 'Email': [email_address], 'telefon': [telefon], 'Spouse': [spouse],
                     'enkelt': [single_room], 'morgenmad': [breakfast], 'pris ialt': [pristotal], 'known': [known]}

        print(" data sendt to excel")
#if year == '2025':

#    def add_data(book_data, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng, rabat,
#                 num_rooms, num_guests, email_address, telefon, single_room, breakfast, pristotal, known,
#                 excel_path='2025output.xlsx'):

#        book_data = {'book nr': [booking_number], 'navn': [name], 'Checkin': [checkin_date],
#                     'checkout': [checkout_date], 'booking dato': [now], 'nation': [nationalitet], 'web': [web],
#                     'ankomst': '', 'bed': [seng], 'rabat': [rabat], 'antal værelser': [num_rooms],
#                     'nr gæst': [num_guests], 'Email': [email_address], 'telefon': [telefon], 'Spouse': '',
#                     'enkelt': [single_room], 'morgenmad': [breakfast], 'pris ialt': [pristotal], 'known': [known]}

#        df1 = pd.DataFrame(book_data)
#        print(df1)
#        rek = int(booking_number)
#        print(rek)
#        with pd.ExcelWriter(excel_path, mode='a', if_sheet_exists="overlay") as writer:
#            pd.DataFrame(book_data).to_excel(writer, sheet_name='book', startrow=rek, startcol=0, index=False, header=False)
#            book_data = {'book nr': [booking_number], 'navn': [name], 'Checkin': [checkin_date],
#                         'checkout': [checkout_date], 'booking dato': [now], 'nation': [nationalitet], 'web': [web],
#                         'ankomst': '', 'bed': [seng], 'rabat': [rabat], 'antal værelser': [num_rooms],
#                         'nr gæst': [num_guests], 'Email': [email_address], 'telefon': [telefon], 'Spouse': '',
#                         'enkelt': [single_room], 'morgenmad': [breakfast], 'pris ialt': [pristotal], 'known': [known]}

#        print(" 2025 data sendt to excel")


