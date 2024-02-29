from fast_bitrix24 import Bitrix
import json


def get_webhook():
    with open('keys/bitrix.json') as f:
        d = json.load(f)
        webhook = d['key']

        return webhook


def get_deal_inform(id):
    b = Bitrix(get_webhook())

    deal = b.get_by_ID(
        'crm.deal.get',
        {id: id}
    )
    contact_id = deal[str(id)]['CONTACT_ID']
    comment = deal[str(id)]['COMMENTS'] if deal[str(id)]['COMMENTS'] else ''

    return contact_id, comment


def get_contact_inform(contact_id):
    b = Bitrix(get_webhook())

    contact = b.call(
        'crm.contact.get',
        {'ID': contact_id}
    )

    name = contact['NAME'] if contact['NAME'] else ''
    last_name = contact['LAST_NAME'] if contact['LAST_NAME'] else ''
    second_name = contact['SECOND_NAME'] if contact['SECOND_NAME'] else ''
    phones = contact['PHONE'] if contact['PHONE'] else ''

    fio = f"{last_name} {name} {second_name}"

    phone = ''
    for ph in phones:
        if ph['VALUE_TYPE'] == 'WORK':
            phone = ph['VALUE']

    return fio, phone

