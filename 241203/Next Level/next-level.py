_id, lv = input().split()


class user:
    def __init__(self, _id, lv):
        self._id = _id
        self.lv = lv


user1 = user("codetree",10)
user2 = user(_id, lv)

print(f"user {user1._id} lv {user1.lv}")
print(f"user {user2._id} lv {user2.lv}")