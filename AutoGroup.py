import maya.cmds as cmds

sels = cmds.ls(selection = True)

for sel in sels:
    grp = cmds.group(empty=True, name=sel + "_GRP")
    transform = cmds.xform(sel, query=True, translation=True, worldSpace=True)
    rotate = cmds.xform(sel, query=True, rotation=True, worldSpace=True)
    cmds.xform(grp, rotation=rotate, translation=transform)
    cmds.parent(sel, grp)