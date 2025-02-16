"""
Representation of CHGCAR objects.

-------------------------------
Charge density data node (stores CHGCAR objects in the repository).
"""
# pylint: disable=abstract-method
# explanation: pylint wrongly complains about (aiida) Node not implementing query
from aiida.orm import SinglefileData


class ChargedensityData(SinglefileData):
    pass
