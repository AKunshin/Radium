import asyncio
from aiohttp import ClientSession
import zipfile


async def download_files(url):
    async with ClientSession() as session:      

        async with session.get(url=url) as response:
            if response.status == 200:
                with open('master.zip', 'wb') as fd:
                    async for chunk in response.content.iter_chunked(10):
                        fd.write(chunk)


async def main():    
    url = f'https://gitea.radium.group/radium/project-configuration/archive/master.zip'

    tasks = []
    for _ in range(3):
        tasks.append(asyncio.create_task(download_files(url)))

    for task in tasks:
        await task

    # extracting the zip file contents
    zf = zipfile.ZipFile('master.zip')
    zf.extractall('./downloads_2')
        

asyncio.run(main())
