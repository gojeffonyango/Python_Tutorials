def search(self, search_value):
    current_node = self.root
    while current_node:
        if search_value==current_node.data.value == search_value:
            return True
        elif search_value < current_node.data:
            current_node = current_node.left_child
        else:
            current_node = current_node.right_child
    return False