class Genre:
    def __init__(self):
        self._name=None
        self._country=''
        self._color=''
        
    def set_name(self,name):
        self._name=name
    def get_name(self):
        return self._name
    def set_countryy(self,country):
        self._country=country
    def get_country(self):
        return self._country
    def set_color(self,color):
        self._color=color
    def get_color(self):
        return self._color
    
    def info(self):
        print('Name - ',self._name,'\nCountry - ',self._country,'\nCover color - ',self._color)
        
    def Sales(self):
        print('Sales')
        
class Drama(Genre):
    def __init__(self):
        super().__init__()
        self._popularity=0
        self._number_of_publishing_houses=0
        
    def set_popularity(self,popularity):
        self._popularity=popularity
    def get_popularity(self):
        return self._popularity
    def set_number_of_publishing_houses(self,number_of_publishing_houses):
        self._number_of_publishing_houses=number_of_publishing_houses
    def get_number_of_publishing_houses(self):
        return self._number_of_publishing_houses
    
    def info(self):
        super().info()
        print('Popularity -',self._popularity,'\nNumber_of_publishing_houses -', self._number_of_publishing_houses)
    
    def Sales(self):
        print ('Drama')
        super().Sales()
        print (self._popularity*self._number_of_publishing_houses)
        

class Novel(Genre):
    def __init__(self):
        super().__init__()
        self._popularity=0
        self._number_of_publishing_houses=0
        self._number_of_books=0
        
    def set_popularity(self,popularity):
        self._popularity=popularity
    def get_popularity(self):
        return self._popularity
    def set_number_of_publishing_houses(self,number_of_publishing_houses):
        self._number_of_publishing_houses=number_of_publishing_houses
    def get_number_of_publishing_houses(self):
        return self._number_of_publishing_houses
    def set_number_of_books(self,number_of_books):
        self.__number_of_books=number_of_books
    def get_number_of_books(self):
        return self._number_of_books
    
    def info(self):
        super().info()
        print('Popularity -',self._popularity,'\nNumber_of_publishing_houses -', self._number_of_publishing_houses,'\nNumber_of_books -', self._number_of_books)
    def Sales(self):
        print ('Novel')
        super().Sales()
        print ((self._popularity+self._number_of_publishing_houses)*self._number_of_books)
    
class Fantasy(Genre):
    def __init__(self):
        super().__init__()
        self._number_pages=0
        
    def set_number_pages(self,number_pages):
        self._number_pages=number_pages
    def get_number_pages(self):
        return self._number_pages
    
    def info(self):
        super().info()
        print('Number pages',self._number_pages)
        
    def Sales(self):
        print('number_pages')
        super().Sales()
        print ('Fantasy ',(self._number_pages**3))

fp=Drama()
ft=Novel()
fc=Fantasy()




fp.set_color('Blue')
fp.set_name('The Gift of the Magi by O. Henry')
fp.set_popularity(5)#Что это?
fp.set_countryy('USA')
fp.set_number_of_publishing_houses(3)

ft.set_color('Pink')
ft.set_name('Christmas Books by C. Dickens')
ft.set_popularity(5)
ft.set_number_of_publishing_houses(5)
ft.set_countryy('UK')
ft.set_number_of_books(6)

fc.set_color('Orange')
fc.set_name('Not found')
fc.set_countryy('Not found')
fc.set_number_pages(0)

fp.info()
fp.Sales()
print('')
ft.info()
ft.Sales()
print('')
fc.info()
fc.Sales()