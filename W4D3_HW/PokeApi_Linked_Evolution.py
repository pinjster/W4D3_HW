from requests import get
from Node import Node
from LinkedList import LinkedList

class PokEvolution():

    def __init__(self):
        self.api_call = 'https://pokeapi.co/api/v2/evolution-chain/'
        self.response = get(f'{self.api_call}{int(user_num)}/')
        self.data = self.response.json()
        self.chain = LinkedList(self.data['chain']['species']['name'])
        try: 
            self.data['chain']['evolves_to'][0]['species']['name']
            self.chain.add_node(self.data['chain']['evolves_to'][0]['species']['name'])
        except:
            pass
        try:  
            self.data['chain']['evolves_to'][0]['evolves_to'][0]['species']['name']
            self.chain.add_node(self.data['chain']['evolves_to'][0]['evolves_to'][0]['species']['name'])
        except:
            pass


while True:
    user_num = input('Enter Poke Evolution Chain No. (1-530): ')
    if user_num.isdigit():
        if int(user_num) in range(1,531):
            poke = PokEvolution()
            print(poke.chain)
        else:
            print('Error: wrong input')
    elif user_num.lower() == 'q' or user_num.lower() == 'quit':
        break
    else:
        print('Error: wrong input')
