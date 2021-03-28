def crawl_amazon_web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
       
        for link in s.findAll('a', {'class':'s-access-detail-page'}):
            movie_title = link.get('title')
            m = re.search( r'Bonus',movie_title)
            if m:
              print(movie_title)
              html_link = link.get('href')
              print(html_link)

crawl_amazon_web(1,'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dmovies-tv&field-keywords=starwars&rh=n%3A2625373011%2Ck%3Astarwars')
  
