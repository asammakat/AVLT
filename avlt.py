'''A simple self balancing AVL tree '''

class avlt:
    def __init__(self, Root, Size):
        self.Root = Root
        self.Size = Size #Number of nodes in the tree

    class Node:
        def __init__(self, Key, Left, Right, Height):
            self.Key = Key # data in node
            self.Left = Left
            self.Right = Right
            self.Height = Height # the number of nodes downstream from current
    
    def getHeight(self, node):
        '''Calculate and return the height of node'''
        if node == None:
            return -1 
        else:
            return 1 + max([self.getHeight(node.Left), self.getHeight(node.Right)])

    def leftRotate(self, parent, N):
        '''Perform a left rotation at N'''
        R = N.Right
        A = N.Left
        B = R.Left
        C = R.Right

        # rotate at root
        if parent == None:
            self.Root = R
            R.Left = N
            N.Right = B
        # rotate to the left of parent
        elif N.Key < parent.Key:
            parent.Left = R
            R.Left = N
            N.Right = B
        # rotate to the right of parent
        else:
            parent.Right = R 
            R.Left = N 
            N.Right = B  

        #update heights
        N.Height = 1 + max(self.getHeight(A), self.getHeight(B))
        R.Height = 1 + max(self.getHeight(C), N.Height)

    def rightRotate(self, parent, N):
        '''Perform a right rotation at N'''
        L = N.Left
        A = L.Left
        B = L.Right
        C = N.Right

        # rotate at root
        if parent == None:
            self.Root = L
            L.Right = N
            N.Left = B
        # rotate to the left of parent
        elif N.Key < parent.Key:
            parent.Left = L
            L.Right = N
            N.Left = B
        # rotate to the right of parent
        else:
            parent.Right = L
            L.Right = N
            N.Left = B

        #update heights
        N.Height = 1 + max(self.getHeight(B),self. getHeight(C))
        L.Height = 1 + max(self.getHeight(A), N.Height)

    def updateAfterInsert(self, path):
        '''
        is sent the path of taken on insert and reverses it. Update the
        heights of the nodes along that path and check if at any node the 
        difference in heights is greater than one. If this condition is met
        perform the appropriate series of rotations
        '''
        #reverse the path so we can traverse back up the tree
        path.reverse()

        # end of path is marked with None, we do not want to use
        # this in the loop
        for i in range(len(path) - 1):
            node = path[i]

            # set height and check if updates are needed
            height = self.getHeight(node)
            
            # if heights match the rest of the tree is correct 
            if node.Height == height:
                return 
            else:
                node.Height = height

            #node.Height = height

            # check if rotations are necessary
            # lHeight and rHeight are the heights of the left and right nodes
            if node.Right == None:
                rHeight = -1
            else:
                rHeight = node.Right.Height
            if node.Left == None:
                lHeight = -1
            else:
                lHeight = node.Left.Height
            
            # if the difference of rHeight and lHeight is more than one rotate
            if abs(lHeight - rHeight) > 1:
                parent = path[i + 1]
                if lHeight > rHeight:
                    # Left leaning at node and node.Left
                    if (self.getHeight(node.Left.Left) 
                        > self.getHeight(node.Left.Right)):
                         self.rightRotate(parent, node)
                    # Left leaning at node and right leaning at node.Left
                    else:
                        self.leftRotate(node, node.Left)
                        self.rightRotate(parent, node)
                else:
                    # right leaning at node and node and node.Right
                    if (self.getHeight(node.Right.Right) 
                        > self.getHeight(node.Right.Left)):
                        self.leftRotate(parent, node)
                    # right leaning ar node and right leaning at node.Right
                    else:
                        self.rightRotate(node, node.Right)
                        self.leftRotate(parent, node)


    
    def insert(self, key):
        '''Insert a node into the tree'''
        path = [] # store the nodes we visit while inserting
        newNode = self.Node(key, None, None, -1) # Node to be inserted
        #insert at root
        if self.Root == None:
            newNode.Height = 0
            self.Root = newNode
            self.Size += 1
        else:
            temp = self.Root
            # because temp will fall out of the tree we much keep track 
            # of the previous node visited
            prev = None 
            while(temp != None): # loop until temp falls out of the tree
                path.append(prev) # store current node 
                prev = temp
                # tree does not contain duplicates
                if key == temp.Key:
                    return
                elif key > temp.Key:
                    temp = temp.Right
                else:
                    temp = temp.Left

            path.append(prev) #last instance of prev has not been appended
            self.Size += 1
            # insert new node
            if(key < prev.Key):
                prev.Left = newNode
            else:
                prev.Right = newNode
        
        # include new node in the path
        path.append(newNode)

        #update the heights after insert and check if rotations are needed
        self.updateAfterInsert(path)