from nltk.tree import Tree
import json

treebank_raw = []
treebank_comps = []
with open('idn_treebank_modified_cleaned.bracket', 'r') as raw_treebank:
    for raw_tree in raw_treebank:
        tree = Tree.fromstring(raw_tree)
        treebank_raw.append(tree)
        tree.chomsky_normal_form(factor='left')
        treebank_comps.append(tree)

        
rules_raw = {}
rules_comps = {}
lhs_raw = {}
lhs_comps = {}
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

for tree in treebank_comps:
    for production in tree.productions():
        if production in rules_comps:
            rules_comps[production] += 1
        else:
            rules_comps[production] = 1
        
        current_lhs = production.lhs()
        if current_lhs in lhs_comps:
            lhs_comps[current_lhs] += 1
        else:
            lhs_comps[current_lhs] = 1

treebank_comps[0].draw()
# print(rules)

# probability_raw = {}
# probability_comps = {}
# for rule in rules_raw:
#     penyebut = lhs_raw[rule.lhs()]
#     probability_raw[rule.unicode_repr()] = rules_raw[rule]/penyebut

# for rule in rules_comps:
#     penyebut = lhs_comps[rule.lhs()]
#     probability_comps[rule.unicode_repr()] = rules_comps[rule]/penyebut

# for prob_raw in probability raw

# with open('dump.json', 'w') as rawdump:
#     json.dump(probability_raw, rawdump)

# print(probability)