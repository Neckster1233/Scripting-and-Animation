import maya.cmds as cmds

def create_control():
    sels = cmds.ls(selection = True)

    for sel in sels:
        grp = cmds.group(empty=True, name=sel + "_GRP")
        transform = cmds.xform(sel, query=True, translation=True, worldSpace=True)
        rotate = cmds.xform(sel, query=True, rotation=True, worldSpace=True)
        ctrl = cmds.circle(normal=[1,0,0], radius=.5)
        cmds.xform(grp, rotation=rotate, translation=transform)
        cmds.xform(ctrl, rotation=rotate, translation=transform)
        cmds.parent(ctrl, grp)
        ctrlname=(grp.rpartition('_') [0])
        ctrlname2='%s_Ctrl' % ctrlname
        newname=cmds.rename(grp, ctrlname2)