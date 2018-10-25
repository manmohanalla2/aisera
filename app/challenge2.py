import requests
import json
import re
import multiprocessing

from utils import get_unique_id

def get_file_content(file_url):
    '''
    returns data in text
    '''
    response = requests.get(file_url)
    data = response.text
    return data


def sequential(file_url):
    '''
    return a dict
    '''
    #passing the url to get the data in file as string format
    data = get_file_content(file_url)
    #removing comma and dots from string
    data = re.sub('[,.]','', data)
    #spliting the data to list
    lst_data = data.split()          
    dict_data = {} 
    for i in lst_data:
        dict_data[i.lower()] = dict_data.get(i.lower(), 0) + 1
    dict_data = json.dumps(dict_data)
    filename = ''.join(['/tmp/sequential',get_unique_id(),'.json'])
    with open(filename, "w") as file:
        file.write(dict_data)
    return dict_data


def parallel(uri):
    '''
    perform actions in parallel
    '''
    #get request to get the html page
    html_page = requests.get(uri)
    html = html_page.text
    #using regex and getting href
    files = re.findall('href="(.*txt)"', html)
    files = [uri + x for x in files]
    #creating 32 threads on 8 processes which is 4 threads each process
    pool = multiprocessing.Pool(32)
    data = pool.map(get_file_content, files)
    data = " ".join(data)
    filename = ''.join(['/tmp/parallel',get_unique_id(),'.json'])
    with open(filename, "w") as file:
        file.write(data)
    pool.close()
    pool.join()
    return data


# print(sequenctial('http://www.gutenberg.org/files/15/text/moby-000.txt'))
# print(parallel('http://www.gutenberg.org/files/15/text/'))