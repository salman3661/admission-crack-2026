import json, ast, re, random, math
from fractions import Fraction
rnd = random.Random(2026)
def load(f): return json.load(open(f))
bank = load('varsity_bank.json')+load('medical_bank.json')+load('weekly_exams.json')
def lst(o):
    if isinstance(o,str):
        try: o=ast.literal_eval(o)
        except Exception: return None
    return o if isinstance(o,list) else None
CHK = {'ভেক্টর':'Vectors','নিউটনীয়':'Newtonian Mechanics','গতিবিদ্যা ও প্রক্ষেপক':'Newtonian Mechanics','কাজ, শক্তি':'Work-Power-Energy',
 'মহাকর্ষ':'Gravitation','গাঠনিক':'States of Matter','পর্যায়বৃত্ত':'Periodic Motion','তরঙ্গ':'Waves','আদর্শ গ্যাস':'Ideal Gas'}
QUOTA = {'Vectors':6,'Newtonian Mechanics':10,'Work-Power-Energy':10,'Gravitation':8,'States of Matter':7,'Periodic Motion':7,'Waves':6,'Ideal Gas':6}
def key(x): return re.sub(r'\W+','',re.sub(r'^\[[^\]]*\]','',x['q']))[:80]
seen=set(); pool={c:[] for c in QUOTA}; allc={c:[] for c in QUOTA}
for x in bank:
    if x.get('subject')!='Physics': continue
    ck=next((v for k,v in CHK.items() if k in x.get('chapter','')),None)
    if not ck: continue
    allc[ck].append(x)
    o=lst(x.get('opts'))
    try: a=int(x['ans'])
    except Exception: continue
    if not o or len(o)!=4 or not 0<=a<4 or len(set(o))<4 or key(x) in seen: continue
    seen.add(key(x)); x['_o']=o; x['_a']=a; pool[ck].append(x)
# chapter stats from bank (honest, data-derived)
stat={}
for c,v in allc.items():
    n=len(v); r2=sum(1 for x in v if str(x.get('repeat_count','0')).isdigit() and int(x['repeat_count'])>=2)
    stat[c]=(n,r2,round(100*r2/n))
# ---------- generated MCQs ----------
def f(x):
    if isinstance(x,Fraction): x=float(x)
    return ('%g'%round(x,3))
def mc(q,ans,dis,hack,trap): return dict(q=q,ans=ans,dis=dis,hack=hack,trap=trap)
G={c:[] for c in QUOTA}
def gen(c):
    def d(fn): G[c].append(fn); return fn
    return d
@gen('Vectors')
def _():
    a=rnd.choice([2,3,4,5,6]);b=rnd.choice([2,4,6,8,10]);s,t=rnd.choice([(30,'1/2'),(60,'√3/2'),(90,'1')])
    ans={'1/2':f(a*b/2),'√3/2':f(a*b)+'√3/2' if False else f"{a*b//2}√3" if (a*b)%2==0 else f"{a*b}√3/2",'1':f(a*b)}[t]
    ds=[f(a*b), f(a*b/2), f(a+b)]+[f"{a*b}√3"]
    return mc(f"Two vectors of magnitude {a} and {b} act at {s}°. What is |A × B|?",ans,[x for x in ds if x!=ans][:3],"|A×B| = AB sinθ (cross → sin, dot → cos).","Using cosθ instead of sinθ.")
@gen('Vectors')
def _():
    p,q_,r=rnd.choice([(2,3,3),(4,2,2),(3,3,1),(6,2,3),(4,4,2)]);m=Fraction(p*r,q_)
    ans=f(-m)
    return mc(f"For what value of m are A = {q_}i + {p}j and B = m i + {r}j perpendicular? (here A·B = 0)",f(-Fraction(p*r,q_)),[f(Fraction(p*r,q_)),f(Fraction(q_*r,p)),f(-Fraction(q_*r,p))],"Perpendicular ⇒ A·B = 0, so m·q + p·r = 0.","Sign error: m comes out negative.") if len({f(-Fraction(p*r,q_)),f(Fraction(p*r,q_)),f(Fraction(q_*r,p)),f(-Fraction(q_*r,p))})==4 else None
@gen('Vectors')
def _():
    k=rnd.choice([2,3,4,5,6,7]);a,b=rnd.choice([(3,4),(5,12),(8,15)]);R=int(math.hypot(a,b))*k
    return mc(f"Two perpendicular forces of {a*k} N and {b*k} N act at a point. The magnitude of the resultant is:",f"{R} N",[f"{(a+b)*k} N",f"{abs(b-a)*k} N",f"{R+k} N"],"Pythagorean triple × k.","Adding magnitudes arithmetically.")
@gen('Vectors')
def _():
    a=rnd.randint(2,5);b=rnd.randint(1,4);c=rnd.randint(2,5);d=rnd.randint(1,4);e=rnd.randint(1,3);g_=rnd.randint(1,3)
    dot=a*c+b*d+e*g_
    return mc(f"If A = {a}i + {b}j + {e}k and B = {c}i + {d}j + {g_}k, then A·B = ?",str(dot),[str(dot+2),str(dot-3),str(a*c+b*d)],"Multiply like components and add; no cross terms.","Forgetting the k·k term.")
@gen('Newtonian Mechanics')
def _():
    u=rnd.choice([10,15,20,25,30]);a=rnd.choice([2,2.5,4,5]);s=u*u/(2*a)
    return mc(f"A car moving at {u} m/s decelerates uniformly at {f(a)} m/s². Its stopping distance is:",f"{f(s)} m",[f"{f(u/a)} m",f"{f(u*u/a)} m",f"{f(s/2)} m"],"s = u²/2a (v=0).","Dropping the factor 2 or using u/a (time).")
@gen('Newtonian Mechanics')
def _():
    m=rnd.choice([0.2,0.5,1,2]);v=rnd.choice([10,20,30]);t=rnd.choice([0.01,0.02,0.05,0.1]);F=2*m*v/t
    return mc(f"A {f(m)} kg ball hits a wall at {v} m/s and rebounds at the same speed, contact time {f(t)} s. Average force:",f"{f(F)} N",[f"{f(F/2)} N",f"{f(F*2)} N",f"{f(m*v/(2*t)*3)} N"],"Elastic rebound: Δp = 2mv; F = Δp/t.","Using Δp = mv (ignoring reversal).")
@gen('Newtonian Mechanics')
def _():
    a=rnd.choice([30,60]);ans=5 if a==30 else 8.66
    th={30:'5',60:'5√3'}[a]
    return mc(f"A block slides on a smooth {a}° incline (g = 10 m/s²). Its acceleration is:",f"{th} m/s²",["10 m/s²",{30:'5√3',60:'5'}[a]+" m/s²","5/2 m/s²"],"Smooth incline: a = g sinθ.","Using cosθ instead of sinθ.") if True else None
@gen('Newtonian Mechanics')
def _():
    m1,m2=rnd.choice([(1,3),(2,6),(3,5),(2,4),(1,2),(4,12)]);a=Fraction(m2-m1,m1+m2)*10
    return mc(f"In an Atwood machine, masses are {m1} kg and {m2} kg (g = 10). Acceleration is:",f(a)+" m/s²",[f((m2-m1)*10/(m2))+" m/s²",f(Fraction(m1+m2,m2-m1)*10)+" m/s²",f(Fraction(m2-m1,2)*10/2)+" m/s²"],"a = (m₂−m₁)g/(m₁+m₂).","Dividing by m₂ only.")
@gen('Newtonian Mechanics')
def _():
    m=rnd.choice([40,50,60,80]);a=rnd.choice([2,5]);
    return mc(f"A {m} kg man stands in a lift accelerating upward at {a} m/s² (g = 10). Apparent weight:",f"{m*(10+a)} N",[f"{m*(10-a)} N",f"{m*10} N",f"{m*a} N"],"Up: m(g+a); down: m(g−a).","Mixing up up/down sign.")
@gen('Work-Power-Energy')
def _():
    m=rnd.choice([100,200,400,500]);h=rnd.choice([10,20,30]);t=rnd.choice([10,20,40]);P=m*10*h/t
    return mc(f"A pump raises {m} kg of water through {h} m in {t} s (g = 10). Power required:",f"{f(P)} W",[f"{f(P*t/10)} W",f"{f(m*h/t)} W",f"{f(P/2)} W"],"P = mgh/t.","Forgetting g.")
@gen('Work-Power-Energy')
def _():
    k=rnd.choice([100,200,400,800]);x=rnd.choice([0.1,0.2,0.05]);U=k*x*x/2
    return mc(f"A spring (k = {k} N/m) is stretched {f(x*100)} cm. Stored energy:",f"{f(U)} J",[f"{f(k*x)} J",f(k*x*x)+" J",f(k*x*x/2*100)+" J"],"U = ½kx²; convert cm→m first.","Leaving x in cm.")
@gen('Work-Power-Energy')
def _():
    F=rnd.choice([20,30,50,100]);d=rnd.choice([4,5,10]);
    return mc(f"A force of {F} N at 60° to the horizontal drags a body {d} m. Work done:",f"{f(F*d/2)} J",[f"{F*d} J",f"{f(F*d*math.sqrt(3)/2)} J" if False else f"{f(F*d/2)}√3 J","0"],"W = Fd cosθ; cos60° = ½.","Using sin60°.")
@gen('Work-Power-Energy')
def _():
    n=rnd.choice([2,3,4]);
    return mc(f"If the speed of a car becomes {n} times, its kinetic energy becomes:",f"{n*n} times",[f"{n} times",f"{n*2} times",f"{f(1/n)} times"],"KE ∝ v².","Choosing linear scaling.")
@gen('Gravitation')
def _():
    k=rnd.choice([1,2,3]);return mc(f"The acceleration due to gravity at a height {k}R above Earth's surface (surface value g) is:",f"g/{(k+1)**2}",[f"g/{k+1}",f"g/{k*k}",f"g/{2*k}"],"g' = g[R/(R+h)]².","Using R/h or forgetting the square.")
@gen('Gravitation')
def _():
    M,Rr=rnd.choice([(2,1),(4,1),(8,2),(9,3),(16,2),(4,2)]);g=Fraction(M,Rr*Rr)
    return mc(f"A planet has {M} times Earth's mass and {Rr} times Earth's radius. Its surface g relative to Earth's:",f"{f(g)} g",[f"{M*Rr} g",f"{f(Fraction(M,Rr))} g",f"{f(Fraction(Rr*Rr,M))} g"],"g ∝ M/R².","Using R instead of R².") if len({f(g),str(M*Rr),f(Fraction(M,Rr)),f(Fraction(Rr*Rr,M))})==4 else None
@gen('Gravitation')
def _():
    n=rnd.choice([4,9,16,25]);r=int(math.sqrt(n))
    return mc(f"A planet's orbital radius is {n} times that of Earth. Its orbital period in years (Kepler III):",f"{f(n**1.5)}",[f(n),f(n*n),f(r)],"T² ∝ r³ ⇒ T = r^{3/2}.","Treating T ∝ r.") if True else None
@gen('Gravitation')
def _():
    k=rnd.choice([2,3,4]);return mc(f"The orbital speed near Earth is v₀. The escape velocity is:",f"√2 v₀",["2 v₀","v₀/√2","v₀"],"vₑ = √2 v₀ (11.2 vs 7.9 km/s).","Forgetting the √2.")
@gen('Gravitation')
def _():
    d=rnd.choice([2,3,4,5]);return mc(f"At depth R/{d} below the surface, g becomes (surface g):",f"{f(Fraction(d-1,d))} g",[f"{f(Fraction(1,d))} g",f"{f(Fraction(d,d-1))} g",f"{f(Fraction(1,d*d))} g"],"Inside: g' = g(1 − d/R).","Applying the square-law outside formula.")
@gen('States of Matter')
def _():
    F=rnd.choice([100,200,400]);L=rnd.choice([1,2,4]);A=rnd.choice([1,2,4]);l=rnd.choice([1,2]);Y=F*L/(A*1e-6*l*1e-3)
    return mc(f"A wire ({L} m, {A} mm²) extends {l} mm under {F} N. Young's modulus:",f"{Y:.1e} Pa",[f"{Y*1000:.1e} Pa",f"{Y/1000:.1e} Pa",f"{Y*10:.1e} Pa"],"Y = FL/(Aℓ); mm² → 10⁻⁶ m², mm → 10⁻³ m.","Unit conversion errors.")
@gen('States of Matter')
def _():
    T=rnd.choice([0.02,0.03,0.05,0.07]);r=rnd.choice([0.01,0.02,0.05]);P=4*T/r
    return mc(f"Excess pressure inside a soap bubble of radius {f(r*100)} cm (T = {f(T)} N/m):",f"{f(P)} Pa",[f"{f(2*T/r)} Pa",f"{f(8*T/r)} Pa",f"{f(4*T*r)} Pa"],"Soap bubble (2 surfaces): 4T/r; drop: 2T/r.","Using 2T/r for a bubble.")
@gen('States of Matter')
def _():
    n=rnd.choice([2,3,4]);return mc(f"If the radius of a capillary tube is made 1/{n}, the rise of liquid becomes:",f"{n} times",[f"{n*n} times",f"1/{n} times",f"{f(math.sqrt(n))} times"],"h ∝ 1/r.","Squaring the ratio.")
@gen('States of Matter')
def _():
    a1,a2,v=rnd.choice([(20,5,2),(12,3,1),(8,2,3),(10,2,4),(30,10,2)]);
    return mc(f"Water flows at {v} m/s in a pipe of area {a1} cm² which narrows to {a2} cm². Speed in the narrow part:",f"{f(a1*v/a2)} m/s",[f"{f(a2*v/a1)} m/s",f"{f(v*(a1-a2))} m/s",f"{f(v)} m/s"],"A₁v₁ = A₂v₂.","Inverting the ratio.")
@gen('States of Matter')
def _():
    h=rnd.choice([1.25,1.8,3.2,5,4.05,7.2]);v=math.sqrt(20*h)
    return mc(f"Water flows from a hole {f(h)} m below the free surface (g = 10). Efflux speed:",f"{f(v)} m/s",[f"{f(v*v)} m/s",f"{f(v/math.sqrt(2))} m/s",f"{f(10*h)} m/s"],"v = √(2gh) (Torricelli).","Forgetting the square root.")
@gen('Periodic Motion')
def _():
    n=rnd.choice([4,9,16]);return mc(f"A mass on a spring has period T. If the mass is made {n} times, the new period is:",f"{f(math.sqrt(n))} T",[f"{n} T",f"{f(1/math.sqrt(n))} T",f"{n*n} T"],"T ∝ √m.","Linear scaling.")
@gen('Periodic Motion')
def _():
    A=rnd.choice([2,4,5,10]);T=rnd.choice([1,2,4]);v=2*math.pi*A/T
    return mc(f"SHM amplitude {A} cm, period {T} s. Maximum speed:",f"{f(2*A/T)}π cm/s",[f"{f(A/T)}π cm/s",f"{f(2*A*T)}π cm/s",f"{f(4*A/T)}π cm/s"],"v_max = Aω = 2πA/T.","Missing 2π.") if len({f(2*A/T),f(A/T),f(2*A*T),f(4*A/T)})==4 else None
@gen('Periodic Motion')
def _():
    n=rnd.choice([4,9,16,25]);return mc(f"A simple pendulum's length is increased {n} times. Its period becomes:",f"{f(math.sqrt(n))} times",[f"{n} times",f"{f(1/math.sqrt(n))} times",f"{n*n} times"],"T ∝ √l.","T ∝ l mistake.")
@gen('Periodic Motion')
def _():
    d=rnd.choice([2,3,4]);ke=Fraction(d*d-1,d*d)
    return mc(f"At displacement x = A/{d}, the fraction of total energy in KE of an SHM oscillator:",f"{ke.numerator}/{ke.denominator}",[f"1/{d*d}",f"1/{d}",f"{d-1}/{d}"],"KE = E(1 − x²/A²).","Reporting PE fraction instead.")
@gen('Periodic Motion')
def _():
    f_=rnd.choice([2,5,10,50]);
    return mc(f"A particle in SHM has frequency {f_} Hz. Its angular frequency is:",f"{2*f_}π rad/s",[f"{f_}π rad/s",f"{f_} rad/s",f"{4*f_}π rad/s"],"ω = 2πf.","Missing the 2.")
@gen('Periodic Motion')
def _():
    k=rnd.choice([1,2,3]);return mc(f"A particle has x = {k}·sin(4πt) (SI). Its time period is:",f"{f(0.5)} s",["2 s","4 s","0.25 s"],"ω = 4π ⇒ T = 2π/ω.","Reading ω as the period.")
@gen('Waves')
def _():
    fq=rnd.choice([100,200,250,500]);l=rnd.choice([0.4,0.5,0.8,1.2]);
    return mc(f"A wave of frequency {fq} Hz and wavelength {f(l)} m has speed:",f"{f(fq*l)} m/s",[f"{f(fq/l)} m/s",f"{f(l/fq)} m/s",f"{f(fq*l*2)} m/s"],"v = fλ.","Dividing instead of multiplying.")
@gen('Waves')
def _():
    f1=rnd.choice([250,256,300,400,512]);b=rnd.choice([2,4,5,6]);
    return mc(f"Two tuning forks of {f1} Hz and {f1+b} Hz sound together. Beats per second:",str(b),[str(2*b),str(f1+b),str(b//2 if b%2==0 else b+1)],"Beats = |f₁ − f₂|.","Adding frequencies.")
@gen('Waves')
def _():
    L=rnd.choice([0.5,0.85,1,0.34]);v=340;return mc(f"A pipe closed at one end has length {f(L)} m (v = 340 m/s). Fundamental frequency:",f"{f(v/(4*L))} Hz",[f"{f(v/(2*L))} Hz",f"{f(v/L)} Hz",f"{f(3*v/(4*L))} Hz"],"Closed: v/4L (odd harmonics); open: v/2L.","Using the open-pipe formula.")
@gen('Waves')
def _():
    n=rnd.choice([4,9,16]);return mc(f"If the tension in a stretched string is made {n} times, the wave speed becomes:",f"{f(math.sqrt(n))} times",[f"{n} times",f"{f(1/math.sqrt(n))} times",f"{n*n} times"],"v = √(T/μ).","Linear scaling.")
@gen('Waves')
def _():
    vs=rnd.choice([10,20,30]);f0=rnd.choice([340,500,680]);v=340;return mc(f"A source of {f0} Hz moves towards a stationary listener at {vs} m/s (sound speed 340). Frequency heard:",f"{f(f0*v/(v-vs))} Hz",[f"{f(f0*v/(v+vs))} Hz",f"{f0+vs} Hz",f"{f0} Hz"],"Approach: denominator v − vₛ (pitch rises).","Using v + vₛ for approach.")
@gen('Ideal Gas')
def _():
    n=rnd.choice([2,3,4,5]);return mc(f"At constant temperature, the volume of a gas is made 1/{n}. Pressure becomes:",f"{n} times",[f"1/{n} times",f"{n*n} times","unchanged"],"Boyle: PV = const.","Inverting Boyle's law.")
@gen('Ideal Gas')
def _():
    n=rnd.choice([4,9,16]);return mc(f"The rms speed of gas molecules becomes {int(math.sqrt(n))} times when absolute temperature becomes:",f"{n} T",[f"{int(math.sqrt(n))} T",f"{n*2} T",f"{n//2} T"],"v_rms ∝ √T ⇒ T ∝ v².","T ∝ v mistake.")
@gen('Ideal Gas')
def _():
    T=rnd.choice([100,200,300,400,600]);k=rnd.choice([2,3]);return mc(f"At constant volume, a gas at {T} K is heated to {T*k} K. The pressure becomes:",f"{k} times",[f"1/{k} times",f"{k*k} times","unchanged"],"P ∝ T (Kelvin) at constant V.","Using °C.")
@gen('Ideal Gas')
def _():
    n=rnd.choice([2,3,4]);return mc(f"The ratio of average KE per molecule of two gases at the same temperature is:","1 : 1",[f"1 : {n}",f"1 : {n*n}",f"{n} : 1"],"KE = (3/2)kT, independent of gas type.","Thinking heavier gas has more KE.")
@gen('Ideal Gas')
def _():
    m1,m2=rnd.choice([(2,32),(4,16),(1,16),(2,8),(4,64)]);r=math.sqrt(m2/m1)
    return mc(f"Ratio of rms speeds of gases of molar mass {m1} and {m2} g/mol at the same T:",f"{f(r)} : 1",[f"{f(m2/m1)} : 1",f"1 : {f(r)}",f"{f(m1/m2)} : 1"],"v_rms ∝ 1/√M.","Forgetting the square root.") if len({f(r),f(m2/m1),f(m1/m2)})==3 else None

@gen('Gravitation')
def _():
    W_=rnd.choice([50,60,70,80,100]);M,Rr=rnd.choice([(4,2),(9,3),(2,1),(8,2),(16,4),(3,1)])
    a=W_*Fraction(M,Rr*Rr)
    return mc(f"A man weighs {W_} kgf on Earth. On a planet with {M}× Earth's mass and {Rr}× radius he would weigh:",f"{f(a)} kgf",[f"{f(W_*M*Rr)} kgf",f"{f(W_*Fraction(M,Rr))} kgf",f"{f(W_*Fraction(Rr*Rr,M))} kgf"],"Weight ∝ M/R².","Radius not squared.") if len({f(a),f(W_*M*Rr),f(W_*Fraction(M,Rr)),f(W_*Fraction(Rr*Rr,M))})==4 else None
@gen('Gravitation')
def _():
    n=rnd.choice([4,9,16,25,36,49]);return mc(f"A satellite orbits at radius {n} times another. Ratio of their orbital speeds (outer : inner):",f"1 : {f(math.sqrt(n))}",[f"1 : {n}",f"{f(math.sqrt(n))} : 1",f"1 : {n*n}"],"v ∝ 1/√r.","Orbital speed falls with radius.")
@gen('Periodic Motion')
def _():
    m,k=rnd.choice([(1,100),(4,25),(1,25),(9,100),(4,100)]);T=2*math.pi*math.sqrt(m/k)
    return mc(f"A {m} kg mass on a spring (k = {k} N/m) oscillates. Time period (in terms of π):",f"{f(2*math.sqrt(m/k))}π s",[f"{f(math.sqrt(m/k))}π s",f"{f(4*math.sqrt(m/k))}π s",f"{f(2*math.sqrt(k/m))}π s"],"T = 2π√(m/k).","Inverting m/k.") if len({f(2*math.sqrt(m/k)),f(math.sqrt(m/k)),f(4*math.sqrt(m/k)),f(2*math.sqrt(k/m))})==4 else None
@gen('Periodic Motion')
def _():
    l=rnd.choice([0.1,0.4,0.9,1.6,2.5,0.25]);return mc(f"A simple pendulum of length {f(l)} m (take g = π² m/s²). Its period:",f"{f(2*math.sqrt(l))} s",[f"{f(math.sqrt(l))} s",f"{f(4*math.sqrt(l))} s",f"{f(2*l)} s"],"T = 2π√(l/g); g = π² cancels π.","Not cancelling π.") if len({f(2*math.sqrt(l)),f(math.sqrt(l)),f(4*math.sqrt(l)),f(2*l)})==4 else None
@gen('Ideal Gas')
def _():
    P1,V1,V2=rnd.choice([(1,6,2),(2,8,4),(4,3,1),(3,10,5),(6,4,2),(5,6,3)]);P2=P1*V1/V2
    return mc(f"A gas at {P1} atm and {V1} L is compressed isothermally to {V2} L. Final pressure:",f"{f(P2)} atm",[f"{f(P1*V2/V1)} atm",f"{f(P1+V1-V2)} atm",f"{f(P2*2)} atm"],"P₁V₁ = P₂V₂.","Inverting the ratio.") if len({f(P2),f(P1*V2/V1),f(P1+V1-V2),f(P2*2)})==4 else None
@gen('Ideal Gas')
def _():
    c=rnd.choice([27,127,327,-173,227]);return mc(f"The temperature {c}°C in kelvin is:",f"{c+273} K",[f"{c} K",f"{c-273} K",f"{c+373} K"],"K = °C + 273.","Using °C in gas laws.")
@gen('Waves')
def _():
    l=rnd.choice([0.2,0.4,0.6,0.8,1.0]);v=rnd.choice([320,340,360]);return mc(f"A string fixed at both ends has length {f(l)} m; wave speed {v} m/s. Fundamental frequency:",f"{f(v/(2*l))} Hz",[f"{f(v/l)} Hz",f"{f(v/(4*l))} Hz",f"{f(2*v/l)} Hz"],"f₁ = v/2L (fixed–fixed).","Using the closed-pipe formula.")
@gen('Vectors')
def _():
    a=rnd.choice([3,4,5,6,8,10,12]);b=rnd.choice([2,3,5,7,9]);return mc(f"Two vectors of magnitudes {a} and {b}: the maximum and minimum possible resultants are:",f"{a+b} and {abs(a-b)}",[f"{a+b} and 0",f"{a*b} and {abs(a-b)}",f"{abs(a-b)} and {a+b+1}"],"Max: parallel (sum); min: antiparallel (difference).","Assuming min is zero.")
@gen('Work-Power-Energy')
def _():
    m=rnd.choice([2,4,5,10]);h=rnd.choice([5,10,20]);return mc(f"A {m} kg body is raised {h} m (g = 10). Gain in potential energy:",f"{m*h*10} J",[f"{m*h} J",f"{m*h*5} J",f"{m*h*100} J"],"PE = mgh.","Omitting g.")
@gen('Newtonian Mechanics')
def _():
    m=rnd.choice([2,5,10,20]);a=rnd.choice([2,3,4,5]);return mc(f"A force acts on a {m} kg body producing acceleration {a} m/s². The force is:",f"{m*a} N",[f"{f(m/a)} N",f"{m+a} N",f"{m*a*2} N"],"F = ma.","Dividing.")
def make_generated(chap,count,used):
    out=[];tries=0
    while len(out)<count and tries<2000:
        tries+=1;m=rnd.choice(G[chap])()
        if not m or m['q'] in used: continue
        dis=list(dict.fromkeys(x for x in m['dis'] if x!=m['ans']))
        if len(dis)<3: continue
        used.add(m['q']);opts=dis[:3]+[m['ans']];rnd.shuffle(opts)
        out.append(dict(q=m['q'],_o=opts,_a=opts.index(m['ans']),gen=True,hack=m['hack'],trap=m['trap']));
    assert len(out)==count,(chap,len(out),count)
    return out
# ---------- build sets ----------
NS=4
bankalloc={c:min(len(pool[c])//NS,QUOTA[c]) for c in QUOTA}
for c in pool: rnd.shuffle(pool[c])
used=set();sets=[[] for _ in range(NS)]
for c in QUOTA:
    for i in range(NS):
        sets[i]+= [(c,x) for x in pool[c][i*bankalloc[c]:(i+1)*bankalloc[c]]]
        sets[i]+= [(c,x) for x in make_generated(c,QUOTA[c]-bankalloc[c],used)]
for s in sets: rnd.shuffle(s); assert len(s)==60
# ---------- written ----------
Wb=json.load(open('physics_written_bank.json'))
def W(ch,q,sol,key): return dict(ch=ch,q=q,sol=sol,key=key)
def wC(i):
    P=lambda *a: a[i]
    out=[]
    a1,b1=P((3,4),(6,8)); out.append(W("Vectors",f"Prove that $(\\vec A+\\vec B)\\cdot(\\vec A-\\vec B)=A^2-B^2$. Hence evaluate it for $|\\vec A|={a1}$, $|\\vec B|={b1}$.",f"Expand: $\\vec A\\cdot\\vec A-\\vec A\\cdot\\vec B+\\vec B\\cdot\\vec A-\\vec B\\cdot\\vec B=A^2-B^2$ (dot product is commutative). Value $={a1*a1}-{b1*b1}={a1*a1-b1*b1}$.","$\\vec A\\cdot\\vec B=\\vec B\\cdot\\vec A$; trap: cross-term does not vanish in a cross product."))
    m=P(2,4); out.append(W("Vectors",f"If $\\vec A={m}\\hat i+3\\hat j-\\hat k$ and $\\vec B=\\hat i-\\hat j+{m}\\hat k$, find $\\vec A\\times\\vec B$ and verify that it is perpendicular to $\\vec A$.",f"$\\vec A\\times\\vec B=(3m-1)\\hat i-(m^2+1)\\hat j+(-m-3)\\hat k=({3*m-1})\\hat i-({m*m+1})\\hat j-({m+3})\\hat k$. Dot with $\\vec A$: ${m}({3*m-1})-3({m*m+1})+({m+3}) = {m*(3*m-1)-3*(m*m+1)+(m+3)}$ ✓.","Determinant sign alternation (+,−,+) for $\\hat j$."))
    u,al=P((40,30),(30,60)); H=u*u*(0.25 if al==30 else 0.75)/20; R=u*u*(math.sqrt(3)/2)/10
    out.append(W("Newtonian Mechanics",f"A ball is thrown at ${u}$ m/s at ${al}^\\circ$ above horizontal ($g=10$). Find the maximum height and the range.",f"$H=\\frac{{u^2\\sin^2\\alpha}}{{2g}}={H:g}$ m; $R=\\frac{{u^2\\sin2\\alpha}}{{g}}={u*u/10:g}\\sin{2*al}^\\circ={R:.1f}$ m.","$H$ uses $\\sin^2\\alpha$ and $2g$; $R$ uses $\\sin2\\alpha$."))
    m,a=P((60,2),(50,4)); out.append(W("Newtonian Mechanics",f"A {m} kg man stands on a weighing scale in a lift. Find the reading when the lift accelerates (i) upward at ${a}$ m/s², (ii) downward at ${a}$ m/s², (iii) falls freely ($g=10$).",f"(i) $m(g+a)={m*(10+a)}$ N; (ii) $m(g-a)={m*(10-a)}$ N; (iii) $0$.","Reading = normal reaction, not true weight."))
    k,x1,x2=P((200,0.1,0.3),(400,0.05,0.15)); out.append(W("Work-Power-Energy",f"A spring of constant ${k}$ N/m is stretched from ${x1}$ m to ${x2}$ m. Find the work done on it.",f"$W=\\tfrac12k(x_2^2-x_1^2)=\\tfrac12({k})({x2*x2:g}-{x1*x1:g})={0.5*k*(x2*x2-x1*x1):g}$ J.","Subtract energies; do not subtract extensions first."))
    h=P(5,1.8); out.append(W("Work-Power-Energy",f"A pendulum bob is released from a height ${h}$ m above its lowest point. Find the speed at the bottom ($g=10$). What is the speed when it is at half that height?",f"Bottom: $v=\\sqrt{{2gh}}=\\sqrt{{{20*h:g}}}={math.sqrt(20*h):g}$ m/s. Half height: $v=\\sqrt{{2g(h/2)}}={math.sqrt(10*h):.2f}$ m/s.","Use drop in height, not total length."))
    out.append(W("Gravitation",f"Calculate the acceleration due to gravity at a height ${P(2,3)}R$ above Earth's surface ($g_0=9.8$). At what height does $g$ fall to $g_0/{P(4,16)}$?",f"$g'=g_0\\left(\\frac{{R}}{{R+h}}\\right)^2=\\frac{{9.8}}{{{(P(2,3)+1)**2}}}={9.8/(P(2,3)+1)**2:.3f}$ m/s². For $g_0/{P(4,16)}$: $R+h={int(math.sqrt(P(4,16)))}R\\Rightarrow h={int(math.sqrt(P(4,16)))-1}R$.","Use $R+h$ in denominator, not $h$."))
    M,Rr=P((8,2),(9,3)); out.append(W("Gravitation",f"A planet has {M} times Earth's mass and {Rr} times its radius. Find $g_p/g_e$ and $v_{{esc,p}}/v_{{esc,e}}$.",f"$g\\propto M/R^2={M}/{Rr*Rr}={M/(Rr*Rr):.3g}$; $v_e\\propto\\sqrt{{M/R}}=\\sqrt{{{M}/{Rr}}}={math.sqrt(M/Rr):.3g}$.","Radius is squared for $g$, square-rooted for $v_e$."))
    F,L,A,l=P((100,2,1,0.5),(300,3,2,1)); out.append(W("States of Matter",f"A wire of length ${L}$ m and cross-section ${A}\\ \\text{{mm}}^2$ is stretched by ${F}$ N, causing ${l}$ mm extension. Find stress, strain and Young's modulus.",f"Stress $=F/A={F/(A*1e-6):.2e}$ Pa; strain $=\\ell/L={l*1e-3/L:.2e}$; $Y={F*L/(A*1e-6*l*1e-3):.2e}$ Pa.","Convert mm²→m² ($10^{-6}$) and mm→m ($10^{-3}$)."))
    T,r=P((0.03,0.01),(0.05,0.02)); out.append(W("States of Matter",f"A soap bubble of radius ${r*100:g}$ cm has surface tension ${T}$ N/m. Find the excess pressure, and compare with that in a liquid drop of the same radius.",f"Bubble: $4T/r={4*T/r:g}$ Pa; drop: $2T/r={2*T/r:g}$ Pa; ratio $2:1$.","Bubble has two free surfaces."))
    a1,a2,v1=P((20,5,3),(16,4,2)); out.append(W("States of Matter",f"Water flows through a horizontal pipe narrowing from ${a1}$ cm² to ${a2}$ cm². Entry speed ${v1}$ m/s. Find exit speed and pressure difference ($\\rho=1000$).",f"$v_2={a1*v1/a2:g}$ m/s; $\\Delta P=\\tfrac12\\rho(v_2^2-v_1^2)={500*((a1*v1/a2)**2-v1*v1):g}$ Pa.","Use $\\tfrac12\\rho$ and squares of speeds."))
    A_,T_,x=P((0.1,2,0.06),(0.2,4,0.12)); out.append(W("Periodic Motion",f"Show that $x=A\\sin\\omega t$ represents SHM. For $A={A_}$ m, $T={T_}$ s, find the speed at $x={x}$ m.","$a=d^2x/dt^2=-\\omega^2x$, so SHM. "+f"$\\omega=2\\pi/T={2*math.pi/T_:.3f}$; $v=\\omega\\sqrt{{A^2-x^2}}={2*math.pi/T_*math.sqrt(A_*A_-x*x):.3f}$ m/s.","$a\\propto -x$ is the SHM test; use $\\sqrt{A^2-x^2}$."))
    m,k=P((2,50),(0.5,200)); out.append(W("Periodic Motion",f"A ${m}$ kg block on a spring of $k={k}$ N/m oscillates. Find its time period. What is the period if the mass is quadrupled?",f"$T=2\\pi\\sqrt{{m/k}}={2*math.pi*math.sqrt(m/k):.3f}$ s; quadrupled mass gives $2T={4*math.pi*math.sqrt(m/k):.3f}$ s.","$T\\propto\\sqrt m$."))
    Tn,mu=P((100,0.01),(36,0.01)); out.append(W("Waves",f"A string of linear density ${mu}$ kg/m is under tension ${Tn}$ N. Find wave speed. For a $1$ m string fixed at both ends, find the fundamental frequency.",f"$v=\\sqrt{{T/\\mu}}={math.sqrt(Tn/mu):g}$ m/s; $f_1=v/2L={math.sqrt(Tn/mu)/2:g}$ Hz.","Fixed–fixed string: $L=\\lambda/2$."))
    vs,f0=P((20,680),(10,510)); out.append(W("Waves",f"A siren of ${f0}$ Hz moves at ${vs}$ m/s toward a stationary listener (sound speed 340). Find heard frequency approaching and receding.",f"Approach: ${f0}\\times340/{340-vs}={f0*340/(340-vs):.1f}$ Hz; recede: ${f0}\\times340/{340+vs}={f0*340/(340+vs):.1f}$ Hz.","Approach lowers denominator."))
    Pp,rho=P((1.0e5,1.2),(2.0e5,2.4)); out.append(W("Ideal Gas",f"Using $P=\\tfrac13\\rho\\overline{{c^2}}$, find the rms speed of gas molecules at $P={Pp:.1e}$ Pa and density $\\rho={rho}$ kg/m³. Hence state the effect of doubling absolute temperature.",f"$c_{{rms}}=\\sqrt{{3P/\\rho}}={math.sqrt(3*Pp/rho):g}$ m/s; doubling $T$ multiplies $c_{{rms}}$ by $\\sqrt2$ ({math.sqrt(3*Pp/rho)*math.sqrt(2):.0f} m/s).","$c_{rms}\\propto\\sqrt T$ (Kelvin)."))
    return out
Wsets=[Wb[0],Wb[1],wC(0),wC(1)]
assert all(len(w)==16 for w in Wsets)
# ---------- output ----------
L='ABCD'
def tagmc(ch,q):
    if q.get('gen'): return f"[Tag: Original pattern-based question (modelled on {ch} board/DU types; not a verbatim past paper) | Repeated: n/a | Chapter hotspot: {stat[ch][2]}%]  [Common Probability: {stat[ch][2]}% (bank-derived: share of {ch} items repeated ≥2×)]"
    return f"[Tag: {q.get('origin','Bank')} | Repeated {q.get('repeat_count','?')}x | {q.get('tag','')}]  [Common Probability: {q.get('probability','N/A')}]"
out=['# Physics 1st Paper — Paper Final: 4 Complete Model Tests\n',
'Each set: **Section A** 60 MCQ (1 mark) + **Section B** 16 written (2.5 marks each = 40). g = 10 m/s² unless stated.\n',
'> **Honesty note on tags.** Questions pulled from the workspace banks carry the origin, repeat count and probability stored in those banks. Questions authored for this guide are labelled *Original* and have **no fabricated past-paper years**; their probability is the share of that chapter\'s bank items repeated ≥2×. These are heuristics from your bank, not official board statistics. Thermodynamic derivations belong to Paper 2; Paper 1 gas questions use the kinetic theory/gas laws.\n',
'Chapter hotspot table (from bank): '+'; '.join(f'{c}: {v[0]} items, {v[2]}% repeated' for c,v in stat.items())+'\n']
for i in range(NS):
    out.append(f'\n---\n\n# MODEL TEST SET {L[i]}\n\n## Section A — MCQ (60)\n')
    for n,(ch,q) in enumerate(sets[i],1):
        t=q['q'] if q.get('gen') else re.sub(r'^\[[^\]]*\]\s*','',q['q'])
        out.append(f'**{n}.** *({ch})* {t}\n'+'\n'.join(f'   - ({"ABCD"[j]}) {o}' for j,o in enumerate(q['_o']))+f'\n   - {tagmc(ch,q)}\n')
    out.append(f'\n### Answer Key, Speed Hack & Trap Alert — Set {L[i]}\n\n| Q | Ans | Speed Hack | Trap Alert |\n|---|---|---|---|')
    for n,(ch,q) in enumerate(sets[i],1):
        if q.get('gen'): h,tr=q['hack'],q['trap']
        else: h=q.get('speed_hack') or q.get('exp') or ''; tr=q.get('trap_alert') or q.get('trap') or ''
        cl=lambda s:str(s).replace('\n',' ').replace('|','/')
        out.append(f'| {n} | {"ABCD"[q["_a"]]} | {cl(h)} | {cl(tr)} |')
    out.append(f'\n## Section B — Written (16 × 2.5 = 40)\n')
    for n,w in enumerate(Wsets[i],1):
        n_,r2,p=stat[w['ch']]
        out.append(f'**{n}.** ({w["ch"]}) {w["q"]}\n   - [Tag: Original problem modelled on {w["ch"]} numerical/proof pattern | Repeated: pattern appears in {n_} bank items | Syllabus core]  [Common Probability: {p}% (bank-derived)]\n')
    out.append(f'\n### Written Solutions & Evaluation Key — Set {L[i]}\n')
    for n,w in enumerate(Wsets[i],1):
        out.append(f'**{n}.** {w["sol"]}  \n   *Formula/Trap key:* {w.get("key","Show formula, substitution with units, and final answer (2.5 marks: formula 1, substitution 1, answer+unit 0.5).")}\n')
open('physics_paper_final_4_model_tests.md','w').write('\n'.join(out))
print('ok',len('\n'.join(out)))
