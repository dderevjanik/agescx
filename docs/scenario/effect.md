# Effect

## About

Effect provide some effect funcionality to scenario. First, must be all conditions accomplished in triggers to order evoke effect.

## Attributes

- **effectType** type of effect
- **check** if is checked
- **aiGoal** change AI
- **amount** how much
- **resource** type of resource [enum.Resource](../enums/resources.md)
- **state** effect state (1 = on, 0 off)
- **selectedCount** how many units affect
- **unitId** id of single unit (0, if selectedCount > 0)
- **unitName** rename unit
- **sourcePlayer** for Player
- **targetPlayer** to Player
- **tech** tech id
- **stringId** string id
- **triggerId** which trigger affect (by Id)
- **x** Point X
- **y** Point Y
- **x1** Area Start X
- **y1** Area Start Y
- **x2** Area End X
- **y2** Area End Y
- **unitGroup** unit group [enum.Groups](../enums/groups.md)
- **unitType** type of unit [enum.Units](../enums/units.md)
- **instructionId** instruction id to evoke
- **text** effect text for instructions
- **filename** path to file
- **unitIds** if selectedCount > 0, list of selected unit Ids

## Methods

## Examples