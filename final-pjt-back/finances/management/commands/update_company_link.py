import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from finances.models import Deposit
import certifi
class Command(BaseCommand):
  def handle(self, *args, **options):
      # finances/static/finances 디렉토리에서 모든 PNG 파일을 검색.
    # URL to crawl
    url = 'https://www.bok.or.kr/portal/main/contents.do?menuNo=200580'

    # Send a GET request to the URL
    response = requests.get(url, verify=False)
    url_list = []
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the main tag
        main_tag = soup.find('main')
        if main_tag:
            # Find all divs with class 'table-striped tac' inside the main tag
            divs = main_tag.find_all('div', class_='table table-striped tac')
            # Loop through each div
            for div in divs:
                # Find the table inside the div
                table = div.find('table')
                if table:
                    # Find the tbody inside the table
                    tbody = table.find('tbody')
                    if tbody:
                        # Find all tr elements inside the tbody
                        rows = tbody.find_all('tr')
                        for row in rows:
                            # Find all td elements inside the tr
                            cols = row.find_all('td')
                            for col in cols:
                                # Find the a element inside the td
                                a_tag = col.find('a')
                                if a_tag:
                                    href = a_tag.get('href')
                                    text = a_tag.get_text(strip=True)
                                    print(f'Text: {text}, Href: {href}')
                                    url_list.append((text, href))
        else:
            print('Main tag not found')
    print(url_list)
    deposits = Deposit.objects.all()
    
    for deposit in deposits:
        found = False
        for url in url_list:
            if url[0] == deposit.company_name:
                deposit.link = url[1]
                deposit.save()
                found = True
                break
        if not found:
            deposit.link = f'http://search.naver.com/search.naver?query={deposit.company_name}'
            deposit.save()
      
    