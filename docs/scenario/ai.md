# AI

## About

If player is controled by Computer, it'll use AI section. 

## Attributes

- **name** name of AI
- **type** type
- **source** source code from .PER file
- **unknown1**
- **unknown2**

## Methods

- **toJSON()**
- **readSource(filename)** read source from a file
- **saveSource(filename)** save source to a file
- **clear()** clear whole AI section

## Examples

Exporting .PER file from player 2

```python
scenario.players[2].ai.saveSource("exported_ai.per")
```
