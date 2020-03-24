# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode()
        self.insert("/", handler)

    def insert(self, path, handler):
        curr_node = self.root
        for component in path:
            if component not in curr_node.children:
                curr_node.insert(component)
            curr_node = curr_node.children[component]
        curr_node.handler = handler

    def find(self, path):
        curr_node = self.root
        for component in path:
            if component not in curr_node.children:
                return None
            curr_node = curr_node.children[component]
        return curr_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.


class RouteTrieNode:
    def __init__(self):
        self.handler = None
        self.children = {}

    def insert(self, component):
        self.children[component] = RouteTrieNode()

# The Router class will wrap the Trie and handle


class Router:
    def __init__(self, handler, not_found_handler=None):
        self.root = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path=None, handler=None):
        if type(path) is not str or path is None or len(path) == 0:
            return "Please check input"
        self.root.insert(self.split_path(path), handler)

    def lookup(self, path=None):
        if type(path) is not str or path is None or len(path) == 0:
            return "Please check input"
        handler = self.root.find(self.split_path(path))
        return handler if handler else self.not_found_handler

    def split_path(self, path):
        components = path.split("/")
        components[0] = "/"
        if components[-1] == "":
            return components[:-1]
        return components


router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))

# Edge case
print(router.lookup(""))  # should print 'Please check input'
print(router.lookup())  # should print 'Please check input'
