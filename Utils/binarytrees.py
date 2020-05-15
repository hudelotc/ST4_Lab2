#Exception
class InvalidOperationError(Exception): pass

#Constructors
def createEmptyTree():
    """ Gets a new empty tree.
        Input: nothing
        Output: an empty binary tree"""
    return {}

def createNode(e, l, r):
    """ Gets a new binary tree from a key and two subtrees.
        Input:  e, the key at the root of the new tree
                l, the left subtree (binary), eventually empty
                r, the right subtree (binary), eventually empty
        Output: a binary tree whose root contains e"""
    if isBinaryTree(l) and isBinaryTree(r):
        return {'key':e, 'left':l, 'right':r}
    else:
        raise InvalidOperationError("l or r is not a binary tree")

def createLeaf(e):
    """ Gets a new leaf of binary tree from a key.
        Input: e, the key at the root of the leaf
        Output: a leaf of binary tree whose root contains e"""
    return createNode(e, createEmptyTree(), createEmptyTree())

#Accessors	
def key(t):
    """ Gets the key of the root of t.
        Input:  t, a binary tree
        Output: an element of a Python's types"""
    
    if isEmptyTree(t):
        raise InvalidOperationError("Empty tree")
    else:
        return t['key']

def left(t):
    """ Gets the left subtree of t.
        Input:  t, a binary tree
        Output: a binary tree that represents the left subtree
                of t"""
    if isEmptyTree(t):
        raise InvalidOperationError("Empty tree")
    else:
        return t['left']

def right(t):
    """ Gets the right subtree of t.
        Input:  t, a binary tree
        Output: a binary tree that represents the right subtree
                of t"""
    if isEmptyTree(t):
        raise InvalidOperationError("Empty tree")
    else:
        return t['right']


def isEmptyTree(t):
    """ Indicates if a tree is empty or not.
        Input:  t, a binary tree
        Output: True if t is empty, False otherwise"""
    return t == {}

def leaves(t):
    """ Gets the list of leaves of t.
        Input:  t, a binary tree
        Output: a list of all leaves of t"""
    if isEmptyTree(t):
        return []
    elif isEmptyTree(left(t)) and isEmptyTree(right(t)):
        return [key(t)]
    else:
        return leaves(left(t)) + leaves(right(t))

def height(t):
    """ Gets the height of the tree.
        Input:  t, a binary tree
        Output: an integer that represents the height of t"""
    if isEmptyTree(t):
        return 0
    else:
        return 1 + max(height(left(t)), height(right(t)))
    
def isBinaryTree(t):
    """Tests if an object a is a binary tree.
		Input: t, a binary tree
		Output: a boolean that indicates if t is a binary tree or not"""
    if type(t)==dict:
        if t == {}:
            return True
        elif list(t.keys()) == ['right', 'key', 'left']:
            return (isBinaryTree (t['left'])) and (isBinaryTree (t['right']))
        else:
            return False
    else:
        return False		

def isLeaf(t):
    """Indicates if t is a leaf or not.
        Input: t, a binary tree
        Output: a boolean that indicates if t is a leaf or not"""
    return (not isEmptyTree(t)) and isEmptyTree(left(t)) and isEmptyTree(right(t))

def leafCount (t):
    """Gets the leaf count.
		Input: t, a binary tree
		Output: an int that represents the number of leaves in t"""
    if isEmptyTree(t):
        return 0
    elif isLeaf (t):
        return 1
    else:
        return leafCount (left(t)) + leafCount(right(t))

def internalNodeCount (t):
    """Gets the internal node count
		Input: t, a binary tree
		Output: an int that represents the number of internal nodes"""
    if isEmptyTree(t):
        return 0
    elif isLeaf(t):
        return 0
    else:
        return 1 + internalNodeCount(left(t)) + internalNodeCount(right(t))
		
#Traversal
def inorderTraversal(t):
    """ Displays all the nodes of t
            with a inorder depth-first traversal.
        Input: t, a binary tree
        Output: nothing"""
    if isEmptyTree(t):
        return
    else:
        inorderTraversal(left(t))
        print(key(t))
        inorderTraversal(right(t))
		
def postorderTraversal(t):
    """ Displays all the nodes of t
            with a postorder depth-first traversal.
        Input: t, a binary tree
        Output: nothing"""
    if isEmptyTree(t):
        return
    else:
        postorderTraversal(left(t))
        postorderTraversal(right(t))
        print(key(t))

def preorderTraversal(t):
    """ Displays all the nodes of t
            with a preorder depth-first traversal.
        Input: t, a binary tree
        Output: nothing"""
    if isEmptyTree(t):
        return
    else:
        print(key(t))
        preorderTraversal(left(t))
        preorderTraversal(right(t))
		
		
def breadthFirstTraversal(t):
    """ Displays all the nodes of t
            with a breadth first traversal.
        Input: t, a binary tree
        Output: nothing"""
    if isEmptyTree(t):
        return
    else:
        queue = createEmptyQueue()
        queue = enqueue(queue, t)
        while not isEmptyTree(queue):
            node = first(queue)
            queue = dequeue(queue)
            print(key(node))
            queue = enqueue(queue, left(node))
            queue = enqueue(queue, right(node))

#Operations
def mirror(t):
    """ Gets the image of t after mirror effect.
        Input:  t, a binary tree, eventually empty
        Output: a binary tree which is the image of t"""
    if isEmptyTree(t):
        return t
    else:
        return createNode( key(t),
                           mirror(right(t)),
                           mirror(left(t)))
			
			
#a tree example to play with in the console			
a = {'key': 1,
     'left': {'key':2,
                'left':{},
                'right':{}},
     'right': {'key':3,
                'left':{'key':4,
                          'left':{},
                          'right':{}},
                'right':{}}}
			
