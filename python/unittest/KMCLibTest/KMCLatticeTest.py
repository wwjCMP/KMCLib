""" Module for testing the KMCLattice class. """


# Copyright (c)  2012  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#


import unittest
import numpy

from KMCLib.KMCUnitCell import KMCUnitCell
from KMCLib.Exceptions.Error import Error

# Import from the module we test.
from KMCLib.KMCLattice import KMCLattice


# Implement the test.
class KMCLatticeTest(unittest.TestCase):
    """ Class for testing the KMCLattice class. """

    def testConstruction(self):
        """ Test the construction of the lattice """
        # Setup a valid unitcell.
        cell_vectors = [[2.3, 0.0, 0.0],
                        [2.4, 3.0, 0.0],
                        [0.0, 0.0, 11.8]]

        basis_points = [[0.0, 0.0, 0.0],
                        [0.5, 0.5, 0.0]]

        unit_cell = KMCUnitCell(cell_vectors=cell_vectors,
                                basis_points=basis_points)

        # Setup the other input.
        repetitions = (10,12,45)
        periodic = (True,True,False)

        # Construct the KMCLattice object.
        lattice = KMCLattice(unit_cell=unit_cell,
                             repetitions=repetitions,
                             periodic=periodic)

        # Check that the unitcell object stored on the class
        # is the same one as constructed here (checked by reference)
        self.assertTrue( unit_cell == lattice._KMCLattice__unit_cell)

    def testQueryLatticeSites(self):
        """ Test that the returned lattice site data is coorect. """
        cell_vectors = [[2.3, 0.0, 0.0],
                        [2.4, 3.0, 0.0],
                        [0.0, 0.0, 11.8]]

        basis_points = [[0.0, 0.0, 0.0],
                        [0.5, 0.5, 0.0]]

        unit_cell = KMCUnitCell(cell_vectors=cell_vectors,
                                basis_points=basis_points)

        # Setup the other input.
        repetitions = (2,1,1)
        periodic = (True,True,False)

        # Construct the KMCLattice object.
        lattice = KMCLattice(unit_cell=unit_cell,
                             repetitions=repetitions,
                             periodic=periodic)

        # These are all the sites in the lattice, given in
        # the fractional coordinates of the original cell.
        sites = lattice.sites()
        ref_sites = numpy.array([[ 0. ,  0. ,  0. ],
                                 [ 0.5,  0.5,  0. ],
                                 [ 1. ,  0. ,  0. ],
                                 [ 1.5,  0.5,  0. ]])

        # Check against a hardcoded reference.
        self.assertAlmostEqual(numpy.linalg.norm(sites-ref_sites), 0.0, 10)

        # Test with another repetition.
        repetitions = (2,3,4)
        lattice = KMCLattice(unit_cell=unit_cell,
                             repetitions=repetitions,
                             periodic=periodic)
        sites = lattice.sites()
        ref_sites = numpy.array([[ 0. ,  0. ,  0. ],
                                 [ 0.5,  0.5,  0. ],
                                 [ 0. ,  0. ,  1. ],
                                 [ 0.5,  0.5,  1. ],
                                 [ 0. ,  0. ,  2. ],
                                 [ 0.5,  0.5,  2. ],
                                 [ 0. ,  0. ,  3. ],
                                 [ 0.5,  0.5,  3. ],
                                 [ 0. ,  1. ,  0. ],
                                 [ 0.5,  1.5,  0. ],
                                 [ 0. ,  1. ,  1. ],
                                 [ 0.5,  1.5,  1. ],
                                 [ 0. ,  1. ,  2. ],
                                 [ 0.5,  1.5,  2. ],
                                 [ 0. ,  1. ,  3. ],
                                 [ 0.5,  1.5,  3. ],
                                 [ 0. ,  2. ,  0. ],
                                 [ 0.5,  2.5,  0. ],
                                 [ 0. ,  2. ,  1. ],
                                 [ 0.5,  2.5,  1. ],
                                 [ 0. ,  2. ,  2. ],
                                 [ 0.5,  2.5,  2. ],
                                 [ 0. ,  2. ,  3. ],
                                 [ 0.5,  2.5,  3. ],
                                 [ 1. ,  0. ,  0. ],
                                 [ 1.5,  0.5,  0. ],
                                 [ 1. ,  0. ,  1. ],
                                 [ 1.5,  0.5,  1. ],
                                 [ 1. ,  0. ,  2. ],
                                 [ 1.5,  0.5,  2. ],
                                 [ 1. ,  0. ,  3. ],
                                 [ 1.5,  0.5,  3. ],
                                 [ 1. ,  1. ,  0. ],
                                 [ 1.5,  1.5,  0. ],
                                 [ 1. ,  1. ,  1. ],
                                 [ 1.5,  1.5,  1. ],
                                 [ 1. ,  1. ,  2. ],
                                 [ 1.5,  1.5,  2. ],
                                 [ 1. ,  1. ,  3. ],
                                 [ 1.5,  1.5,  3. ],
                                 [ 1. ,  2. ,  0. ],
                                 [ 1.5,  2.5,  0. ],
                                 [ 1. ,  2. ,  1. ],
                                 [ 1.5,  2.5,  1. ],
                                 [ 1. ,  2. ,  2. ],
                                 [ 1.5,  2.5,  2. ],
                                 [ 1. ,  2. ,  3. ],
                                 [ 1.5,  2.5,  3. ]])

        # Check against a hardcoded reference.
        self.assertAlmostEqual(numpy.linalg.norm(sites-ref_sites), 0.0, 10)

    def testQueryRepetitions(self):
        """ Test that the returned repetitions data is coorect. """
        cell_vectors = [[2.3, 0.0, 0.0],
                        [2.4, 3.0, 0.0],
                        [0.0, 0.0, 11.8]]

        basis_points = [[0.0, 0.0, 0.0],
                        [0.5, 0.5, 0.0]]

        unit_cell = KMCUnitCell(cell_vectors=cell_vectors,
                                basis_points=basis_points)

        # Setup the repetitions.
        repetitions = (2,1,1)
        periodic = (True,True,False)

        # Construct the KMCLattice object.
        lattice = KMCLattice(unit_cell=unit_cell,
                             repetitions=repetitions,
                             periodic=periodic)

        # Check that the repetitions are the same.
        self.assertEqual(lattice.repetitions()[0], repetitions[0])
        self.assertEqual(lattice.repetitions()[1], repetitions[1])
        self.assertEqual(lattice.repetitions()[2], repetitions[2])

    def testQueryBasis(self):
        """ Test that the returned basis data is coorect. """
        cell_vectors = [[2.3, 0.0, 0.0],
                        [2.4, 3.0, 0.0],
                        [0.0, 0.0, 11.8]]

        basis_points = [[0.0, 0.0, 0.0],
                        [0.5, 0.5, 0.0]]

        unit_cell = KMCUnitCell(cell_vectors=cell_vectors,
                                basis_points=basis_points)

        # Setup the repetitions.
        repetitions = (2,1,1)
        periodic = (True,True,False)

        # Construct the KMCLattice object.
        lattice = KMCLattice(unit_cell=unit_cell,
                             repetitions=repetitions,
                             periodic=periodic)

        # Check that the basis is the one from the unitcell.
        self.assertAlmostEqual(numpy.linalg.norm(lattice.basis() - lattice._KMCLattice__unit_cell.basis()), 0.0, 10)


    def testGlobalIndex(self):
        """ Test that the global index function returns correct values. """
        cell_vectors = [[2.3, 0.0, 0.0],
                        [2.4, 3.0, 0.0],
                        [0.0, 0.0, 11.8]]

        basis_points = [[0.0, 0.0, 0.0],
                        [0.5, 0.5, 0.0]]

        unit_cell = KMCUnitCell(cell_vectors=cell_vectors,
                                basis_points=basis_points)

        # Setup the repetitions.
        nI = 2
        nJ = 12
        nK = 3
        nB = 2
        repetitions = (nI,nJ,nK)
        periodic = (True,True,False)

        # Construct the KMCLattice object.
        lattice = KMCLattice(unit_cell=unit_cell,
                             repetitions=repetitions,
                             periodic=periodic)

        # Loop through all indices and check that the globalIndex function computes them correctly.
        increment = 0
        for i in range(nI):
            for j in range(nJ):
                for k in range(nK):
                    for b in range(nB):
                        index = lattice._globalIndex(i,j,k,b)
                        self.assertEqual(index, increment)
                        increment += 1

    def testConstructionFailUnitcell(self):
        """ Test that construction of the lattice fails if the unitcell parameter has the wrong type."""
        # Setup a wrong unitcell.
        unit_cell = "KMCUnitCell"

        # Setup the other input.
        repetitions = (10,12,45)
        periodic = (True,True,False)

        # Construct the KMCLattice object.
        self.assertRaises(Error, lambda: KMCLattice(unit_cell=unit_cell,
                                                    repetitions=repetitions,
                                                    periodic=periodic))

    def testConstructionFailRepetitions(self):
        """ Test that construction of the lattice fails if the periodic parameter is incorrect."""
        # Setup a valid unitcell.
        cell_vectors = [[2.3, 0.0, 0.0],
                        [2.4, 3.0, 0.0],
                        [0.0, 0.0, 11.8]]

        basis_points = [[0.0, 0.0, 0.0],
                        [0.5, 0.5, 0.0]]

        unit_cell = KMCUnitCell(cell_vectors=cell_vectors,
                                basis_points=basis_points)

        periodic = (False,True,True)

        # Fail because of not being a sequence.
        repetitions = 1
        self.assertRaises(Error, lambda: KMCLattice(unit_cell=unit_cell,
                                                    repetitions=repetitions,
                                                    periodic=periodic))

        # Fail because of wrong length.
        repetitions = (1,2,3,4,5)
        self.assertRaises(Error, lambda: KMCLattice(unit_cell=unit_cell,
                                                    repetitions=repetitions,
                                                    periodic=periodic))

        # Fail because of wrong type.
        repetitions = (1,3.0,1)
        self.assertRaises(Error, lambda: KMCLattice(unit_cell=unit_cell,
                                                    repetitions=repetitions,
                                                    periodic=periodic))

    def testConstructionFailPeriodic(self):
        """ Test that construction of the lattice fails if the periodic parameter is incorrect."""
        # Setup a valid unitcell.
        cell_vectors = [[2.3, 0.0, 0.0],
                        [2.4, 3.0, 0.0],
                        [0.0, 0.0, 11.8]]

        basis_points = [[0.0, 0.0, 0.0],
                        [0.5, 0.5, 0.0]]

        unit_cell = KMCUnitCell(cell_vectors=cell_vectors,
                                basis_points=basis_points)

        repetitions = (10,12,45)

        # Fail because of not being a sequence.
        periodic = True
        self.assertRaises(Error, lambda: KMCLattice(unit_cell=unit_cell,
                                                    repetitions=repetitions,
                                                    periodic=periodic))

        # Fail because of wrong length.
        periodic = (True,True,True,True)
        self.assertRaises(Error, lambda: KMCLattice(unit_cell=unit_cell,
                                                    repetitions=repetitions,
                                                    periodic=periodic))

        # Fail because of wrong type.
        periodic = (True,True,1)
        self.assertRaises(Error, lambda: KMCLattice(unit_cell=unit_cell,
                                                    repetitions=repetitions,
                                                    periodic=periodic))


if __name__ == '__main__':
    unittest.main()

