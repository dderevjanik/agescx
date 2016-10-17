# SCX format

## Introduction

Scx format was formed by Esemble Studios, [Microsoft] for their games, first time for [Age of Empires]  (1997) and second for [Age of Empires 2]  (1999), and for their last game on genie engine [Star Wars: Galactic Battlegrounds]. Format is used to store maps (scenarios). It's uses C++98 standart datatypes. Also scenario data are compressed with DEFLAT method. This document primary describes scx format used for Age of Empires 2, version 1.21.

## Format Standart

Most of this document originaly writen by DiGit's. specification with knowledge by AOHH and Iberico format and finally extend with me.

## List of Structures

* [**Uncompressed Header**](#uncompressed-header) -basic information about scenario
* [**Compressed Data**](#compressed-data) -compressed information about scenario
* [Player Data 1](#player-data1) -
* [**Messages**](#messages) -messages like instructions and hints
* [**Cinematics**](#cinematics) -cinematics file names
* [Background Image](#background-image) -background image information
* [Bitmap Info Header](#bitmap-info-header) -image information (if image incldued)
* [Player Data 2](#player-2-data) -
* [AI Files](#struct-ai-files) -ai files included
* [Resources](#struct-resources) -resources for player (wo population)
* [**Global Victory**](#global-victory) -global victory information
* [**Diplomacy**](#diplomacy) -diplomacy for every player
* [Diplomacy per Player](#struct-diplomacy-per-player)
* [Disables](#disables) -disables tehnologies, units and buildings
* [**Map**](#map) -information about map
* [Terrain](#struct-terrain) -information about tile(s) (type and elevation)
* [Units Section](#units-section) -how many units section is described
* [Player Data 4](#struct-player-data-4) -
* [Player Units](#struct-player-units) -how many units are stored per player
* [**Unit**](#struct-unit) -all unit information
* [Player Data 3](#player-data-3) - 
* [Player Data 3 Sub](#struct-player-data-3) -
* [Triggers Section](#triggers-section) -how many triggers
* [**Trigger**](#structure-trigger) -all stored triggers
* [**Efffect**](#structure-effect) -all stored effects for trigger
* [**Condition**](#structure-condition) -all stored conditoins for trigger
* [Included Files](#included-files) -included files
* [PER File Error](#per-file-error) -PER file error

## About Scenario

Here you will find interesting info about scenario files

### Coords

Coordinations [0, 0] starts from left point of map, continue to top of map [0, mapWidth]. Tiles are one dimension array, starting from position [0, 0].This image shows how are Tile[x, y] calculated. 

![Map Coordinations](img/map_coords.png)

## Format

### Data Types

A note about data lengths: they specify both the length of the data and
how to interpret it. For example:

* **s32** is a signed 32-bit integer
* **u16** is an unsigned 16-bit integer
* **f32** is a 32-bit (single-precision) floating point number
* **c4** is a 4-byte character string
* **str16** is a variable-length character string (see below)
* **40** means 40 bytes of data
* **16*u16** means 16 unsigned 16-bit integers

Variable-length character strings are stored in the scenario as length/data
pairs. For example "str16" means there is a 16-bit length field with value n
followed by n bytes (characters). str32 is also used, but more rarely.

### Uncompressed Header ###

Length | Requires   | Description
-------|------------|----------------------------------------------------
c4     |            | Version (ASCII): 1.10, 1.18, 1.21
u32    |            | Length of header (excluding version and self)
s32    |            | Savable
u32    |Savable >= 2| Timestamp of last save
str32  |            | Scenario Instructions
u32    |            | Individual Victories Used
u32    |            | Player count (thanks iberico)


### Compressed DataIt uses Deflate method with *(-MAX_WBITS, for python)*

#### Header

Length | MinVer | Description
-------|--------|----------------------------------------------------
u32    |        | Next unit ID to place
f32    |        | Version 2
16*256 |        | ASCII player names
16*u32 | 1.18   | string table player names
16*16  |        | Player Data#1 see [sub-struct below](#player-data1)
u8     |        | Conquest Mode
u16    |        | Mission Items Counter = n
u16    |        | Mission Available
f32    |        | Mission Timeline
n*30   |        | Mision Item (each 30 bytes)
str16  |        | Original filename, created while first scenario save

##### Player Data#1

Length | MinVer | Description
-------|--------|----------------------------------------------------
u32    |        | Boolean: Active
u32    |        | Boolean: Human
u32    |        | Civilization, see IDs at this document
u32    |        | CTY Mode

#### Messages

Length | MinVer | Description
-------|--------|----------------------------------------------------
u32    | 1.18   | String table, Instructions
u32    | 1.18   | String table, Hints
u32    | 1.18   | String table, Victory
u32    | 1.18   | String table, Loss
u32    | 1.18   | String table, History
u32    | 1.22   | String table, Scouts
str16  |        | ASCII, Instructions
str16  |        | ASCII, Hints
str16  |        | ASCII, Victory
str16  |        | ASCII, Loss
str16  |        | ASCII, History
str16  | 1.22   | ASCII, Scouts

#### Cinematics

Length | MinVer | Description
-------|--------|----------------------------------------------------
str16  |        | ASCII, Pregame cinematic filename
str16  |        | ASCII, Victory cinematic filename
str16  |        | ASCII, Loss cinematic filename
1      |        | Separator (! in some version)

#### Background Image

Length | MinVer | Description
-------|--------|----------------------------------------------------
str16  |        | ASCII, Background filename
u32    |        | Picture Version
u32    |        | Bitmap width
s32    |        | Bitmap height
s16    |        | Picture Orientation
40+SIZE|        | [BITMAPINFOHEADER](#bitmap-info-header) (if width >= 0 && height >= 0)

#### Bitmap Info Header

**WARNING:** This section is readed only if above **Include** value is -1 or 2 !
Look at this [btmp info header article] about format spec for more information

Length     | MinVer | Description
-----------|--------|----------------------------------------------------
s32        |        | Size
u32        |        | Width
s32        |        | Height
s16        |        | Planes
s16        |        | BitCount
u32        |        | Compression
u32        |        | SizeImage **SIZ**
u32        |        | XPels
u32        |        | YPels
U32        |        | Colors Used **CLR**
u32        |        | Important Colors
u32***CLR**|        | Calculated: u32*ColorsUsed
u32***SIZ**|        | Calculated: u32*SizeImage


#### Player 2 Data

Length | MinVer | Description
-------|--------|----------------------------------------------------
32str16|        | Unknown strings (2 per player?)
16str16|        | AI names, one per player
16*var |        | AI files, see [sub-struct below](#struct-ai-files)
u8     |        | AI type, 0 = custom, 1 = standard, 2 = none. Thanks iberico.
u32    |        | Separator, 0xFFFFFF9D
16*24  |        | Resources, see [sub-struct below](#struct-resources)

##### Struct: AI Files

Length | MinVer | Description
-------|--------|----------------------------------------------------
u32    |        | unknown, always 0
u32    |        | unknown, always 0
str32  |        | AI .per file text

##### Struct: Resources

Length | MinVer | Description
-------|--------|----------------------------------------------------
u32    |        | Gold
u32    |        | Wood
u32    |        | Food
u32    |        | Stone
u32    |        | "Ore X", not used in AOK
u32    |        | Trade Goods

#### Global Victory

Length | MinVer | Description
-------|--------|----------------------------------------------------
u32    |        | Separator, 0xFFFFFF9D
u32    |        | Boolean: conquest required? (for custom vict)
u32    |        | Ruins
u32    |        | Artifacts
u32    |        | Discovery
u32    |        | Explored % of map required
u32    |        | Gold
u32    |        | Boolean: all custom conditions required?
u32    |        | Mode, see below
u32    |        | Required score for score victory
u32    |        | Time for timed game, in 10ths of a year (eg, 100 = 10yr)

#### Diplomacy

Length  | MinVer | Description
--------|--------|----------------------------------------------------
16*64   |        | Per-player diplomacy, see [sub-struct](#struct-diplomacy-per-player) below
16*12*60|        | Individual Victories (12 Conditions per 16 Players)
u32     |        | Separator, 0xFFFFFF9D
16*u32  |        | Boolean: Allied vict, per-player. Ignored (see PData3). Thanks iberico.

##### Struct: Diplomacy Per-player

Length | MinVer | Description
-------|--------|----------------------------------------------------
16*u32 |        | Stance with each player, 0 = allied, 1 = neutral, 3 = enemy

#### Disables

Length | MinVer | Description
-------|--------|----------------------------------------------------
16*u32 |        | Per-player, number of disabled techs
16*120 |        | Per-player, Disabled technology IDs (30*u32)
16*120 | 1.30   | Per-player, Extra disabled technologies (30*u32)
16*u32 |        | Per-player, number of disabled units
16*120 |        | Per-player, Disabled unit IDs (30*u32)
16*120 | 1.30   | Per-player, Extra disabled units (30*u32)
16*u32 |        | Per-player, number of disabled buildings
16*80  |        | Per-player, Disabled building IDs (20*u32)
16*160 | 1.30   | Per-player, Extra disabled buildings (40*u32)
u32    |        | Combat Mode
u32    |        | Naval Mode
u32    |        | Boolean: all techs
16*u32 |        | Per-player, starting age. See below. 0-8 Players, 9 - Gaia, 10-16 Unused players

#### Map

Length          | MinVer | Description
----------------|--------|-------------------------------------------
u32             |        | Separator, 0xFFFFFF9D
s32             |        | Player 1 camera, Y
s32             |        | Player 1 camera, X
s32             | 1.21   | AI Type (see list at bottom)
u32             |        | Map Width (AOK caps at 256), **W**
u32             |        | Map Height (AOK caps at 256), **H**
**W**\***H**\*3 |        | Terrain data, see [sub-struct](#struct-terrain) below

##### Struct: Terrain

Tiles are one dimensional array. There's not any X or Y. It's calculated internal. First tile[X:0, Y:0] starts at leftmost corner and continues at uppest corner of minimap. See [example image](#coords) how tiles are readed.

length | minver | description
-------|--------|----------------------------------------------------
u8     |        | terrain id, see list at bottom
u8     |        | elevation
u8     |        | unused = 0

#### Units Section

length    | minver | description
----------|--------|----------------------------------------------------
u32       |        | number of unit sections. I've always seen = 9. **P**
8*28      |        | Player Data 4, see [sub-struct](#struct-player-data-4) below
**P***var |        | Player Units, see [sub-struct](#struct-player-units) below. GAIA units come first.

##### Struct: Player Data 4

length | minver | description
-------|--------|----------------------------------------------------
f32    |        | Food, duplicate
f32    |        | Wood, duplicate
f32    |        | Gold, duplicate
f32    |        | Stone, duplicate
f32    |        | "Ore X", duplicate
f32    |        | Trade Goods Not in SW:GB.
f32    | 1.21   | Population limit

##### Struct: Player Units

length   | minver | description
---------|--------|----------------------------------------------------
u32      |        | Unit count, **N**
**N***29 |        | Units, see [sub-struct](#struct-unit) below

##### Struct: Unit

length | minver | description
-------|--------|----------------------------------------------------
f32    |        | X position
f32    |        | Y position
f32    |        | Z position
u32    |        | ID (for triggers, etc.)
u16    |        | Unit "constant", e.g. Archer, Man-at-arms
u8     |        | Status = 2
f32    |        | Rotation, in radians
u16    |        | Initial animation frame
u32    |        | Garrisonned in ID

#### Player Data 3

length | minver | description
-------|--------|----------------------------------------------------
u32    |        | Number of players? Always = 9
8*64   |        | Player Data 3, per player. See [sub-struct](#struct-player-data-3) below.
f64    |        | Trigger Version = 1.6

##### Struct: Player Data 3

length    | minver | description
----------|--------|----------------------------------------------------
str16     |        | Constant name, like "Player 1"
f32       |        | Initial Camera, X (for Player 1 = editor camera)
f32       |        | Initial Camera, Y
s16       |        | Unknown, similar to camera X
s16       |        | Unknown, similar to camera Y
u8        |        | Boolean: Allied Victory (AOK reads this one)
u16       |        | Player count for diplomacy, **P**
**P***u8  |        | Diplomacy for interaction: 0 = allied, 1 = neutral, 2 = ?, 3 = enemy
9*u32     |        | Diplomacy for AI system: 0=GAIA, 1=self, 2=allied, 3=neutral, 4=enemy
u32       |        | Color, see values below
f32       |        | Victory Version, TODO: below are Victory conditions and effects (need to clarify these structures):
u16       |        | Unknown, **DAT**
8*u8      |        | Only included if above f32 value == 2.0
**DAT***44|        | Unknown structure, found in Grand Theft Empires
7*u8      |        | Usually 0
s32       |        | Seems to be 0 if Unknown == 1.0, -1 if Unknown == 2.0

#### Triggers Section

length     | minver | description
-----------|--------|----------------------------------------------------
s8         |        | Trigger instructions start
s32        |        | Number of triggers = 0, **T**
**T**\*var |        | Trigger data, see [sub-struct](#structure-trigger) below
**T**\*u32 |        | Trigger display order array

##### Structure: Trigger

length     | minver | description
-----------|--------|----------------------------------------------------
u32        |        | Boolean: enabled?
s8         |        | Boolean: looping?
s32        |        | String Table ID = -1
u8         |        | Boolean: objective?
u32        |        | Description order (in objectives)
u32        |        | Trigger starting time
str32      |        | Trigger description
str32      |        | Trigger name (max 44 characters in UI)
s32        |        | Number of effects = **E**
**E**\*var |        | Effect data, see [sub-struct](#structure-effect) below
**E**\*s32 |        | Effect display order array
s32        |        | Number of conditions = **C**
**C**\*var |        | Condition data, see [sub-struct](#structure-condition) below
**C**\*s32 |        | Condition display order array

##### Structure: Effect

length    | minver | description
----------|--------|----------------------------------------------------
s32       |        | Effect type
s32       |        | Check, always = 0x17
s32       |        | AI script goal
s32       |        | Amount, used for hp and attack
s32       |        | Resource type
s32       |        | Diplomacy, state for change
s32       |        | N.o. units selected = **N**
s32       |        | Unit ID
s32       |        | Unit Name 
s32       |        | Player Source
s32       |        | Player Target
s32       |        | Technology
s32       |        | String ID
s32       |        | Sound resource ID
s32       |        | Display Time (display instructions)
s32       |        | Trigger ID (activate/deactivate)
s32       |        | Location X
s32       |        | Location Y
s32       |        | Area 1 X
s32       |        | Area 1 Y
s32       |        | Area 2 X
s32       |        | Area 2 Y
s32       |        | Unit Group
s32       |        | Unit Type (Civilian, Military, Building, Other)
s32       |        | Instruction Panel
str32     |        | Instruction Text
str32     |        | Sound filename
s32***N** |        | Selected units IDs

##### Structure: Condition

length | minver | description
-------|--------|----------------------------------------------------
s32    |        | Condition Type
s32    |        | Check, always = 0x10
s32    |        | Amount (of Object, Diffculty)
s32    |        | Resource Type
s32    |        | Unit object
s32    |        | Unit ID
s32    |        | Unit Name
s32    |        | Player
s32    |        | Technology
s32    |        | Timer
s32    |        | Unknown
s32    |        | Area 1 X
s32    |        | Area 1 Y
s32    |        | Area 2 X
s32    |        | Area 2 Y
s32    |        | AI Signal

#### Included Files

length | minver | description
-------|--------|----------------------------------------------------
u32    |        | Boolean: files included?
u32    |        | Boolean: PER File Error, data included?
396    |        | PER File Error, if PER File Error included
var    |        | Included files

#### PER File Error

This data contains details about the last error occurrence in the PER files. This data is ignored during reading, but is written when saving a scenario with a PER file error. 
The engine outputs the details on debug mode. The developers must have needed this feature to debug their AI scripting in scenarios. Normally, a dialog box contains a message about the details of the error. I don't see why they needed this; maybe they wanted to see the data in raw binary form.
*-by AOHH*

length | minver | description
-------|--------|----------------------------------------------------
256    |        | Name of corrupted PER File
u32    |        | Unknown ID (either PER file ID or Player ID)
u32    |        | Line of error in PER File
u32    |        | Interruption line in PER File
124    |        | Extracted code from PER File
u32    |        | Error Code

[Age of Empires]: http://en.wikipedia.org/wiki/Age_of_Empires
[Age of Empires 2]: http://en.wikipedia.org/wiki/Age_of_Empires_II:_The_Age_of_Kings
[Star Wars: Galactic Battlegrounds]: http://en.wikipedia.org/wiki/Star_Wars:_Galactic_Battlegrounds
[btmp info header article]: http://www.herdsoft.com/ti/davincie/davp3xo2.htm
[Microsoft]: http://www.microsoft.com


