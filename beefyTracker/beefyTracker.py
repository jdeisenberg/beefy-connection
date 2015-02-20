import sys

if len(sys.argv) < 2:
        print("Please pass a csv file as an argument.")
        sys.exit()

open_CSV_File= open(sys.argv[1],"r")

for line in open_CSV_File:
    first_name,last_name,email,org,phone,address,city,state,post_code,lang,irc,fb,twit,comments,fas_id=line.split(",")
    print(last_name)
