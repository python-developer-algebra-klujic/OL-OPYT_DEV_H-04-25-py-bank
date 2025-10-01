#region INIT DATA
from typing import Dict


bank = {
    'id': 1,
    'name': 'Lipa po lipa d.d.',
    'hq': {
        'street': 'Kratka ulica 5',
        'postal_code': '10290',
        'city': 'Zapresic',
        'country': 'Hrvatska'
    }
}

currency = {
    'id': 1,
    'name': 'Euro',
    'symbol': '€',
    'code': 'EUR'
}

transactions = []
'''
id; date_time; amout; currnecy; bank_account; transaction_type [withdrow, deposit]
'''

bank_account = {
    'id': 1,
    'IBAN': 'HR45875465481354654',
    'balance': 0.00,
    'opening_date': '2025-09-29',
    'bank': bank,
    'currency': currency,
    'transactions': transactions
}

company = {
    'id': 1,
    'name': 'ABC Software d.o.o.',
    'tax_id': '01234567890',
    'hq': {
        'street': 'Duga ulica 15',
        'postal_code': '10290',
        'city': 'Zapresic',
        'country': 'Hrvatska'
    },
    'email': 'info@abc-software.hr',
    # 'bank_account': bank_account
    'bank_account': {}
}

#endregion


# Prikaz detalja racuna
def transform_key(key: str) -> str:
    keys = key.split('_')
    if len(keys) == 1:
        return f'{keys[0].capitalize()}'
    else:
        title = ''
        for element in keys:
            title += f'{element.capitalize()} '
        return title


def display_entity_details(entity: Dict) -> None:
    # print(f'{"ID":<15} {bank_account['id']:<20}')
    # print(f'{"IBAN":<15} {bank_account['IBAN']:<20}')
    for key, value in entity.items():
        key = transform_key(key)
        if type(value) == dict:
            print()
            print(key)
            display_entity_details(value)
        elif type(value) == float:
            print(f'{key:<15} {value:>15.3f} EUR')
        else:
            print(f'{key:<15} {str(value):<20}')


display_entity_details(bank_account)
