# Units

## About

This class handles all units in scenario. Really, it doesn't store any units, only reference on PlayerUnits, which really store all units. With this class you can really easily iterate ower all units in scenario using python FOR.

## Attributes

- **nextId** next unit ID

## Methods

- **toJSON()**
- **delUnit(id)** delete unit(s) with specific ID
- **delAll()** delete all units in scenario
- **getById(id)** get unit(s) by ID, return as list
- **exists(id)** boolean, true if unit(s) with ID already exist
- **new(owner, **unitConfig)** creating new unit to specific owner, check unitConfig

## Examples

changing all units types by 1

*Note: this example is only for demnostration, because result is ugly*

```python
for unit in scenario.units:
    unit.type += 1
```