import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu error')
else:
    print('Tudo ok')
    # print(site.read())