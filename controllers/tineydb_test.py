from tinydb import Query, TinyDB

data_base = TinyDB("test_.json")
# serialized_player_table = data_base.table('Player')
user = Query()


def insert_data_base():
    data_base.insert({"name": "joh", "age": 27})


insert_data_base()


def search():
    return data_base.search(user["name"] == "joh")


# t = search()
# print(t)
# t[0]['name'] = 'jonss'
# data_base.write_back()
def update():
    # serialized_player_table.update({'continat': '123'}, user.name == 'john')
    q = search()
    for l in q:
        if l["name"] == "joh":
            l["age"] = 30
        print("hhh", l)
    print("qqqq", q)
    data_base.save(q)


# update()

# update()
def remove():
    data_base.remove(user.name == "eoo")


# remove()
# update()
# print(data_base.all())
# serialized_player_table.update({'name': 'john5'}, user.name == 'john3')
# print(serialized_player_table.search(user.name=='john5'))

from itertools import permutations, combinations

print("======avant sorted======")
print(list(permutations(list(range(4)), 4)))
