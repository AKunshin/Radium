from io import BytesIO
import requests
import zipfile


def download_a_files(url: str):
    response = requests.get(url)

    # extracting the zip file contents
    zf = zipfile.ZipFile(BytesIO(response.content))
    zf.extractall('./downloads')


def main():
    url = 'https://gitea.radium.group/radium/project-configuration/archive/master.zip'
    download_a_files(url)


if __name__ == '__main__':
    main()
