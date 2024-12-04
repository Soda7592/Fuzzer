import argparse
import requests
import json
import uuid
from fake_useragent import UserAgent


def MakeUrl(base_url, endpoint, args) :
    url = base_url + endpoint
    data = {}
    args = args.split(',')
    for i in args :
        data[i] = ''
    return url, data
# return url with data

def ParseArgs(args_path) :
    l = open(args_path, 'r').readlines()
    args = []
    for i in l:
        if '\n' in i :
            args.append(i.strip('\n'))
        else :
            args.append(i)
    return args
# return args in list type and all values is empty. 

def ParseEnd(endpoint_path) :
    l = open(endpoint_path, 'r').readlines()
    endpoints = []
    for i in l:
        if '\n' in i :
            endpoints.append(i.strip('\n'))
        else :
            endpoints.append(i)
    return endpoints

def InjectionTest(url, data) :
    checkurl = 'http://192.168.88.140:7788/connection'
    ua = UserAgent().random
    headers = {'user-agent': ua}
    wordlist = open('wordlists/XSS.txt', 'r').readlines()
    status = {}
    code_list = []
    # resBefore = requests.get(url + '/connection', headers=headers)
    # file = open(f'result/Before_{url}', 'a')
    # file.write(resBefore.text)
    for w in wordlist:
        InjectFlag = 0
        for key in data :
            data[key] = w
        res = requests.post(url, data, headers=headers)
        if res.status_code not in code_list :
            status[str(res.status_code)] = 1
            code_list.append(res.status_code)
        else :
            status[str(res.status_code)] += 1
        resAfter = requests.get(checkurl, headers=headers)
            # file = open(f'.\\result/After', 'a')
            # file.write(resAfter.text)
        # print(w)
        if w in resAfter.text :
            print(f'\033[35m[!] There might have a Injectable vulnerability in \033[0m\033[32m{key}\033[0m with payload \n >> {w}\033[31m\033[0m')
            InjectFlag = 1
        if InjectFlag == 0 :
            print(f'\033[35m[!] There might not have a Injectable vulnerability in \033[0m\033[32m{key}\033[0m')
        for k in status :
            print(f'[+] Status code {k}: {status[k]}')
    print('')

def main(base_url, endpoint_path, args_path, Isinject) :
    ua = UserAgent().random
    headers = {'user-agent': ua}
    endpoints = ParseEnd(endpoint_path)
    args = ParseArgs(args_path) # open(args_path, 'r')
    for i in range(len(endpoints)) :
        url, data = MakeUrl(base_url, endpoints[i], args[i])
        code_list = []
        # if Isinject == 1 :
        #     InjectionTest(url, data)
        print("\033[32m[!] Now testing: \033[0m\033[31m" + url + "\033[0m")
        wordlist = open('wordlists/int.txt', 'r').readlines()
        status = {}
        Inj_data = data
        for w in wordlist:
            for key in data :
                data[key] = w
            res = requests.post(url, data, headers=headers)
            if res.status_code not in code_list :
                status[str(res.status_code)] = 1
                code_list.append(res.status_code)
            else :
                status[str(res.status_code)] += 1
        print('\033[33mAfter the testing, the status codes are: \033[0m')
        for k in status :
            print(f'[+] Status code {k}: {status[k]}')
        # f = open('.\\result' + endpoints[i] + '_Atfer' + '.html', 'w')
        # f.write(requests.get('http://192.168.88.140:7788/connection').text)
        print(f'\033[34mEnd of testing for endpoint :\033[0m\033[32m {url}\033[0m')
        
        if Isinject == 1 :
            print("\033[32m[!] Now let's start a injection testing: \033[0m\033[31m" + url + "\033[0m")
            InjectionTest(url, Inj_data)
    


# python .\main.py -u http://192.168.88.140:7788 -e .\endpoint.txt -a .\arguments.txt -d 1
def DeleteAllProject(base_url):
    ua = UserAgent().random
    url = base_url + '/delete_project'
    headers = {'user-agent': ua}
    res = requests.post(url, data = {'p_id':32}, headers=headers)
    for i in range(1000) :
        res = requests.post(url, data = {'p_id':i}, headers=headers)

# python .\main.py -u http://192.168.88.140:7788 -e .\endpoint.txt -a .\arguments.txt -t 1
def CreateRandomProject(base_url, endpoint_path) :
    ua = UserAgent().random
    url = base_url + endpoint_path
    headers = {'user-agent': ua}
    for i in range(20) :
        uid = uuid.uuid1()
        data = {'p_name':uid, 'p_pwd':str(uid)[:6]}
        res = requests.post(url, headers=headers, data=data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web API Fuzzer !")
    parser.add_argument("-u", "--url", type=str, help="URL to fuzz", required=True)
    parser.add_argument("-e", "--endpoint", type=str, help="Provide a endpoint text file path to fuzz", required=True)
    parser.add_argument("-a", "--arguments", type=str, help="Arguments for endpoints", required=True)
    parser.add_argument('-r', "--risk", type=int, help="Test vulnerability in risk Level for fuzzing test. If you want to test it set this vaule to 1. (default=0)",default=0, required=False)
    parser.add_argument("-t", "--test", type=int, help="Create some random projects. If you want to do this operation, specify this arg to 1. (default=0)", default=0, required=False)
    parser.add_argument("-d", "--delete", type=int, help="Delete all projects. If you want to do this operation, specify this arg to 1. (default=0)", default=0, required=False)
    parser.add_argument("-pass", "--password", type=str, help="If you want to test the web apis with some loggined session give me a vaild password", required=False)
    parser.add_argument("-user", "--username", type=str, help="If you want to test the web apis with some loggined session give me a vaild username", required=False)
    args = parser.parse_args()
    if(args.test == 1) :
        CreateRandomProject(args.url, '/new_project')
    elif(args.delete == 1) :
        DeleteAllProject(args.url)
    else :
        main(args.url, args.endpoint, args.arguments, args.risk)