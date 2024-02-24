def display_invoice(username, amount, due_date):
    print(f'{username}')
    print(f'Your bill of ${amount:.2f} is due: {due_date}')

display_invoice('FXDS', 28.09, "01/01")