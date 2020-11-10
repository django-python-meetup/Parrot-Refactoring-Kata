from enum import Enum
from dataclasses import dataclass
from typing import Union


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3



def _base_speed(self):
    return self._base_speed

def _coconut_load_based(self):
    return max(0, self._base_speed - self._load_factor * self.number_of_coconuts)

def _possibly_nailed(self):
    if self.nailed:
        return 0
    else:
        return self._compute_base_speed_for_voltage


speed_funcs = {
    ParrotType.EUROPEAN: _base_speed,
    ParrotType.AFRICAN: _coconut_load_based,
    ParrotType.NORWEGIAN_BLUE: _possibly_nailed,
}


@dataclass
class Parrot:
    type_of_parrot: ParrotType
    number_of_coconuts: int
    voltage: Union[int, float]
    nailed: bool

    def speed(self):
        return speed_funcs[self.type_of_parrot](self)

    @property
    def _compute_base_speed_for_voltage(self):
        return min([24.0, self.voltage * self._base_speed])

    @property
    def _load_factor(self):
        return 9.0
    @property
    def _base_speed(self):
        return 12.0

