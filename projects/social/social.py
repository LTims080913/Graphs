import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        possible_friendships = []
        for u in range(num_users):
            self.add_user("random name")
        for i1 in range(1, num_users + 1):
            for i2 in range(1, num_users + 1):
                if i1 < i2:
                    possible_friendships.append((i1, i2))
        random.shuffle(possible_friendships)
        for p in possible_friendships[:(num_users * avg_friendships) // 2]:
            self.add_friendship(p[0], p[1])
                    
        # Add users

        # Create friendships

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        seen = []
        queue = Queue()
        queue.enqueue(user_id)
        while queue.size() > 0:
            item = queue.dequeue()
            if item not in seen:
                seen.append(item)
                for adj in self.friendships[item]:
                    queue.enqueue(adj)
        
        for s in seen:
            visited[s] = self.bfs(user_id, s)

        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if starting_vertex == destination_vertex:
            return [starting_vertex]
        visited = []
        queue = Queue()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            path = queue.dequeue()
            v = path[-1]
            if v not in visited:
                for adj in self.friendships[v]:
                    new_path = list(path)
                    new_path.append(adj)
                    queue.enqueue(new_path)
                    if adj == destination_vertex:
                        return new_path

                visited.append(v)




if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)


# visited = []
# queue = Queue()
# queue.enqueue(starting_vertex)
# while queue.size() > 0:
#     item = queue.dequeue()
#     if item not in visited:
#         visited.append(item)
#         print(item)
#         for adj in self.vertices[item]:
#             queue.enqueue(adj)