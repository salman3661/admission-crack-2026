"""Rebalance Paper Final tests by DU 'Ka' weighted chapter quota + interleave + repair LaTeX control chars."""
import json, re, random, collections
D = "admission_webapp/src/data/"
ld = lambda n: json.load(open(D + n, encoding="utf-8"))
sv = lambda n, d: json.dump(d, open(D + n, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---- LaTeX repair: \n,\t,\f,\b,\r control chars that were eaten from \nu \theta \frac \beta \rho
CTRL = {"\n": "n", "\t": "t", "\f": "f", "\b": "b", "\r": "r"}
FIXES = [(re.compile(r"\n(u|eq|abla|ot|i|e)(?![a-z])"), None)]
def fix_str(s):
    def span(m):
        t = m.group(0)
        t = re.sub(r"\n(?=(u|eq|abla|otin|i|eg|e|ot)(?![A-Za-z]))", r"\\n", t)
        t = re.sub(r"\t(?=(heta|au|imes|ext|o|an|ilde)\b|(heta|au|imes|ext|an|ilde))", r"\\t", t)
        t = re.sub(r"\f(?=rac|orall)", r"\\f", t)
        t = re.sub(r"\x08(?=eta|ar|inom)", r"\\b", t)
        t = re.sub(r"\r(?=ho|ight|ightarrow|m)", r"\\r", t)
        return t
    return re.sub(r"\$[^$]*\$", span, s)
repaired = 0
def walk(o):
    global repaired
    if isinstance(o, str):
        n = fix_str(o)
        if n != o: repaired += 1
        return n
    if isinstance(o, list): return [walk(x) for x in o]
    if isinstance(o, dict): return {k: walk(v) for k, v in o.items()}
    return o

syn = walk(ld("chapter_synthetic_predictors.json"))
bank = walk(ld("paper_final_bank.json"))
bp = {c["id"]: c for c in ld("master_chapter_blueprint.json")["chapters"]}

PHY1 = {1: 2.5, 2: 6.5, 3: 6.5, 4: 8.5, 5: 7.5, 6: 6.5, 7: 5.5, 8: 6.5, 9: 5.5, 10: 5.5}

def norm_paper(p): return "1" if ("১" in p or "1" in p) else "2"
def norm_subj(s): return "Higher Math" if "Math" in s else s

pools = collections.defaultdict(lambda: collections.defaultdict(list))
for ch in syn["chapters"]:
    cid = ch.get("chapter_id") or ""
    for p in ch["predictors"]:
        pools[(norm_subj(ch["subject"]), norm_paper(ch.get("paper", "")))][cid].append((ch, p))

def weights(subj, paper, cids):
    w = {}
    for cid in cids:
        c = bp.get(cid)
        if subj == "Physics" and paper == "1" and c: w[cid] = PHY1.get(int(cid.split("_")[-1]), 5)
        else:
            w[cid] = sum(t.get("repeat_frequency", 1) for t in c["mega_types"]) if c else 1
    return w

def quota(w, caps, total=60):
    tot = sum(w.values()); raw = {k: v / tot * total for k, v in w.items()}
    q = {k: min(max(1, int(v)), caps[k]) for k, v in raw.items()}
    while sum(q.values()) != total:
        if sum(q.values()) < total:
            k = max((k for k in q if q[k] < caps[k]), key=lambda k: raw[k] - q[k]); q[k] += 1
        else:
            k = max((k for k in q if q[k] > 1), key=lambda k: q[k] - raw[k]); q[k] -= 1
    return q

def interleave(items, key, rnd):
    items = items[:]; rnd.shuffle(items); out = []
    while items:
        for i, it in enumerate(items):
            if len(out) < 2 or not (key(out[-1]) == key(it) == key(out[-2])) and key(out[-1]) != key(it):
                out.append(items.pop(i)); break
        else:
            out.append(items.pop(0))
    return out

def to_q(conv, ch, p, idx, convert):
    return convert(p, ch, idx)

import importlib.util
spec = importlib.util.spec_from_file_location("b4", "build_4tier_banks.py"); b4 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b4)

report = []
for t in bank["tests"]:
    subj, paper = norm_subj(t["subject"]), norm_paper(t["paper"])
    pool = pools[(subj, paper)]
    rnd = random.Random(t["id"])
    caps_v = {cid: len(v) for cid, v in pool.items()}
    w = weights(subj, paper, list(pool))
    if t["track"] == "varsity":
        q = quota(w, {k: min(c, 99) for k, c in caps_v.items()})
        used_n = 0
        offset = 0
    else:
        # medical: take from the tail of each chapter pool so it differs from the varsity test
        q = quota(w, caps_v)
    picks = []
    for cid, n in q.items():
        lst = pool[cid]
        if t["track"] == "varsity": sel = lst[:n]
        else: sel = lst[::-1][:n]
        for i, (ch, p) in enumerate(sel): picks.append(b4.convert_synthetic_to_quiz(p, ch, i))
    t["mcqs"] = interleave(picks, lambda x: x["blueprint_chapter_id"], rnd)
    t["target_mcqs"] = len(t["mcqs"])
    if t["track"] == "medical":
        t["mcq_marks"] = t["total_marks"] = len(t["mcqs"])
    if t["written_questions"]: rnd.shuffle(t["written_questions"])
    runs = max((sum(1 for _ in g) for _, g in __import__("itertools").groupby(x["blueprint_chapter_id"] for x in t["mcqs"])), default=0)
    report.append((t["id"], len(t["mcqs"]), len(set(q.values())), runs, {k.split("_")[-1]: v for k, v in q.items()}))

bank["metadata"]["balance"] = "DU Ka weighted chapter quota, interleaved"
sv("paper_final_bank.json", bank)
sv("chapter_synthetic_predictors.json", syn)
for r in report: print(r)
print("repaired strings:", repaired)
