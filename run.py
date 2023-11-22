import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
import warnings


warnings.filterwarnings('ignore')


def main():
    key = SAC.from_json_keyfile_name('GScredential.json')
    client = gspread.authorize(key)
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

