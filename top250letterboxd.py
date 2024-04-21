import requests
from bs4 import BeautifulSoup


#URL = 'https://www.igdb.com/top-100/games'
URL = 'https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/'

def print_data(soup) -> None:
    # Get Data
    res = ''
    for i, movie in enumerate(soup.find_all('img', class_="image")):
        res += f"{i+1}. {movie['alt']}\n"

    return res


def main(page_num) -> None:
    response = requests.get(f'{URL}/page/{page_num}')

    soup = BeautifulSoup(response.text, 'html.parser')

    print(f'Page {page_num}. \n{print_data(soup)}')
    

    next_page = soup.find("a", class_="next")

    if next_page is None: 
        exit()
    else:

        main(page_num+1)

if __name__ == "__main__":
    main(1)

#TODO: Lookup how to get multiple pages as it is only returning the first 100 in the list
#TODO: Try to get it to work with IGDB data