import json, ast, re, random
random.seed(2026)
def load(f): return json.load(open(f))
bank = load('varsity_bank.json')+load('medical_bank.json')+load('weekly_exams.json')
def lst(o):
    if isinstance(o,str):
        try: o=ast.literal_eval(o)
        except Exception: return None
    return o if isinstance(o,list) else None
CH = {  # chapter keyword -> (name, per-set count)
 'ভেক্টর':('Vectors',6),'নিউটনীয়':('Newtonian Mechanics',6),'গতিবিদ্যা ও প্রক্ষেপক':('Newtonian Mechanics',4),
 'কাজ, শক্তি':('Work-Power-Energy',10),'মহাকর্ষ':('Gravitation',8),'গাঠনিক':('States of Matter',7),
 'পর্যায়বৃত্ত':('Periodic Motion',7),'তরঙ্গ':('Waves',6),'আদর্শ গ্যাস':('Ideal Gas',6)}
def key(x): return re.sub(r'\W+','',re.sub(r'^\[[^\]]*\]','',x['q']))[:80]
seen=set(); pool={}
for x in bank:
    if x.get('subject')!='Physics': continue
    ck=next((k for k in CH if k in x.get('chapter','')),None)
    o=lst(x.get('opts')); 
    try: a=int(x['ans'])
    except Exception: continue
    if not ck or not o or len(o)!=4 or not 0<=a<4 or len(set(o))<4: continue
    if len(set(o))<4 or key(x) in seen: continue
    seen.add(key(x)); x['_o']=o; x['_a']=a
    pool.setdefault(ck,[]).append(x)
sets=[[],[]]
quota={}
for ck,(name,n) in CH.items(): quota[ck]=n
def cap(ck): return len(pool.get(ck,[]))//2
short=0
for ck in quota:
    if cap(ck)<quota[ck]: short+=quota[ck]-cap(ck); quota[ck]=cap(ck)
while short:
    for ck in quota:
        if short and cap(ck)>quota[ck]: quota[ck]+=1; short-=1
for ck,(name,_) in CH.items():
    n=quota[ck]; p=pool.get(ck,[]); random.shuffle(p)
    sets[0]+= [(name,q) for q in p[:n]]; sets[1]+=[(name,q) for q in p[n:2*n]]
assert all(len(s)==60 for s in sets),[len(s) for s in sets]
W=json.load(open('physics_written_bank.json'))
L='ABCD'
out=['# Physics 1st Paper — Paper Final Model Tests (2 Sets)\n',
 'Each set: **Section A** 60 MCQ (1 mark) + **Section B** 16 written (2.5 marks each = 40). Use g = 10 m/s² unless stated (g = 9.8 where given). MCQs are drawn from the workspace banks (deduplicated, no question repeats across sets); written questions are newly authored.\n']
for i,s in enumerate(sets):
    out.append(f'\n---\n\n# MODEL TEST SET {"AB"[i]}\n\n## Section A — MCQ (60)\n')
    for n,(ch,q) in enumerate(s,1):
        t=re.sub(r'^\[[^\]]*\]\s*','',q['q'])
        out.append(f'**{n}.** *({ch})* {t}\n'+'\n'.join(f'   - ({L[j]}) {o}' for j,o in enumerate(q['_o']))+'\n')
    out.append(f'\n### Answer Key & Speed Hacks — Set {"AB"[i]}\n\n| Q | Ans | Hack |\n|---|---|---|')
    for n,(ch,q) in enumerate(s,1):
        h=(q.get('speed_hack') or q.get('exp') or '').replace('\n',' ').replace('|','/')
        out.append(f'| {n} | {L[q["_a"]]} | {h} |')
    out.append(f'\n## Section B — Written (16 × 2.5 = 40)\n')
    for n,w in enumerate(W[i],1):
        out.append(f'**{n}.** ({w["ch"]}) {w["q"]}\n')
    out.append(f'\n### Written Solutions — Set {"AB"[i]}\n')
    for n,w in enumerate(W[i],1):
        out.append(f'**{n}.** {w["sol"]}\n')
open('physics_paper_final_model_tests.md','w').write('\n'.join(out))
print('ok')
