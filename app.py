from flask import Flask, request, render_template
from bd import get_all_deal, create_entry
from bitrix import get_deal_inform, get_contact_inform
from google_sheet import insert_in_google
import logging
app = Flask(__name__)

webhook = ""


def write_deal_bd(id):

    contact_id, comment = get_deal_inform(id)

    if contact_id:
        fio, phone = get_contact_inform(contact_id)

        if fio:
            try:
                create_entry(fio, phone, comment)
            except Exception as e:
                logging.error('Ошибка записи в бд' + str(e))
            try:
                insert_in_google(fio, phone, comment)
            except Exception as e:
                logging.error('Ошибка записи в гугл таблицы' + str(e))


@app.route('/', methods=['POST'])
def result():
    data = request.form

    data_dict = request.form.to_dict()
    write_deal_bd(data_dict['data[FIELDS][ID]'])

    return 'OK'


@app.route('/', methods=['GET'])
def get_result():
    return 'Тестовое задание'


@app.route('/deals/')
def show_deals():
    deals = get_all_deal()
    return render_template('deals.html', deals=deals)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
