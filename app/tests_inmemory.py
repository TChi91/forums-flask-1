from app import models, store
from time import sleep

# MEMBERS STORE ------>>>>



def create_members():

    member1 = models.Members("Majd", 36)
    member2 = models.Members("Rida", 28)
    member3 = models.Members("Manhal", 29)
    member4 = models.Members("Majd", 50)
    print(member1)
    print(member2)
    print(member3)
    print(member4)
    print("=" * 30)

    return member1, member2, member3, member4


def store_should_add_models(members_instances, member_store):

    for member in members_instances:
        member_store.add(member)


def stores_should_be_similar():

    member_store1 = store.MembersStore()
    member_store2 = store.MembersStore()
    if member_store1.get_all() is member_store2.get_all():
        print("Same stores elements !")


def print_all_members(member_store):
    print("=" * 30)

    for member in member_store.get_all():
        print(member)

    print("=" * 30)


def get_by_id_should_retrieve_same_object(member_store, member2):
    member2_retrieved = member_store.get_by_id(member2.id)

    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")


def update_should_modify_object(member_store, member3):
    member3_copy = models.Members(member3.name, member3.age)
    member3_copy.id = 3

    if member3_copy is not member3:
        print("member3 and member3_copy are not the same !")

    print(member3_copy)
    member3_copy.name = "john"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))

def print_same_names(member_store):
    for member in member_store.get_by_name("Majd"):
        print(member)
    print("=" * 10)

def catch_exception_when_deleting():
    try:
        member_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")


def create_posts(members_instances):
    post1 = models.Post("Agriculture", "Agriculture is amazing", members_instances[0].id)
    post2 = models.Post("Engineering", "I love engineering", members_instances[0].id)

    post3 = models.Post("Medicine", "Medicine is great", members_instances[1].id)
    post4 = models.Post("Architecture", "Spectacular art", members_instances[1].id)
    post5 = models.Post("Astronomy", "Space is awesome", members_instances[1].id)

    post6 = models.Post("Geology", "Earth is our friend", members_instances[2].id)
    post7 = models.Post("ComputerSci", "Our passion", members_instances[2].id)
    post8 = models.Post("Algorithms", "Yeah, more of that", members_instances[2].id)
    post9 = models.Post("Operating Systems", "Ewww", members_instances[2].id)

    print(post1)
    print(post2)
    print(post3)
    print("=" * 30)

    return post1, post2, post3, post4, post5, post6, post7, post8, post9


def store_should_add_posts(posts_instances, post_store):
    for member in posts_instances:
        post_store.add(member)


def store_should_get_members_with_posts(member_store, post_store):
    members_with_posts = member_store.get_members_with_posts(post_store.get_all())

    for member_with_posts in members_with_posts:
        print(f"{member_with_posts} has posts:")
        for post in member_with_posts.posts:
            print(f"\t{post}")

        print("=" * 10)

def store_should_get_top_two(member_store, post_store):
    top_two_members = member_store.get_top_two(post_store.get_all())

    for member_with_posts in top_two_members:
        print(f"{member_with_posts} has posts:")
        for post in member_with_posts.posts:
            print(f"\t{post}")


def print_by_date(post_store):
    print("=" * 30)

    for post in post_store.get_posts_by_date(post_store.get_all()):
        print(post)

    print("=" * 30)


members_instances = create_members()
member1, member2, member3, member4 = members_instances

member_store = store.MembersStore()

store_should_add_models(members_instances, member_store)

stores_should_be_similar()

print_all_members(member_store)

get_by_id_should_retrieve_same_object(member_store, member2)

update_should_modify_object(member_store, member3)

catch_exception_when_deleting()

print_all_members(member_store)

print_same_names(member_store)


posts_instances = create_posts(members_instances)
post1, post2, post3, post4, post5, post6, post7, post8, post9 = posts_instances

post_store = store.PostsStore()

store_should_add_posts(posts_instances, post_store)

store_should_get_members_with_posts(member_store, post_store)

store_should_get_top_two(member_store, post_store)

print_by_date(post_store)


# POST STORE ------------------>>>>>>>


"""
def store_should_add_models(posts_instances, post_store):
    for post in posts_instances:
        post_store.add(post)

def stores_should_be_similar():

    post_stor1 = store.PostsStore()
    post_store2 = store.PostsStore()
    if post_stor1.get_all() is post_store2.get_all():
        print("Same stores elements !")


def print_all_posts(post_store):
    print("=" * 30)

    for post in post_store.get_all():
        print(post)

    print("=" * 30)

def get_by_id_should_retrieve_same_object(post_store, post2):
    post2_retrieved = post_store.get_by_id(post2.id)

    if post2 is post2_retrieved:
        print("post2 and post2_retrieved are matching !")


def update_should_modify_object(post_store, post3):
    post3_copy = models.Post(post3.title, post3.content)
    post3_copy.id = 3

    if post3_copy is not post3:
        print("post3 and post3_copy are not the same !")

    print(post3_copy)
    post3_copy.title = "Post3_C"
    post_store.update(post3_copy)
    print(post_store.get_by_id(post3.id))


def catch_exception_when_deleting():
    try:
        post_store.delete(10)
    except ValueError:
        print("It should be an existence entity before deleting !")


stores_should_be_similar()

print_all_posts(post_store)

get_by_id_should_retrieve_same_object(post_store, post2)

update_should_modify_object(post_store, post3)

catch_exception_when_deleting()

print_all_posts(post_store)
"""
