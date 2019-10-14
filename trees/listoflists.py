def buildTree(a):
    return [a, [], []]

def insertLeft(root,newBranch):     #root is the subtree and index 0 of root 
    t = root.pop(1)                 #represents value of subtree and index 1 and 2
    if len(t) > 1:                  #represents value of left child and right child of subtree
        root.insert(1,[newBranch,t,[]]) 
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = buildTree("a")
insertLeft(r,"b")
insertRight(r,"c")
l = getLeftChild(r)
insertRight(l,"d")
m = getRightChild(r)
insertLeft(m,"e")
insertRight(m,"f")
print(r)


