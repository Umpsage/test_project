import requests
from constant import SEARCH_ENGINE_URL
from bs4 import BeautifulSoup

class SearchEngine:
    result = []
    def search(self,word):
        search_word = self.construct_word(word)
        result_text = ''
        if search_word:
            url = SEARCH_ENGINE_URL + search_word
            result = requests.get(url)
            if result.status_code == 200:
                data = BeautifulSoup(result.text,'html.parser')
                for ptag in data.find_all('p'):
                    result_text += ptag.get_text()
                return result_text
            elif result.status_code == 404:
                return Exception('Search parameter not found')
            elif result.status_code ==500:
                return Exception('An error occured in the engine server.')
        else:
            return Exception('Invalid search word')

                
                
    def construct_word(self,word: str) ->str:
        try:
            if word:
                word = word.strip()
                return word.title().replace(' ','_')
            else:
                raise Exception
        except:
            return None
