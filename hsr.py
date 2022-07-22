#Part of a hybrid recommendation system

import numpy as np
import itertools
from scipy.spatial import distance

def dbstateGenerator(qubitId, qubitFeatureFilm, numberIndex):
  iterate = 2 ** qubitId
  qubitFeatureFilmUser = qubitFeatureFilm
  Tab = list(itertools.product(range(2), repeat=qubitId))
  tableId = np.array(Tab)
  tableFeatureFilm = np.random.randint(2, size=(iterate, qubitFeatureFilm))
  tableFeatureUser = np.random.randint(2, size=(1, qubitFeatureFilmUser))
  matrixIndex = []
  for i in range(iterate):
    dbstateLoop = np.hstack((tableId[i], tableFeatureFilm[i], tableFeatureUser[0])).ravel()
    matrixIndex.append(dbstateLoop.tolist())
    matrixIndex = np.array(matrixIndex)
    dbState = matrixIndex[numberIndex]
    vectorState = np.zeros(2 ** (qubitId + qubitFeatureFilm + qubitFeatureFilmUser))
    value = 1 / np.sqrt(2 ** qubitId)
  for j in range(iterate):
    position = sum(val * 2 ** index for index, val in enumerate(reversed(matrixIndex[j])))
  vectorState[position] = value
  return tableId, tableFeatureFilm, tableFeatureUser, matrixIndex, dbState, vectorState, value, qubitFeatureFilm

def kNN(tableFeatureFilm, tableFeatureUser, matrixIndex, vectorStateSize, qubitFeatureFilm):
  n = 0
  tableDistance = []
  size = np.size(tableFeatureFilm[:, 1])
  for n in range(size):
    Distance = distance.hamming(tableFeatureFilm[n], tableFeatureUser[0]) * qubitFeatureFilm
    tableDistance.append(Distance.tolist())
    tableDistance = np.array(tableDistance)
    distVectorState = np.zeros(vectorStateSize)
  for j in range(size):
    position = sum(val * 2 ** index for index, 
				val in enumerate(reversed(matrixIndex[j])))
    distVectorState[position] = 1 / np.sqrt(2 ** tableDistance[j])
  return distVectorState

def amplitude_amplification(tableFeatureFilm, tableFeatureUser, matrixIndex, vectorStateSize, qubitFeatureFilm, after_kNN):
  n = 0
  tableDistance = []
  size = np.size(tableFeatureFilm[:, 1])
  for n in range(size):
    Distance = distance.hamming(tableFeatureFilm[n], tableFeatureUser[0]) * qubitFeatureFilm
    tableDistance.append(Distance.tolist())
    tableDistance = np.array(tableDistance)
    distVectorState = np.zeros(vectorStateSize)
  for j in range(size):
    position = sum(val * 2 ** index for index, val in enumerate(reversed(matrixIndex[j])))
    distVectorState[position] = 1 / np.sqrt(2 ** tableDistance[j])
  Indices = []
  for idx in range(0, len(after_kNN)):
    if after_kNN[idx] > 0:
      Indices.append(idx)
    after_kNN_max = np.max(after_kNN)
  MaxInd = []
  for idx in range(0, len(after_kNN)):
    if after_kNN[idx] == np.max(after_kNN):
      MaxInd.append(idx)
  maxSmallAmp = 0.20
  nrSmallAmp = len(Indices) - len(MaxInd)
  MinInd = Indices
  for u in range(0, len(MaxInd)):
    MinInd.remove(MaxInd[u])
  SmallAmplitudeTable = []
  for p in range(0, nrSmallAmp):
    x = random.uniform(0.01, maxSmallAmp / 2 - np.sum(SmallAmplitudeTable))
    SmallAmplitudeTable.append(x)
  LagreAmplitudeTable = []
  for r in range(0, len(MaxInd)):
    z = (1 - np.sum(SmallAmplitudeTable)) / (len(MaxInd))
    LagreAmplitudeTable.append(z)
  GroverVector = np.zeros_like(after_kNN)
  GroverVector[MaxInd] = LagreAmplitudeTable
  GroverVector[MinInd] = SmallAmplitudeTable
  return GroverVector

def show_quantum_state_for_movie_database():
  nn = len(tableId)
  amplitudes = after_amplitude_amplification[np.where(after_amplitude_amplification!=0)]
  offset1 = QubitID-2
  offset2 = QubitFeature-2
  space = ' '
  print("id "+offset1*space+"|feature movie"+offset2*space+"| feature user"+offset2*space+"| probability | hamming distance")
  n = 0
  tableDistance = []
  size = np.size(tableFeatureFilm[:, 1])
  for n in range(size):
    Distance = distance.hamming(tableFeatureFilm[n], tableFeatureUser[0]) * qubitFeatureFilm
    tableDistance.append(Distance.tolist())
    tableDistance = np.array(tableDistance)
  for ind in range(0,nn):
    ID_A = ''
  for length in range(0,QubitID):
    ID = matrixIndex[ind,length]
    ID_A = str(ID_A)+str(ID)
    CF_A = ''
  for length in range(QubitID, QubitID+QubitFeature):
    CF = matrixIndex[ind, length]
    CF_A = str(CF_A) + str(CF)
    CU_A = ''
  for length in range(QubitID+QubitFeature, QubitID+QubitFeature+QubitFeature):
    CU = matrixIndex[ind, length]
    CU_A = str(CU_A) + str(CU)
    AM = amplitudes[ind]
    OH = tableDistance[ind]
    print(ID_A,'|',str(CF_A),'         |',str(CU_A),' |',format(AM,'.7f'),'  |',int(OH))

  return