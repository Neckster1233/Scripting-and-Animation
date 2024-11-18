# Python Macro Script

import maya.cmds as cmds

# Create Base Sphere
cmds.polySphere(radius = 3, subdivisionsX = 20, subdivisionsY = 20, axis = (0, 1, 0), createUVs = 2, constructionHistory = 1)
cmds.move(0, 3, 0, relative = True)

#Create Middle Sphere
cmds.polySphere(radius=2, subdivisionsX=20, subdivisionsY=20, axis=(0, 1, 0), createUVs=2, constructionHistory=1)
cmds.polySphere(edit=True, radius=2)
cmds.move(0, 7, 0, relative = True)

#Create Head Sphere
cmds.polySphere(radius = 1, subdivisionsX = 20, subdivisionsY = 20, axis = (0, 1, 0), createUVs = 2, constructionHistory = 1)
cmds.move(0, 9.5, 0, relative = True)

#Create Nose Cone
cmds.polyCone(radius=1, height=2, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=0, axis=(0, 1, 0), roundCap=0, createUVs=3, constructionHistory=1)
cmds.move(0, 9.5, 1.1, relative = True)
cmds.scale(.3, .5, .275, relative = True)
cmds.rotate(90, 0, 0, objectSpace=True, forceOrderXYZ=True, relative = True)

#Create Right Eye
cmds.polySphere(radius=1, subdivisionsX=20, subdivisionsY=20, axis=(0, 1, 0), createUVs=2, constructionHistory=1)
cmds.move(-.3, 9.7, .8, relative = True)
cmds.scale(.167, .167, .167, relative = True)

#Create Left Eye
cmds.polySphere(radius=1, subdivisionsX=20, subdivisionsY=20, axis=(0, 1, 0), createUVs=2, constructionHistory=1)
cmds.move(.3, 9.7, .8, relative = True)
cmds.scale(.167, .167, .167, relative = True)

#Create Top Button
cmds.polySphere(radius=1, subdivisionsX=20, subdivisionsY=20, axis=(0, 1, 0), createUVs=2, constructionHistory=1)
cmds.move(0, 6.9, 1.9, relative = True)
cmds.scale(.195, .195, .195, relative = True)

#Create Middle Button
cmds.polySphere(radius=1, subdivisionsX=20, subdivisionsY=20, axis=(0, 1, 0), createUVs=2, constructionHistory=1)
cmds.move(0, 5, 2.1, relative = True)
cmds.scale(.195, .195, .195, relative = True)

#Create Bottom Button
cmds.polySphere(radius=1, subdivisionsX=20, subdivisionsY=20, axis=(0, 1, 0), createUVs=2, constructionHistory=1)
cmds.move(0, 3.7, 2.8, relative = True)
cmds.scale(.195, .195, .195, relative = True)
