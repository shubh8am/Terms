import streamlit as st

st.header(":rainbow[Spectral Terms Calculator....]", divider="red")

res={"s":0,"p":1,'d':2,'f':3,'up':1/2,'down':-1/2}
orb={0:"s",1:"p",2:"d",3:"f",4:"g",5:"h"}
terms=[]

def valid(i):
	return res.get(i[1])<int(i[0])
	
def total_spin(no_of_e,rooms):
	if no_of_e<=rooms:
		return no_of_e*res.get("up")
	elif no_of_e>rooms:
		return rooms*res.get("up")+(no_of_e-rooms)*res.get("down")

	
	
#user input config

state=[{"n":int(i[0]),"l":res.get(i[1]),"s":total_spin(int(i[2]),2*res.get(i[1])+1)} for i in st.text_input("\tEnter Valence Configuration: ").split(" ") if valid(i)]


#S=| S1+S2 | to | S1 - S2 |
spin=[(state[0].get("s")+state[1].get("s")-i) for i in range(1+int(state[0].get("s")+state[1].get("s")-abs(state[0].get("s")-state[1].get("s"))))]


#L=| L1+L2 | to | L1 - L2 |
orbit=[round((state[0].get("l")+state[1].get("l")-i),2) for i in range(1+int(state[0].get("l")+state[1].get("l")-abs(state[0].get("l")-state[1].get("l"))))]


#J=| L+S | to | L - S |
for s in spin:
	for l in orbit:
		j=[(s+l-i) for i in range(1+int(s+l-abs(s-l)))]
		terms.append(str(int(2*s+1))+orb.get(l)+str(j))
		
# spectral terms printing
print("\t|---Spectral Terms---|")
if st.button("Find", type="primary"):
	col1,col2 =st.columns(2)
	with col1:
		with st.expander("Spectral Symbols👇"):
			st.write(terms)

	






"""orbitals = {"s": [0, 2], "p": [1, 6], "d": [2, 10], "f": [3, 14]}
spin_individual = []
total_s = []
total_l = []
total_j = []
spectral_terms, originalTerms, ipTerms = [], [], []
final_input_terms = []
ip = st.text_input("Enter Your input:")


# input validation
def is_valid(l):
    if (l[1] < l[0]):
        return True
    else:
        return False
# 3
def valid(l):
    if (orbitals.keys().__contains__(l[1])):
        term = convert(l)
        if (term[1] < term[0]):
            return term
        else:
            st.error('Orbital Quantum number cannot be greater that Principle Quantum number....\nTry some other input',
                     icon="🚨")
    else:
        st.write("I am not aware of given sub-orbital:", f':red[{l[1]}]')


# 4 conversion of azimuthal quantum number
def convert(l):
    return [int(l[0]), orbitals.get(l[1])[0], int(l[2])]


# 6
def addspin(i):
    half = (orbitals.get(i[1])[1]) / 2
    spin = 0
    if float(i[2]) <= half:
        spin = float(i[2]) * 0.5
    if float(i[2]) > half:
        spin = half * 0.5 + (float(i[2]) - half) * (-0.5)
    return spin


# 2
def findSpectralTerms(ip):
    originalTerms = [[k for k in t] for t in ip.split(" ")]
    ipTerms = [valid([k for k in t]) for t in ip.split(" ")]
    spin_individual = [addspin(i) for i in originalTerms]
    create_range(spin_individual[0], spin_individual[1], total_s)
    create_range(ipTerms[0][1], ipTerms[1][1], total_l)
    create_terms()


def create_range(r1, r2, r):
    for i in range(int((abs(r1 - r2)) / 0.5), int(((abs(r1 + r2) / 0.5) + 1)), 2):
        r.append(i / 2)


# 6
def create_terms():
    for s in total_s:
        for l in total_l:
            for j in range(int((abs(l - s)) / 0.5), int(((abs(l + s) / 0.5) + 1)), 2):
                total_j.append(j / 2)
    for s in total_s:
        for l in total_l:
            for j in total_j:
                a =str(int( (2 * s + 1) ))+[x for x in orbitals if orbitals.get(x)[0] == l][0] + str(j)
                spectral_terms.append(a)


# 
if st.button("Find", type="primary"):
    findSpectralTerms(ip)
    col1,col2 =st.columns(2)
    with col1:
        with st.expander("Spectral Symbols👇"):
            st.write(spectral_terms)

"""
