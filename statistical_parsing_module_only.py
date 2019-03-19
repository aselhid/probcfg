from nltk.tree import Tree
from nltk.grammar import PCFG, Nonterminal
from nltk import induce_pcfg
from nltk.parse.viterbi import ViterbiParser
import json

treebank_cnf = []
with open('idn_treebank_modified_cleaned.bracket', 'r') as raw_treebank:
    for raw_tree in raw_treebank:
        tree = Tree.fromstring(raw_tree)
        tree.chomsky_normal_form(factor='left')
        treebank_cnf.append(tree)

r = []

for tree in treebank_cnf:
    r.extend(tree.productions())

S = Nonterminal('S')
pcfg = induce_pcfg(S, r)

viterbi = ViterbiParser(pcfg)
possible_trees = viterbi.parse(['saya', 'membeli', 'minyak', 'dan', 'air',
                                'kelapa_sawit', 'setiap', 'minggu', 'pagi'])

for tree in possible_trees:
    tree.draw()
