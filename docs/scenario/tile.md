# Tile

## About

Terrain is created from tiles, total number of tiles in scenario = scenario.map.width * scenario.map.height.

## Attributes

- **row (readonly)** row number
- **col (readonly)** collumn number
- **x (readonly)** x position (collumn)
- **y (readonly)** y position (row)
- **type** type of terrain, check [enums.Terrain](../enums/terrains.md)
- **elevation** eleavation
- **unknown** unknown

## Methods

- **toJSON()** return dict
- **position()** position in scenario
- **clear()** set default to terrain
- **flat()** set elevation to 0
- **up(increase=1)** increase elevation
- **down(decrease=1)** decrease elavtion

## Examples

selecting a tile from scenario

```python
tile = scenario.tiles.tile[2][1]  # select a tile from row 2 and collumn 1 
```

placing a Forest Tree on selected tile

```python
# previous code
scenario.units.new(owner=0, type=411, x=tile.x, y=tile.y)
```

creating cross from leaves under Forest tree

```python
# previous code
x = tile.x
y = tile.y
scenario.tiles[x][y].type = 5
scenario.tiles[x-1][y].type = 5
scenario.tiles[x+1][y].type = 5
scenario.tiles[x][y-1].type = 5
scenario.tiles[x][y+1].type = 5
```

