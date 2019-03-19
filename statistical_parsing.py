from nltk.tree import Tree
import json

treebank_raw = []
treebank_cnf = []
with open('idn_treebank_modified_cleaned.bracket', 'r') as raw_treebank:
    for raw_tree in raw_treebank:
        tree = Tree.fromstring(raw_tree)
        treebank_raw.append(tree)

        tree = tree.copy(deep=True)
        tree.chomsky_normal_form(factor='left')
        treebank_cnf.append(tree)

lexical_count = {}
rules_raw = {}
rules_cnf = {}
lhs_raw = {}
lhs_cnf = {}
probability_raw = {}
probability_cnf = {}

"""
The count of lexical rule probably will change on A -> B removal.
Keep the count of lexical rule before removal.
"""
for tree in treebank_cnf:
    for production in tree.productions():
        if production.is_lexical() and len(production.rhs()) == 1:
            if production in lexical_count:
                lexical_count[production] += 1
            else:
                lexical_count[production] = 1

# Remove A -> B where A,B is nonterminal.
for tree in treebank_cnf:
    for subtree in tree.subtrees(filter=lambda x: len(x) == 1 and not isinstance(x[0], str)):
        new_child = subtree[0]
        subtree.clear()
        subtree.extend(new_child)

for tree in treebank_raw:
    for production in tree.productions():
        if production in rules_raw:
            rules_raw[production] += 1
        else:
            rules_raw[production] = 1

        current_lhs = production.lhs()
        if current_lhs in lhs_raw:
            lhs_raw[current_lhs] += 1
        else:
            lhs_raw[current_lhs] = 1

for tree in treebank_cnf:
    for production in tree.productions():
        if production in rules_cnf:
            rules_cnf[production] += 1
        else:
            rules_cnf[production] = 1

        current_lhs = production.lhs()
        if current_lhs in lhs_cnf:
            lhs_cnf[current_lhs] += 1
        else:
            lhs_cnf[current_lhs] = 1

for rule in rules_raw:
    denumerator = lhs_raw[rule.lhs()]
    probability_raw[rule.unicode_repr()] = rules_raw[rule] / denumerator

for rule in rules_cnf:
    denumerator = lhs_cnf[rule.lhs()]
    probability_cnf[rule.unicode_repr()] = rules_cnf[rule] / denumerator

# for prob_raw in probability raw

# with open('dump.json', 'w') as rawdump:
#     json.dump(probability_raw, rawdump)

# print(probability)
