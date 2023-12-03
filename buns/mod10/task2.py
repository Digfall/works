import requests
import re

def get_subheadings(url):
    # Получаем HTML-код страницы
    response = requests.get(url)
    html_code = response.text

    # Используем регулярное выражение для поиска подзаголовков в тегах <h3>
    pattern = re.compile(r'<h3.*?>(.*?)</h3>', re.DOTALL)
    subheadings = re.findall(pattern, html_code)

    return subheadings

if __name__ == "__main__":
    url = "http://www.columbia.edu/~fdc/sample.html"
    result = get_subheadings(url)

    # Выводим результат
    print(result)
