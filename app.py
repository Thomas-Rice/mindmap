from anytree import *
from flask import request
from Application_Factory import Application_Factory
from Messages import *

af = Application_Factory()
app = af.create_app()
messages = Messages()
db = af.init_db(app)


class MindMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


class Leaf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map_name = db.Column(db.Text)
    path = db.Column(db.Text)
    text = db.Column(db.Text)


@app.route('/api/maps', methods=['POST'])
def create_mind_map():
    req_data = request.get_json()

    if 'id' in req_data:
        name = req_data['id']
        try:
            mind_map_model = create_mind_map(name)
        except(Exception):
            return messages.id_type

        add_model_to_db(mind_map_model)
        return messages.mind_map_crated(name)
    else:
        return messages.mindmap_missing_id


def create_mind_map(map_name):
    if isinstance(map_name, str):
        return MindMap(name=map_name)
    else:
        raise Exception(messages.mindmap_id_type)


def create_leaf(map_name, path, text):
    if isinstance(path, str) and isinstance(text, str):
        return Leaf(map_name=map_name, path=path, text=text)
    else:
        raise Exception(messages.path_and_text_type)


def add_model_to_db(model):
    db.session.add(model)
    db.session.commit()


@app.route('/api/maps/<map_name>', methods=['POST'])
def add_leaf(map_name):
    req_data = request.get_json()

    if 'path' not in req_data:
        return messages.path_and_text_error
    if 'text' not in req_data:
        return messages.path_and_text_error

    path = req_data['path']
    text = req_data['text']

    leaf = create_leaf(map_name, path, text)
    add_model_to_db(leaf)
    return messages.leaf_added(map_name, path, text)


@app.route('/api/maps/<map_name>/<path:path>', methods=['GET'])
def read_leaf(map_name, path):
    query = db.session.query(Leaf).filter(Leaf.map_name == map_name, Leaf.path == path).first()

    if query is None:
        return messages.read_leaf_missing_id_or_map

    result = (query.path, query.text)

    return format_leaf_results(result)


def format_leaf_results(result):
    return {'path': result[0], 'text': result[1]}


@app.route('/api/maps/<map_name>', methods=['GET'])
def print_tree(map_name):
    pretty = request.args.get('pretty')
    if pretty:
        result = db.session.query(Leaf).filter(Leaf.map_name == map_name).all()
        if not result:
            return Messages.read_tree_no_results

        leafs = split_path(result)

        nodes = create_node_tree(map_name, leafs)

        return output_tree(nodes)


def split_path(result):
    leafs = []
    for i, ele in enumerate(result):
        path = ele.path
        path = path.split("/")
        leafs.append(path)
    return leafs


def create_node_tree(map_name, leafs):
    nodes = [Node(map_name)]
    for leaf in leafs:
        for i, element in enumerate(leaf):
            if i is 0:
                nodes.append(Node(element, parent=nodes[0]))
            else:
                nodes.append(Node(element, parent=nodes[-1]))
    return nodes


def output_tree(nodes):
    test = ""
    for pre, fill, node in RenderTree(nodes[0]):
        test += ("\n%s%s" % (pre, node.name))

    return test


# app.run()
