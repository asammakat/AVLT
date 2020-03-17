from avlt import avlt
                
def printTree(cur):
    if cur == None:
        return
    else:
        printTree(cur.Left) 
        print("Key: ", cur.Key, "Height: ", cur.Height)
        printTree(cur.Right)

def testRightRotateRightOfParent():
    testTree = avlt(None, 0)

    testTree.insert(100)
    testTree.insert(50)
    testTree.insert(150)
    testTree.insert(40)
    testTree.insert(200)
    testTree.insert(75)
    testTree.insert(60)
    testTree.insert(55)  

    printTree(testTree.Root)  
    

def testRightRotateLeftOfParent():
    testTree = avlt(None, 0)

    testTree.insert(100)
    testTree.insert(150)
    testTree.insert(50)
    testTree.insert(25)
    testTree.insert(10)

    printTree(testTree.Root)


def testRightRotateAtRoot():
    testTree = avlt(None, 0)

    testTree.insert(100)
    testTree.insert(50)
    testTree.insert(25)

    printTree(testTree.Root)

    print("Size: ", testTree.Size)

def testLeftRotateAtRoot():
    testTree = avlt(None, 0)

    testTree.insert(100)
    testTree.insert(150)
    testTree.insert(200)

    printTree(testTree.Root)  

def testLeftRotateRightOfParent():
    testTree = avlt(None, 0)

    testTree.insert(100)
    testTree.insert(50)
    testTree.insert(150)
    testTree.insert(200)
    testTree.insert(250)    
    
    printTree(testTree.Root)  

def testLeftRotateLeftOfParent():
    testTree = avlt(None, 0)

    testTree.insert(100)
    testTree.insert(50)
    testTree.insert(200)
    testTree.insert(25)
    testTree.insert(250)
    testTree.insert(150)
    testTree.insert(125)
    testTree.insert(110)

    printTree(testTree.Root)  

def testRLAtRoot():
    testTree = avlt(None, 0)

    testTree.insert(100)
    testTree.insert(150)
    testTree.insert(125)

    printTree(testTree.Root)  


def testRLRightOfParent():
    testTree = avlt(None, 0)

    testTree.insert(100)
    testTree.insert(50)
    testTree.insert(200)
    testTree.insert(250)
    testTree.insert(225)

    printTree(testTree.Root)

def testRLLeftOfParent():
    testTree = avlt(None, 0)

    testTree.insert(100)
    testTree.insert(50)
    testTree.insert(150)
    testTree.insert(75)
    testTree.insert(60)

    printTree(testTree.Root)

def testLLAtRoot():
    testTree = avlt(None, 0)

    testTree.insert(100)
    testTree.insert(50)
    testTree.insert(75)

    printTree(testTree.Root)
def testLLRightOrParent():
    testTree = avlt(None, 0)

    testTree.insert(100)
    testTree.insert(50)
    testTree.insert(150)
    testTree.insert(75)
    testTree.insert(60)

    printTree(testTree.Root)

def testLLLeftOfParent():
    testTree = avlt(None, 0)
    
    testTree.insert(100)
    testTree.insert(50)
    testTree.insert(150)
    testTree.insert(25)
    testTree.insert(40)

    printTree(testTree.Root)

def testChars():
    testTree = avlt(None, 0)
    testTree.insert("Apple")

    printTree(testTree.Root)




def main():

    # testTree = avlt(None, 0)
    # print("ADD 7")
    # testTree.insert(7)
    # print("ADD 3")
    # testTree.insert(3)
    # print("ADD 9")
    # testTree.insert(9)
    # print("ADD 6")
    # testTree.insert(6)
    # print("ADD 10")
    # testTree.insert(10)
    # print("ADD 100")
    # testTree.insert(100)
    # print("ADD 4")
    # testTree.insert(4)
    
    # printTree(testTree.Root)

    testRightRotateAtRoot()
    testRightRotateLeftOfParent()
    testRightRotateRightOfParent()
    testLeftRotateAtRoot()
    testLeftRotateRightOfParent()
    testLeftRotateLeftOfParent()
    testRLAtRoot()
    testRLRightOfParent()
    testRLLeftOfParent()
    testLLAtRoot()
    testLLRightOrParent()
    testLLLeftOfParent()
     
    testChars()        

    print("END OF MAIN")

main()