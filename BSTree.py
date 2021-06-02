import argparse

class Node():
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.value)

class BS_tree():
    def __init__(self):
        self.root = None

    def inorder(self, output):      # print the in-order traversal of binary search tree
        node_list = [] 
        node_list = self._inorder(self.root, node_list)
        node_str = ' '.join(map(str, node_list)) + ' ' + '\n'
        output.write(node_str)

    def _inorder(self, root, node_list):
        if root != None :
            self._inorder(root.left_child, node_list)
            node_list.append(str(root.value))
            self._inorder(root.right_child, node_list)
        else:
            pass

        return node_list


    def preorder(self, output):     # print the pre-order traversal of binary search tree
        node_list = [] 
        node_list = self._preorder(self.root, node_list)
        node_str = ' '.join(map(str, node_list)) + ' ' + '\n'
        output.write(node_str)

    def _preorder(self, root, node_list):
        if root != None :
            node_list.append(str(root.value))
            self._preorder(root.left_child, node_list)            
            self._preorder(root.right_child, node_list)
        else:
            pass

        return node_list

    def postorder(self, output):    # print the post-order traversal of binary search tree
        # TODO
        node_list = [] 
        node_list = self._postorder(self.root, node_list)
        node_str = ' '.join(map(str, node_list)) + ' ' + '\n'
        output.write(node_str)
      
    def _postorder(self, root, node_list):
        if root != None :           
            self._postorder(root.left_child, node_list)            
            self._postorder(root.right_child, node_list)
            node_list.append(str(root.value))
        else:
            pass

        return node_list
        
    def find_max(self, output):     # print the maximum number in binary search tree
        # TODO
        if self.root != None :
            max_node = self.root
            while max_node.right_child != None:
                max_node = max_node.right_child
            max_value = str(max_node.value)+'\n'
        
        output.write(max_value) 

    def find_min(self, output):     # print the minimum number in binary search tree
        min_value = str(self._find_min(self.root)) + '\n'
        output.write(min_value)

    def _find_min(self, root):
        if root != None :
            min_node = root
            while min_node.left_child != None:
                min_node = min_node.left_child
            min_value = min_node.value
            return min_value
        else:
            return None
    def insert(self, key):          # insert one node
        new_node = Node(key)
        self.root = self._insert(self.root, new_node)
        
    def _insert(self, root, node):
        if root == None :
            root = node
        else :
            if node.value  > root.value :
                root.right_child = self._insert(root.right_child, node)
            else:
                root.left_child = self._insert(root.left_child, node)
        return root
                
    def delete(self, key):          # delete one node
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root == None:
            return root
        elif key > root.value :
            root.right_child = self._delete(root.right_child, key)
        elif key < root.value :
            root.left_child = self._delete(root.left_child, key)
        else:
            #if the node only has one child or no child
            if root.left_child == None:
                temp = root.right_child
                root = None
                return temp
            elif root.right_child == None:
                temp = root.left_child
                root = None
                return temp
            #if the node has two childs
            else:
                #find the min value in right subtree
                min_value = self._find_min(root.right_child)
                root.value = min_value
                root.right_child = self._delete(root.right_child, min_value)
        return root


    def level(self, output):        # print the height of binary search tree(leaf = 0)
        root_level = str(self._level(self.root))+'\n'
        output.write(root_level)

    def _level(self, root):
        if root == None :
            return -1
        else:
            level = max(self._level(root.left_child), self._level(root.right_child))+1
            return level

    def internalnode(self, output): # print the internal node in binary search tree from the smallest to the largest 
        node_list = []
        node_list = self._internalnode(self.root, node_list)
        node_str = ' '.join(map(str, node_list)) + ' ' + '\n'
        output.write(node_str)

    def _internalnode(self, root, node_list):
        if root != None :
            self._internalnode(root.left_child, node_list)
            if root.left_child != None or root.right_child != None:
                node_list.append(str(root.value))
            self._internalnode(root.right_child, node_list)
        return node_list

    def leafnode(self, output):     # print the leafnode in BST from left to right
        node_list = []
        node_list = self._leafnode(self.root, node_list)
        node_str = ' '.join(map(str, node_list)) + ' ' + '\n'
        output.write(node_str)


    def _leafnode(self, root, node_list):
        if root != None :
            self._leafnode(root.left_child, node_list)
            if root.left_child == None and root.right_child == None:
                node_list.append(str(root.value))
            self._leafnode(root.right_child, node_list)
        return node_list

    def main(self, input_path, output_path):
        #########################
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # It's important and repeat three times
        #########################
        output = open(output_path, 'w')
        with open(input_path, 'r', newline='') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("insert"):
                    value_list = lines.split(' ')
                    for value in value_list[1:]:
                        self.insert(int(value))
                if lines.startswith('inorder'):
                    self.inorder(output)
                if lines.startswith('preorder'):
                    self.preorder(output)
                if lines.startswith('postorder'):
                    self.postorder(output)
                if lines.startswith('max'):
                    self.find_max(output)
                if lines.startswith('min'):
                    self.find_min(output)
                if lines.startswith('delete'):
                    value_list = lines.split(' ')
                    self.delete(int(value_list[1]))
                if lines.startswith('level'):
                    self.level(output)
                if lines.startswith('internalnode'):
                    self.internalnode(output)
                if lines.startswith('leafnode'):
                    self.leafnode(output)
        output.close()
if __name__ == '__main__' :
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default = './input_3.txt',help="Input file root.")
    parser.add_argument("--output", type=str, default = './output_3.txt',help="Output file root.")
    args = parser.parse_args()
    
    BS = BS_tree()
    BS.main(args.input, args.output)

    

