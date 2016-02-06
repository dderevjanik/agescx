# Players

## About

Is reference to all players (also non-playable) [class.Player](player.md)

## Attributes

## Methods

- **toJSON()**
- **byColor()** get players with specific color
- **byCivilization()** get players with specific civilization
- **byAge()** get players with specific age
- **humans()** get human players
- **computers()** get computer players
- **startResources()** set to starting resources to all players
- **activeAll()** activate all players
- **deactiveAll()** deactivate all players
- **active()** get active players
- **inactive()** get inactive players

## Examples

get gaia player from scenario

```python
gaia = scenario.players[0]  # 0 == gaia
```

clear all units for inactive players

```python
inactivePlayers = scenario.players.inactive()
for player in inactivePlayers:
    player.delAll()  # delete all units
```