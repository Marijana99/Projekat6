from bs4 import BeautifulSoup
import requests,openpyxl
excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Top Rated Movies'
print(excel.sheetnames)
sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating'])


try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()    # za provjeravanje gresaka
    soup = BeautifulSoup(source.text,'html.parser') # tekst sa web stranice pretvori u ...
    movies = soup.find('tbody',class_="lister-list").find_all('tr') #trazi sve tagove gdje su filmovi

    for movie in movies:
        name = movie.find('td',class_="titleColumn").a.text # film po film u name ubacuje imena
        rank = movie.find('td',class_= "titleColumn").get_text(strip=True).split('.')[0]  # dobija listu, za redni br filma
        year = movie.find('td',class_= "titleColumn").span.text.strip('()')   # span je naziv taga, dobija godinu objave filma
        #strip () da se rijesi zagrade kod godine (1990) dobije 1990
        rating = movie.find('td',class_="ratingColumn imdbRating").strong.text  # strong je tag trazi text, rating =ocjena filma
        


        # strip 
        print(rank,name,year,rating) # ispise informacije za sve filmove 
        sheet.append([rank,name,year,rating])# u excel ce stavljati red po red
      
   # print(len(movies))  # mora ih biti 250
    


except Exception as e:
    print(e)

excel.save('IMDB MovieRatings.xlsx')    
    