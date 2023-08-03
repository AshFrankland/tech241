import json
# import os
import urllib.request

# json = json.loads(open('example.json').read())
#
# value = json['name']
#
# print(value)

# script to make an absolute of the JSON file
# script_dir = os.path.dirname(__file__)
# print("The script is located at: " + script_dir)
# script_absolute_path = os.path.join(script_dir, 'example.json')
# print("The script absolute path is: " + script_absolute_path)
#
# # Script to parse JSON
# json = json.loads(open(script_absolute_path).read())
# value = json["name"]
# print(value)

# Loop through the JSON
# for key in json:
#     value = json[key]
#     print("The key and value are {} = {}".format(key, value))

# remote example
with urllib.request.urlopen('http://jsonplaceholder.typicode.com/todos/1') as url:
    data = json.load(url)
    print(data)
