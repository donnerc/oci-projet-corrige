
import urllib.request

def get_page(url):

    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        html = html.decode('utf-8')

    except:
        return ''

    return html

def test_get_page():
    print(get_page("http://www.collegedusud23.ch"))


def main():
    test_get_page()

if __name__ == '__main__':
    main()