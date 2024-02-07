class User:
    all_posts = {}

    def __init__(self, name, email, username):
        self.name = name 
        self.email = email
        self.username = username
        self.posts = []
        

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

    def password(self, secret_code):
        return f"{self.name}'s password is {secret_code}"
    
    def create_post(self, post_content):
        if self in User.all_posts:
            User.all_posts[self].append(post_content)
        else:
            User.all_posts[self] = [post_content]
        print(f"{self.name} created a new post: {post_content}")

    @staticmethod
    def get_all_posts():
        return User.all_posts
    
for user, posts in User.get_all_posts().items():
    print(f"{user.name}'s posts:")
    for post in posts:
        print(post)



user1 = User("Kevin", "Kevin@gmail.com", "kmcalister")
user2 = User("George", "George@yahoo.com", "gcostanza")

user1.create_post("Keep the change")
user1.create_post("I'm dreaming of a white christmas")


user2.create_post("I wish i wasn't bald")
user2.create_post("I love the Yankees")


print(User.all_posts)

# john = User("John", "john@gmail.com", "John123")
# kevin = User("kevin", "kevin@gmail.com", "kevin123")
# # kevin.password("12345")
# # john.password("password789")
# print(john)
# print(kevin)