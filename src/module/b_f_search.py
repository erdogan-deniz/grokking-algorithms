from collections import deque


graph = {
         "you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"],
         "alice": ["peggy"], "claire": ["thom", "jonny"],
         "anuj": [], "peggy": [], "thom": [], "jonny": []
        }


def is_seller(name: str):
    return name == "peggy"


def find_seller(name, names):
    searched_que = deque()
    searched_que += names[name]
    checked = []

    while searched_que:
        person = searched_que.popleft()

        if person not in checked:
            checked.append(person)

            if is_seller(person):
                print(f"Seller is {person}")

                return True
            else:
                searched_que += graph[person]

    return False


find_seller("you", graph)
