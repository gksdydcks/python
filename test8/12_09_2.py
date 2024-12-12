#                 ###클래스
# a = dict()  #클래스
# a= set()    #클래스

# class b:    #틀 ex)붕어빵 틀
#     pass

# bb1=b()       #객체 ex)붕어빵
# bb2=b()
# bb3=b()

# class Movie:
#     title = "범죄도시4"
# movie1 = Movie()
# movie2 = Movie()

# print(movie1.title)
# print(movie2.title)

# movie1.title ="파묘"
# print(movie1.title)
# print(movie2.title)

# #!!#method
class Movie:
    name = ''
    def print_msg(msg):
        print(msg)
    def modify(self, movie):
        self.name = movie
    def print_name(self):
        print(self.name)

movie1 = Movie()
movie2 = Movie()

Movie.print_msg("print하기")
# Movie.modify(movie1, "print하기")
movie1.modify("프린트하기3")
movie1.print_name()
movie2.modify("프린트하기4")
print("movie2.name", movie2.name)
