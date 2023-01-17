from tabulate import tabulate
from datetime import datetime

#Transaction object construcor
class Transaction:
    '''
    A class to represent a cashier transaction

    ....

    Attributes
    ----------
    item : dict
        a dictionary that has item name as key,
         and has value of list that contain item quantity and item price.

    discount : dict
        a dictionary that store discount value,
         and the key represent condition that should be satishfied
         to get the discount. 
         "a" when total pay is between Rp200.000,00 and Rp300.000,00
         "b" when total pay is between Rp300.000,00 and Rp500.000,00 
         "c" when total pay is above Rp500.000,00

    datetime 
        Describe transaction time.

    Methods
    -------
    add_item(item_name, item_qty, item_price)
        Add name, quantity, and price of item into order list.
    
    update_item_name(item_name,update_item_name)
        Change the name of an item in order list.

    update_item_qty(item_name,update_item_qty)
        Change quantity of an item in order list.

    update_item_price(item_name,update_item_price)
        Change price of an item in order list.

    delete_item(item_name)
        Delete an item(name,quantity,price data) in the order list.

    reset_transcation()
        Clear all data in order list.

    check_order()
        Show the order list

    total_price()
        Show the total amount of the transaction.
    '''
    def __init__(self):
        """
        Constructs all the necessary attributes for the transaction object.

        Parameters
        ----------
            None
        """
        self.item={}
        self.discount={'a':0.05,'b':0.08,'c':0.1}
        self.time=datetime.now()
        
    #Function for add item in order list
    def add_item(self, item_name:str, item_qty:int, item_price:int) -> dict:
        '''
        Add key-value pair to item dictonary with item_name as a key,
         and list that contain item_qty and item_price as value.

        Parameters
        ----------
            item_name: str 
                The name of item that is ordered
            item_qty: int 
                The quantity of item that is ordered
            item_price: int 
                The price of the item that is ordered

        Return
        ------
            item : dict
                Dictionary with this format 
                 (item_name:[item_qty, item_price]).
        '''
        try:
            item_name=item_name.lower().replace("_"," ").strip()
            item_qty=int(item_qty)
            item_price=int(item_price)
            self.item[item_name]=[]
            self.item[item_name].append(item_qty)
            self.item[item_name].append(item_price)
            print(f'{item_name} has been added to order list')
            return self.item
        except (ValueError,AttributionError):
            print('Wrong in input arguments. Please try again!')
    
    #Function to update the item_name
    def update_item_name(self,item_name,update_item_name):
        '''
        Change a key of item dictionnary without change its value.

        Parameters
        ----------
            item_name: str
                The selected key that want to changed.
            update_item_name: str
                The new key that replace selected key.
        
        Return
        ------
            item: dict
                Item dictionary with updated key-value pair 
                 (update_new_item:[item_qty,item_price]).
        '''
        try:
            update_item_name=update_item_name.lower().strip()
            self.item[update_item_name]=self.item.pop(item_name)
            print('item name has been updated successfully')
            return self.item
        except KeyError:
            print('The item that you want to change is not available')
        except AttributeError:
            print('You assigned wrong type of input. Please try again!')
    
    #Function to update the item_qty
    def update_item_qty(self,item_name,update_item_qty):
        '''
        Only change value[0] (defined as item_qty) of a selected key-value pair,
         and remain key and value[1] same.

        Parameters
        ----------
            item_name: str
                The selected key that has value[0] that is want to changed.
            update_item_qty: int
                The new quantity that want to assigned to value[0] of a selected
                 key-value pair.
        
        Return
        ------
            item: dict
                Item dictionary with updated key-value pair 
                 (item_name:[update_item_qty,item_price]).
        '''
        try:
            update_item_qty=int(update_item_qty/1)
            self.item[item_name][0]=update_item_qty
            print(f'Quantity of {item_name} has successfully updated')
            return self.item
        except TypeError:
             print('Wrong in input arguments. Please try again!')
        except KeyError:
             print('The item that you want to change is not available')
    
    #Function to update the item_price
    def update_item_price(self,item_name,update_item_price):
        '''
        Only change value[1] (defined as item_price) of a selected key-value pair,
         and remain key and value[0] same.

        Parameters
        ----------
            item_name: str
                The selected key that has value[1] that is want to changed.
            update_item_price: int
                The new price that want to assigned to value[1] of a selected
                 key-value pair.
        
        Return
        ------
            item: dict
                Item dictionary with updated key-value pair 
                 (item_name:[tem_qty,update_item_price]).
        '''
        try:
            update_item_price=int(update_item_price/1)
            self.item[item_name][1]=update_item_price
            print(f'Price of {item_name} has successfully updated')
            return self.item
        except TypeError:
             print('Wrong in input arguments. Please try again!')
        except KeyError:
             print('The item that you want to change is not available')
    
    #Function for delete selected item in order list
    def delete_item(self,item_name):
        '''
        Remove a key-value pair in item dictonary.

        Parameters
        ----------
            item_name: str 
                The key of key-value pair that want to be removed
        Return
        ------
            item : dict
                Dictionary that has no selected key-value pair.
        '''
        try:
            del self.item[item_name]
            print(f'{item_name} has been deleted')
            return self.item
        except KeyError:
             print('The item that you want to delete is not available')
    
    #Function to delete all item in order list
    def reset_transaction(self):
        '''
        Remove all key-value pair in item dictonary.

        Parameters
        ----------
            None

        Return
        ------
            item : dict
                Empty dictionary.
        '''
        message='Are you sure want to reset the transaction? (yes/no)'
        confirm=input(message).lower().strip()
        if confirm == 'yes':
            self.item={}
            print('All item has been deleted')
            return self.item
        else:
            print('Reset transaction is cancelled')
    
    #Function to show order list
    def check_order(self):
        '''
        Show table of order list.

        Parameters
        ----------
            None

        Return
        ------
            Return a Tabulate table of order list.
             This table contain name, quantitiy,
             price, and total price of an item.
        '''
        try:
            for a in self.item.keys():
                if bool(a):
                    for b in self.item[a]:
                        if bool(b):
                            pesan='Your order list is ready'
                            pass
                        else: 
                            pesan=(f'The {a} has no item/qty data, please update')
                            break
                else:
                    pesan=("Your order list is empty")
                    break
            print(pesan)
        except:
            print('Your order list is empty')
        headers=['Nama Item','Jumlah Item','Harga Item','Total Harga']
        tables=[]
        for k in self.item.keys():
            table=[k,self.item[k][0],self.item[k][1],(self.item[k][0] * self.item[k][1])]
            tables.append(table)
        tabulated=tabulate(tables,headers=headers,showindex='always')
        print(tabulated)  

    #Function to show the total amount of a transaction
    def total_price(self):
        '''
        Show total amount of a transaction after
         adjusted by discount if satishfied the condition.

        Parameters
        ----------
            None

        Return
        ------
            total_price : int
                Amount of a transaction after adjusted
                 by the discount. The condition is follow
                 the discount dictionary.
            
            Return a Tabulate table of order list.
             This table contain name, quantitiy,
             price, and total price of an item.
        '''
        total_pay = 0
        cutprice=0
        for k in self.item.keys():
            pay=self.item[k][0]*self.item[k][1]
            total_pay+=pay
        if total_pay in range(200000,300001):
            cutprice=total_pay * self.discount['a']
            total_pay=int(total_pay - cutprice)
            return total_pay
        elif total_pay in range(300000,500001):  
            cutprice=total_pay * self.discount['b']
            total_pay=int(total_pay - cutprice)
            return total_pay 
        elif total_pay >= 500000:  
            cutprice=total_pay * self.discount['c']
            total_pay=int(total_pay - cutprice)
            return total_pay
        else :
            total_pay=int(total_pay) 
        print('Order list \n')
        self.check_order() 
        print('\n')
        print(f'You get discount Rp{cutprice}, your bill is Rp{total_pay}')
        print('\n')
        print('Thank you for your transaction')

