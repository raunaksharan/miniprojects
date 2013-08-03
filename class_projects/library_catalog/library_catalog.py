'''
Created on 3/08/2013

@author: luke
'''

class Library(object):

    def __init__(self):
        self._books = []
        
    @property
    def books_all(self):
        return self._books
    
    @property
    def books_out(self):
        if self._books: 
            return [book for book in self._books if book.checked_out]
        return False
    
    @property
    def books_in(self):
        pass
    
    def _clear_data(self):
        """
        Reverts all dat ato expected data upon creation
        """
        self._books     = []
    
    def add_books(self,*args):
        def add_book(book):
            if isinstance(book,Book):
                self._books.append(book)
                
        for arg in args:
            # in case arg is iter of books
            if hasattr(arg,'__iter__'):
                for val in arg:
                    add_book(val)
            else: # presumably it's a book
                add_book(arg)
        return True

    
class Book(object):
    
    def __init__(self,title,isbn,author,genre):
        for val in (title,isbn,author,genre):
            if not isinstance(val,str):
                raise TypeError("Expected str but received {0}".format(type(val)))
        self._title     = title
        if len(isbn)!= 13:
            raise AttributeError
        self._isbn      = isbn
        self._author    = author
        self._genre     = genre
        self._checked_out= False
        
    @property
    def title(self):
        return self._title
    
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def author(self):
        return self._author
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def checked_out(self):
        return self._checked_out
    
    @checked_out.setter
    def checked_out(self,res):
        if not isinstance(res,bool):
            raise TypeError("Expected boolean but recieved {0}".format(type(res)))
        self._checked_out   = res
        
        
if __name__ == '__main__':
    pass