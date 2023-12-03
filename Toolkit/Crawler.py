import os
import shutil
import zipfile
import requests
from tqdm import tqdm
from pathlib import Path
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed


download_dir = Path(__file__).resolve().parent.parent / 'audio-files'

html_page = requests.get('http://ecs.utdallas.edu/loizou/speech/noizeus')

soup = BeautifulSoup(html_page.content, 'html.parser')
file_urls = soup.findAll('a')
links = [link.get('href') for link in file_urls]

file_list = []

for i in links:
    if '.zip' in i and '/' not in i:
        file_list.append(i)


def download_file(file_name):
    download_url = 'https://ecs.utdallas.edu/loizou/speech/noizeus/' + file_name
    response = requests.get(download_url)
    if "content-disposition" in response.headers:
        content_disposition = response.headers["content-disposition"]
        filename = content_disposition.split("filename=")[1]
    else:
        filename = download_url.split("/")[-1]
    with open(download_dir / file_name, mode="wb") as file:
        file.write(response.content)
    print(f"Downloaded file {filename}")
    return file_name


def extract_zip(file):
    file_path = download_dir / file
    with zipfile.ZipFile(file_path) as zip_file:
        for member in zip_file.namelist():
            filename = os.path.basename(member)
            if not filename:
                continue
            source = zip_file.open(member)
            target = open(os.path.join(download_dir, filename), "wb")
            with source, target:
                shutil.copyfileobj(source, target)
    os.remove(file_path)
    print(f"Extracted file {file}")


with tqdm(total=len(file_list)) as progress_bar:
    n_threads = len(file_list)
    with ThreadPoolExecutor(n_threads) as executor:
        futures = [executor.submit(download_file, url) for url in file_list]
        for future in as_completed(futures):
            file_name = future.result()
            extract_zip(file_name)
            progress_bar.update(1)
