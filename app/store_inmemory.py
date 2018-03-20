from app import models
from operator import attrgetter
import itertools, copy


class BaseStore():

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        result = None
        all_items_instance = self.get_all()
        for item_instance in all_items_instance:
            if id == item_instance.id:  # replaced is cuz The operators is and is not test for object identity: x is y is true if and only if x and y are the same object.
                result = item_instance
                break
        return result


    def update(self, item_instance):
        result = item_instance
        all_items_instance = self.get_all()
        for index, current_item_instance in enumerate(all_items_instance):
            if current_item_instance.id == item_instance.id:
                all_items_instance[index] = item_instance
        return result


    def delete(self, id):
        item_instance = self.get_by_id(id)
        self._data_provider.remove(item_instance)


    def entity_exist(self, item_instance):
        result = False
        if self.get_by_id(item_instance.id) is not None:
            result = True
        return result


# MEMBERS FUNCS --------------------->>>>>>

class MembersStore(BaseStore):
    members = []
    last_id = 1

    def __init__(self):
        super().__init__(MembersStore.members, MembersStore.last_id)


    #get_by_name STARTS... many generators or comprehension

    def get_by_name(self, member_name):
        return (member for member in self.get_all() if member.name == member_name)

    # (((def get_by_name(self, member_name):
    #   all = self.get_all()
    #  for memb in all:
    #     if str(member_name) == str(memb.name):
    #        yield memb

    # def get_by_name(self, member_name):
    #   return [member for member in self.get_all() if member.name == member_name]

    # def get_members_with_posts(self, all_posts):
    #  all_members = self.get_all()
    # for member in all_members:
    #    for post in all_posts:
    #       if member.id == post.member_id:
    #           member.posts.append(post)
    # return all_members)))
    # get_by_name ENDZ ...........


    def get_members_with_posts(self, all_posts):
        all_members = copy.deepcopy(self.get_all())

        for member, post in itertools.product(all_members, all_posts):
            if member.id == post.member_id:
                member.posts.append(post)

        for member in all_members:
            yield member

    def get_top_two(self, all_posts):
        all_members_posts = list(self.get_members_with_posts(all_posts))
        all_members_posts.sort(key=lambda x: len(x.posts), reverse=True)
        return all_members_posts[:10]



# POSTS CLASS ------------------------------>>>>>>>


class PostsStore(BaseStore):
    posts = []
    last_id = 1

    def __init__(self):
        super().__init__(PostsStore.posts, PostsStore.last_id)

    def get_posts_by_date(self, all_posts):
        all_posts.sort(key=lambda x: x.date, reverse=True)

        for post in all_posts:
            yield post
