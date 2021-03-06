import doctest
import importlib
import sys
from distutils.version import LooseVersion

import pytest
import numpy as np


module_names = """\
ase.atoms
ase.build.tools
ase.cell
ase.collections.collection
ase.dft.kpoints
ase.eos
ase.formula
ase.geometry.cell
ase.geometry.geometry
ase.io.ulm
ase.lattice
ase.phasediagram
ase.spacegroup.spacegroup
ase.spacegroup.xtal
ase.symbols
""".split()


@pytest.mark.parametrize('modname', module_names)
def test_doctest(modname):
    if sys.version_info < (3, 6):
        pytest.skip('Test requires Python 3.6+, this is {}'
                    .format(sys.version_info))

    # Older numpies format arrays differently.
    # We use the printoptions contextmanager from numpy 1.15:
    # https://docs.scipy.org/doc/numpy/release.html#id45
    if LooseVersion(np.__version__) < '1.15':
        pytest.skip('need numpy >= 1.15')

    mod = importlib.import_module(modname)
    with np.printoptions(legacy='1.13'):
        print(mod, doctest.testmod(mod, raise_on_error=True))
