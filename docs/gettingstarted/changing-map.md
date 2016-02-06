# Changing map

![Map coords](../img/map_coords.png)

## Get tiles from row

in case, you want to get all tiles in ROW with index 0 (which is first row in scenario), then change terrain type of tiles it contains.

for more terrain types, check [enums.terrains](../enums/terrains.md)

```python
>>> firstRow = scenario.tiles[0]  # get first row
>>> for tile in first row:
        tile.type = 4
```

## Get tile from middle of map

```python
>>> cx, cy = scenario.map.width//2, scenario.map.height//2  # get coordinations
>>> middleTile = scenario.tiles[cx][cy]
```

## Elevating up whole map

elevating all tiles in scenario with tiles.

```python
>>> scenario.tiles.incElevation(increase=2)
```

increase 2 means increase all tile up 2. Tile with elevation 3 will have 5

## Replacing all desert with grass1

```python
>>> scenario.tiles.replaeTerrain(14, 0)
```

14 = Desert, which terrain type will be replaced

0 = Grass 1, with this terrain type

## Clear elevation

```python
>>> scenario.tiles.clearTerrain()
>>> scenario.tiles.clearTerrain(0)  # same as above
```

all tiles will have terrain type = 0 (in both cases)

