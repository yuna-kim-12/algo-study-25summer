import sys
sys.stdin = open('n.txt')

n = int(input())
tree = {}

for _ in range(n):
    m, l, r = map(str, input().split())
    tree[m] = [l, r]

preO = []
inO = []
postO = []

#root->left->right
def preorder(root):
    if root != '.':
        preO.append(root)
        preorder(tree[root][0])
        preorder(tree[root][1])

#left-> root-> right
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        inO.append(root)
        inorder(tree[root][1])

#left-> right -> root
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        postO.append(root)


preorder('A')
inorder('A')
postorder('A')

print("".join(map(str, preO)))
print("".join(map(str, inO)))
print("".join(map(str, postO)))