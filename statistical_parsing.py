from nltk.tree import Tree

treebank = []
with open('idn_treebank_modified.bracket', 'r') as raw_treebank:
    for raw_tree in raw_treebank:
        tree = Tree.fromstring(raw_tree)
        tree.chomsky_normal_form()
        treebank.append(tree)
