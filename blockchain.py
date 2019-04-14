#Initalize empty blockchain list
gensis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = []
open_transactions = []
owner = 'Jabari'

def last_bc_value():
    """Returns last value of blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_tx(recipent, sender=owner, amount=1.0):
    """append a new value and last value to blockchain"""
    transaction = {
      'sender': sender, 
      'recipent': recipent, 
      'amount': amount,
                }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    block = {
       'previous_hash': 123,
       'index': len(blockchain)
       'transactions': open_transactions
            }
    blockchain.append(block)
    

def get_trans_value():
    """"Returns transaction amount from user input as a float"""
    #Get user input and transform it from string to a float and store it
    tx_recipent = input('Enter the recipent of transaction:')
    tx_amount = float(input('Your transaction amount: '))
    return (tx_recipent, tx_amount)

def get_user_choice():
    """Get user choice and return it"""
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    # Output blockchain list to console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)

def verify_chain():
    block_index = 0
    is_valid = True 
    for block in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
                is_valid = True
        else: 
            is_valid = False
            break
        block_index += 1
    return is_valid

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_trans_value()
        recipent, amount = tx_data
        #add transaction amount to the blockchain
        add_tx(recipent, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        #print the blocks of the chain
        print_blockchain_elements()
    elif user_choice == 'h':
        #make sure cant hack blockchain if its empty1
        if len(blockchain) >=1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False 
    else:
        print('Input invalid, pick value from list')
    if not verify_chain():
        print('Invalid Blockchain')
        break 
else:
    print('User done!')


print('done!')