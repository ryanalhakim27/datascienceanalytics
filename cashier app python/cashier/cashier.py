''' This module providing class represent a transaction in a cashier system.

This module using datetime and tabulate library.
Datetime is used for show the transaction time.
Tabulate is used for make tabulation of order list. 
So please install the library before you run this module!.
 
'''
#Import necessary library
from datetime import datetime
from tabulate import tabulate

#Transaction object construcor
class Transaction:
    '''
    A class to represent a cashier transaction

    Examples:
        >>> t1= Transaction()

    Attributes:
        item (dict): A dictionary that has item name as key,
            and has value of list that contain item quantity and item price.

        discount (dict): A dictionary that store discount value,
            and the key represent condition that should be 
            satishfied to get the discount.
            <br>"a" when total pay is between Rp200.000,00 and Rp300.000,00.
            <br>"b" when total pay is between Rp300.000,00 and Rp500.000,00.
            <br>"c" when total pay is above Rp500.000,00.

        datetime(str): Describe transaction time.
    '''
    def __init__(self):
        """ Inits all the necessary attributes for the transaction object."""
        self.item={}
        self.discount={'a':0.05,'b':0.08,'c':0.1}
        self.time=datetime.now()

    #Function for add item in order list
    def add_item(self, item_name:str, item_qty:int, item_price:int) -> dict:
        '''Add key-value pair to item dictonary with item_name as a key,
            and list that contain item_qty and item_price as value.

        Examples:
            >>> t1 = Transaction()
            >>> t1.add_item('Ayam Goreng', 2, 20000)
            ayam goreng has been added to order list
            {'ayam goreng': [2, 20000]}
            >>> t1.add_item('Pasta Gigi', 3, 15000)
            pasta gigi has been added to order list
            {'ayam goreng': [2, 20000], 'pasta gigi': [3, 15000]}

        Args:
            item_name (str): The name of item that is ordered.
            item_qty (int): The quantity of item that is ordered.
            item_price (int): The price of the item that is ordered.

        Returns:
            item (dict): Dictionary with this format
                (item_name:[item_qty, item_price]).
                Note that item name was formatted to lower case and strip.
        '''
        try:
            item_name=item_name.lower().replace('_',' ').strip()
            item_qty=int(item_qty)
            item_price=int(item_price)
            self.item[item_name]=[]
            self.item[item_name].append(item_qty)
            self.item[item_name].append(item_price)
            print(f'{item_name} has been added to order list')
            return self.item
        except (ValueError, AttributeError):
            print('Wrong in input arguments. Please try again!')

    #Function to update the item_name
    def update_item_name(self,item_name,update_item_name):
        '''Change a key of item dictionnary without change its value.

        Examples:
            >>> t1 = Transaction()
            >>> t1.add_item('Ayam Goreng', 2, 20000)
            ayam goreng has been added to order list
            {'ayam goreng': [2, 20000]}
            >>> t1.update_item_name('ayam goreng','ayam bakar')
            item name has been updated successfully
            {'ayam bakar': [2, 20000]}

        Args:
            item_name (str): The selected key that want to changed.
            update_item_name (str): The new key that replace selected key.

        Returns:
            item (dict): Item dictionary with updated key-value pair
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
        '''Only change value[0] (defined as item_qty) of a selected key-value pair,
            and remain key and value[1] same.

        Examples:
            >>> t1 = Transaction()
            >>> t1.add_item('Ayam Goreng', 2, 20000)
            ayam goreng has been added to order list
            {'ayam goreng': [2, 20000]}
            >>> t1.update_item_qty('ayam goreng',5)
            Quantity of ayam goreng has successfully updated
            {'ayam goreng': [5, 20000]}

        Args:
            item_name (str): The selected key that has value[0] 
                that is want to changed.
            update_item_qty (int): The new quantity that want to assigned to 
                value[0] of a selected key-value pair.

        Returns:
            item (dict): Item dictionary with updated key-value pair
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
        '''Only change value[1] (defined as item_price) of 
            a selected key-value pair, and remain key and value[0] same.

        Examples:
            >>> t1 = Transaction()
            >>> t1.add_item('Ayam Goreng', 2, 20000)
            ayam goreng has been added to order list
            {'ayam goreng': [2, 20000]}
            >>> t1.update_item_price('ayam goreng',15000)
            Price of ayam goreng has successfully updated
            {'ayam goreng': [2, 15000]}

        Args:
            item_name (str): The selected key that has 
                value[1] that is want to changed.
            update_item_price (int): The new price that want to assigned to 
                value[1] of a selected key-value pair.

        Returns:
            item (dict): Item dictionary with updated key-value pair
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
        '''Remove a key-value pair in item dictonary.

        Examples:
            >>> t1 = Transaction()
            >>> t1.add_item('Ayam Goreng', 2, 20000)
            ayam goreng has been added to order list
            {'ayam goreng': [2, 20000]}
            >>> t1.add_item('Pasta Gigi', 3, 15000)
            pasta gigi has been added to order list
            {'ayam goreng': [2, 20000], 'pasta gigi': [3, 15000]}
            >>> t1.delete_item('pasta gigi')
            pasta gigi has been deleted
            {'ayam goreng': [2, 20000]}

        Args:
            item_name (str): The key of key-value pair that want to be removed.

        Returns
            item (dict): Dictionary that has no selected key-value pair.
        '''
        try:
            del self.item[item_name]
            print(f'{item_name} has been deleted')
            return self.item
        except KeyError:
            print('The item that you want to delete is not available')

    #Function to delete all item in order list
    def reset_transaction(self, param1=None):
        ''' Remove all key-value pair in item dictonary.

        Examples:
            >>> t1 = Transaction()
            >>> t1.add_item('Ayam Goreng', 2, 20000)
            ayam goreng has been added to order list
            {'ayam goreng': [2, 20000]}
            >>> t1.reset_transaction()
            All item has been deleted
            {}

            This method need confirmation yes or no. If the input was no
                reset_transaction is cancelled.

        Args:
            param1 (:obj:`str`, optional): The first parameter. 
                Defaults to None.

        Returns:
            item (dict): Empty dictionary.
        '''
        self.item={}
        print('All item has been deleted')
        print(self.item)

    #Function to show order list
    def check_order(self, param1=None):
        '''Show table of order list.

        Args:
            param1 (:obj:`str`, optional): The first parameter. 
                Defaults to None.

        Returns:
            tabulate_table (str): Return a Tabulate table of order list.
                This table contain name, quantitiy,
                price, and total price of an item.
        '''
        try:
            for a in self.item.keys():
                if bool(a):
                    for b in self.item[a]:
                        if bool(b):
                            pesan='Your order list is ready'
                        else:
                            pesan=f'The {a} has no item/qty data, please update'
                            break
                else:
                    pesan='Your order list is empty'
                    break
            print(pesan)
        except ValueError:
            print('Your order list is empty')
        headers=['Nama Item','Jumlah Item','Harga Item','Total Harga']
        tables=[]
        for k in self.item.keys():
            table=[k,self.item[k][0],self.item[k][1],(self.item[k][0] * self.item[k][1])]
            tables.append(table)
        tabulated=tabulate(tables,headers=headers,showindex='always')
        print(tabulated)

    #Function to show the total amount of a transaction
    def total_price(self, param1=None):
        '''Show total amount of a transaction after
         adjusted by discount if satishfied the condition.

        Args:
            param1 (:obj:`str`, optional): The second parameter. 
                Defaults to None.

        Returns:
            total_price (int): Amount of a transaction after adjusted
                 by the discount. The condition is follow
                 the discount dictionary.

            tabulate_table (str): Return a Tabulate table of order list.
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
