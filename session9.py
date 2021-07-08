from collections import namedtuple
from faker import Faker
import datetime
from datetime import date
from datetime import time
import operator
from decimal import Decimal
from decimal import getcontext
import decimal
import contextlib
import time
from collections import Counter
import math
from math import isclose
import random
from random  import uniform
from random import randint
fake = Faker()

def calculateage(birthDate: "date of birthof person") -> "Returns Age in years":
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

class Fprofile(namedtuple('Fprofile', ('name', 'sex', 'birthdate', 'blood_group', 'current_location'))):
    @classmethod
    def calculateage(cls, fprofile) -> "Returns Age in years":
        'This class method calculates age of given list of profile'
        birthDate = fprofile.birthdate
        today = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age

    @classmethod
    def aver_age(cls, fprofiles) -> 'This class method calculates average age of given list of profiles':
        'This class method calculates average age of given list of profiles'
        if not all(isinstance(fprofile, cls) for fprofile in fprofiles):
            raise ValueError('All items in sequence must be of type {}'.format(cls.__name__))
        return sum(cls.calculateage(fprofile) for fprofile in fprofiles) / len(fprofiles)

    @classmethod
    def max_age(cls, fprofiles) -> "Returns Max age of given list of profiles":
        'This class method calculates max age of given list of profiles'
        if not all(isinstance(fprofile, cls) for fprofile in fprofiles):
            raise ValueError('All items in sequence must be of type {}'.format(cls.__name__))
        return max(cls.calculateage(fprofile) for fprofile in fprofiles)

    @classmethod
    def mean_current_location(cls, fprofiles) -> "Returns Mean current Location of given list of profiles":
        "Returns Mean current Location of given list of profiles"
        if not all(isinstance(fprofile, cls) for fprofile in fprofiles):
            raise ValueError('All items in sequence must be of type {}'.format(cls.__name__))
        mean_lat = sum(fprofile.current_location[0] for fprofile in fprofiles) / len(fprofiles)
        mean_long = sum(fprofile.current_location[1] for fprofile in fprofiles) / len(fprofiles)
        return (mean_lat, mean_long)

    @classmethod
    def largest_blood_type(cls, fprofiles) -> "Returns Largest Blood Group of given list of profiles":
        'This class method returns largest blood group of given list of profiles'
        if not all(isinstance(fprofile, cls) for fprofile in fprofiles):
            raise ValueError('All items in sequence must be of type {}'.format(cls.__name__))
        Blood_group_count = Counter(fprofile.blood_group for fprofile in fprofiles)
        return max(Blood_group_count, key=Blood_group_count.get)

Fprofile.__doc__ = 'Profile of Employees/User'
Fprofile.name.__doc__ = 'Name of Employees/User '
Fprofile.sex.__doc__ = 'Sex of Employees/User'
Fprofile.birthdate.__doc__ = 'Date of birth of Employees/User'
Fprofile.blood_group.__doc__ = 'Blood group of Employees/User'
Fprofile.current_location.__doc__ = 'Current location of Employees/User'

def function_profile_creation(count: "Number of profile to be created using faker"):
    "Returns  profile stored in  named_tuple and dictionary in tupple and list respecitvely  for user defined count"
    LIST_tuple = []
    LIST_dict = []
    for n in range(count):
        x = fake.profile()
        # Tuple based
        LIST_tuple.append(Fprofile(x['name'], x['sex'], x['birthdate'], x['blood_group'], x['current_location']))
        # Dictionary based
        LIST_dict.append({'name': x['name'], 'sex': x['sex'], 'birthdate': x['birthdate'], 'blood_group': x['blood_group'],'current_location': x['current_location']})
    return tuple(LIST_tuple), LIST_dict

def function_profile_data_tuple_process(tuple: "tuple of Named tuple"):
    """
    This function returns following for given list of profiles stores in Namedtuple
    - Average age in given set of profiles
    - Age of oldest person in given set of profiles
    -mean location of  in given set of profiles
    -largest_blood_type  in given set of profiles
    """
    average_age = Fprofile.aver_age(tuple)
    oldest_person_age = Fprofile.max_age(tuple)
    mean_current_location = Fprofile.mean_current_location(tuple)
    largest_blood_type = Fprofile.largest_blood_type(tuple)
    return average_age, oldest_person_age, mean_current_location, largest_blood_type

def function_profile_data_dict_process(LIST_d: "List of dictionary"):
    """
    This function returns following for given list of profiles stores in Dictionary
    - Average age in given set of profiles
    - Age of oldest person in given set of profiles
    -mean location of  in given set of profiles
    -largest_blood_type  in given set of profiles
    """
    oldest_person_age_d = 0
    blood_group_count_d = {'O+': 0, 'B-': 0, 'AB+': 0, 'B+': 0, 'O-': 0, 'AB-': 0, 'A-': 0, 'A+': 0}
    average_age_d = 0
    mean_current_location_d = (0, 0)
    average_age_d = 0
    Num_profile = len(LIST_d)
    for n in range(Num_profile):
        ##Max age
        age = calculateage(LIST_d[n]['birthdate'])
        oldest_person_age_d = max(oldest_person_age_d, age)
        ##average age
        age = calculateage(LIST_d[n]['birthdate'])
        average_age_d = (average_age_d * n + age) / (n + 1)
        ##mean_current_location
        mean_current_location_d = Decimal(
            (mean_current_location_d[0] * n + LIST_d[n]['current_location'][0]) / (n + 1)), Decimal(
            (mean_current_location_d[1] * n + LIST_d[n]['current_location'][1]) / (n + 1))
        ###Max Blood group
        blood_group_count_d[LIST_d[n]['blood_group']] = blood_group_count_d[LIST_d[n]['blood_group']] + 1
    largest_blood_type_d = (max(blood_group_count_d.items(), key=operator.itemgetter(1))[0])
    return average_age_d, oldest_person_age_d, mean_current_location_d, largest_blood_type_d


Stock_weight_norm = namedtuple('Stock_weight_norm', ('name', 'nw'))
Stock_weight_norm.__doc__ = 'Stock Weight Details for Day trade'
Stock_weight_norm.name.__doc__ = 'Name of Stock'
Stock_weight_norm.nw.__doc__ = 'Normilized weight of Stock that day'


class Stock(namedtuple('Stock', ('name', 'symbol', 'open', 'high', 'close', 'low', 'weight'))):

    @classmethod
    def normilized_weight(cls, stocks) -> "returns normalized values for ":
        'This class method calculates normalized weights for given set of weights '
        if not all(isinstance(stock, cls) for stock in stocks):
            raise ValueError('All items in sequence must be of type {}'.format(cls.__name__))
        Total_weight = sum(stock[6] for stock in stocks)
        normilized_weights = [Stock_weight_norm(stock.name, (stock.weight / Total_weight)) for stock in stocks]
        return tuple(normilized_weights)

    @classmethod
    def stock_ex_value(cls, stocks) -> "returns normalized values for ":
        'This class method calculates normalized weights for given set of weights '
        if not all(isinstance(stock, cls) for stock in stocks):
            raise ValueError('All items in sequence must be of type {}'.format(cls.__name__))
        normilized_weights = cls.normilized_weight(stocks)
        Exch_open = sum(
            s.open * norw.nw if s.name == norw.name else "error" for s, norw in zip(stocks, normilized_weights))
        Exch_high = sum(
            s.high * norw.nw if s.name == norw.name else "error" for s, norw in zip(stocks, normilized_weights))
        Exch_close = sum(
            s.close * norw.nw if s.name == norw.name else "error" for s, norw in zip(stocks, normilized_weights))
        Exch_low = sum(
            s.low * norw.nw if s.name == norw.name else "error" for s, norw in zip(stocks, normilized_weights))
        return Exch_open, Exch_high, Exch_close, Exch_low


Stock.__doc__ = 'Stock Detail for Day trade'
Stock.name.__doc__ = 'Name of Stock'
Stock.symbol.__doc__ = 'symbol of Stock'
Stock.open.__doc__ = 'Opening Value of Stock that day'
Stock.high.__doc__ = 'highest Value of Stock that day'
Stock.close.__doc__ = 'closing highest Value of Stock that day'
Stock.low.__doc__ = 'closing lowest Value of Stock that day'
Stock.weight.__doc__ = 'weight Stock that day'


def function_fstock_creation(count: "Number of stock to be created using faker"):
    "Returns  profile stored in named tuple and dictionary in tuple and list respecitvely for user defined count"
    Stock_list=[]
    Stock_list_dict=[]
    for n in range(count):
        name=fake.company()
        symbol=name[:3]
        low=uniform(100,5000)
        high=uniform(low,5000)
        open=uniform(low,high)
        close=uniform(low,high)
        weight=uniform(0.8,1.2)
        Stock_list.append(Stock(name,symbol,open,high,close,low,weight))
        Stock_list_dict.append({"name": name,"symbol" : symbol,"open":open,"high":high,"close":close,"low":low,"weight":weight})
    return tuple(Stock_list),Stock_list_dict


