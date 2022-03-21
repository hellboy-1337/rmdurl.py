from urllib.parse import urlparse ,splitquery, parse_qs, parse_qsl
import argparse
from termcolor import colored
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file")
args = parser.parse_args()
OutPut=open("filtered_url.txt","w")
if args.input_file:
    input_file=open(args.input_file,"r").readlines()
    main_list=[]
    filtered_url=[]
    for url in input_file:
        url=url.strip('\n')
        parsed_url = urlparse(url)
        if len(parsed_url.query)>0:
            only_keys=[]
            only_keys.append(parsed_url.scheme+"://"+parsed_url.netloc+parsed_url.path)
            for keys in parsed_url.query.split('&'):
                onlykey=(keys.split("="))
                only_keys.append(onlykey[0])
            if str(only_keys) not in main_list:
                main_list.append(str(only_keys))
                filtered_url.append(url)
            else:
                pass
    for filtered in filtered_url:
        OutPut.writelines(filtered+"\n")
    print(colored("Before   : "+str(len(input_file)),"green"))
    print(colored("After    : "+str(len(filtered_url)),"blue"))
    print(colored("Output File Name is : filtered_url.txt","yellow"))
