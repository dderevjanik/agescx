# Scenario Basic

describe basic functions of agescx module

## Attributes

## Methods

## Examples

### New

```python
from agescx import *

scenario = Scenario()
```

will create blank scenario

### Load

there's two way to load scenario.

while initializing 

```python
from agescx import *

scenario = Scenario("myScenario.scx")
```

or 

```python
from agescx import *

scenario = Scenario()
scenario.load("myScenario.scx")
```

### Save

```python
scenario.save("myEditedScenario.scx")
```
