# Unit

## About

## Attributes

- **id (readonly)** unit specific ID
- **owner (readonly)** player, who owns this unit
- **type** type of unit, check [units enums](../enums/units.md)
- **x** unit x position
- **y** unit y position
- **angle** starting angle 
- **frame** starting frame
- **inId** garisson, in which unit is this unit garissoned
- **unknown1**
- **unknown2**

## Methods

- **toJSON()**
- **move(dx, dy)** how many tiles move unit

## Examples

randomize rotation angles on all units

```python
from random import randint

for unit in scenario.units:
    unit.angle = randint(0, 13)  # max angle is 14.0
```

