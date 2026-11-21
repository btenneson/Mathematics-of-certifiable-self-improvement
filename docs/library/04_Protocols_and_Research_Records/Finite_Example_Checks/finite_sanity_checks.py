"""Reproducible finite-example checks for W1--W3.

This is a small scenario checker, NOT formal verification of general theorems
and NOT validation of the empirical CAMI/FORGE architecture.
"""
from itertools import combinations, product
import unittest


def winning_with_budget(vertices, edges, controllers, targets, b):
    """Finite attractor on budget states; adversary edge overrun = failure."""
    win = {(t, r) for t in targets for r in range(b + 1)}
    while True:
        new = set(win)
        for x in vertices:
            if x in targets: continue
            for r in range(b + 1):
                arcs = edges[x]
                if x in controllers:
                    condition = any(c <= r and (y, r-c) in win for c,y in arcs)
                else:
                    condition = bool(arcs) and all(c <= r and (y, r-c) in win for c,y in arcs)
                if condition: new.add((x,r))
        if new == win: break
        win = new
    return win


def min_force(vertices, edges, controllers, targets, start, max_budget=30):
    for b in range(max_budget+1):
        if (start,b) in winning_with_budget(vertices,edges,controllers,targets,b):
            return b
    return float('inf')


def stable_partition(vertices, edges, labels):
    # Tuple of frozensets, deterministic sorted for reproducible logging.
    blocks = [frozenset(v for v in vertices if labels[v] == lab)
              for lab in sorted(set(labels.values()))]
    while True:
        lookup = {x:i for i,b in enumerate(blocks) for x in b}
        next_blocks = []
        for block in blocks:
            bysig = {}
            for x in sorted(block):
                sig = frozenset((c, lookup[y]) for c,y in edges[x])
                bysig.setdefault(sig, []).append(x)
            next_blocks.extend(frozenset(x) for x in bysig.values())
        if len(next_blocks) == len(blocks): return blocks
        blocks = next_blocks


def min_receipt_cover(H, domains):
    actions = sorted(domains)
    for k in range(1, len(actions)+1):
        for combo in combinations(actions, k):
            if set().union(*(domains[a] for a in combo)) >= set(H):
                return k, combo
    return float('inf'), None


def belief_winning_with_budget(B0, transitions, observations, targets, b):
    """Observation-based reachability with universally chosen observable replies."""
    from itertools import combinations
    X=sorted(transitions)
    allB=[]
    for k in range(1,len(X)+1):
        for subset in combinations(X,k):
            if len({observations[x] for x in subset}) == 1:
                allB.append(frozenset(subset))
    win={(B,r) for B in allB if B<=set(targets) for r in range(b+1)}
    while True:
        new=set(win)
        for B in allB:
            if B <= set(targets): continue
            common=set.intersection(*(set(transitions[x]) for x in B))
            for r in range(b+1):
                for a in common:
                    replies=set((c, observations[y]) for x in B for c,y in transitions[x][a])
                    good=True
                    for c,obs in replies:
                        Bnext=frozenset(y for x in B for d,y in transitions[x][a]
                                        if d==c and observations[y]==obs)
                        if c>r or (Bnext,r-c) not in win:
                            good=False;break
                    if good: new.add((B,r));break
        if new==win:return (frozenset(B0),b) in win
        win=new


class FiniteCases(unittest.TestCase):
    def test_W1_identical_cost_signatures(self):
        X=['x','y','t']
        E={'x':[(1,'t')], 'y':[(1,'t')], 't':[(0,'t')]}
        labels={'x':('controller','nonterminal'), 'y':('controller','nonterminal'), 't':('controller','target')}
        P=stable_partition(X,E,labels)
        self.assertTrue(any({'x','y'}==set(b) for b in P))
        self.assertEqual(min_force(X,E,set(X),{'t'},'x'),1)
        self.assertEqual(min_force(X,E,set(X),{'t'},'y'),1)

    def test_W2_equal_value_not_strongly_equivalent(self):
        X=['x','y','z','t']
        E={'x':[(1,'t')], 'y':[(1,'z')], 'z':[(0,'t')], 't':[(0,'t')]}
        labels={a:('controller','target' if a=='t' else 'nonterminal') for a in X}
        P=stable_partition(X,E,labels)
        self.assertFalse(any({'x','y'} <= set(b) for b in P))
        self.assertEqual(min_force(X,E,set(X),{'t'},'x'),1)
        self.assertEqual(min_force(X,E,set(X),{'t'},'y'),1)

    def test_W3_two_hidden_states(self):
        H=['L','R']
        domains={'u':{'L'}, 'v':{'R'}}
        self.assertEqual(min_receipt_cover(H,domains)[0],2)
        trans={'L':{'u':[(1,'t')],'v':[(1,'sink')]},
               'R':{'u':[(1,'sink')],'v':[(1,'t')]},
               't':{'u':[(0,'t')],'v':[(0,'t')]},
               'sink':{'u':[(0,'sink')],'v':[(0,'sink')]}}
        obs={'L':'hidden','R':'hidden','t':'target','sink':'sink'}
        self.assertFalse(belief_winning_with_budget({'L','R'},trans,obs,{'t'},10))
        self.assertTrue(belief_winning_with_budget({'L'},trans,obs,{'t'},1))
        self.assertTrue(belief_winning_with_budget({'R'},trans,obs,{'t'},1))

    def test_W3_pairwise_global_gap(self):
        H=[1,2,3]
        D={'a':{1,3},'b':{1,2},'c':{2,3}}
        self.assertEqual(min_receipt_cover(H,D)[0],2)
        for i,j in combinations(H,2):
            self.assertTrue(any({i,j} <= S for S in D.values()))
        self.assertFalse(any(set(H) <= S for S in D.values()))

    def test_W2_sampled_stable_quotients(self):
        import random
        rng=random.Random(1729)
        for _ in range(30):
            X=['0','1','2','3','t']
            owner={x:rng.choice(['C','A']) for x in X}
            owner['t']='C'
            edges={'t':[(0,'t')]}
            for x in X[:-1]:
                edges[x]=[(rng.randrange(4),rng.choice(X)) for _ in range(rng.randrange(1,4))]
            labels={x:(owner[x],x=='t') for x in X}
            P=stable_partition(X,edges,labels)
            q={x:str(i) for i,b in enumerate(P) for x in b}
            QX=sorted(set(q.values()))
            QE={}
            for i,b in enumerate(P):
                x=next(iter(b))
                QE[str(i)]=sorted(set((c,q[y]) for c,y in edges[x]))
            controls={x for x in X if owner[x]=='C'}
            qcontrols={q[x] for x in X if owner[x]=='C'}
            for x in X:
                self.assertEqual(min_force(X,edges,controls,{'t'},x,20),
                                 min_force(QX,QE,qcontrols,{q['t']},q[x],20))

    def test_W3_exhaustive_three_state_receipt_tables(self):
        H=[0,1,2]
        acts=['a','b','c']
        for mask in range(2**9):
            D={a:{x for x in H if (mask >> (3*i+x))&1}
               for i,a in enumerate(acts)}
            optimum,_=min_receipt_cover(H,D)
            scheme=float('inf')
            for k in range(1,4):
                valid=False
                for messages in product(range(k), repeat=3):
                    for action_choices in product(acts,repeat=k):
                        if all(x in D[action_choices[messages[x]]] for x in H):
                            valid=True;break
                    if valid: break
                if valid: scheme=k;break
            self.assertEqual(optimum,scheme)

    def test_W3_threshold_monotonicity(self):
        H=['L','R']; D1={'u':{'L'},'v':{'R'}}; D2={'u':{'L','R'},'v':{'R'}}
        self.assertLessEqual(min_receipt_cover(H,D2)[0],min_receipt_cover(H,D1)[0])


if __name__=='__main__':
    unittest.main(verbosity=2)
