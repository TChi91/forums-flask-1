from app import models, db
from sqlalchemy import desc, func


class BaseStore():
    def __init__(self, data_provider):
        self.data_provider = data_provider

    def get_all(self):
        return self.data_provider.query.all()

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def get_by_id(self, id):
        return self.data_provider.query.get(id)

    def update(self, entity, fields):
        result = self.data_provider.query.filter_by(id = entity.id).update(fields)
        db.session.commit()
        return result

    def delete(self, id):
        result = self.data_provider.query.filter_by(id = id).delete()
        db.session.commit()
        return result

    def entity_exists(self, entity):
        result = True

        if self.get_by_id(entity.id) is None:
            result = False

        return result


# MEMBERS FUNCS --------------------->>>>>>

class MembersStore(BaseStore):
    members = []
    last_id = 1

    def __init__(self):
        super().__init__(models.Members)

    #get_by_name STARTS... many generators or comprehension

    def get_by_name(self, member_name):
        return self.data_provider.query.filter_by(name = member_name)

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


    def update(self, entity):
        fields = {"name": entity.name, "age": entity.age}
        return super().update(entity, fields)

    def get_members_with_posts(self):
        return self.data_provider.query.join(models.Members.posts)

    def get_top_two(self):
        return self.data_provider.query(PostsStore, func.count(models.Members.posts).label('total')).order_by('total DESC')


# POSTS CLASS ------------------------------>>>>>>>


class PostsStore(BaseStore):
    posts = []
    last_id = 1

    def __init__(self):
        super().__init__(models.Post)

    def get_posts_by_date(self, all_posts):
        all_posts.sort(key=lambda x: x.date, reverse=True)

        for post in all_posts:
            yield post

    def update(self, entity):
        fields = {"title": entity.title, "content": entity.content}
        return super().update(entity, fields)
