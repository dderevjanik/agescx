# Adding new unit

## Something about unit ID

Every unit on map has own special ID, with every call of **addNew()** method, it will create with next unique unit ID. If you want add specific ID to unit, add optional argument with custom ID **addNew(id=397)**.

Check all [class.Unit(blank)](#) attributes and methods 

## Adding unit to specific player

Creating unit for Player 1

```python
scenario.players[1].units.new()
```

Creating unit for Gaia Player

```python
scenario.players[0].units.new() # Player 0 = Gaia Player
```

## Unit at positions

```python
scenario.players[1].units.new(x=23, y=5)
```

For more information about coordinations in scenario, check [class.Tiles](../scenario/tiles.md)

## Adding Knight or other real unit

Adding specific unit, you have to know unit type ID. For example, in this case, Knight has id type=38. 

For list of all unit types, check [enums.Units](../enums/units.md)

```python
scenario.plyers[1].units.new(x=23, y=5, type=38)
```