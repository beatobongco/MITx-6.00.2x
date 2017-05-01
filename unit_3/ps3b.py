import random


class NoChildException(Exception):
  pass


class SimpleVirus(object):

  def __init__(self, maxBirthProb, clearProb):
    self.clearProb = clearProb
    self.maxBirthProb = maxBirthProb

  def getMaxBirthProb(self):
    return self.maxBirthProb

  def getClearProb(self):
    return self.clearProb

  def doesClear(self):
    return random.random() <= self.getClearProb()

  def reproduce(self, popDensity):
    if random.random() < self.getMaxBirthProb() * (1 - popDensity):
      return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
    else:
      raise NoChildException


class Patient(object):

  def __init__(self, viruses, maxVirusPop):
    self.viruses = viruses
    self.maxVirusPop = maxVirusPop

  def getViruses(self):
    return self.viruses.copy()

  def addVirus(self, newVirus):
    return self.viruses.append(newVirus)

  def removeVirus(self, virus):
    self.viruses.remove(virus)

  def getPopDensity(self):
    return self.getTotalPop() / self.maxVirusPop

  def getTotalPop(self):
    return len(self.getViruses())

  def update(self):
    for virus in self.getViruses():
      if virus.doesClear():
        self.removeVirus(virus)
    for virus in self.getViruses():
      try:
        self.addVirus(virus.reproduce(self.getPopDensity()))
      except NoChildException:
        pass

    return len(self.getViruses())

import pylab
from statistics import mean


def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
  TIME = 300

  results = [[] for _ in range(TIME)]

  for _ in range(numTrials):
    viruses = [SimpleVirus(maxBirthProb, clearProb) for _ in range(numViruses)]
    patientZero = Patient(viruses, maxPop)
    for i in range(TIME):
      curr = patientZero.update()
      results[i].append(curr)

  averaged = [mean(result) for result in results]
  print(averaged)
  pylab.plot(averaged)
  pylab.title('SimpleVirus simulation')
  pylab.xlabel('Time Steps')
  pylab.ylabel('Average Virus Population')
  pylab.legend()
  pylab.show()


#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
  """
  Representation of a virus which can have drug resistance.
  """

  def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
    """
    Initialize a ResistantVirus instance, saves all parameters as attributes
    of the instance.

    maxBirthProb: Maximum reproduction probability (a float between 0-1)

    clearProb: Maximum clearance probability (a float between 0-1).

    resistances: A dictionary of drug names (strings) mapping to the state
    of this virus particle's resistance (either True or False) to each drug.
    e.g. {'guttagonol':False, 'srinol':False}, means that this virus
    particle is resistant to neither guttagonol nor srinol.

    mutProb: Mutation probability for this virus particle (a float). This is
    the probability of the offspring acquiring or losing resistance to a drug.
    """
    SimpleVirus.__init__(self, maxBirthProb, clearProb)
    self.resistances = resistances
    self.mutProb = mutProb

  def getResistances(self):
    """
    Returns the resistances for this virus.
    """
    return self.resistances.copy()

  def getMutProb(self):
    """
    Returns the mutation probability for this virus.
    """
    return self.mutProb

  def isResistantTo(self, drug):
    """
    Get the state of this virus particle's resistance to a drug. This method
    is called by getResistPop() in TreatedPatient to determine how many virus
    particles have resistance to a drug.

    drug: The drug (a string)

    returns: True if this virus instance is resistant to the drug, False
    otherwise.
    """
    try:
      return self.resistances[drug]
    except KeyError:
      return False

  def reproduce(self, popDensity, activeDrugs):
    """
    Stochastically determines whether this virus particle reproduces at a
    time step. Called by the update() method in the TreatedPatient class.

    A virus particle will only reproduce if it is resistant to ALL the drugs
    in the activeDrugs list. For example, if there are 2 drugs in the
    activeDrugs list, and the virus particle is resistant to 1 or no drugs,
    then it will NOT reproduce.

    Hence, if the virus is resistant to all drugs
    in activeDrugs, then the virus reproduces with probability:

    self.maxBirthProb * (1 - popDensity).

    If this virus particle reproduces, then reproduce() creates and returns
    the instance of the offspring ResistantVirus (which has the same
    maxBirthProb and clearProb values as its parent). The offspring virus
    will have the same maxBirthProb, clearProb, and mutProb as the parent.

    For each drug resistance trait of the virus (i.e. each key of
    self.resistances), the offspring has probability 1-mutProb of
    inheriting that resistance trait from the parent, and probability
    mutProb of switching that resistance trait in the offspring.

    For example, if a virus particle is resistant to guttagonol but not
    srinol, and self.mutProb is 0.1, then there is a 10% chance that
    that the offspring will lose resistance to guttagonol and a 90%
    chance that the offspring will be resistant to guttagonol.
    There is also a 10% chance that the offspring will gain resistance to
    srinol and a 90% chance that the offspring will not be resistant to
    srinol.

    popDensity: the population density (a float), defined as the current
    virus population divided by the maximum population

    activeDrugs: a list of the drug names acting on this virus particle
    (a list of strings).

    returns: a new instance of the ResistantVirus class representing the
    offspring of this virus particle. The child should have the same
    maxBirthProb and clearProb values as this virus. Raises a
    NoChildException if this virus particle does not reproduce.
    """

    for drug in activeDrugs:
      if not self.isResistantTo(drug):
        raise NoChildException

    if random.random() < self.getMaxBirthProb() * (1 - popDensity):

      resistances = self.getResistances()

      for r in resistances:
        if resistances[r]:
          if random.random() < self.getMutProb():
            resistances[r] = False
        elif random.random() < self.getMutProb():
          resistances[r] = True

      return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(),
                            resistances=resistances, mutProb=self.getMutProb())

    raise NoChildException


class TreatedPatient(Patient):
  """
  Representation of a patient. The patient is able to take drugs and his/her
  virus population can acquire resistance to the drugs he/she takes.
  """

  def __init__(self, viruses, maxPop):
    """
    Initialization function, saves the viruses and maxPop parameters as
    attributes. Also initializes the list of drugs being administered
    (which should initially include no drugs).

    viruses: The list representing the virus population (a list of
    virus instances)

    maxPop: The  maximum virus population for this patient (an integer)
    """
    Patient.__init__(self, viruses, maxPop)
    self.drugs = set()

  def addPrescription(self, newDrug):
    """
    Administer a drug to this patient. After a prescription is added, the
    drug acts on the virus population for all subsequent time steps. If the
    newDrug is already prescribed to this patient, the method has no effect.

    newDrug: The name of the drug to administer to the patient (a string).

    postcondition: The list of drugs being administered to a patient is updated
    """
    self.drugs.add(newDrug)


  def getPrescriptions(self):
    """
    Returns the drugs that are being administered to this patient.

    returns: The list of drug names (strings) being administered to this
    patient.
    """
    return self.drugs

  def getResistPop(self, drugResist):
    """
    Get the population of virus particles resistant to the drugs listed in
    drugResist.

    drugResist: Which drug resistances to include in the population (a list
    of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

    returns: The population of viruses (an integer) with resistances to all
    drugs in the drugResist list.
    """
    count = 0
    for virus in self.viruses:
      for drug in drugResist:
        if not virus.isResistantTo(drug):
          break
      else:
        count += 1
    return count

  def update(self):
    """
    Update the state of the virus population in this patient for a single
    time step. update() should execute these actions in order:

    - Determine whether each virus particle survives and update the list of
      virus particles accordingly

    - The current population density is calculated. This population density
      value is used until the next call to update().

    - Based on this value of population density, determine whether each
      virus particle should reproduce and add offspring virus particles to
      the list of viruses in this patient.
      The list of drugs being administered should be accounted for in the
      determination of whether each virus particle reproduces.

    returns: The total virus population at the end of the update (an
    integer)
    """
    c = self.getViruses().copy()
    for virus in c:
      if virus.doesClear():
        self.viruses.remove(virus)

    c = self.getViruses().copy()

    for virus in c:
      try:
        self.viruses.append(virus.reproduce(self.getTotalPop() / self.getMaxPop(), self.getPrescriptions()))
      except NoChildException:
        pass

    return len(self.getViruses())

from statistics import mean
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
  """
  Runs simulations and plots graphs for problem 5.

  For each of numTrials trials, instantiates a patient, runs a simulation for
  150 timesteps, adds guttagonol, and runs the simulation for an additional
  150 timesteps.  At the end plots the average virus population size
  (for both the total virus population and the guttagonol-resistant virus
  population) as a function of time.

  numViruses: number of ResistantVirus to create for patient (an integer)
  maxPop: maximum virus population for patient (an integer)
  maxBirthProb: Maximum reproduction probability (a float between 0-1)
  clearProb: maximum clearance probability (a float between 0-1)
  resistances: a dictionary of drugs that each ResistantVirus is resistant to
               (e.g., {'guttagonol': False})
  mutProb: mutation probability for each ResistantVirus particle
           (a float between 0-1).
  numTrials: number of simulation runs to execute (an integer)

  """

  results1 = [[] for _ in range(150)]
  results2 = [[] for _ in range(150)]
  for _ in range(numTrials):
    viruses = []
    for _ in range(numViruses):
      viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    p = TreatedPatient(viruses, maxPop)
    for i in range(150):
      results1[i].append(p.update())
    p.addPrescription('guttagonol')
    for i in range(150):
      results2[i].append(p.update())

  averaged1 = [mean(result) for result in results1]
  averaged2 = [mean(result) for result in results2]
  pylab.plot(averaged1)
  pylab.plot(averaged2)
  pylab.title('ResistantVirus simulation')
  pylab.xlabel('time step')
  pylab.ylabel('# viruses')
  pylab.legend()
  pylab.show()
