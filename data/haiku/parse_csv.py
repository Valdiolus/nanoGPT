#https://www.kaggle.com/datasets/sulphatet/twitter-financial-news?resource=download

import csv
import re

with open('all_haiku.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    i = 0
    txt_file = open('input.txt', 'w')
    for row in reader:
        strings = row[1:4]

            #for x in r_str:
            #    new_r = ''.join(filter(str.isalpha, x)) + ' '
                #print(new_r)

        #for str in strings:
        #    newstring = re.sub(r"[^a-zA-Z ]+", "", str)
        #    print(newstring)
        upd_strings = []
        for str in strings:
            #print(str, len(str))
            if len(str) > 0:
                if str[0] == ' ':
                    while str[0] == ' ':
                        str = str[1:]
                if str[-1] == ' ':
                    while str[-1] == ' ':
                        str = str[:-1] 
                upd_strings.append(re.sub(r"[^a-zA-Z ]+", "", str)) 
            else:
                upd_strings.append('')
        # skip text and label 
        if i > 0: 
            #print(strings)
            txt_file.write(upd_strings[0] + ';' + upd_strings[1] + ';' + upd_strings[2] +'\n')
            #if i > 10:
            #    quit()
        i+=1

    print("Added", i-1, "strings of text")
