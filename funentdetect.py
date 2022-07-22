#Selected functions of entdetector


import numpy
import operator
import cmath
import math
	
def hamming(str1, str2):
  assert len(str1) == len(str2)
  ne = operator.ne
  return sum(map(ne, str1, str2))
	
def prob_calculate(lset, testpattern1, dn, scale, verbose = 0):
  probe0=0.0;
  probe1=0.0;
  ap0=0.0;
  ap1=0.0;
  regQ0 = []
  regQ1 = []
  for pattern in lset:
    dH=hamming(pattern,testpattern1)
    probe0 = scale * ( math.cos( (math.pi / (2.0 * dn)) * dH) )
    probe1 = scale * ( math.sin( (math.pi / (2.0 * dn)) * dH) )
    regQ0 = regQ0 + [probe0]
    regQ1 = regQ1 + [probe1]
    ap0 += probe0 ** 2;
    ap1 += probe1 ** 2;
    return ap0, ap1, regQ0, regQ1
	
def qra_16elems_rcmd(t, indeks):
  dn = 6.0;
  lset = ["000000", "000110", "001001", "001111", "000100", "000010", "001011", "100000",  "100110",
          "101111", "100100", "100010", "101101", "101001", "101011", "101011"];	
  testset = indeks
  regQ0 = []
  regQ1 = []
  for p in testset:
    [ap0, ap1, regQ0, regQ1] = prob_calculate(lset, p, dn, 1.0 / math.sqrt(16), verbose=1)
  regQ0 = [a / math.sqrt(ap0) for a in regQ0]
  probRegQ0 = [a * a for a in regQ0]
  L = 16
  q = 2
  mrtbl = [0.31440905434759225, 0.31440905434759225];
  mnrtbl = [0.15720452717379615, 0.15720452717379615, 0.2722862282448571, 0.2722862282448571, 
            0.08137505121783044, 0.22232077439563225, 0.3036958256134626, 0.22232077439563225, 
            0.22232077439563225, 0.3036958256134626, 0.15720452717379615, 0.2722862282448571,
            0.2722862282448571, 0.3036958256134626]
  mr = np.mean(mrtbl);
  mnr = np.mean(mnrtbl)
  sigmanr = np.var(mnrtbl)
  Pmax = 1 - (L - q) * sigmanr - 0.5 * ((L - q) * abs(mnr ** 2) + q * abs
    (mr ** 2)) + (0.5 * abs((L - q) * mnr ** 2 + q * (mr ** 2)))
  fplus = mnr + 1j * math.sqrt(q / (L - q)) * mr;
  fminus = mnr - 1j * math.sqrt(q / (L - q)) * mr;
  omega = math.acos(1 - 2 * (q / L))
  kavgtime = -1j * cmath.sqrt((L - q) / 4 * q) * (
  cmath.exp(1j * omega * t) * fplus - cmath.exp(-1j * omega * t) * fminus)
  lavgtime0 = 0.5 * (cmath.exp(1j * omega * t) * fplus + cmath.exp(-1j * omega * t) * fminus)
  lavgtime0org = lavgtime0;
  kavgtime = -1j * cmath.sqrt((L - q) / 4 * q) * (
  cmath.exp(1j * omega * t) * fplus - cmath.exp(-1j * omega * t) * fminus)
  lavgtime0 = 0.5 * (cmath.exp(1j * omega * t) * fplus + cmath.exp(-1j * omega * t) * fminus)
  lavgtime = 0.5 * (cmath.exp(1j * omega * t) * fplus + cmath.exp(-1j * omega * t) * fminus)
  ltbl = []
  for i in range(0, 14):
    litime = lavgtime + ((-1) ** t) * (mnrtbl[i] - lavgtime0org)
    ltbl = ltbl + [abs(litime)];
  
  return ltbl