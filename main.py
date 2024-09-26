from engine import SearchEngine

def test_engine():
    try:
        print('Welcome to Search Engine')
        google = SearchEngine()
        while True:
            search_word = input('Search for a word:')
            if search_word:
                result = google.search(search_word)
                display = input('Do you want dispaly the entire search result Y/N ?')
                if display.lower() == 'y' or display.lower() == 'yes':
                    print(result)
                else:
                    lines = int(input('How paragraph do you wish to display:'))
                    if lines:
                        paragraphs = result.split('\n')
                        paragraph_lines = paragraphs[:lines]
                        print(paragraph_lines)
    except:
        pass

test_engine() 

