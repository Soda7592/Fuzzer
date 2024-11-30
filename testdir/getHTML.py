import requests
import argparse

def getHTML():
    parser = argparse.ArgumentParser(description="Get HTML content from a website.")
    parser.add_argument("-u", "--url", type=str, help="URL to get HTML content.", required=True)
    args = parser.parse_args()
    url = args.url

    headers = {'user-agent': 'Mozilla/5.0'}
    try:    
        response = requests.get(url, headers=headers)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(e)

    file = open('response2.html', 'w')
    file.write(response.text)
    
    return response.text

if __name__ == "__main__":
    getHTML()