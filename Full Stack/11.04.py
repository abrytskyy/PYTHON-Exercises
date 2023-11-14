# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def get_coord(self):
#         return self.x, self.y
# vec = Vector(10, 20)
# coord1 = vec.get_coord()
# coord2 = Vector.get_coord(vec)
# print(coord1)
# print(coord2)

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def is_in_range(self, arg):
        pass
vec = Vector(10, 20)
vec.is_in_range(5)

# class Video:
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f"Video is playing {self.name}")
#
# class YouTube:
#     videos = []
#
#     @classmethod
#     def add_method(cls, video):
#         cls.video.append(video)
#
#     @classmethod
#     def play(self, video_index):
#         Video.play(cls.videos[video_index])
# video1 = Video()
# video2 = Video()
#
# video1.create("Python")
# video2.create("Python OOP")
#
# YouTube.add