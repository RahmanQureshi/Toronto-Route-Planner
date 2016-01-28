class AddressPoints:
    
    def __init__(self):
        import pickle
        self.ap_map = pickle.load(open('addresspoints.p'))
        self.replaceMap = {
            'road':'rd',
            'street':'st',
            'lane':'ln',
            'saint':'st',
            'avenue':'ave',
            'boulevard':'blvd',
            'crescent':'cres',
            'court':'crt',
            'circle':'crcl',
            'west' : 'w',
            'east': 'e',
            'north': 'n',
            'south':'s'
        }
        
    def translate(self, address):
        """Attempt to format address corresponding to address point file convention.
        """
        import string
        address = address.lower()
        address = ''.join([letter for letter in address if letter not in set(string.punctuation)])
        address = ' '.join([word if word not in self.replaceMap else self.replaceMap[word] for word in address.split(' ')])
        return address
        
    def get(self, address):
        """Return record of address point of address.
        
            Arguments:
            address - string - human readable address
        """
        return self.ap_map[self.translate(address)]