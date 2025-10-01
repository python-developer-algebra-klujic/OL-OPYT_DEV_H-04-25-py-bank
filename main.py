#region IMPORTS
import os
from typing import Dict

#endregion


#region INIT DATA
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
    'bank_account': bank_account
}

#endregion


#region FUNCTIONS
def wait_for_user():
    input('Za nastavak pritisnite tipku ENTER! ')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def logout_screen():
    print('Pozdrav')


def get_id(enity: Dict) -> int:
    return enity['id']


def company_has_account():
    if company['bank_account'] == {}:
        return False
    else:
        return True


def main_menu() -> int:
    clear_screen()
    print()
    print('*'*90)
    # header()
    print()
    print('1. Prikaz detalja racuna')
    print('0. Izlaz')
    print()
    print('*'*90)
    print()
    # TODO napraviti provjeru je li korisnik unio brojku iz izbornika
    return int(input('Upisite broj ispred akcije koju zelite pokrenuti: '))


def display_account_details():
    pass


def main():
    # Provjera ima li firma otvoren racun.
    if company_has_account():
        menu_item = main_menu()

        if menu_item == 0:
            return
        elif menu_item == 1:
            display_account_details()
    else:
        print('pokreni funkciju za otvaranje accounta ')
        # create_bank_account()
        wait_for_user()


#endregion


#region MAIN PROGRAM
if __name__ == '__main__':
    # ucitavanje pocetnih vrijednosti iz datoteka load_init_data()
    main()
#endregion


#region END PROGRAM
clear_screen()
logout_screen()
wait_for_user()
#endregion
