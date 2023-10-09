# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.

from multiprocessing import Process
import requests
import time 

urls=['https://hips.hearstapps.com/hmg-prod/images/wisteria-in-bloom-royalty-free-image-1653423554.jpg', 
      'https://upload.wikimedia.org/wikipedia/commons/a/a5/Flower_poster_2.jpg', 
      'https://hips.hearstapps.com/hmg-prod/images/summer-flowers-64418cf119d36.jpg', 
      'https://images.immediate.co.uk/production/volatile/sites/10/2018/02/5984c00b-1474-4218-b327-59490057a7b6-f3cff11.jpg', 
      'https://hips.hearstapps.com/hmg-prod/images/flower-meanings-1671510935.jpg', 
      'https://hips.hearstapps.com/hmg-prod/images/close-up-of-purple-crocus-flowers-united-kingdom-uk-royalty-free-image-1674159456.jpg',
      'https://grangettos.com/cdn/shop/articles/IMG_2019_2000x.jpg',]

def download(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://', '').replace('.','_').replace('/','') + '.jpg' 
    with open('flaskk/f4/f4_images_multiprocessing/' + filename, "wb") as f: 
        f.write(response.content)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds") 
        
processes = [] 
start_time = time.time() 

if __name__ =='__main__': 
    for url in urls: 
        process = Process(target=download, args=(url,)) 
        processes.append(process) 
        process.start() 
        
    for process in processes: 
        process.join()
