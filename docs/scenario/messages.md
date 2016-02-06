# Messsages

## About

Every message contains Text and String ID.

![Hints Menu](../img/menu_hints.png)

Every line has exactly **54 chars**, text after that will occurs in new line. You can't use special chars like *'\n'* or *'\t'*. Only solution to place text on new line is to full current line with spaces ' '.

## Attributes

- **briefing** (readonly)
- **objectives** (readonly)
- **hints** (readonly)
- **victory** (readonly)
- **loss** (readonly)
- **history** (readonly)
- **scouts** (readonly)

## Examples

putting some objectives

```python
>>> scenario.messages.objectives.text = "Destroy enemy castle"
```

giving special string id to hints

```python
>>> scenario.messages.objectives.id = 23
```