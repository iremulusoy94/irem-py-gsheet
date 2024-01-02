import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
# import warnings


# warnings.filterwarnings('ignore')


def main():
    # key = SAC.from_json_keyfile_name('credentials (2).json')
    key = {
        "type": "service_account",
        "project_id": "irem-python",
        "private_key_id": "5675f183dcaab70ef5fdf9e45df1c2fc962b4978",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDG1hhNevdOqsU/\njCRcVTwARPh1wUinhjYmQzksXT1uKCBd8CpOOOXlbCeGyWKEk9NILqEr2WJacpy6\nNq9nlUBkn8yrO43K5Pi/OA9HDYGBU82jKhU8hS+VIyqDM94qsCf8nQBx6ANBrVPe\nFqPbZ/nLB6LSfEIWW4AmOyWN1kLPE+m0GRtOz1MxsRINOsh6FY4DyJCQmocGDCHO\n0Fr15F3QeiE/uAwVKVGfw9eT2M9dNrodUU/LBgq5eK2ypXvoEVKf4KFpbxT2jXyW\nXq3xeiolK1Jn/wPqhvbq9aIoJ08k99GxUXHKrzOFA/rux++hK3ntOroY/GCls8E3\nxwePB8C9AgMBAAECggEAIU7rGkufkxeLXGZbDvaeSwNCxeMfiySx/H3lXXevGz1w\nkpvxUlI4vNJ92pfwv3nN+nkJOcG8Np+dfpo7jvQTKegVDpg23Aa4XrwC3ym1iJcj\nyxH5Jb6/5lFSRVFShb8lq60XTn2J0h45fuo2/8GuuCKq1WzIW1tvn7fnxhde8LY/\nJYNVrhNzKI7w5HaCCWqYyNKtO8gxZU6fpwMGmxLrdusHZtarf07GnA7WAPmNbVR/\nYsGrHOTdnBt1lJtJtdVZeZfRYISsA0Qwo+i4f0Qaa2Xtk71JIwGFx7FJi8Y93B5J\nBa4o2n9s0A2wcmg6J6FJ+blXhhVxpt9BH1Xyh+SkJwKBgQDlvQvQ4w55DPklddEV\nO+ABYVvm03oIR/9fyRnXyurKQCgWmcGCMHR2+G09Dn2tFM1m6z+H63EN78srHrT+\nIm+HE3/zxFOPUYL2vTpnrod6ZQvVnrUkcU4uHZ/fVw/IVfKAK2IFln9ig+ukFE2c\nMDLxYfJa+4b+cxUy6MiKARQdNwKBgQDdkL5IppsPMT/t6UMwo5IbTzPMz3rrWO33\njtf+pcq0qvkz+6r0yPaFOCJzZbA8gcyt4t4ZSatKlAtHvoiK5bpvdDyDJrKlsne8\nfgpSyKQibgvOsBultRCExw+RPZjP0lEid7fvnEjsSYWM8B/0VEpmx2PPuIygXl3e\n/OCHj9ArqwKBgGhh8clyMPQ9OcKUenBMaSYXZ1tEgPDcTaLmy3ApyW4lolFKgQq3\nG2Om0nNobx/CEOWPQ6ltB0wOxOANrqy9VrEn4f4PGOxIW9nh9nR/bxzkZnEkECfD\nt4LqgOZIN2qN6oXjsEDbtXs8d0dw1iZ+G9di6mv+VsKr5VjhPaS+grYXAoGBALeV\nHPVZhpU5+3yHkHKWtZMHNyZ2q6ShlNtQcku+14yHNeEKoAYfFZQghPsUwMgBzLQv\njFNrpRAwRoB1sPFVk/qRVypcQB3nGCsITEl3kfgtMn9ZkC7nLf62aYGwhhN8clma\n1L8mwY13Bb9Xn0J1LQioIV2Vzn96cVE4OlpYoOXtAoGBAIlnfbkRIJQDfNRV2Ch4\nnlMuiuO4eivzlp3IjM8aMwg792fVqpRfwXPR4BtK9rVIdy8xOwKnPUpV7ku1X3Ca\ns34U6i/5mJRh7AuBO3jWBasU23EeB6Z4HQu7cPslH+eQVy/5eVm0M8FLXg18b5An\n8aBpwgTKlYfOs+TTECzovC7c\n-----END PRIVATE KEY-----\n",
        "client_email": "irem-gsheet@irem-python.iam.gserviceaccount.com",
        "client_id": "104113034408280920324",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/irem-gsheet%40irem-python.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }

    client = gspread.service_account_from_dict(key)
    ss = client.open('Inventory Mgmt')
    ws_stock = ss.worksheet('stock')
    ws_txn = ss.worksheet('txn')

    stock_sku = ws_stock.col_values(1)
    stock_qty = ws_stock.col_values(2)
    stock_price = ws_stock.col_values(3)

    print('   Enter Transaction Details\n'
          '=================================')

    txn = input('>>   Enter Txn Type-> (B: Buy || S: Sale):  ').lower()
    if txn == 'b':
        txn = 'Buy'
    elif txn == 's':
        txn = 'Sale'
    elif txn == 'p':
        txn = 'Produced'

    sku = input('>>   Enter SKU:  ')

    # check if SKU is in stock for sale
    if txn == 'Sale':
        if sku not in stock_sku:
            print('This item is out of stock!!!')
            exit()
        else:
            n = stock_sku.index(sku)
            available_qty = float(stock_qty[n])
            if available_qty == 0:
                print('This item is out of stock!!!')
                exit()
            print(f'    Available qty for {sku}: {available_qty}')

    qty = float(input('>>   Enter Quantity:  '))
    price = float(input('>>   Enter Price:  '))
    txn_list = [sku, txn, qty, price, qty*price]
    ws_txn.append_row(txn_list)
    update_stock_list(ws_stock, stock_sku, stock_qty, stock_price, txn_list)

    print('Transaction Successfully updated!\n'
          '=================================\n'
          '                                 ')


def update_stock_list(ws_stock, stock_sku, stock_qty, stock_price, txn_list):
    sku = txn_list[0]
    txn = txn_list[1]
    qty = txn_list[2]
    price = txn_list[3]
    if txn == 'Buy':
        if sku in stock_sku:
            n = stock_sku.index(sku)
            old_qty = float(stock_qty[n])
            new_qty = old_qty + qty

            old_price = float(stock_price[n])
            new_price = round((old_qty * old_price + qty*price)/new_qty, 2)
            new_amount = new_price * new_qty
            txn_list = [sku, new_qty, new_price, new_amount]
            rg = 'A' + str(n + 1) + ':D' + str(n + 1)
            ws_stock.update(rg, [txn_list])
        else:
            txn_list.pop(1)
            ws_stock.append_row(txn_list)
    else:
        n = stock_sku.index(sku)
        old_qty = float(stock_qty[n])
        new_qty = old_qty - qty
        stock_price_x = stock_price[n].replace(',', '.')
        new_amount = float(stock_price_x) * new_qty
        txn_list = [sku, new_qty, price, new_amount]
        rg = 'A' + str(n + 1) + ':D' + str(n + 1)
        ws_stock.update(rg, [txn_list])


if __name__ == "__main__":
    while True:
        main()

