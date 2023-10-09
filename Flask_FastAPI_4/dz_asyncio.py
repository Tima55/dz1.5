# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.

import asyncio
import aiohttp
import time 

urls=['https://hips.hearstapps.com/hmg-prod/images/wisteria-in-bloom-royalty-free-image-1653423554.jpg', 
      'https://upload.wikimedia.org/wikipedia/commons/a/a5/Flower_poster_2.jpg', 
      'https://hips.hearstapps.com/hmg-prod/images/summer-flowers-64418cf119d36.jpg', 
      'https://images.immediate.co.uk/production/volatile/sites/10/2018/02/5984c00b-1474-4218-b327-59490057a7b6-f3cff11.jpg', 
      'https://hips.hearstapps.com/hmg-prod/images/flower-meanings-1671510935.jpg', 
      'https://hips.hearstapps.com/hmg-prod/images/close-up-of-purple-crocus-flowers-united-kingdom-uk-royalty-free-image-1674159456.jpg',
      'https://grangettos.com/cdn/shop/articles/IMG_2019_2000x.jpg',]

async def download(url): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(url) as response: 
            filename = 'asyncio_' + url.replace('https://', '').replace('.jpg','').replace('.','_').replace('/','') + '.jpg' 
        
            with open('flaskk/f4/f4_images_asyncio/' + filename, "wb") as f:
                total, size = (0, 4092)
                res = response.content.iter_chunked(size)
                async for chunk in res:
                    f.write(chunk)
                    total += size
                    print(f"Downloaded {url}: {total/1024:.2f} kB in {time.time() - start_time:.2f} seconds") 

async def main():
    tasks=[]
    for url in urls: 
        task=asyncio.ensure_future(download(url)) 
        tasks.append(task) 
        await asyncio.gather(*tasks) 
        
start_time = time.time() 

if __name__ =='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
