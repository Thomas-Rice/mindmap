class Messages:
    path_and_text_error = "This Request needs path and text data \n path: 'Test' \n text: 'Test'"
    id_type = "id must be of type string"
    mindmap_missing_id = "<h1>id needs to be supplied in order to create a new mind map \n { 'id' : 'my-map'} </h1>"
    read_leaf_missing_id_or_map = "No Results Found For The Combination Of Map ID and Path - Please Use Check Map ID & Path Are Correct"
    path_and_text_type = "path & text must be of type string"
    read_tree_no_results = "No Results Found for Given Map Name - Check If Map Exists"

    def mind_map_crated(self, name):
        return f"Created MindMap with name: {name} "

    def leaf_added(self, map_name, path, text):
        return f"Created Leaf in MindMap: {map_name} with path: {path} and text: {text} "