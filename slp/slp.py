#requests to talk easily with API's
import requests

#json
import json

#to use strip to remove spaces in textfiles.
import sys

#two variables to squeeze a string between these two so it will become a full uri
part1 = 'http://game-api.skymavis.com/game-api/clients/'
part2 = '/items/1'

#open the outputfile before the for loop
text_file = open("test.txt", "w")

#open the file which contains the strings
with open('ronin.txt', 'r') as f:
    for i in f:    
        uri = part1 + i.strip(' \n\t') + part2
        text_file.write(uri)
        text_file.write("\n")

text_file.close()

#open a new file textfile for saving the responses from the api
text_file = open("responses.txt", "w")

#delete old slp and ronind txt data
#import os
#os.remove("ronintotal.txt")
#os.remove("roninid.txt")

#send every uri to the api and write the respsones to a textfile
with open('test.txt', 'r') as f2:
   for i in f2:
     uri = i.strip(' \n\t')
     batch = requests.get(i)
     data = batch.text
     y = json.loads(data)
     print(y["total"],file=open('ronintotal.txt', 'a'))
     print(y["client_id"],file=open('roninid.txt', 'a'))
     text_file.write(data)
     text_file.write('\n')

text_file.close()

