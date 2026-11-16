"""Rebuild separated QB pools from existing in-repo data (no fabricated questions)."""
import json, re, collections, shutil
D='admission_webapp/src/data/'
ld=lambda f:json.load(open(D+f+'.json'))
V,M,W=ld('varsity_bank'),ld('medical_bank'),ld('weekly_exams')
key=lambda x:re.sub(r'\s+',' ',re.sub(r'^\[.*?\]\s*','',x.get('question') or x.get('q') or '')).strip()
tags=lambda x:' '.join(str(x.get(k) or '') for k in ('origin','tag','source_book'))
is_mat=lambda x:bool(re.search(r'MAT|DAT|Medical|মেডি',tags(x)))
is_du=lambda x:bool(re.search(r'DU|Varsity|Hubohu|Udvash|ঢাবি',tags(x)))
# repeat stats across every bank
occ=collections.defaultdict(set)
for L in (V,M,W):
    for x in L:
        for m in re.findall(r"(?:DU|MAT|DAT)[^|,;\]]*?\d{2,4}(?:-\d{2})?|DU Hubohu|DU Repeat|MAT Direct|MAT Line",tags(x)): occ[key(x)].add(m.strip())
chap=collections.Counter()
for L in (V,W):
    for x in L:
        if is_du(x): chap[x.get('blueprint_chapter_id') or x.get('chapter')]+=1
# Medical: strictly MAT/DAT-tagged
M2=[x for x in M if is_mat(x)]
seen=set(); M3=[]
for x in M2:
    k=key(x)
    if k in seen: continue
    seen.add(k); x['bank_type']='medical'; M3.append(x)
# Varsity: bank + DU/Varsity-tagged weekly, excluding MAT-only
seen=set(); V3=[]
for x in V+[w for w in W if is_du(w)]:
    k=key(x)
    if k in seen or (is_mat(x) and not is_du(x)): continue
    seen.add(k); x['bank_type']='varsity'; V3.append(x)
# Enrich
def enrich(x):
    k=key(x); n=max(len(occ.get(k,())),1 if (is_du(x) or is_mat(x)) else 0)
    x['repeat_count']=n
    x['origin_badge']=x.get('origin') or ('DU' if is_du(x) else 'MAT' if is_mat(x) else '')
    if is_du(x) or occ.get(k):
        x['du_repeat_tag']=f"{x['origin_badge']} | Repeated {n}x | চ্যাপ্টারে {chap.get(x.get('blueprint_chapter_id') or x.get('chapter'),0)}টি DU/Varsity প্রশ্ন"
for L in (V3,M3,W): [enrich(x) for x in L]
for x in W: x['bank_type']='weekly'
for name,L in (('varsity_bank',V3),('medical_bank',M3),('weekly_exams',W)):
    s=json.dumps(L,ensure_ascii=False,indent=2)
    for p in (D,'src/data/','./'):
        open(p+name+'.json','w').write(s)
for n in ('questions','quizzes'):
    for p in ('src/data/','./'):
        try: shutil.copy(D+n+'.json',p+n+'.json')
        except Exception as e: print(e)
print('varsity',len(V3),'medical',len(M3),'weekly',len(W),'V&M overlap',len({key(x) for x in V3}&{key(x) for x in M3}))
