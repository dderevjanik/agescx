# Installation

In order to use agescx you must have installed atleast [Python 3.4](https://www.python.org/downloads/)

## Installation

*NOTE: doesn't work, yeat*

```
$ pip install agescx
```

or with easy_install 
 
```
$ easy_install agescx
```

If you want install manual or develop version, download this repository, unpack it and from 
command line type

```
$ python setup.py install
```

if they're no error, installation runned properly

## Usage

open python and run this code

```python
from agescx import *
```

if some error pop, you don't have installed agescx or you have 
old python 2.x version.

## Examples

Here some examples you are able to do with newly installed module

### Print player 1 name
```python
from agescx import *

scenario = Scenario("PathToScenario.scx")
player1 = scenario.players[1]
print(player1.name)
```

### Print all player names

```python
for player in scenario.players:
    print(player.name)
```

*it also print "" for gaia, which is player with index 0*

### Resize map

```python
scenario.map.resize(32, 32) # width and height
```

*don't forget to save map, because agescx don't have auto-save*

### Create new unit for player 1

when creating new unit, you have to know number of type of your unit you want to create. For example, 67=knight ...check [Unit types](#)

```python
scenario.players[1].units.new(x=1, y=0, type=67)
```
