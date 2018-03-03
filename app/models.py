import datetime

# Members Class --------------->>>>>>

class Members:
    def __init__(self, member_name, member_age):
        self.id = 0
        self.name = member_name
        self.age = member_age
        self.posts = []

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


# Posts Class --------------->>>>>>

class Post:
    def __init__(self,post_title,post_content, member_id=0):
        self.id = 0
        self.title = post_title
        self.content = post_content
        self.member_id = member_id
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}"
