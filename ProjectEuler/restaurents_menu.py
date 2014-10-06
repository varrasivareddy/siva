"""
Programme to find the restaurants for the selected items.

Note:
  This programme considers the input csv file should be in the
  same directory where you were running this programme.

"""
import csv
import sys


class RestaurantFinder(object):
  """
  Class to find the restaurant haing all the selected items.
  """

  def get_restaurant(self):
    """
    Method to get the restaurant.
    """
    try:
      input_data = self.parse_input()
      self.search_in_csv(input_data)
    except ValueError, e:
      print e.args[0]
    except IOError:
      print 'There is no file exist with "{}"'.format((input_data['csv_file_name']))
    except Exception, e:
      print e.args[0]

  def search_in_csv(self, input_data):
    """
    Method to search over the csv data.

    Args:
      input_data: dict having file name, search words.

    Returns:
      Boolean.
    """
    temp_list = []
    csv_data = self.get_csv_data(input_data['csv_file_name'])
    for item in input_data['search_words']:
      if not csv_data.get(item):
        raise ValueError('No Restaurants found for the selected items.')
      temp_list.extend([csv_data[item].keys()])

    # step to find the restaurant having all the selected items.
    restaurants = set(temp_list[0]).intersection(*temp_list)

    if not restaurants:
      raise ValueError('No Restaurants found for the selected items.')

    # statements to find and print the restaurant and price.
    for restaurant in restaurants:
      sum = 0
      for item in input_data['search_words']:
        sum += float(csv_data[item][restaurant])
      print restaurant, sum
    return True

  def get_csv_data(self, file_name):
    """
    Method to read the csv data from the file.

    Args:
      file_name: str name of the csv file.

    Returns:
      Dict od Dict having item as keys and restaurant and prices.
      Ex:
        {'item1': {6: 4.0},
         'item2': {5: 34.0}}
    """
    csv_data = {}

    with open(file_name, 'rb') as csvfile:
      data = csv.reader(csvfile, delimiter=',', quotechar='|')
      rows = [i for i in data]
 
      for data in rows:
        if len(data) <= 2:
          raise ValueError('Please enter proper csv data. Ex. 5,6.0,ietm1,item2')

        for item in data[2:]:
          try:
            int(data[0])
            int(data[1])
          except Exception:
            raise ValueError('Please enter valid data for price or restaurant number.')

          if item in csv_data.keys():
            csv_data[item][data[0]] = data[1]
          else:
            csv_data[item] = {data[0]: data[1]}

      return csv_data

  def parse_input(self):
    """
    Method Parse the input.

    Returns:
      Dict having fine names and data.
      Ex:
        {'csv_file_name': 'test.csv',
         'search_words': ['word1', 'word2']}
    """
    input_dict = {}
    input_data = sys.argv

    if len(input_data) <= 1:
      raise ValueError('Please give us the csv file and the items to search.')

    if len(input_data) >= 2 and not '.csv' in input_data[1]:
      raise ValueError('Please enter the proper csv file name.')

    try:
      search_words = input_data[2:]
      if not input_data[2:]:
        raise IndexError()

      input_dict['search_words'] = search_words
      input_dict['csv_file_name'] = input_data[1]
        
    except IndexError, Exception:
      raise ValueError('Please enter the items to search.')

    return input_dict

obj = RestaurantFinder()
obj.get_restaurant()