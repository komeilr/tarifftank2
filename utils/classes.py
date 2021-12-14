from django.db.models.query import QuerySet
from django.db.models import Model
import tarifftank.models
from django.db.models import Q


class TariffCA:
    """Structure class to hold all hs codes in a heading"""
    def __init__(self, tariff=None, year='2022'):
        if len(tariff) != 4:
            raise ValueError("Length of heading must be 4 digits")  
              
        self.tariff:str = tariff
        self.set_tariff_table(year)             
        #self.queryset:QuerySet = self._query_tariff()
        
    def set_tariff_table(self, year:str) -> Model:
        """
        Sets db model that represents the canadian tariff by year
        :params: year: str
        :return: django.db.model
        """
        self.year = year
        self.tariff_table = vars(tarifftank.models)[f"CA{self.year}"]
        self.queryset = self._query_tariff()     
        
    def _query_tariff(self) -> QuerySet:
        """returns all HS codes contained in a heading"""
        query = self.tariff_table.objects.filter(
            Q(tariff__icontains=self.tariff) |            
            Q(tariff=f'{self.tariff[:2]}.{self.tariff[2:]}')    # tariff string becomes xx.xx
        ).order_by('tariff')
        
        if not query:
            raise ValueError("Invalid HS heading")
        
        return query
    
    def _get_dashes(self, tariff:str) -> int:
        
        digits = tariff.replace('.', '')[4:][::-1] # remove dots, drop first four digits and reverse        
        dashcount = len(digits)        
        for digit in digits:
            if digit == '0':
                dashcount -= 1
            else:
                break
        return dashcount
        # return len(t[4:]) - min(1, t[-2:].count('0'))
    
    def _base_dict(self, q:Model, level:int) -> dict:
        """ returns basic dictionary structure for Heading type
        input: 3 element list containing hscode, description and unit of measure"""


        return {
            'tariff': q.tariff,            
            'description': q.desc1,
            'is_heading':level < 1,
            'year':self.year,
            'uom': q.uom,
            'level': level,
            'is_link':len(q.tariff) == 13,
            'is_general_description':len(q.tariff) in [6, 9, 12],
            'dashes':self._get_dashes(q.tariff)
        }

    
    def _key_chain(self, tariff_string:str):
        """generates a list of strings signifying heading, subheading and tariff levels of a tariff
        input: str representing tariff gen_keychain('3926.90.99.90')
        \>>> ['3926', '3926.90', '3926.90.99']"""

        return [tariff_string[:i] for i in range(4, 13, 3)]
    
    def _get_dict_to_insert(self, hs_dict: dict, chain: list, level = 0) -> dict:
        """input: dictionary, list
        recursive, returns dictionary if key in chain"""

        if not chain:
            return hs_dict

        for _key in chain:
            if _key in hs_dict:
                hs_dict, level = self._get_dict_to_insert(hs_dict[_key], chain, level=level + 1)
                break
        return hs_dict, level
    
    def gen_tariff_dict(self):
        """generates dictionary structure of heading"""

        tariff_dict = {}
        level = 0
        heading = self.tariff
        tariff_dict[heading] = self._base_dict(self.queryset[0], level)
        # print(f"DEBUG: {tariff_dict}")

        for q in self.queryset[1:]:
            tariff = q.tariff
            curr_dict, level = self._get_dict_to_insert(tariff_dict, self._key_chain(tariff))
            curr_dict[tariff] = self._base_dict(q, level)

        return tariff_dict
    
    def get_query_dict(self):
        base_dict = {
            '39.26': {
                'description': None
            }
        }
        
    def book_view_terminal(self, _dict=None):
        """ prints to terminal book view format of heading recursively"""
        d = _dict or self.gen_tariff_dict()
        for k, v in d.items():            
            if isinstance(v, dict):
                if len(k.replace('.', '')) % 2 != 0:
                    #print("\t" * v['level'] + "-" * (len(k) - 5) + f" {v['description']}")
                    print("\t" * v['level'] + "-" * v['dashes'] + f" {v['description']}")
                else:
                    #print("\t" * v['level'], k, "-" * (len(k) - 8), v['description'])
                    print("\t" * v['level'], k, "-" * v['dashes'], v['description'])
                self.book_view_terminal(v)
    
    def console_print(self):
        d = '\t'
        print(f"Tariff\t\tDesc")
        for q in self.queryset:
            print(f"{q.tariff}\t{d if len(q.tariff) < 8 else ''}{q.desc1}")
    
    def __str__(self):
        return f"<TARIFF {self.tariff}>"
    
    def __repr__(self):
        return f"<TARIFF {self.tariff}>"