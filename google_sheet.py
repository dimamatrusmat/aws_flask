import gspread
from oauth2client.service_account import ServiceAccountCredentials


def insert_in_google(name, number, comment):

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    json_keyfile = 'keys/key1.json'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key('1yzE1vdmTtyWvUoZI6tBxhzt49O9jSlZBr9qKJ7kfcu8').sheet1

    new_row = [name, number, comment]

    sheet.append_row(new_row)


if __name__ == '__main__':
    insert_in_google('Александров Александр Александрович', '+7932951231', 'Хотет куть ноутбук')