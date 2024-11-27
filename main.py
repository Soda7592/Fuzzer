import argparse
import requests
import json
from fake_useragent import UserAgent

def main(base_url, endpoint_path, args_path) :
    ua = UserAgent().random
    headers = {'user-agent': ua}
    endpoints = open(endpoint_path, 'r').readlines()
    args = open(args_path, 'r')
    for end in endpoints :
        print(end.strip('\n'))
        for i in args :
            data = {}
            arg = i.strip('\n').split(',')
            for key in arg:
                key = key.split(':')
                data[key[0]] = key[1]
            print(json.dumps(data))
            print('')
        url = base_url + end
        response = requests.post(url, data, headers=headers)
        if response.status_code == 200 :
            print("[+] Status: 200")
            print("[+] You might need to take more attention to this result.")
        elif response.status_code == 403 :
            print("[-] Status: 403") 
            print("[-] This endpoint is forbidden.")
        elif response.status_code == 404 :
            print("[-] Status: 404")
            print("[-] This endpoint is not found.")
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web API Fuzzer !")
    parser.add_argument("-u", "--url", type=str, help="URL to fuzz", required=True)
    parser.add_argument("-e", "--endpoint", type=str, help="Provide a endpoint text file path to fuzz", required=True)
    parser.add_argument("-a", "--arguments", type=str, help="Arguments for endpoints", required=True)
    parser.add_argument("-pass", "--password", type=str, help="If you want to test the web apis with some loggined session give me a vaild password", required=False)
    parser.add_argument("-user", "--username", type=str, help="If you want to test the web apis with some loggined session give me a vaild username", required=False)
    
    args = parser.parse_args()
    main(args.url, args.endpoint, args.arguments)