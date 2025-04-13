import pandas as pd
from pathlib import Path
import streamlit


def add_data(year, book_data, booking_number, name, checkin_date, checkout_date, now, nationalitet, web, seng, procent,
             num_rooms, num_guests, email_address, telefon, spouse, single_room, breakfast, pristotal, known,
             excel_path='url'):

    book_data = {'book nr': [booking_number], 'navn': [name], 'Checkin': [checkin_date],
                 'checkout': [checkout_date], 'booking dato': [now], 'nation': [nationalitet], 'web': [web],
                 'ankomst': '', 'bed': [seng], 'rabat': [procent], 'antal værelser': [num_rooms],
                 'nr gæst': [num_guests], 'Email': [email_address], 'telefon': [telefon], 'Spouse': [spouse],
                 'enkelt': [single_room], 'morgenmad': [breakfast], 'pris ialt': [pristotal], 'known': [known]}

    #file_id = '1QGGa7LG9OfryfefhJ4QohGYxqjNJ-fPg'
    #url = f'https://drive.google.com/uc?id={file_id}'
    url = 'https://my.microsoftpersonalcontent.com/personal/3be7f4b38f07ed41/_layouts/15/download.aspx?UniqueId=8f07ed41-f4b3-20e7-803b-347a00000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiI4MTRkMjJlYi05ZmY2LTRmZWMtYjcxNi04M2VkNWYxODdiNWUiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDQ1NjcxNTkifQ.FFKEiUyAVvvwNfcY-XURV5o9txNuDgDlkOqPCoOs9hxXaz6o8Xdl5JCuNqip1DsYf1PsL_eppOQaiMs8yAb19B-913qbl_Wm6WhBWSDg_ABTsKtoOjtZk2BobGKAMOe5YGKBVx2XRg9yYECK78nF6SL-BdlLvwDQ9h1-lk2xzHYjkuvQz-RUbDVP98oGUEulb0HyDoXoNHKXIKPWaDqwaO3Z1nX2ArxeJUsrYpCpyOVO9DgfZmZbXpN1ISaCftId69f-sL8p3VeBPp60q14wR6RSLRTCR6OogS6_n5FaT_i7WEWROhZZGQCQu8b-mj49cj7oK433D799xHEWQGZMj9aAtmgOlnNmYPd2DTR4vsJHqwRdku9GZHMxh6E5gMMnX1nDq9TiNRRgXxY_PfCkuQ.bfdtvAsY4-xAmvqfIV-uZJK8wsuXFS4ogvhuQHXceS4&ApiVersion=2.0&AVOverride=1'
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


