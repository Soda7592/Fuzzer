import argparse
import requests

def main(url, endpoint_path, args_path) :
    endpoints = open(endpoint_path, 'r')
    args = open(args_path, 'r')
    
        
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web API Fuzzer !")
    parser.add_argument("-u", "--url", type=str, help="URL to fuzz", required=True)
    parser.add_argument("-e", "--endpoint", type=str, help="Provide a endpoint text file path to fuzz", required=True)
    parser.add_argument("-a", "--arguments", type=str, help="Arguments for endpoints", required=True)
    parser.add_argument("-pass", "--password", type=str, help="If you want to test the web apis with some loggined session give me a vaild password", required=False)
    parser.add_argument("-user", "--username", type=str, help="If you want to test the web apis with some loggined session give me a vaild username", required=False)
    
    args = parser.parse_args()
    main(args.url, args.endpoint, args.arguments)