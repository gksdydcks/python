#             ##생성자(constructor)
# # class Movie:
# #     def __init__(self):
# #         print("Hello")

# # movie = Movie()

# class Movie:
#     # count = 0 #초기화 선언 여기선 의미 없음

#     # def __init__(self, title="오징어 게임", audience=300):
#     def __init__(self, title, audience):
#         self.title = title
#         self.audience = audience

# movie1 = Movie("파묘", 100)
# movie2 = Movie("파묘2", 200)

# print(movie1.title, movie1.audience)
# print(movie2.title, movie2.audience)

# # movie3 = Movie()
# print(movie3.title, movie3.audience)

class Movie:
    count = 0 
    def __init__(self, title, audience):
        self.title = title
        self.audience = audience
        Movie.count += 1     #Movie.count라는 카운터 변수

movie1 = Movie("파묘", 100)
print(Movie.count)
movie2 = Movie("파묘2", 200)

print(movie1.count)
print(movie2.count)
print(Movie.count)
Movie.count +=1
print(movie1.count)
print(movie2.count)
print(Movie.count)
movie1.count +=1
print(movie1.count)
print(movie2.count)
print(Movie.count)
Movie.count +=1
print(movie1.count)
print(movie2.count)
print(Movie.count)


