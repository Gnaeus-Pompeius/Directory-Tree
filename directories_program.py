from unicodedata import name


class TreeNode:
    def __init__(self, name = "", left = None, right = None):
        self.name = name
        self.left = left
        self.right = right



def ls_print(curr, curr_root):
    if curr != None:
        ls_print(curr.left, curr_root)
        if curr != curr_root:
            print(curr.name)
        ls_print(curr.right, curr_root)

def iinsert(tree, name):
    if tree is None:
        return TreeNode(name)
    else:
        if tree.name == name:
            print("  Subdirectory with same name already in directory")
            return tree
        elif tree.name < name:
            tree.right = insert(tree.right, name)
        elif tree.name > name:
            tree.left = insert(tree.left, name)
    return tree

def insert(tree, name):
    if tree:
        if tree.name == name:
            print("  Subdirectory with same name already in directory")
            return tree
        elif name < tree.name:
            if tree.left is None:
                tree.left = TreeNode(name)
            else:
                tree.left = insert(name)
        elif name > tree.name:
            if tree.name is None:
                tree.right = TreeNode(name) 
            else:
                tree.right = insert(tree.right, name)
    else:
        tree.name = name


def inorderTraversal(self, root):
    res = []
    if root:
        res = self.inorderTraversal(root.left)
        res.append(root.data)
        res = res + self.inorderTraversal(root.right)
    return res

def iinsert(tree, name):
    if tree is None:
        return TreeNode(name)
    else:
        if tree.name == name:
            print("  Subdirectory with same name already in directory")
            return tree
        elif tree.name < name:
            tree.right = insert(tree.right, name)
        elif tree.name > name:
            tree.left = insert(tree.left, name)
    return tree

def iinsert(self, data):

    if self.name:
        if data < self.name:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        elif data > self.name:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)
    else:
        self.name = data
def move(curr, name):
    if curr == None:
        return None
    if curr.name == name:
        return curr
    if curr.name < name:
        if curr.right.name is not None:
            return move(curr.right, name)
    if curr.name > name:
        if curr.left.name is not None:
            return move(curr.left, name)
    return curr


    """
    if curr.left != None:
        if curr.left.name == dir:
            return curr.left
    if curr.right != None:
        if curr.right.name == dir:
            return curr.right
    else:
        print("  No folder with that name exists")
        return curr
"""

def move_back(root, curr):
    if root.left != None:
        if root.left == curr:
            return root.name 
    if root.right != None:
        if root.right == curr:
            return root.name
    if root.name < curr:
        if root.right != None:
            return move_back(root.right, curr)
        else:
            return move_back(root.left, curr)
    if root.name > curr:
        if root.left != None:
            return move_back(root.left, curr)
        else:
            return move_back(root.right, curr)
    return curr

def mmove_back(root, curr):
    if root.left == curr:
        return root.name
    if root.right == curr:
        return root.name

    if root.name < curr.name:
        if root.right is not None:
            return move_back(root.right, curr)
    if root.name > curr.name:
        if root.left is not None:
            return move_back(root.left, curr)
    
    #return curr

def sort(root):
    # Traverse / In-Order
    # (Vinstri-Node, Node, Hægri-Node)
    if root:
        sort(root.left)
        
        print(root.name)

        sort(root.right)

    





    



'''
Note that all the "if False" and "if True" are simply there to
give you the correct success and error message formats.
You can use if sentences or try catch or any other
means of programming you control flow.
You can make an encapsulting class for everything and start with that,
rather than starting with the single TreeNode("root").
Just make sure the input and output of the program is exactly as
specified and fits with the  expected_out.txt when the tester
program is run with the original commands.txt.
Then feel free to make your own, more extensive tests.'''

def run_commands_on_tree(tree):
    print("  current directory: " + tree.name)
    root = tree
    current = tree
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
            insert(current, command[1])
        elif command[0] == "ls":
            print("current directory: " + current.name)
            print("  Listing the contents of current directory, " + current.name)
            ls_print(current, current) # Add the name of the directory here

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            if command[1] == "..":
                if current == root:
                    print("Exiting directory program")
                    break
                current = move_back(root, current)
                print("current directory: " + str(current.name))
                
            else:
                if current != command[1]: 
                    next_curr = move(current, command[1])
                    if next_curr == None:
                        print("  No folder with that name exists")
                    else:
                        current = next_curr
                        print("  current directory: " + str(current.name)) # Add the name of the current directory here

        elif command[0] == "rm":
            print("  removing directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            if True:
                print("  directory successfully removed!")
            else:
                print("  No folder with that name exists")
        else:
            print("  command not recognized")





def run_directories_program():
    # YOU CAN CHANGE THE WHOLE THING IF YOU LIKE!!
    # YOU CAN DESIGN THIS DIFFERENTLY IF IT SUITS YOU
    run_commands_on_tree(TreeNode("root"))

if __name__ == "__main__":
    run_directories_program()
    
