import asyncio
import os
import glob

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wb_api.settings")
import django

django.setup()
import aiohttp
from article.models import Article
from openpyxl import load_workbook


async def choose_interval(quer: int):
    if quer < 1000:
        vole = 0
        par = 0
        await create_list_url(quer, vole, par)
    if 1000 <= quer < 10000:
        vole = 0
        par = int(str(quer)[:1])
        await create_list_url(quer, vole, par)
    if 10000 <= quer < 100000:
        vole = 0
        par = int(str(quer)[:2])
        await create_list_url(quer, vole, par)
    if 100000 <= quer < 1000000:
        vole = int(str(quer)[:1])
        par = int(str(quer)[:3])
        await create_list_url(quer, vole, par)
    if 1000000 <= quer < 10000000:
        vole = int(str(quer)[:2])
        par = int(str(quer)[:4])
        await create_list_url(quer, vole, par)
    if 10000000 <= quer < 100000000:
        vole = int(str(quer)[:3])
        par = int(str(quer)[:5])
        await create_list_url(quer, vole, par)
    if 100000000 <= quer < 1000000000:
        vole = int(str(quer)[:4])
        par = int(str(quer)[:6])
        await create_list_url(quer, vole, par)
    if 1000000000 <= quer < 10000000000:
        vole = int(str(quer)[:5])
        par = int(str(quer)[:7])
        await create_list_url(quer, vole, par)


async def create_list_url(quer, vole, par):
    ls = []
    for i in range(1, 10):
        url = f'https://basket-0{i}.wb.ru/vol{vole}/part{par}/{quer}/info/ru/card.json'
        ls.append(url)
    await asyncio.gather(
        *(get_link(url) for url in ls),
        return_exceptions=True
    )


async def get_link(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                res = await response.json()
                await create_art(res)
                return res


async def create_art(res):
    art = res.get('nm_id')
    imt = res.get('imt_name')
    brand = res.get('selling').get('brand_name')
    name_art = (brand + '/' + imt)
    await Article.objects.filter(art=art).aupdate(name=name_art, brand=brand)


async def get_list_file():
    list_of_files = glob.glob('./file/excel/*.xlsx')
    latest_file = max(list_of_files, key=os.path.getctime)
    excel_data = load_workbook(latest_file)
    sheet = excel_data.active
    count = 0
    for worksheet in excel_data:
        for cell in worksheet['A']:
            a = str(cell)
            if len(a) != 0:
                count += 1
            else:
                continue
        ls = []
        for row in range(1, count):
            full_art = sheet[row][0].value
            ls.append(full_art)
            await Article.objects.aget_or_create(art=full_art)
        await search_art(ls)


async def search_art(ls):
    await asyncio.gather(
        *(choose_interval(art) for art in ls),
        return_exceptions=True
    )
