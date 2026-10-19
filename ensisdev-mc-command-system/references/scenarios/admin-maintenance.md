# Scenario — Administration / Maintenance

## When this scenario applies

The project exposes runtime administration such as reload, save, debug, version, diagnostics, conversion or repair.

## Separation rule

Plugin/system administration should not be mixed into ordinary resource operations just because the same root command exists.

A resource root may contain:

```text
list
info
create
edit
remove
```

while a system root handles:

```text
version
save
reload
debug
convert
```

if that matches the existing product surface.

## Reload

Define exactly what reload affects. Never imply a complete process restart if only configuration is re-read.

## Save

Only expose a manual save command when runtime state/persistence semantics make it meaningful.

## Debug

Debug commands should be clearly privileged and must not accidentally enable sensitive output for ordinary users.

## Convert

Conversion should make source format and scope explicit. Bulk conversion is a migration operation, not a casual edit.
