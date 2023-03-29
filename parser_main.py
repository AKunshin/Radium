import requests
from bs4 import BeautifulSoup


def get_links():
    url = 'https://gitea.radium.group/radium/project-configuration'
    response = requests.get(url)
    # with open(file='index.html', mode='w') as file:
    #     file.write(response.text)

    with open(file='index.html') as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    body = soup.find(class_='ui single line table mt-0')
    trs = body.find_all('a')
    for tr in trs:
        tr = tr.text.split()
        print(tr)


def get_file_names():
    pass

def download_files():
    pass

def main():
    get_links()


if __name__ == "__main__":
    main()