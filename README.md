![Logo](./resources/icon.png)

# KICAD-Trace-Length

Measure trace length and equivalent resistance.

## Installation

copy the content of plugin folder to:
```
~/.local/share/kicad/8.0/3rdparty/plugins/TraceLength
```


copy the content of resource folder to:
```
~/.local/share/kicad/8.0/3rdparty/resources/TraceLength
```

## How to

1. Select a track on the PCB;

2. press `u` to select the connected trace;

3. press the Plugin icon ![](./plugins/icon.png) to execute trace measurement.

## SRC icons

Icons was created using [Greenfish](http://greenfishsoftware.org/gfie.php).
Icon sources are in `.gfie` greenfish extension.

### TODO

- [ ] check for discontinuity on trace.
- [ ] extract trace thickness from stackup.