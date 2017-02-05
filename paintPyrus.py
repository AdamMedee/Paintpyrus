
from pickle import * #For added flavour
from time import sleep
from pygame import *
from math import *
from sys import *
from random import *
from tkinter import *
from tkinter.colorchooser import *

#Inialize pygame and font
init()
font.init()
mixer.init()

#Keeps prompts onfront of the screen
root = Tk()
root.withdraw()

#Variables to do with the screen
width = 1200
height = 700
running = True #Whether program is running
screen=display.set_mode((width,height),HWSURFACE|DOUBLEBUF|RESIZABLE)
transCanvas = Surface((width, height), SRCALPHA)
gameScreen = 0 #0 is Homescreen, 1 is painting screen
myClock = time.Clock()

#Rects
canvasRect = Rect(width*0.3, 0, width*0.7, height*0.7)




#################################################################################################### 
#################################################################################################### 

#Loading and formatting images
homeScreenOriginal = transform.scale(image.load("paintPyrusFiles/images/backgrounds/background3.png"), (width, height))
paintScreenLeftOriginal = transform.scale(image.load("paintPyrusFiles/images/backgrounds/Background-UndertaleToolButtons.png"), (int(width*0.3), height))
paintScreenBottomOriginal = transform.scale(image.load("paintPyrusFiles/images/backgrounds/Background-UndertaleStamps.png"), (int(width*0.71), int(height*0.3)))
optionScreenOriginal = transform.scale(image.load("paintPyrusFiles/images/backgrounds/optionsBackground.jpg"), (width, height))
                                                  
colourPaletteOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/ColourGrid.jpg"), (int(width*0.2), int(height*0.2)))
soundButtonOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/ButtonImage-MUTE.png"), (int(width*0.02), int(height*0.03)))
stampOneUndertaleHeartOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/undertaleHeart.png"), (int(width*0.06), int(width*0.06)))
paintButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/paintUnselected.png"), (int(width*0.1),int(height*0.05)))
paintButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/paintSelected.png"), (int(width*0.1),int(height*0.05)))
optionsButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/optionsUnselected.png"), (int(width*0.14),int(height*0.05)))
optionsButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/optionsSelected.png"), (int(width*0.14),int(height*0.05)))
heartSelectOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/undertaleHeart.png"), (int(width*0.03), int(height*0.05)))
toolPencilButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/pencilUnselected.png"), (int(width*0.09), int(height*0.05)))
toolPencilButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/pencilSelected.png"), (int(width*0.09), int(height*0.05)))
toolEraserButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/eraserUnselected.png"), (int(width*0.09), int(height*0.05)))
toolEraserButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/eraserSelected.png"), (int(width*0.09), int(height*0.05)))
toolSprayButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/sprayUnselected.png"), (int(width*0.075), int(height*0.05)))
toolSprayButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/spraySelected.png"), (int(width*0.075), int(height*0.05)))
toolPenButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/penUnselected.png"), (int(width*0.045), int(height*0.05)))
toolPenButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/penSelected.png"), (int(width*0.045), int(height*0.05)))
toolMarkerButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/markerUnselected.png"), (int(width*0.09), int(height*0.05)))
toolMarkerButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/markerSelected.png"), (int(width*0.09), int(height*0.05)))
toolFillButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/fillUnselected.png"), (int(width*0.06), int(height*0.05)))
toolFillButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/fillSelected.png"), (int(width*0.06), int(height*0.05)))
toolPixelateButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/pixelateUnselected.png"), (int(width*0.1), int(height*0.05)))
toolPixelateButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/pixelateSelected.png"), (int(width*0.1), int(height*0.05)))
toolBlurButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/blurUnselected.png"), (int(width*0.06), int(height*0.05)))
toolBlurButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/blurSelected.png"), (int(width*0.06), int(height*0.05)))
shapeButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/shapesSelected.png"), (int(width*0.11), int(height*0.08)))
shapeButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/shapesUnselected.png"), (int(width*0.11), int(height*0.08)))
homeButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/homeSelected.png"), (int(width*0.08), int(height*0.05)))
homeButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/homeUnselected.png"), (int(width*0.08), int(height*0.05)))
colourPaletteOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/ColourGrid.jpg"), (int(width*0.2), int(height*0.2)))
blackToWhiteOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/blackToWhite.jpg"), (int(width*0.2), int(height*0.04)))
whiteHeartColOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/whiteHeart.png"), (int(width*0.05),int(height*0.08)))
openNextPageWhiteOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/shapePageNextWhite.png"), (int(width*0.015), int(height*0.08)))
openNextPageGrayOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/shapePageNextGray.png"), (int(width*0.015), int(height*0.08)))
clearButtonOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/clearScreen.png"), (int(width*0.08), int(height*0.06)))
sizeBarOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/resizingBar.png"), (int(width*0.22), int(height*0.06)))
rectButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/rectangleUnselected.png"), (int(width*0.04), int(height*0.05)))
rectButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/rectangleSelected.png"), (int(width*0.04), int(height*0.05)))
ellipseButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/ellipseUnselected.png"), (int(width*0.04), int(height*0.05)))
ellipseButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/ellipseSelected.png"), (int(width*0.04), int(height*0.05)))
lineButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/lineUnselected.png"), (int(width*0.04), int(height*0.05)))
lineButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/lineSelected.png"), (int(width*0.04), int(height*0.05)))
triangleButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/triangleUnselected.png"), (int(width*0.04), int(height*0.05)))
triangleButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/triangleSelected.png"), (int(width*0.04), int(height*0.05)))
arcButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/arcUnselected.png"), (int(width*0.04), int(height*0.05)))
arcButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/arcSelected.png"), (int(width*0.04), int(height*0.05)))
polygonButtonUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/polygonUnselected.png"), (int(width*0.04), int(height*0.05)))
polygonButtonSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/polygonSelected.png"), (int(width*0.04), int(height*0.05)))
pageDownWhiteOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/pageDownWhite.png"), (int(width*0.16), int(height*0.04)))
pageDownGrayOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/pageDownGray.png"), (int(width*0.16), int(height*0.04)))
stampsSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/stampsSelected.png"), (int(width*0.16), int(height*0.09)))
stampsUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/stampsUnselected.png"), (int(width*0.16), int(height*0.09)))
sceneUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/sceneUnselected.png"), (int(width*0.16), int(height*0.09)))
sceneSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/sceneSelected.png"), (int(width*0.16), int(height*0.09)))
filtersSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/filtersSelected.png"), (int(width*0.16), int(height*0.09)))
filtersUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/filtersUnselected.png"), (int(width*0.16), int(height*0.09)))
undoSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/undoSelected.png"), (int(width*0.04), int(height*0.07)))
undoUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/undoUnselected.png"), (int(width*0.04), int(height*0.07)))
redoSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/redoSelected.png"), (int(width*0.04), int(height*0.07)))
redoUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/redoUnselected.png"), (int(width*0.04), int(height*0.07)))
saveSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/saveSelected.png"), (int(width*0.094), int(height*0.07)))
saveUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/saveUnselected.png"), (int(width*0.094), int(height*0.07)))
openSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/openSelected.png"), (int(width*0.094), int(height*0.07)))
openUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/openUnselected.png"), (int(width*0.094), int(height*0.07)))
colourUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/colourUnselected.png"), (int(width*0.2), int(height*0.09)))
colourSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/colourSelected.png"), (int(width*0.2), int(height*0.09)))
dropperUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/dropperUnselected.png"), (int(width*0.03), int(height*0.04)))
dropperSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/dropperSelected.png"), (int(width*0.03), int(height*0.04)))
rainbowUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/rainbowUnselected.png"), (int(width*0.03), int(height*0.04)))
rainbowSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/rainbowSelected.png"), (int(width*0.03), int(height*0.04)))

filledUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/filledUnselected.png"), (int(width*0.14), int(height*0.06)))
filledSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/filledSelected.png"), (int(width*0.14), int(height*0.06)))
NoTitleOriginal = transform.scale(image.load("paintPyrusFiles/images/titles/NO.png"), (int(width*0.04), int(height*0.06)))
YesTitleOriginal = transform.scale(image.load("paintPyrusFiles/images/titles/YES.png"), (int(width*0.06), int(height*0.06)))
LinesTitleOriginal = transform.scale(image.load("paintPyrusFiles/images/titles/LINES.png"), (int(width*0.1), int(height*0.06)))
DensityTitleOriginal = transform.scale(image.load("paintPyrusFiles/images/titles/DENSITY.png"), (int(width*0.07), int(height*0.06)))
PixelTitleOriginal = transform.scale(image.load("paintPyrusFiles/images/titles/PIXEL.png"), (int(width*0.07), int(height*0.06)))
BleedTitleOriginal = transform.scale(image.load("paintPyrusFiles/images/titles/BLEED.png"), (int(width*0.07), int(height*0.06)))
OpacityTitleOriginal = transform.scale(image.load("paintPyrusFiles/images/titles/OPACITY.png"), (int(width*0.07), int(height*0.06)))

#Lines
lineStraightOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/lineButtonStraight.png"), (int(width*0.03), int(height*0.06)))
lineRoundedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/lineButtonRounded.png"), (int(width*0.03), int(height*0.06)))
lineDottedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/lineButtonDotted.png"), (int(width*0.03), int(height*0.06)))
lineDashedOneOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/lineButtonDashedOne.png"), (int(width*0.03), int(height*0.06)))
lineDashedTwoOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/lineButtonDashedTwo.png"), (int(width*0.03), int(height*0.06)))

#Help boxes
helpBackgroundsOriginal = transform.scale(image.load("paintPyrusFiles/images/help/backgroundsHelp.png"), (int(width*0.4), int(height*0.3)))
helpClearOriginal = transform.scale(image.load("paintPyrusFiles/images/help/clearHelp.png"), (int(width*0.4), int(height*0.3)))
helpColourOriginal = transform.scale(image.load("paintPyrusFiles/images/help/colourHelp.png"), (int(width*0.4), int(height*0.3)))
helpCutOriginal = transform.scale(image.load("paintPyrusFiles/images/help/cutHelp.png"), (int(width*0.4), int(height*0.3)))
helpDropperOriginal = transform.scale(image.load("paintPyrusFiles/images/help/dropperHelp.png"), (int(width*0.4), int(height*0.3)))
helpEllipseOriginal = transform.scale(image.load("paintPyrusFiles/images/help/ellipseHelp.png"), (int(width*0.4), int(height*0.3)))
helpEraserOriginal = transform.scale(image.load("paintPyrusFiles/images/help/eraserHelp.png"), (int(width*0.4), int(height*0.3)))
helpFillOriginal = transform.scale(image.load("paintPyrusFiles/images/help/fillHelp.png"), (int(width*0.4), int(height*0.3)))
helpFiltersOriginal = transform.scale(image.load("paintPyrusFiles/images/help/filtersHelp.png"), (int(width*0.4), int(height*0.3)))
helpHexagonOriginal = transform.scale(image.load("paintPyrusFiles/images/help/hexagonHelp.png"), (int(width*0.4), int(height*0.3)))
helpLineOriginal = transform.scale(image.load("paintPyrusFiles/images/help/lineHelp.png"), (int(width*0.4), int(height*0.3)))
helpMarkerOriginal = transform.scale(image.load("paintPyrusFiles/images/help/markerHelp.png"), (int(width*0.4), int(height*0.3)))
helpOpenOriginal = transform.scale(image.load("paintPyrusFiles/images/help/openHelp.png"), (int(width*0.4), int(height*0.3)))
helpPencilOriginal = transform.scale(image.load("paintPyrusFiles/images/help/pencilHelp.png"), (int(width*0.4), int(height*0.3)))
helpPenOriginal = transform.scale(image.load("paintPyrusFiles/images/help/penHelp.png"), (int(width*0.4), int(height*0.3)))
helpPixelateOriginal = transform.scale(image.load("paintPyrusFiles/images/help/pixelateHelp.png"), (int(width*0.4), int(height*0.3)))
helpPolygonOriginal = transform.scale(image.load("paintPyrusFiles/images/help/polygonHelp.png"), (int(width*0.4), int(height*0.3)))
helpRainbowOriginal = transform.scale(image.load("paintPyrusFiles/images/help/rainbowHelp.png"), (int(width*0.4), int(height*0.3)))
helpRectangleOriginal = transform.scale(image.load("paintPyrusFiles/images/help/rectangleHelp.png"), (int(width*0.4), int(height*0.3)))
helpRedoOriginal = transform.scale(image.load("paintPyrusFiles/images/help/redoHelp.png"), (int(width*0.4), int(height*0.3)))
helpSaveOriginal = transform.scale(image.load("paintPyrusFiles/images/help/saveHelp.png"), (int(width*0.4), int(height*0.3)))
helpShapesOriginal = transform.scale(image.load("paintPyrusFiles/images/help/shapesHelp.png"), (int(width*0.4), int(height*0.3)))
helpSizeOriginal = transform.scale(image.load("paintPyrusFiles/images/help/sizeHelp.png"), (int(width*0.4), int(height*0.3)))
helpSprayOriginal = transform.scale(image.load("paintPyrusFiles/images/help/sprayHelp.png"), (int(width*0.4), int(height*0.3)))
helpStampsOriginal = transform.scale(image.load("paintPyrusFiles/images/help/stampsHelp.png"), (int(width*0.4), int(height*0.3)))
helpTextOriginal = transform.scale(image.load("paintPyrusFiles/images/help/textHelp.png"), (int(width*0.4), int(height*0.3)))
helpTriangleOriginal = transform.scale(image.load("paintPyrusFiles/images/help/triangleHelp.png"), (int(width*0.4), int(height*0.3)))
helpUndoOriginal = transform.scale(image.load("paintPyrusFiles/images/help/undoHelp.png"), (int(width*0.4), int(height*0.3)))
helpListOriginal = [helpBackgroundsOriginal, helpClearOriginal, helpColourOriginal, helpCutOriginal,
                    helpDropperOriginal, helpEllipseOriginal, helpEraserOriginal, helpFillOriginal,
                    helpFiltersOriginal, helpHexagonOriginal, helpLineOriginal, helpMarkerOriginal,
                    helpOpenOriginal, helpPencilOriginal, helpPenOriginal, helpPixelateOriginal,
                    helpPolygonOriginal, helpRainbowOriginal, helpRectangleOriginal, helpRedoOriginal,
                    helpSaveOriginal, helpShapesOriginal, helpSizeOriginal, helpSprayOriginal,
                    helpStampsOriginal, helpTextOriginal, helpTriangleOriginal, helpUndoOriginal]

stampAlphysOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/alphys.png"), (int(width*0.075), int(height*0.1)))
stampAsgoreOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/asgore.png"), (int(width*0.075), int(height*0.1)))
stampCharaOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/chara.png"), (int(width*0.075), int(height*0.1)))
stampFloweyOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/flowey.png"), (int(width*0.075), int(height*0.1)))
stampFriskOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/frisk.png"), (int(width*0.075), int(height*0.1)))
stampMettatonOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/mettaton.png"), (int(width*0.075), int(height*0.1)))
stampPapyrusOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/papyrus.png"), (int(width*0.075), int(height*0.1)))
stampSansOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/sans.png"), (int(width*0.075), int(height*0.1)))
stampTorielOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/toriel.png"), (int(width*0.075), int(height*0.1)))
stampUndyneOriginal = transform.scale(image.load("paintPyrusFiles/images/stamps/undyne.png"), (int(width*0.075), int(height*0.1)))

scene1Original = transform.scale(image.load("paintPyrusFiles/images/backgrounds/scene1.jpg"), (int(width*0.7), int(height*0.7)))
scene2Original = transform.scale(image.load("paintPyrusFiles/images/backgrounds/scene2.jpg"), (int(width*0.7), int(height*0.7)))
scene3Original = transform.scale(image.load("paintPyrusFiles/images/backgrounds/scene3.png"), (int(width*0.7), int(height*0.7)))
scene4Original = transform.scale(image.load("paintPyrusFiles/images/backgrounds/scene4.png"), (int(width*0.7), int(height*0.7)))
scene5Original = transform.scale(image.load("paintPyrusFiles/images/backgrounds/scene5.png"), (int(width*0.7), int(height*0.7)))
scene6Original = transform.scale(image.load("paintPyrusFiles/images/backgrounds/scene6.jpg"), (int(width*0.7), int(height*0.7)))
scene7Original = transform.scale(image.load("paintPyrusFiles/images/backgrounds/scene7.jpg"), (int(width*0.7), int(height*0.7)))
scene8Original = transform.scale(image.load("paintPyrusFiles/images/backgrounds/scene8.png"), (int(width*0.7), int(height*0.7)))
transparentScreenOriginal = transform.scale(image.load("paintPyrusFiles/images/backgrounds/transparentBackground.png"), (int(width*0.7), int(height*0.7)))

fontsTitleOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/fontsTitle.png"), (int(width*0.08), int(height*0.06)))
textButtonOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/textSelected.png"), (int(width*0.06), int(height*0.05)))
italicsUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/italicsUnselected.png"), (int(width*0.03), int(height*0.04)))
italicsSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/italicsSelected.png"), (int(width*0.03), int(height*0.04)))
boldUnselectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/boldUnselected.png"), (int(width*0.03), int(height*0.04)))
boldSelectedOriginal = transform.scale(image.load("paintPyrusFiles/images/buttons/boldSelected.png"), (int(width*0.03), int(height*0.04)))

font8Bit = transform.scale(image.load("paintPyrusFiles/images/buttons/font8bit.png"), (int(width*0.09), int(height*0.06)))
fontArial = transform.scale(image.load("paintPyrusFiles/images/buttons/fontArial.png"), (int(width*0.09), int(height*0.06)))
fontComic = transform.scale(image.load("paintPyrusFiles/images/buttons/fontComic.png"), (int(width*0.09), int(height*0.06)))
fontImpact = transform.scale(image.load("paintPyrusFiles/images/buttons/fontImpact.png"), (int(width*0.09), int(height*0.06)))
fontRoman = transform.scale(image.load("paintPyrusFiles/images/buttons/fontRoman.png"), (int(width*0.09), int(height*0.06)))
fontButtonsListOriginal = [font8Bit, fontArial, fontComic, fontImpact, fontRoman]
fontButtonsList = [font8Bit, fontArial, fontComic, fontImpact, fontRoman]





#Second copy of all images. When screen becomes small then large, this keeps images from becoming pixelated
homeScreen = homeScreenOriginal
paintScreenLeft = paintScreenLeftOriginal
paintScreenBottom = paintScreenBottomOriginal
optionScreen = optionScreenOriginal
colourPalette = colourPaletteOriginal
soundButton = soundButtonOriginal
stampOneUndertaleHeart = stampOneUndertaleHeartOriginal
paintButtonUnselected = paintButtonUnselectedOriginal
paintButtonSelected = paintButtonSelectedOriginal
optionsButtonUnselected = optionsButtonUnselectedOriginal
optionsButtonSelected = optionsButtonSelectedOriginal
heartSelect = heartSelectOriginal
toolPencilButtonUnselected = toolPencilButtonUnselectedOriginal
toolPencilButtonSelected = toolPencilButtonSelectedOriginal
toolEraserButtonUnselected = toolEraserButtonUnselectedOriginal
toolEraserButtonSelected = toolEraserButtonSelectedOriginal
toolSprayButtonUnselected = toolSprayButtonUnselectedOriginal
toolSprayButtonSelected = toolSprayButtonSelectedOriginal
toolPenButtonUnselected = toolPenButtonUnselectedOriginal
toolPenButtonSelected = toolPenButtonSelectedOriginal
toolMarkerButtonUnselected = toolMarkerButtonUnselectedOriginal
toolMarkerButtonSelected = toolMarkerButtonSelectedOriginal
toolFillButtonUnselected = toolFillButtonUnselectedOriginal
toolFillButtonSelected = toolFillButtonSelectedOriginal
toolPixelateButtonUnselected = toolPixelateButtonUnselectedOriginal
toolPixelateButtonSelected = toolPixelateButtonSelectedOriginal
toolBlurButtonUnselected = toolBlurButtonUnselectedOriginal
toolBlurButtonSelected = toolBlurButtonSelectedOriginal
shapeButtonSelected = shapeButtonSelectedOriginal
shapeButtonUnselected = shapeButtonUnselectedOriginal
homeButtonSelected = homeButtonSelectedOriginal
homeButtonUnselected = homeButtonUnselectedOriginal
colourPalette = colourPaletteOriginal
blackToWhite = blackToWhiteOriginal
whiteHeartCol = whiteHeartColOriginal
openNextPageWhite = openNextPageWhiteOriginal
openNextPageGray = openNextPageGrayOriginal
clearButton = clearButtonOriginal
sizeBar = sizeBarOriginal
rectButtonUnselected = rectButtonUnselectedOriginal
rectButtonSelected = rectButtonSelectedOriginal
ellipseButtonSelected = ellipseButtonSelectedOriginal
ellipseButtonUnselected = ellipseButtonUnselectedOriginal
triangleButtonSelected = triangleButtonSelectedOriginal
triangleButtonUnselected = triangleButtonUnselectedOriginal
lineButtonSelected = lineButtonSelectedOriginal
lineButtonUnselected = lineButtonUnselectedOriginal
arcButtonSelected = arcButtonSelectedOriginal
arcButtonUnselected = arcButtonUnselectedOriginal
polygonButtonSelected = polygonButtonSelectedOriginal
polygonButtonUnselected = polygonButtonUnselectedOriginal
pageDownWhite = pageDownWhiteOriginal
pageDownGray = pageDownGrayOriginal
stampsSelected = stampsSelectedOriginal
stampsUnselected = stampsUnselectedOriginal
sceneSelected = sceneSelectedOriginal
sceneUnselected = sceneUnselectedOriginal
filtersSelected = filtersSelectedOriginal
filtersUnselected = filtersUnselectedOriginal
undoSelected = undoSelectedOriginal
undoUnselected = undoUnselectedOriginal
redoSelected = redoSelectedOriginal
redoUnselected = redoUnselectedOriginal
saveSelected = saveSelectedOriginal
saveUnselected = saveUnselectedOriginal
openSelected = openSelectedOriginal
openUnselected = openUnselectedOriginal
colourSelected = colourSelectedOriginal
colourUnselected = colourUnselectedOriginal
dropperSelected = dropperSelectedOriginal
dropperUnselected = dropperUnselectedOriginal
rainbowSelected = rainbowSelectedOriginal
rainbowUnselected = rainbowUnselectedOriginal
filledSelected = filledSelectedOriginal
filledUnselected = filledUnselectedOriginal
NoTitle = NoTitleOriginal
YesTitle = YesTitleOriginal
LinesTitle = LinesTitleOriginal
DensityTitle = DensityTitleOriginal
PixelTitle = PixelTitleOriginal
BleedTitle = BleedTitleOriginal
OpacityTitle = OpacityTitleOriginal
lineStraight = lineStraightOriginal
lineRounded = lineRoundedOriginal
lineDotted = lineDottedOriginal
lineDashedOne = lineDashedOneOriginal
lineDashedTwo = lineDashedTwoOriginal
helpBackgrounds = helpBackgroundsOriginal
helpClear = helpClearOriginal
helpColour = helpColourOriginal
helpCut = helpCutOriginal
helpDropper = helpDropperOriginal
helpEllipse = helpEllipseOriginal
helpEraser = helpEraserOriginal
helpFill = helpFillOriginal
helpFilters = helpFiltersOriginal
helpHexagon = helpHexagonOriginal
helpLine = helpLineOriginal
helpMarker = helpMarkerOriginal
helpOpen = helpOpenOriginal
helpPencil = helpPencilOriginal
helpPen = helpPenOriginal
helpPixelate = helpPixelateOriginal
helpPolygon = helpPolygonOriginal
helpRainbow = helpRainbowOriginal
helpRectangle = helpRectangleOriginal
helpRedo = helpRedoOriginal
helpSave = helpSaveOriginal
helpShapes = helpShapesOriginal
helpSize = helpSizeOriginal
helpSpray = helpSprayOriginal
helpStamps = helpStampsOriginal
helpText = helpTextOriginal
helpTriangle = helpTriangleOriginal
helpUndo = helpUndoOriginal
helpList = [helpBackgrounds, helpClear, helpColour, helpCut,
                    helpDropper, helpEllipse, helpEraser, helpFill,
                    helpFilters, helpHexagon, helpLine, helpMarker,
                    helpOpen, helpPencil, helpPen, helpPixelate,
                    helpPolygon, helpRainbow, helpRectangle, helpRedo,
                    helpSave, helpShapes, helpSize, helpSpray,
                    helpStamps, helpText, helpTriangle, helpUndo]

stampAlphys = stampAlphysOriginal
stampAsgore = stampAsgoreOriginal
stampChara = stampCharaOriginal
stampFlowey = stampFloweyOriginal
stampFrisk = stampFriskOriginal
stampMettaton = stampMettatonOriginal
stampPapyrus = stampPapyrusOriginal
stampSans = stampSansOriginal
stampToriel = stampTorielOriginal
stampUndyne = stampUndyneOriginal
stampList = [stampAlphys, stampAsgore, stampChara, stampFlowey, stampFrisk,
             stampMettaton, stampPapyrus, stampSans, stampToriel, stampUndyne]
stampListOriginal = [stampAlphysOriginal, stampAsgoreOriginal, stampCharaOriginal, stampFloweyOriginal, stampFriskOriginal,
             stampMettatonOriginal, stampPapyrusOriginal, stampSansOriginal, stampTorielOriginal, stampUndyneOriginal]

scene1 = scene1Original
scene2 = scene2Original
scene3 = scene3Original
scene4 = scene4Original
scene5 = scene5Original
scene6 = scene6Original
scene7 = scene7Original
scene8 = scene8Original
transparentScreen = transparentScreenOriginal
sceneList = [scene1, scene2, scene3, scene4,
             scene5, scene6, scene7, scene8]
sceneListOriginal = [scene1Original, scene2Original, scene3Original, scene4Original,
                       scene5Original, scene6Original, scene7Original, scene8Original]
sceneNum = -1 #This says what background is currently selected. -1 means none at all
fontsTitle = fontsTitleOriginal
textButton = textButtonOriginal
italicsUnselected = italicsUnselectedOriginal
italicsSelected = italicsSelectedOriginal
boldUnselected = boldUnselectedOriginal 
boldSelected = boldSelectedOriginal 






#Loading music
#music = ["paintPyrusFiles/music/musicPeaceful.ogg"]
#mixer.music.load("paintPyrusFiles/music/musicPeaceful.ogg")
#mixer.music.play(-1)

#Loading Fonts

#Mouse variables
click = False #Left clicking
rightClick = False #Right clicking
release = False #Releasing the mouse
leftHold = False
rightHold = False
scroll = 0
mx, my = 0, 0 #Mouse position
mxO, myO = 0, 0 #Mouse position in the previous frame
pixelSet = []

#Variables to do with drawing
size = 50 #Determines the global size for all tools
transparency = 4 #Marker transparency
pixelateStrength = 4 #Determines effectiveness of pixelation
penBleed = 50 #Amount pen will bleed when right clicked
sprayDensity = 300 #Relative to number of pixels changed per frame when spray is used
drawState = "pencil" #Lets program know which tool is selected
shape = "rectangle" #Lets program know which shape is selected
lineType = "straight" #There is straight, rounded, dotted, dashed 1, and dashed 2
fillShape = True #Whether or not shapes will be filled
undoList = [] #Contains images of canvas after every action
redoList = [] #Fills up when undo is used
clearCharge = 0 #Variable for the clear button so it clears when held
currentStamp = stampList[0] #Stamp currently chosen

uglyColour = (41, 37, 18) #Colour for highlighter tool that makes background transparent. Ugly colour rarely used
highlightCover = Surface((width, height)).convert() 
highlightCover.set_alpha(50)
highlightCover.fill(uglyColour)
highlightCover.set_colorkey(uglyColour)


#Text boxes Variables
currentText = ""
eventText = ""
bolded = False
italics = False
#Numbers clicked and their shift counterparts
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", ".", "/", "'", ";", "\\", "[", "]"]
numbersShift = [")", "!", "@", "#", "$", "%", "^", "&", "*", "(", "<", ">", "?", "\"", ":", "|", "{", "}"]
textOn = False

#fontType 
fontNumber = 0 #Which font in the list is selected
fontList = ["paintPyrusFiles/fonts/8bit.ttf", "arial", "comicsansms", "impact", "timesnewroman"]

#Colours
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 150, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
PINK = (255, 150, 150)
GRAY = (120, 120, 120)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
colourOne = RED #Colour one, used for more drawing tools
colourTwo = BLUE #Colour two, secondary functions of tools
colOneRainbow = False #Whether primary colour is rainbow
colTwoRainbow = False #Whether secondary colour is rainbow
colourSelect = 1 #The colour currently being changed

rainbowR = 255 #Red value of rainbow colour
rainbowG = 0 #Green value of rainbow colour
rainbowB = 0 #Blue value of rainbow colour
rainbowRate = 2 #How quickly rainbow changes
#Rates to determines whether each colour increases, decreases, or remains constant
rainbowRRate = -rainbowRate
rainbowGRate = rainbowRate
rainbowBRate = 0

shapePage = 0 #Page to display certain shapes
stampPage = 0 #Page to display certain stamps
scenePage = 0 #Page to display certain scenes
filterPage = 1 #Page to display certain filters

helping = False
hRelease = False
markerStart = False
dropperUsed = False #Stops page from being appended to undo when dropper is used
#All the numbers for filters which are put in an algorithm to tint the screen
filterFormulae = [((0.393, 0.769, 0.189), (0.349, 0.686, 0.168), (0.272, 0.534, 0.131)),
                  ((0.233, 0.233, 0.233), (0.233, 0.233, 0.233), (0.233, 0.233, 0.233)),
                  ((0.7, 0.15, 0.15), (0.15, 0.15, 0.15), (0.15, 0.15, 0.15)),
                  ((0.3, 0.3, 0.3), (0.4, 0.4, 0.4), (0.2, 0.2, 0.2)),
                  ((0.3, 0.4, 0.2), (0.3, 0.4, 0.2), (0.3, 0.4, 0.2)),
                  ((1, 0.25, 0.25), (0.25, 1, 0.25), (0.25, 0.25, 1))]

#Music variables
musicList = ["paintPyrusFiles/music/HopesAndDreams.ogg",
             "paintPyrusFiles/music/Undertale.ogg",
             "paintPyrusFiles/music/Megalovania.ogg",
             "paintPyrusFiles/music/Bergen.ogg",
             "paintPyrusFiles/music/TrueHero.ogg"]
             
#Volume of music
volume = 1.0


#################################################################################################### 
####################################################################################################



#Function to find whether a point is in a rectangle
#Multiple rects don't have to be made for every object
def inRect(rect, mouse):
     if mouse[0] > rect[0] and mouse[0] < rect[0]+rect[2] and mouse[1] > rect[1] and mouse[1] < rect[1]+rect[3]:
          return True
     else:
          return False

#Clears the canvas
def canvasClear(surf, width, height):
     global sceneNum
     draw.rect(screen, (255, 255, 255), (width*0.3, 0, width*0.7, height*0.7), 0)
     sceneNum = -1

def curvedLine(surf, colour, pointOne, pointTwo, thickness):
     #Next three lines find distance of mouse from pos 1 to pos 2
     dx=pointOne[0] - pointTwo[0]
     dy=pointOne[1] - pointTwo[1]
     dist=int(sqrt(dx**2+dy**2)) + 1
     #Generates a series of circles from mouse pos of previous frame to current frame
     for i in range(dist):
          xPos=int(pointTwo[0]+i*dx/dist)  
          yPos=int(pointTwo[1]+i*dy/dist)  
          draw.circle(surf,colour,(xPos,yPos),thickness//2)


#################################################################################################### 
#################################################################################################### 

# Functions for buttons
# They deal with global variables, so they can't be put in a seperate file
#All buttons have similar structure
def toolButton(surf, rect, tool, imageUnselect, imageSelect, heart,  mouse, click, width, height):
     global drawState #Gets which tool is currently used
     surf.blit(imageUnselect, (rect[0], rect[1]))
     if inRect(rect, mouse):
          surf.blit(imageSelect, (rect[0], rect[1])) #Highlights tool mouse is over
          if click:
               drawState = tool #Changes drawstate to tool when clicked
     if tool == drawState:
          surf.blit(heart, (rect[0]-width*0.03, rect[1])) #Highlights tool if selected

def shapeButton(surf, rect, newShape, imageUnselect, imageSelect, mouse, click):
     global shape
     surf.blit(imageUnselect, (rect[0], rect[1]))
     draw.rect(surf, (255, 255, 0), rect, 3)
     if inRect(rect, mouse) or shape == newShape:
          surf.blit(imageSelect, (rect[0], rect[1]))
          draw.rect(surf, (255, 0, 0), rect, 3)
          if click:
               shape = newShape

def stampButton(surf, rect, stamp, mouse, click):
     global currentStamp
     surf.blit(stamp, (rect[0], rect[1]))
     draw.rect(surf, (255, 255, 0), rect, 4)
     if inRect(rect, mouse) or stamp == currentStamp:
          draw.rect(surf, (255, 0, 0), rect, 4)
          if click:
               currentStamp = stamp

def sceneButton(surf, rect, img, mouse, release, width, height, imgNum):
     global sceneNum
     draw.rect(surf, (255, 255, 0), rect, 4)
     icon = transform.scale(img, (int(rect[2]), int(rect[3])))
     surf.blit(icon, (rect[0], rect[1]))
     if inRect(rect, mouse):
          draw.rect(surf, (255, 0, 0), rect, 4)
          if release:
               surf.blit(img, (width*0.3, 0))
               sceneNum = imgNum

def filterButton(surf, rect, col, mouse, release, width, height, filt):
     draw.rect(surf, col, rect, 0)
     draw.rect(surf, (255, 255, 0), rect, 4)
     if inRect(rect, mouse):
          draw.rect(surf, (255, 0, 0), rect, 4)
          if release:
               #Changes each pixel to a colour depending on its current colour
               for i in range(int(width*0.3), int(width)):
                    for j in range(int(height*0.7)):
                         r, g, b, a = surf.get_at((i, j))
                         rNew = int(min(255,r*filt[0][0] + g*filt[0][1] + b*filt[0][2]))
                         gNew = int(min(255,r*filt[1][0] + g*filt[1][1] + b*filt[1][2]))
                         bNew = int(min(255,r*filt[2][0] + g*filt[2][1] + b*filt[2][2]))
                         surf.set_at((i, j), (rNew, gNew, bNew))



#################################################################################################### 
#################################################################################################### 
mixer.music.load(choice(musicList))
mixer.music.play(-1)
while running:
     display.set_caption("Paintpyrus    FPS: %d" % int(myClock.get_fps())) #Title of program. Also shows the frames per second
     dropperUsed = False
     hRelease = False #Whether h is released to blit screen over help box
     markerStart = False
     click = False #Left click
     rightClick = False #Right click
     release = False #Left or right mouse button released
     leftHold = mouse.get_pressed()[0]#Left mouse button is held
     rightHold = mouse.get_pressed()[2]#Right mouse button is held
     scroll = 0 #How much mouse has been scrolled
     mx, my = mouse.get_pos() #Position of mouse in current frame
     Rrelease = False
     
     eventText = ""
     for action in event.get():
          if action.type == QUIT:
               running = False #Whether program is running or not
               continue #Continue breaks loop right after clicking X instead of running one more frame
          if action.type == MOUSEBUTTONDOWN:
               if action.button == 1:
                    click = True
                    paintScreen = screen.subsurface(canvasRect).copy() #Gets image of canavs before shape appears
                    xStart, yStart = mx, my #Start for when shapes/cut is used
                    #Adjusts start so its in the canvas
                    if xStart > width:
                         xStart = width
                    elif xStart < width*0.3:
                         xStart = width*0.3
                    if yStart > height*0.7:
                         yStart = height*0.7
                    elif yStart < 0:
                         yStart = 0
                    #Stamp being used is updated
                    stampPrinted = currentStamp
                         
               if action.button == 3:
                    rightClick = True
                    highlightCover.fill(uglyColour) #Fill highlight which makes it all transparent
               #Scroll is a number and not a boolean so multiple scrolls can be registered per frame
               if action.button == 4: #Scroll is a number so multiple scrolls can be registered in a single frame
                    scroll += 1
               if action.button == 5:
                    scroll -= 1 
          elif action.type == MOUSEBUTTONUP:
               if action.button == 1 or action.button == 3: #Checks whether left or right buttons were released
                    release = True
               if action.button == 3:
                    Rrelease = True
          elif action.type == KEYUP:
               if action.key == K_h:
                    hRelease = True #Disables help dialog if displayed

                    
          elif action.type == KEYDOWN: #If anything is being typed
               if 96<action.key<123 or action.key == 32: #Adds letter or space to eventText
                    eventText+=chr(action.key)
               if chr(action.key) in numbers: #Adds numbers
                    eventText+=chr(action.key)
               if key.get_pressed()[K_LSHIFT] or key.get_pressed()[K_RSHIFT]: 
                    eventText = eventText.upper() #If shifted makes letters capitalized
                    for i in range(len(numbers)):
                         eventText = eventText.replace(numbers[i], numbersShift[i]) #If number shift displayes secondary char for number
               if key.get_pressed()[K_RETURN]: #Brings line down and empties currentText when user clicks enter
                    startY += textRender.get_height()
                    currentText = ""
                    textScreen = screen.subsurface(canvasRect).copy()
               if key.get_pressed()[K_BACKSPACE]:
                    if len(currentText) > 0: #Checks if string is empty
                         currentText = currentText[:len(currentText)-1] #If not removes one letter
                         


               
          elif action.type == VIDEORESIZE: #Adjusts canvas and all images if resizing
               
               screensize = action.size
               #Keeps width at a minimum of 400 pixels so program doesn't crash
               if screensize[0] < 400:
                    width = 400
               else:
                    width = screensize[0]
               #Keeps height at a minimum of 300 pixels so program doesn't crash
               if screensize[1] < 300:
                    height = 300
               else:
                    height = screensize[1]
               #Resized display screen
               screen = display.set_mode((width, height), RESIZABLE)
               #Resizing all images and canvas rect to be relative to window size
               homeScreen = transform.scale((homeScreenOriginal), (width, height))
               paintScreenLeft = transform.scale((paintScreenLeftOriginal), (int(width*0.3), height))
               paintScreenBottom = transform.scale((paintScreenBottomOriginal), (int(width*0.71), int(height*0.3)))
               optionScreen = transform.scale((optionScreenOriginal), (width, height))
               colourPalette = transform.scale((colourPaletteOriginal), (int(width*0.2), int(height*0.2)))
               soundButton = transform.scale((soundButtonOriginal), (int(width*0.02), int(height*0.03)))
               stampOneUndertaleHeart = transform.scale((stampOneUndertaleHeartOriginal), (int(width*0.06), int(width*0.06)))
               paintButtonUnselected = transform.scale((paintButtonUnselectedOriginal), (int(width*0.1),int(height*0.05)))
               paintButtonSelected = transform.scale((paintButtonSelectedOriginal), (int(width*0.1),int(height*0.05)))
               optionsButtonUnselected = transform.scale((optionsButtonUnselectedOriginal), (int(width*0.14),int(height*0.05)))
               optionsButtonSelected = transform.scale((optionsButtonSelectedOriginal), (int(width*0.14),int(height*0.05)))
               heartSelect = transform.scale((heartSelectOriginal), (int(width*0.03), int(height*0.05)))
               toolPencilButtonUnselected = transform.scale(toolPencilButtonUnselectedOriginal, (int(width*0.09), int(height*0.05)))
               toolPencilButtonSelected = transform.scale(toolPencilButtonSelectedOriginal, (int(width*0.09), int(height*0.05)))
               toolEraserButtonUnselected = transform.scale(toolEraserButtonUnselectedOriginal, (int(width*0.09), int(height*0.05)))
               toolEraserButtonSelected = transform.scale(toolEraserButtonSelectedOriginal, (int(width*0.09), int(height*0.05)))
               toolSprayButtonUnselected = transform.scale(toolSprayButtonUnselectedOriginal, (int(width*0.075), int(height*0.05)))
               toolSprayButtonSelected = transform.scale(toolSprayButtonSelectedOriginal, (int(width*0.075), int(height*0.05)))
               toolPenButtonUnselected = transform.scale(toolPenButtonUnselectedOriginal, (int(width*0.045), int(height*0.05)))
               toolPenButtonSelected = transform.scale(toolPenButtonSelectedOriginal, (int(width*0.045), int(height*0.05)))
               toolMarkerButtonUnselected = transform.scale(toolMarkerButtonUnselectedOriginal, (int(width*0.09), int(height*0.05)))
               toolMarkerButtonSelected = transform.scale(toolMarkerButtonSelectedOriginal, (int(width*0.09), int(height*0.05)))
               toolFillButtonUnselected = transform.scale(toolFillButtonUnselectedOriginal, (int(width*0.06), int(height*0.05)))
               toolFillButtonSelected = transform.scale(toolFillButtonSelectedOriginal, (int(width*0.06), int(height*0.05)))
               toolPixelateButtonUnselected = transform.scale(toolPixelateButtonUnselectedOriginal, (int(width*0.1), int(height*0.05)))
               toolPixelateButtonSelected = transform.scale(toolPixelateButtonSelectedOriginal, (int(width*0.1), int(height*0.05)))
               toolBlurButtonUnselected = transform.scale(toolBlurButtonUnselectedOriginal, (int(width*0.06), int(height*0.05)))
               toolBlurButtonSelected = transform.scale(toolBlurButtonSelectedOriginal, (int(width*0.06), int(height*0.05)))
               shapeButtonSelected = transform.scale(shapeButtonSelectedOriginal, (int(width*0.11), int(height*0.08)))
               shapeButtonUnselected = transform.scale(shapeButtonUnselectedOriginal, (int(width*0.11), int(height*0.08)))
               homeButtonUnselected = transform.scale(homeButtonUnselectedOriginal, (int(width*0.08), int(height*0.05)))
               homeButtonSelected = transform.scale(homeButtonSelectedOriginal, (int(width*0.08), int(height*0.05)))
               colourPalette = transform.scale(colourPaletteOriginal, (int(width*0.2), int(height*0.2)))
               blackToWhite = transform.scale(blackToWhite, (int(width*0.2), int(height*0.04)))
               whiteHeartCol = transform.scale(whiteHeartColOriginal, (int(width*0.05), int(height*0.08)))
               openNextPageWhite = transform.scale(openNextPageWhiteOriginal, (int(width*0.015), int(height*0.08))) 
               openNextPageGray = transform.scale(openNextPageGrayOriginal, (int(width*0.015), int(height*0.08)))
               clearButton = transform.scale(clearButtonOriginal, (int(width*0.08), int(height*0.06)))
               sizeBar = transform.scale(sizeBarOriginal, (int(width*0.22), int(height*0.06)))
               rectButtonSelected = transform.scale(rectButtonSelectedOriginal, (int(width*0.04), int(height*0.05)))
               rectButtonUnselected = transform.scale(rectButtonUnselectedOriginal, (int(width*0.04), int(height*0.05)))
               ellipseButtonUnselected = transform.scale(ellipseButtonUnselectedOriginal, (int(width*0.04), int(height*0.05)))
               ellipseButtonSelected = transform.scale(ellipseButtonSelectedOriginal, (int(width*0.04), int(height*0.05)))
               lineButtonUnselected = transform.scale(lineButtonUnselectedOriginal, (int(width*0.04), int(height*0.05)))
               lineButtonSelected = transform.scale(lineButtonSelectedOriginal, (int(width*0.04), int(height*0.05)))
               triangleButtonUnselected = transform.scale(triangleButtonUnselectedOriginal, (int(width*0.04), int(height*0.05)))
               triangleButtonSelected = transform.scale(triangleButtonSelectedOriginal, (int(width*0.04), int(height*0.05)))
               arcButtonUnselected = transform.scale(arcButtonUnselectedOriginal, (int(width*0.04), int(height*0.05)))
               arcButtonSelected = transform.scale(arcButtonSelectedOriginal, (int(width*0.04), int(height*0.05)))
               polygonButtonUnselected = transform.scale(polygonButtonUnselectedOriginal, (int(width*0.04), int(height*0.05)))
               polygonButtonSelected = transform.scale(polygonButtonSelectedOriginal, (int(width*0.04), int(height*0.05)))
               pageDownWhite = transform.scale(pageDownWhiteOriginal, (int(width*0.16), int(height*0.04)))
               pageDownGray = transform.scale(pageDownGrayOriginal, (int(width*0.16), int(height*0.04)))
               stampsSelected = transform.scale(stampsSelectedOriginal, (int(width*0.16), int(height*0.09)))
               stampsUnselected = transform.scale(stampsUnselectedOriginal, (int(width*0.16), int(height*0.09)))
               sceneSelected = transform.scale(sceneSelectedOriginal, (int(width*0.16), int(height*0.09)))
               sceneUnselected = transform.scale(sceneUnselectedOriginal, (int(width*0.16), int(height*0.09)))
               filtersSelected = transform.scale(filtersSelectedOriginal, (int(width*0.16), int(height*0.09)))
               filtersUnselected = transform.scale(filtersUnselectedOriginal, (int(width*0.16), int(height*0.09)))
               undoSelected = transform.scale(undoSelectedOriginal, (int(width*0.04), int(height*0.07)))
               undoUnselected = transform.scale(undoUnselectedOriginal, (int(width*0.04), int(height*0.07)))
               redoSelected = transform.scale(redoSelectedOriginal, (int(width*0.04), int(height*0.07)))
               redoUnselected = transform.scale(redoUnselectedOriginal, (int(width*0.04), int(height*0.07)))
               saveSelected = transform.scale(saveSelectedOriginal, (int(width*0.094), int(height*0.07)))
               saveUnselected = transform.scale(saveUnselectedOriginal, (int(width*0.094), int(height*0.07)))
               openSelected = transform.scale(openSelectedOriginal, (int(width*0.094), int(height*0.07)))
               openUnselected = transform.scale(openUnselectedOriginal, (int(width*0.094), int(height*0.07)))
               colourUnselected = transform.scale(colourUnselectedOriginal, (int(width*0.2), int(height*0.09)))
               colourSelected = transform.scale(colourSelectedOriginal, (int(width*0.2), int(height*0.09)))
               dropperUnselected = transform.scale(dropperUnselectedOriginal, (int(width*0.03), int(height*0.04)))
               dropperSelected = transform.scale(dropperSelectedOriginal, (int(width*0.03), int(height*0.04)))
               rainbowUnselected = transform.scale(rainbowUnselectedOriginal, (int(width*0.03), int(height*0.04)))
               rainbowSelected = transform.scale(rainbowSelectedOriginal, (int(width*0.03), int(height*0.04))) 
               filledUnselected = transform.scale(filledUnselectedOriginal, (int(width*0.14), int(height*0.06)))
               filledSelected = transform.scale(filledSelectedOriginal, (int(width*0.14), int(height*0.06)))
               NoTitle = transform.scale(NoTitleOriginal, (int(width*0.04), int(height*0.06)))
               YesTitle = transform.scale(YesTitleOriginal, (int(width*0.06), int(height*0.06)))
               LinesTitle = transform.scale(LinesTitleOriginal, (int(width*0.1), int(height*0.06)))
               DensityTitle = transform.scale(DensityTitleOriginal, (int(width*0.07), int(height*0.06)))
               PixelTitle = transform.scale(PixelTitleOriginal, (int(width*0.07), int(height*0.06)))
               BleedTitle = transform.scale(BleedTitleOriginal, (int(width*0.07), int(height*0.06)))
               OpacityTitle = transform.scale(OpacityTitleOriginal, (int(width*0.07), int(height*0.06)))
               transparentScreen = transform.scale(transparentScreenOriginal, (int(width*0.7), int(height*0.7)))
               fontsTitle = transform.scale(fontsTitleOriginal, (int(width*0.08), int(height*0.06)))
               textButton = transform.scale(textButtonOriginal, (int(width*0.06), int(height*0.05)))
               italicsUnselected = transform.scale(italicsUnselectedOriginal, (int(width*0.03), int(height*0.04)))
               italicsSelected = transform.scale(italicsSelectedOriginal, (int(width*0.03), int(height*0.04)))
               boldUnselected = transform.scale(boldUnselectedOriginal, (int(width*0.03), int(height*0.04)))
               boldSelected = transform.scale(boldSelectedOriginal , (int(width*0.03), int(height*0.04)))
               lineStraight = transform.scale(lineStraightOriginal , (int(width*0.03), int(height*0.06)))
               lineRounded = transform.scale(lineRoundedOriginal , (int(width*0.03), int(height*0.06)))
               lineDotted = transform.scale(lineDottedOriginal , (int(width*0.03), int(height*0.06)))
               lineDashedOne = transform.scale(lineDashedOneOriginal , (int(width*0.03), int(height*0.06)))
               lineDashedTwo = transform.scale(lineDashedTwoOriginal , (int(width*0.03), int(height*0.06)))

               #Updates highlight canvas
               highlightCover = Surface((width, height)).convert()
               highlightCover.set_alpha(transparency*20)
               highlightCover.fill(uglyColour)
               highlightCover.set_colorkey(uglyColour)
                                             
               canvasRect = Rect(width*0.3, 0, width*0.7, height*0.7)

               #Lists of objects which are changed
               for i in range(len(stampList)):
                    stampList[i] = transform.scale(stampListOriginal[i], (int(width*0.075), int(height*0.1)))
               for i in range(len(sceneList)):
                    sceneList[i] = transform.scale(sceneListOriginal[i], (int(width*0.7), int(height*0.7)))
               for i in range(len(helpList)):
                    helpList[i] = transform.scale(helpListOriginal[i], (int(width*0.4), int(height*0.3)))
               for i in range(len(fontButtonsList)):
                    fontButtonsList[i] =  transform.scale(fontButtonsListOriginal[i], (int(width*0.09), int(height*0.06)))

               #Resizes all images in undo and redo lists to make them canvas size compatable
               try:
                    for i in range(len(undoList)):
                         undoList[i] = transform.scale((undoList[i]), (int(width*0.7), int(height*0.7)))
                    for i in range(len(redoList)):
                         redoList[i] = transform.scale((redoList[i]), (int(width*0.7), int(height*0.7)))
                    screen.blit(undoList[-1], (width*0.3, 0))
               except:
                    canvasClear(screen, width, height)


          #################################################################################################### 
          #################################################################################################### 
               

     if gameScreen == 1: #The painting screen
          #This is the if structure which determines what the mouse does when clicked onto the canvas
          if inRect(canvasRect, (mx, my)) and not helping:
               #Size is controlled by scrolling wheel and dragging of the size bar
               if scroll>0:
                    size+=(scroll+size//100)
               elif scroll<0:
                    size+=(scroll-size//100)
               #Limits to the size keeps the program from crashing
               if size < 1:
                    size = 1
               elif size > 500:
                    size = 500

               #If structure which controls tool being used. Except for shape, all tools 
               #are functions stored in another program to keep the code cleaner.
               if leftHold or click:
                    if drawState == "pencil": #Free drawing tool. Uses primary colour
                         curvedLine(screen, colourOne, (mx, my), (mxO, myO), size)
                              
                    elif drawState == "eraser": #Erases drawn objects but keeps the background
                         #Erasing a square
                         dx=mx-mxO
                         dy=my-myO
                         dist=int(sqrt(dx**2+dy**2)) + 1 
                         for i in range(dist):
                              xPos=int(mxO+i*dx/dist)  
                              yPos=int(myO+i*dy/dist)
                              try:
                                   if sceneNum >= 0:
                                        eraseWidth = size
                                        eraseHeight = size
                                        eraseX = xPos-eraseWidth//2
                                        eraseY = yPos-eraseHeight//2
                                        #Checking if eraser is hitting the borders and adjusting so eraser can work on edges
                                        #If on border decreases size or start to prevent crashing
                                        if xPos-size//2<=width*0.3:
                                             eraseWidth = (xPos-width*0.3) + size//2
                                             eraseX = width*0.3+1
                                        elif xPos+size//2>=width:
                                             eraseWidth = (width-xPos) + size//2
                                             eraseX = width - eraseWidth-1
                                        if yPos-size//2<=0:
                                             eraseHeight = (yPos) + size//2
                                             eraseY = 0
                                        elif yPos+size//2>=height*0.7:
                                             eraseHeight = (height*0.7-yPos) + size//2
                                             eraseY = height*0.7 - eraseHeight-1

                                        #Blits background over the drawing to erase
                                        sample = sceneList[sceneNum].subsurface([eraseX-width*0.3, eraseY, eraseWidth, eraseHeight])
                                        screen.blit(sample, (eraseX, eraseY))            
                                   else:
                                        #If no abckground is selected draws white rectangle instead
                                        draw.rect(screen, WHITE, [xPos-size//2, yPos-size//2, size, size], 0)
                              except:
                                   pass
                         
                    elif drawState == "spray": #Sets a number of random pixels in a radius around mouse
                         for i in range(int(((1+sprayDensity)/900)*size**2//10+1)): #Pixels changed relative to size
                              xPos = randint(-size//2, size//2) + mx
                              yPos = randint(-size//2, size//2) + my
                              dist = int(sqrt((xPos-mx)**2+(yPos-my)**2))
                              if dist < size//2: #If in radius of mouse changes colour of pixel
                                   screen.set_at((xPos, yPos), colourOne)
                                   
                    elif drawState == "pen": #Draws and changes thickness depending on speed
                         dx=mx-mxO
                         dy=my-myO
                         dist=int(sqrt(dx**2+dy**2)) + 10
                         penSize = size//(dist*5)+1 #Cant be too large or doesnt look nice. Inversely proportional to distance
                         for i in range(dist): #
                              xPos=int(mxO+i*dx/dist)  
                              yPos=int(myO+i*dy/dist)  
                              draw.circle(screen,colourOne,(xPos,yPos),penSize)
                                   
                    elif drawState == "marker": #Draws a line of translucent circles
                         dx=mx-mxO
                         dy=my-myO
                         dist=int(sqrt(dx**2+dy**2)) + 1
                         for i in range(dist):
                              xPos=int(mxO+i*dx/dist)  
                              yPos=int(myO+i*dy/dist)  
                              transSurf = Surface((size, size),SRCALPHA) #Surface for circle to be drawn on
                              draw.circle(transSurf,(colourOne[0], colourOne[1], colourOne[2], transparency),(size//2,size//2),size//2) #Draws a circle with transparency on the canvas
                              screen.blit(transSurf, (xPos-size//2, yPos-size//2)) #Blits it to screen
                              
                    elif drawState == "fill": #Fill tool. Fills an area on the screen
                         pixelList = [(mx, my)] #Holds points to be filled
                         colourStart = screen.get_at((mx, my)) #Colour being checked for to see whether it should be filled
                         if colourStart != colourOne: #Making sure start colour and new colour are different to prevent infinite loo[
                              while len(pixelList) > 0: #While there are still points to be filled
                                   if inRect(canvasRect, pixelList[0]) and screen.get_at(pixelList[0]) == colourStart: #If pixel is an canvas and is start colour it will fill it
                                        screen.set_at((pixelList[0]), colourOne)
                                        #Appends point around that point to list
                                        pixelList.append((pixelList[0][0], pixelList[0][1]-1))
                                        pixelList.append((pixelList[0][0], pixelList[0][1]+1))
                                        pixelList.append((pixelList[0][0]-1, pixelList[0][1]))
                                        pixelList.append((pixelList[0][0]+1, pixelList[0][1]))
                                   del pixelList[0] #Remove point from the list
                         
                    elif drawState == "pixelate" and click: #If user clicks an area, it pixelates that spot
                         try: #Still crashes if screen is too small and pixelate hits two sides at once so try except is needed
                              pixelateWidth = size
                              pixelateHeight = size
                              pixelateX = mx-pixelateWidth//2
                              pixelateY = my-pixelateHeight//2
                              #Checking if pixelate is hitting the borders and adjusting so pixelate can work on edges
                              #If on border decreases size or start to prevent crashing
                              if pixelateX<=width*0.3:
                                   pixelateWidth = (mx-width*0.3) + size//2
                                   pixelateX = width*0.3+1
                              elif pixelateX+pixelateWidth>=width:
                                   pixelateWidth = (width-mx) + size//2
                                   pixelateX = width - pixelateWidth-1
                              if pixelateY<=0:
                                   pixelateHeight = (my) + size//2
                                   pixelateY = 1
                              elif pixelateY+pixelateHeight>=height*0.7:
                                   pixelateHeight = (height*0.7-my) + size//2
                                   pixelateY = height*0.7 - pixelateHeight-1
                              #Takes section of the screen, makes it small, brings it back to normal size, then blits it. 
                              sect = screen.subsurface((pixelateX, pixelateY, pixelateWidth, pixelateHeight)).copy()
                              sect = transform.scale(sect, (int(pixelateWidth//pixelateStrength), int(pixelateHeight//pixelateStrength)))
                              sect = transform.scale(sect, (int(pixelateWidth), int(pixelateHeight)))
                              screen.blit(sect, (pixelateX, pixelateY))
                         except:
                              pass



                    #THE END OF CODE FOR DRAWING TOOLS PRIMARY FUNCTION

                    
                    elif drawState == "stamp":
                         if rightClick:
                              stampPrinted = transform.rotate(stampPrinted, 90) #Rotates stamp is user right clicks
                         screen.blit(paintScreen, (width*0.3, 0)) #Consatntly blit canvas before shape onto screen so shape doesnt drag and display everywhere
                         image = transform.scale(stampPrinted, (int(size*2+10), int(size*2+10))) #Resizing of the image
                         screen.blit(image, (mx-size-5, my-size-5)) #Blits the stamp

                    #Block of code checks if draw state is equal to shape to later go and check which shape
                    elif drawState == "shape" or drawState == "cut":
                         

                         screen.blit(paintScreen, (width*0.3, 0)) #Consatntly blit canvas before shape onto screen so shape doesnt drag and display everywhere

                         if drawState == "cut" and not rightClick: #Takes portion of the screen which you can move around and resize
                              cutRect = Rect(xStart, yStart, mx-xStart, my-yStart)
                              cutRect.normalize() #Fixes negative sizes                              
                              draw.rect(screen, BLACK, cutRect, 1) #Draws a rect so user knows which area is being selected
                         
                         #Rectangle tool
                         elif shape == "rectangle": #Draws a rectangle
                              rectangleRect = Rect(xStart, yStart, mx-xStart, my-yStart)
                              rectangleRect.normalize() #Fixes negative sizes
                              if fillShape:
                                   draw.rect(screen, colourTwo, rectangleRect, 0) #Draws a filled rectangle with colour two
                              draw.rect(screen, colourOne, rectangleRect, size//5+1) #Draws border around rectangle
                              #Now draws squares to fix empty spots in the corners of the rectangle
                              if size > 10: #Onyl if size > 10 because squares on rectangles with smaller sizes look weird
                                   draw.rect(screen, colourOne, [xStart - (size//5)//2, yStart - (size//5)//2, size//5, size//5], 0)
                                   draw.rect(screen, colourOne, [mx - (size//5)//2, my - (size//5)//2, size//5, size//5], 0)
                                   draw.rect(screen, colourOne, [xStart - (size//5)//2, my - (size//5)//2, size//5, size//5], 0)
                                   draw.rect(screen, colourOne, [mx - (size//5)//2, yStart - (size//5)//2, size//5, size//5], 0)

                         #Ellipse tool
                         elif shape == "ellipse":
                              ellipseRect = Rect(xStart, yStart, mx-xStart, my-yStart)
                              ellipseRect.normalize() 
                              try: #Try to fix error when thickness exceeds border
                                   if fillShape:
                                        draw.ellipse(screen, colourTwo, ellipseRect, 0) #Draws filled ellipse
                                   #Draws 5 ellipses to fill in empty holes that appear when only one ellipse is drawn
                                   draw.ellipse(screen, colourOne, ellipseRect, size//5+1)
                                   draw.ellipse(screen, colourOne, [ellipseRect[0]+1,ellipseRect[1],ellipseRect[2],ellipseRect[3]], size//5+1)
                                   draw.ellipse(screen, colourOne, [ellipseRect[0]-1,ellipseRect[1],ellipseRect[2],ellipseRect[3]], size//5+1)
                                   draw.ellipse(screen, colourOne, [ellipseRect[0],ellipseRect[1]+1,ellipseRect[2],ellipseRect[3]], size//5+1)
                                   draw.ellipse(screen, colourOne, [ellipseRect[0],ellipseRect[1]-1,ellipseRect[2],ellipseRect[3]], size//5+1)
                              except:
                                   #If thickness is too large, fill ellipse with border colour
                                   draw.ellipse(screen, colourOne, ellipseRect, 0)

                         #Triangle tool
                         elif shape == "triangle": #Draws an isosceles triangle                    
                              if fillShape:
                                   #Draws filled polygon
                                   draw.polygon(screen, colourTwo, [(xStart+(mx-xStart)//2, yStart), (mx, my), (xStart, my)], 0)
                              #Draws three lines instead of polygon to fill in empty corners
                              curvedLine(screen, colourOne, (mx, my), (xStart+(mx-xStart)//2, yStart), size//5+1)
                              curvedLine(screen, colourOne, (xStart+(mx-xStart)//2, yStart), (xStart, my), size//5+1)
                              curvedLine(screen, colourOne, (xStart, my), (mx, my), size//5+1)

                         #Line tool
                         elif shape == "line": #Draws different types of lines
                              if lineType == "straight": #Regular straight line
                                   draw.line(screen, colourOne, (xStart, yStart), (mx, my), size//5+1)
                                   
                              elif lineType == "rounded": #Rounded edges
                                   curvedLine(screen, colourOne, (xStart, yStart), (mx, my), size//5+1)
                                   
                              elif lineType == "dotted": #Dotted
                                   dx = mx - xStart
                                   dy = my - yStart
                                   dist = int(sqrt((dx**2+dy**2)))+1
                                   #Similar to rounded line function but large interval when drawing circles
                                   for i in range(0, dist, (size//5+1)*2):
                                        xPos = int(dx*(i/dist))+ xStart
                                        yPos = int(dy*(i/dist)) + yStart
                                        draw.circle(screen, colourOne, (xPos, yPos), size//10+1)
                                        
                              elif lineType == "dashedOne": #Dashed
                                   dx = mx - xStart
                                   dy = my - yStart
                                   dist = int(sqrt((dx**2+dy**2)))+1
                                   #Similar to dotted but draws small lines instead
                                   for i in range(0, dist, (size//5+1)*4):
                                        xPos1 = int(dx*(i/dist))+ xStart
                                        yPos1 = int(dy*(i/dist)) + yStart
                                        xPos2 = int(dx*((i+(size//5+1)*3)/dist))+ xStart
                                        yPos2 = int(dy*((i+(size//5+1)*3)/dist)) + yStart
                                        draw.line(screen, colourOne, (xPos1, yPos1), (xPos2, yPos2), size//5+1)

                              elif lineType == "dashedTwo": #Dashed but spaces have a secondary colour
                                   #Draws regular line behind dotted line to give a filled line effect
                                   draw.line(screen, colourTwo, (xStart, yStart), (mx, my), size//5+1)
                                   dx = mx - xStart
                                   dy = my - yStart
                                   dist = int(sqrt((dx**2+dy**2)))+1
                                   for i in range(0, dist, (size//5+1)*4):
                                        xPos1 = int(dx*(i/dist))+ xStart
                                        yPos1 = int(dy*(i/dist)) + yStart
                                        xPos2 = int(dx*((i+(size//5+1)*3)/dist))+ xStart
                                        yPos2 = int(dy*((i+(size//5+1)*3)/dist)) + yStart
                                        draw.line(screen, colourOne, (xPos1, yPos1), (xPos2, yPos2), size//5+3)

                         #Arc tool
                         elif shape == "hexagon": #Draws a hexagon where opposite sides are equal
                              if fillShape: #Draws filled hexagon
                                   draw.polygon(screen, colourTwo, [(xStart+(mx-xStart)//3, yStart),(xStart+2*(mx-xStart)//3, yStart),(mx, yStart+(my-yStart)//2),(xStart+2*(mx-xStart)//3, my),(xStart+(mx-xStart)//3, my),(xStart, yStart+(my-yStart)//2)], 0)
                              #Draws 6 lines instead of polygon to look smoother and fill corners
                              curvedLine(screen, colourOne, (xStart+(mx-xStart)//3, yStart), (xStart+2*(mx-xStart)//3, yStart), size//5+1)
                              curvedLine(screen, colourOne, (xStart+2*(mx-xStart)//3, yStart), (mx, yStart+(my-yStart)//2), size//5+1)
                              curvedLine(screen, colourOne, (mx, yStart+(my-yStart)//2), (xStart+2*(mx-xStart)//3, my), size//5+1)
                              curvedLine(screen, colourOne, (xStart+2*(mx-xStart)//3, my), (xStart+(mx-xStart)//3, my), size//5+1)
                              curvedLine(screen, colourOne, (xStart+(mx-xStart)//3, my), (xStart, yStart+(my-yStart)//2), size//5+1)
                              curvedLine(screen, colourOne, (xStart, yStart+(my-yStart)//2), (xStart+(mx-xStart)//3, yStart), size//5+1)
                     

                         #Polygon tool
                         elif shape == "polygon" and click:
                              #Gets images to blit onto screen while polygon is selected so it doesnt overlap
                              paintScreen = screen.subsurface(canvasRect).copy()
                              homeLeftImage = screen.subsurface((0, 0, width*0.3, height)).copy()
                              homeBottomImage = screen.subsurface((width*0.3, height*0.7, width*0.7, height*0.3)).copy()

                              #Gets starting position of polygon 
                              xNewStart, yNewStart = mx, my #Every time a user clicks, new start will be last click
                              xStart, yStart = mx, my
                              
                              polygonPointList = [(xStart, yStart)] #Points in the polygon
                              polygonShape = True #True while polygon is being made
                              while polygonShape:
                                        display.set_caption("Paintpyrus    FPS: %d" % int(myClock.get_fps())) #Title of program. Also shows the frames per second
                                        #Smaller version of event handling at the beginning of the game loop
                                        click = False
                                        release = False
                                        scroll = 0
                                        mx, my = mouse.get_pos()
                                        for action in event.get():
                                             if action.type == MOUSEBUTTONDOWN:
                                                  if action.button == 1:
                                                       click = True
                                                  if action.button == 3:
                                                       rightClick = True
                                             if action.type == MOUSEBUTTONUP:
                                                  if action.button == 3:
                                                       release = True
                                                  
                                        if inRect(canvasRect, (mx, my)):
                                             if click:
                                                  #Will add points to polygon list and update newstart variables
                                                  paintScreen = screen.subsurface(canvasRect).copy()
                                                  xNewStart, yNewStart = mx, my
                                                  polygonPointList.append((mx, my))
                                                  
                                             screen.blit(paintScreen, (width*0.3, 0))
                                             #Draws a line so user can see what next line will look like
                                             curvedLine(screen, colourOne, (mx, my),(xNewStart, yNewStart), size//5+1)

                                             
                                             if rightClick: #Closes shape when user right clicks
                                                  draw.line(screen, colourOne, (mx, my), (xStart, yStart), size//5+1)
                                                  polygonPointList.append((mx, my))
                                                  polygonShape = False
                                                  if fillShape:
                                                       try:
                                                            draw.polygon(screen, colourTwo, polygonPointList, 0)
                                                            draw.polygon(screen, colourOne, polygonPointList, size//5+1)
                                                       except:
                                                            pass
                                                       #Appends to undo
                                                       undoList.append(screen.subsurface(canvasRect).copy())
                                                       redoList = []
                                        #Blits background so polygon doesnt overlap
                                        screen.blit(homeLeftImage, (0, 0))
                                        screen.blit(homeBottomImage, (width*0.3, height*0.7))
                                        display.flip()
                                        myClock.tick(60) #Runs the clock so time data can be extrapolated

                         
     
          #################################################################################################### 
          ####################################################################################################
                                     #RIGHT CLICKING SECONDARY FUNCTIONS OF DRAWING TOOLS
                                        
               elif rightHold or click:
                    
                    #Same as pencil but uses colour two instead
                    if drawState == "pencil":
                         curvedLine(screen, colourTwo, (mx, my), (mxO, myO), size)
                              
                    elif drawState == "eraser": #A white pencil
                         curvedLine(screen, WHITE, (mx, my), (mxO, myO), size)
                              
                    elif drawState == "spray": #Draws a bar code pattern
                         for i in range(int(((1+sprayDensity)/900)*size//10+1)):
                              xPos = randint(-size, size) + mx #Gets a random x position
                              draw.line(screen, colourOne, (xPos, my-size//2), (xPos, my+size//2), 1) #Draws a line there
                                   
                    elif drawState == "pen": #Changes thickness with cursor speed. Also has bleed component
                         dx=mx-mxO
                         dy=my-myO
                         dist=int(sqrt(dx**2+dy**2)) + 10
                         penSize = size//(dist*5)+1 #Like before pensize is inversely proportional to distance
                         for i in range(dist):
                              xPos=int(mxO+i*dx/dist)  
                              yPos=int(myO+i*dy/dist)  
                              draw.circle(screen,colourOne,(xPos,yPos),penSize)
                              bleedChance = randint(1, 5000) #Whether the pen will drip at the current circle being drawn
                              if bleedChance < penBleed:
                                   blood = randint(1, penBleed+1) #Amount of bleed and opacity of bleed
                                   for j in range(blood): #Draws line straight down of transparent circles slowly getting smaller and less opaque
                                        bleedSize = penSize - int((j*penSize//2)/blood) #Thickness of blood
                                        transSurf = Surface((size, size),SRCALPHA)
                                        draw.circle(transSurf,(colourOne[0], colourOne[1], colourOne[2], 255-int(j*255/blood)),(bleedSize,bleedSize),bleedSize)
                                        screen.blit(transSurf, (xPos-bleedSize, yPos+j))
     
                   
                    elif drawState == "marker": #Highlighter tool
                         dx=mx-mxO
                         dy=my-myO
                         dist=int(sqrt(dx**2+dy**2)) + 1
                         highlightCover.set_alpha(transparency*20) #Updates transparency
                         for i in range(dist): #Draws like pencil
                              xPos=int(mxO+i*dx/dist)  
                              yPos=int(myO+i*dy/dist)  
                              draw.circle(highlightCover, colourOne, (xPos, yPos), size//2)
                         #Blits background
                         if len(undoList) > 0:
                              screen.blit(undoList[-1], (width*0.3, 0))
                         else:
                              canvasClear(screen, width, height)
                         #Blits transparent background colour onto the screen
                         screen.blit(highlightCover, (0, 0))

                              
                    elif drawState == "fill": #The same as the fill with left click except it uses colour two
                         pixelList = [(mx, my)]
                         colourStart = screen.get_at((mx, my))
                         if colourStart != colourTwo:
                              while len(pixelList) > 0:
                                   event.pump()
                                   if inRect(canvasRect, pixelList[0]) and screen.get_at(pixelList[0]) == colourStart:
                                        screen.set_at((pixelList[0]), colourTwo)
                                        pixelList.append((pixelList[0][0], pixelList[0][1]-1))
                                        pixelList.append((pixelList[0][0], pixelList[0][1]+1))
                                        pixelList.append((pixelList[0][0]-1, pixelList[0][1]))
                                        pixelList.append((pixelList[0][0]+1, pixelList[0][1]))
                                   del pixelList[0]
                         
                    elif drawState == "pixelate": #Blur tool
                         pixelList = [(mx, my)]
                         for i in range(2*(size//15)**2): #Works similar to fill in the pattern it goes in
                              #Difference is it doesnt check current colour to decide on whethe it should continue
                              if inRect(canvasRect, pixelList[0]):
                                   try:
                                        #Gets the average of the pixels around the current pixel and sets it to that colour
                                        rAvg = ((screen.get_at((pixelList[0][0]-1, pixelList[0][1]))[0] + screen.get_at((pixelList[0][0]+1, pixelList[0][1]))[0] + screen.get_at((pixelList[0][0], pixelList[0][1]-1))[0] + screen.get_at((pixelList[0][0], pixelList[0][1]+1))[0]))/4
                                        gAvg = ((screen.get_at((pixelList[0][0]-1, pixelList[0][1]))[1] + screen.get_at((pixelList[0][0]+1, pixelList[0][1]))[1] + screen.get_at((pixelList[0][0], pixelList[0][1]-1))[1] + screen.get_at((pixelList[0][0], pixelList[0][1]+1))[1]))/4
                                        bAvg = ((screen.get_at((pixelList[0][0]-1, pixelList[0][1]))[2] + screen.get_at((pixelList[0][0]+1, pixelList[0][1]))[2] + screen.get_at((pixelList[0][0], pixelList[0][1]-1))[2] + screen.get_at((pixelList[0][0], pixelList[0][1]+1))[2]))/4
                                        screen.set_at((pixelList[0]), (rAvg, gAvg, bAvg))
                                        #Appends pixels around it to the list
                                        if (pixelList[0][0], pixelList[0][1]-1) not in pixelList:
                                             pixelList.append((pixelList[0][0], pixelList[0][1]-1))
                                        if (pixelList[0][0], pixelList[0][1]+1) not in pixelList:
                                             pixelList.append((pixelList[0][0], pixelList[0][1]+1))
                                        if (pixelList[0][0]-1, pixelList[0][1]) not in pixelList:
                                             pixelList.append((pixelList[0][0]-1, pixelList[0][1]))
                                        if (pixelList[0][0]+1, pixelList[0][1]) not in pixelList:
                                             pixelList.append((pixelList[0][0]+1, pixelList[0][1]))
                                        del pixelList[0]
                                   except:
                                        pass
                         
                         
          #################################################################################################### 
          ####################################################################################################
          #Text Tool
               toolButton(screen, (width*0.12, height*0.6, width*0.06, height*0.05), "text", textButton, textButton, heartSelect,  (mx, my), click, width, height)
               if drawState == "text":
                    if release and not textOn: #Starts new textbox if textbox not already in use
                         textOn = True
                         startX, startY = mx, my
                         currentText = "" #Text to be displayed
                         
                         if fontNumber == 0: #Since font one is custom had to be initialized differently
                              currentFont = font.Font(fontList[0], size+2)
                         else:
                              currentFont = font.SysFont(fontList[fontNumber%5], size+2)
                         currentFont.set_bold(bolded) #Sets bolded if bolded is true
                         currentFont.set_italic(italics) #Sets italics if italics are true
                         textScreen = screen.subsurface(canvasRect).copy() #Will be displayed on screen so backspace is visible to user
                         
          if textOn and drawState == "text":       
               currentText+=eventText #Add event text to text that will be displayed
               textRender = currentFont.render(currentText, 1, colourOne)
               #Blits background then text onto screen
               screen.blit(textScreen, (width*0.3, 0))
               screen.blit(textRender, (startX, startY))

               #If user clicks outside of textbox, will end text tool
               if click and not inRect((startX, startY, textRender.get_width(), textRender.get_height()), (mx, my)):
                    textOn = False
                    undoList.append(screen.subsurface(canvasRect).copy())
                    textScreen = screen.subsurface(canvasRect).copy()
                    redoList = []

                    
          #################################################################################################### 
          ####################################################################################################
          #SELECTING A SHAPE, MOVING IT, AND RESIZING IT
                    
          if not Rrelease and release and inRect(canvasRect, (mx, my)):
               #Whether or not shape is selected, done at the top to keep points more up to date
               selectRect1 = False
               selectRect2 = False
               selectRect3 = False
               selectRect4 = False
               selectRect5 = False
               selectRect6 = False
               selectRect7 = False
               selectRect8 = False
               dragRect = False
               #Selecting shape or using cut
               if drawState == "shape":
                    toolSelected = True
                    #Select coords are not constantly moving unless dragged
                    xSelectStart, ySelectStart = xStart, yStart 
                    xSelectEnd, ySelectEnd = mx, my
                    #Copies sides of screen so shape doesnt look out of bounds
                    screenLeftSelect = screen.subsurface((0, 0, width*0.3, height)).copy()
                    screenBottomSelect = screen.subsurface((width*0.3, height*0.7, width*0.7, height*0.3)).copy()
                    if shape == "rectangle" or shape == "hexagon" or shape == "ellipse" or shape == "triangle":
                         while toolSelected:
                              display.set_caption("Paintpyrus    FPS: %d" % int(myClock.get_fps())) #Title of program. Also shows the frames per second
                              leftHold, rightHold = mouse.get_pressed()[0], mouse.get_pressed()[2]
                              click = False
                              release = False
                              scroll = 0
                              mx, my = mouse.get_pos()
                              #If node is selected, will resize it in accordance with mouse position
                              #Mouse.get_pressed() is used so its more up to date
                              #Select nodes on corners
                              if selectRect1:
                                   xSelectStart, ySelectStart = mouse.get_pos()
                                   selectRect1 = False
                              elif selectRect2:
                                   xSelectStart, ySelectEnd = mouse.get_pos()
                                   selectRect2 = False
                              elif selectRect3:
                                   xSelectEnd, ySelectStart = mouse.get_pos()
                                   selectRect3 = False
                              elif selectRect4:
                                   xSelectEnd, ySelectEnd = mouse.get_pos()
                                   selectRect4 = False
                              #Select nodes on edges
                              elif selectRect5:
                                   xSelectStart = mouse.get_pos()[0]
                              elif selectRect6:
                                   xSelectEnd = mouse.get_pos()[0]
                              elif selectRect7:
                                   ySelectStart = mouse.get_pos()[1]
                              elif selectRect8:
                                   ySelectEnd = mouse.get_pos()[1]

                              #Dragging rect changes position accordance to movement
                              elif dragRect:
                                   xSelectStart += (mx-mxO)
                                   ySelectStart += (my-myO)
                                   xSelectEnd += (mx-mxO)
                                   ySelectEnd += (my-myO)
                                   dragRect = False

                              
                              #Event loop
                              for action in event.get():
                                   if action.type == MOUSEBUTTONDOWN:
                                        #Event mouse handling
                                        if action.button == 1:
                                             click = True
                                        if action.button == 3:
                                             rightClick = True
                                        if action.button == 4:
                                             scroll+=1
                                        if action.button == 5:
                                             scroll-=1
                                   if action.type == MOUSEBUTTONUP:
                                        if action.button == 1:
                                             release = True
                                             leftHold = False
                                             #If mouse is released unselects edge nodes
                                             selectRect5 = False
                                             selectRect6 = False
                                             selectRect7 = False
                                             selectRect8 = False
                                             
                              #Size is controlled by scrolling wheel and dragging of the size bar
                              if scroll>0:
                                   size+=(scroll+size//100)
                              elif scroll<0:
                                   size+=(scroll-size//100)
                              #Limits to the size keeps the program from crashing
                              if size < 1:
                                   size = 1
                              elif size > 500:
                                   size = 500
                              #Blits paintScreen like regular shape tool
                              screen.blit(paintScreen, (width*0.3, 0))
                              #Updates selectRect
                              selectRect = Rect(xSelectStart, ySelectStart, xSelectEnd-xSelectStart, ySelectEnd-ySelectStart)
                              selectRect.normalize() #Fixes negative values

                              #Very similar to regular shape except different vars are used for position and size
                              if shape == "rectangle":
                                   rectangleRect = Rect(selectRect)
                                   rectangleRect.normalize()
                                   if fillShape:
                                        draw.rect(screen, colourTwo, rectangleRect, 0)
                                   draw.rect(screen, colourOne, rectangleRect, size//5+1)
                                   if size > 10:
                                        draw.rect(screen, colourOne, [xSelectStart - (size//5)//2, ySelectStart - (size//5)//2, size//5, size//5], 0)
                                        draw.rect(screen, colourOne, [xSelectEnd - (size//5)//2, ySelectEnd - (size//5)//2, size//5, size//5], 0)
                                        draw.rect(screen, colourOne, [xSelectStart - (size//5)//2, ySelectEnd - (size//5)//2, size//5, size//5], 0)
                                        draw.rect(screen, colourOne, [xSelectEnd - (size//5)//2, ySelectStart - (size//5)//2, size//5, size//5], 0)
                              elif shape == "ellipse":
                                   ellipseRect = Rect(selectRect)
                                   ellipseRect.normalize()
                                   try:
                                        if fillShape:
                                             draw.ellipse(screen, colourTwo, ellipseRect, 0)
                                        draw.ellipse(screen, colourOne, ellipseRect, size//5+1)
                                        draw.ellipse(screen, colourOne, [ellipseRect[0]+1,ellipseRect[1],ellipseRect[2],ellipseRect[3]], size//5+1)
                                        draw.ellipse(screen, colourOne, [ellipseRect[0]-1,ellipseRect[1],ellipseRect[2],ellipseRect[3]], size//5+1)
                                        draw.ellipse(screen, colourOne, [ellipseRect[0],ellipseRect[1]+1,ellipseRect[2],ellipseRect[3]], size//5+1)
                                        draw.ellipse(screen, colourOne, [ellipseRect[0],ellipseRect[1]-1,ellipseRect[2],ellipseRect[3]], size//5+1)
                                   except:
                                        draw.ellipse(screen, colourOne, ellipseRect, 0)
                              elif shape == "hexagon":
                                   if fillShape: 
                                        draw.polygon(screen, colourTwo, [(xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectStart),(xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectStart),(xSelectEnd, ySelectStart+(ySelectEnd-ySelectStart)//2),(xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectEnd),(xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectEnd),(xSelectStart, ySelectStart+(ySelectEnd-ySelectStart)//2)], 0)
                                   curvedLine(screen, colourOne, (xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectStart), (xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectStart), size//5+1)
                                   curvedLine(screen, colourOne, (xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectStart), (xSelectEnd, ySelectStart+(ySelectEnd-ySelectStart)//2), size//5+1)
                                   curvedLine(screen, colourOne, (xSelectEnd, ySelectStart+(ySelectEnd-ySelectStart)//2), (xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectEnd), size//5+1)
                                   curvedLine(screen, colourOne, (xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectEnd), (xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectEnd), size//5+1)
                                   curvedLine(screen, colourOne, (xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectEnd), (xSelectStart, ySelectStart+(ySelectEnd-ySelectStart)//2), size//5+1)
                                   curvedLine(screen, colourOne, (xSelectStart, ySelectStart+(ySelectEnd-ySelectStart)//2), (xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectStart), size//5+1)
                              elif shape == "triangle":
                                   if fillShape:
                                        draw.polygon(screen, colourTwo, [(xSelectStart+(xSelectEnd-xSelectStart)//2, ySelectStart), (xSelectEnd, ySelectEnd), (xSelectStart, ySelectEnd)], 0)
                                   curvedLine(screen, colourOne, (xSelectEnd, ySelectEnd), (xSelectStart+(xSelectEnd-xSelectStart)//2, ySelectStart), size//5+1)
                                   curvedLine(screen, colourOne, (xSelectStart+(xSelectEnd-xSelectStart)//2, ySelectStart), (xSelectStart, ySelectEnd), size//5+1)
                                   curvedLine(screen, colourOne, (xSelectStart, ySelectEnd), (xSelectEnd, ySelectEnd), size//5+1)

                              #Draws nodes and outline around the shape
                              draw.rect(screen, YELLOW, [xSelectStart-5, ySelectStart-5, 10, 10], 0)
                              draw.rect(screen, YELLOW, [xSelectStart-5, ySelectEnd-5, 10, 10], 0)
                              draw.rect(screen, YELLOW, [xSelectEnd-5, ySelectStart-5, 10, 10], 0)
                              draw.rect(screen, YELLOW, [xSelectEnd-5, ySelectEnd-5, 10, 10], 0)
                              draw.rect(screen, YELLOW, [xSelectStart-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5, 10, 10], 0)
                              draw.rect(screen, YELLOW, [xSelectEnd-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5, 10, 10], 0)
                              draw.rect(screen, YELLOW, [xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectStart-5, 10, 10], 0)
                              draw.rect(screen, YELLOW, [xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectEnd-5, 10, 10], 0)

                              draw.rect(screen, BLACK, [xSelectStart-5, ySelectStart-5, 10, 10], 1)
                              draw.rect(screen, BLACK, [xSelectStart-5, ySelectEnd-5, 10, 10], 1)
                              draw.rect(screen, BLACK, [xSelectEnd-5, ySelectStart-5, 10, 10], 1)
                              draw.rect(screen, BLACK, [xSelectEnd-5, ySelectEnd-5, 10, 10], 1)
                              draw.rect(screen, BLACK, [xSelectStart-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5, 10, 10], 1)
                              draw.rect(screen, BLACK, [xSelectEnd-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5, 10, 10], 1)
                              draw.rect(screen, BLACK, [xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectStart-5, 10, 10], 1)
                              draw.rect(screen, BLACK, [xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectEnd-5, 10, 10], 1)

                              #Blits background so shape doesnt overlap
                              screen.blit(screenLeftSelect, (0, 0))
                              screen.blit(screenBottomSelect, (width*0.3, height*0.7))
                              display.flip()

                              #If holding onto a node program will select that node
                              if leftHold:
                                   if inRect((xSelectStart-5, ySelectStart-5, 10, 10), (mx, my)):
                                        selectRect1 = True
                                   elif inRect((xSelectStart-5, ySelectEnd-5, 10, 10), (mx, my)):
                                        selectRect2 = True
                                   elif inRect((xSelectEnd-5, ySelectStart-5, 10, 10), (mx, my)):
                                        selectRect3 = True
                                   elif inRect((xSelectEnd-5, ySelectEnd-5, 10, 10), (mx, my)):
                                        selectRect4 = True
                                   elif inRect((xSelectStart-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5, 10, 10), (mx, my)):
                                        selectRect5 = True
                                   elif inRect((xSelectEnd-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5,10, 10), (mx, my)):
                                        selectRect6 = True
                                   elif inRect((xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectStart-5, 10, 10), (mx, my)):
                                        selectRect7 = True
                                   elif inRect((xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectEnd-5, 10, 10), (mx, my)):
                                        selectRect8 = True
                                   elif inRect(selectRect, (mx, my)):
                                        dragRect = True
                                               
                              mxO, myO = mx, my #Sets old mx, my coords
                              myClock.tick(60) #Runs the clock so time data can be extrapolated
                              #If clicked outside of shape, deselects the shape
                              if release and not(selectRect1 or selectRect2 or selectRect3 or selectRect4 or selectRect5 or selectRect6 or selectRect7 or selectRect8 or dragRect):
                                   if not inRect((selectRect[0]-5, selectRect[1]-5, selectRect[2]+10, selectRect[3]+10), (mx, my)):
                                        toolSelected = False
                                        screen.blit(paintScreen, (width*0.3, 0))
                                        #Re draws everything so nodes dont remain
                                        if shape == "rectangle":
                                             rectangleRect = Rect(xSelectStart, ySelectStart, xSelectEnd-xSelectStart, ySelectEnd-ySelectStart)
                                             rectangleRect.normalize()
                                             if fillShape:
                                                  draw.rect(screen, colourTwo, rectangleRect, 0)
                                             draw.rect(screen, colourOne, rectangleRect, size//5+1)
                                             draw.rect(screen, colourOne, [xSelectStart - (size//5)//2, ySelectStart - (size//5)//2, size//5, size//5], 0)
                                             draw.rect(screen, colourOne, [xSelectEnd - (size//5)//2, ySelectEnd - (size//5)//2, size//5, size//5], 0)
                                             draw.rect(screen, colourOne, [xSelectStart - (size//5)//2, ySelectEnd - (size//5)//2, size//5, size//5], 0)
                                             draw.rect(screen, colourOne, [xSelectEnd - (size//5)//2, ySelectStart - (size//5)//2, size//5, size//5], 0)
                                        elif shape == "ellipse":
                                             ellipseRect = Rect(selectRect)
                                             ellipseRect.normalize()
                                             try:
                                                  if fillShape:
                                                       draw.ellipse(screen, colourTwo, ellipseRect, 0)
                                                  draw.ellipse(screen, colourOne, ellipseRect, size//5+1)
                                                  draw.ellipse(screen, colourOne, [ellipseRect[0]+1,ellipseRect[1],ellipseRect[2],ellipseRect[3]], size//5+1)
                                                  draw.ellipse(screen, colourOne, [ellipseRect[0]-1,ellipseRect[1],ellipseRect[2],ellipseRect[3]], size//5+1)
                                                  draw.ellipse(screen, colourOne, [ellipseRect[0],ellipseRect[1]+1,ellipseRect[2],ellipseRect[3]], size//5+1)
                                                  draw.ellipse(screen, colourOne, [ellipseRect[0],ellipseRect[1]-1,ellipseRect[2],ellipseRect[3]], size//5+1)
                                             except:
                                                  draw.ellipse(screen, colourOne, ellipseRect, 0)
                                        elif shape == "hexagon":
                                             if fillShape: 
                                                  draw.polygon(screen, colourTwo, [(xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectStart),(xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectStart),(xSelectEnd, ySelectStart+(ySelectEnd-ySelectStart)//2),(xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectEnd),(xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectEnd),(xSelectStart, ySelectStart+(ySelectEnd-ySelectStart)//2)], 0)
                                             curvedLine(screen, colourOne, (xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectStart), (xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectStart), size//5+1)
                                             curvedLine(screen, colourOne, (xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectStart), (xSelectEnd, ySelectStart+(ySelectEnd-ySelectStart)//2), size//5+1)
                                             curvedLine(screen, colourOne, (xSelectEnd, ySelectStart+(ySelectEnd-ySelectStart)//2), (xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectEnd), size//5+1)
                                             curvedLine(screen, colourOne, (xSelectStart+2*(xSelectEnd-xSelectStart)//3, ySelectEnd), (xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectEnd), size//5+1)
                                             curvedLine(screen, colourOne, (xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectEnd), (xSelectStart, ySelectStart+(ySelectEnd-ySelectStart)//2), size//5+1)
                                             curvedLine(screen, colourOne, (xSelectStart, ySelectStart+(ySelectEnd-ySelectStart)//2), (xSelectStart+(xSelectEnd-xSelectStart)//3, ySelectStart), size//5+1)
                                        elif shape == "triangle":
                                             if fillShape:
                                                  draw.polygon(screen, colourTwo, [(xSelectStart+(xSelectEnd-xSelectStart)//2, ySelectStart), (xSelectEnd, ySelectEnd), (xSelectStart, ySelectEnd)], 0)
                                             curvedLine(screen, colourOne, (xSelectEnd, ySelectEnd), (xSelectStart+(xSelectEnd-xSelectStart)//2, ySelectStart), size//5+1)
                                             curvedLine(screen, colourOne, (xSelectStart+(xSelectEnd-xSelectStart)//2, ySelectStart), (xSelectStart, ySelectEnd), size//5+1)
                                             curvedLine(screen, colourOne, (xSelectStart, ySelectEnd), (xSelectEnd, ySelectEnd), size//5+1)

               elif drawState == "cut": #Cuts tool selects part of the screen and makes it moveable and resizable
                    cutAreaOriginal = screen.subsurface(cutRect).copy()
                    draw.rect(screen, WHITE, cutRect, 0)
                    toolSelected = True
                    #Select coords are not constantly moving unless dragged
                    xSelectStart, ySelectStart = xStart, yStart 
                    xSelectEnd, ySelectEnd = mx, my
                    #Copies sides of screen so shape doesnt look out of bounds
                    paintScreen = screen.subsurface((width*0.3, 0, width*0.7, height*0.7)).copy()
                    screenLeftSelect = screen.subsurface((0, 0, width*0.3, height)).copy()
                    screenBottomSelect = screen.subsurface((width*0.3, height*0.7, width*0.7, height*0.3)).copy()
                    while toolSelected:
                         display.set_caption("Paintpyrus    FPS: %d" % int(myClock.get_fps())) #Title of program. Also shows the frames per second
                         leftHold, rightHold = mouse.get_pressed()[0], mouse.get_pressed()[2]
                         click = False
                         release = False
                         scroll = 0
                         mx, my = mouse.get_pos()
                         #Everything is the same as the above loop for shapes except for blitting the actual part of the screen and transforming
                         #Takes selected nodes and resizes them to mouse position
                         if selectRect1:
                              xSelectStart, ySelectStart = mouse.get_pos()
                              selectRect1 = False
                         elif selectRect2:
                              xSelectStart, ySelectEnd = mouse.get_pos()
                              selectRect2 = False
                         elif selectRect3:
                              xSelectEnd, ySelectStart = mouse.get_pos()
                              selectRect3 = False
                         elif selectRect4:
                              xSelectEnd, ySelectEnd = mouse.get_pos()
                              selectRect4 = False
                              
                         elif selectRect5:
                              xSelectStart = mouse.get_pos()[0]
                         elif selectRect6:
                              xSelectEnd = mouse.get_pos()[0]
                         elif selectRect7:
                              ySelectStart = mouse.get_pos()[1]
                         elif selectRect8:
                              ySelectEnd = mouse.get_pos()[1]
                         #Move rect with mouse movement
                         elif dragRect:
                              xSelectStart += (mx-mxO)
                              ySelectStart += (my-myO)
                              xSelectEnd += (mx-mxO)
                              ySelectEnd += (my-myO)
                              dragRect = False

                         
                              
                         for action in event.get():
                              if action.type == MOUSEBUTTONDOWN:
                                   if action.button == 1:
                                        click = True
                                   if action.button == 3:
                                        rightClick = True
                                   if action.button == 4:
                                        scroll+=1
                                   if action.button == 5:
                                        scroll-=1
                              if action.type == MOUSEBUTTONUP:
                                   if action.button == 1:
                                        release = True
                                        leftHold = False
                                        selectRect5 = False
                                        selectRect6 = False
                                        selectRect7 = False
                                        selectRect8 = False

                         screen.blit(paintScreen, (width*0.3, 0))

                         selectRect = Rect(xSelectStart, ySelectStart, xSelectEnd-xSelectStart, ySelectEnd-ySelectStart)
                         selectRect.normalize()
                         #Updates size of selected screen area
                         cutArea = transform.scale(cutAreaOriginal, (selectRect[2], selectRect[3]))
                         #Blits it to the screen
                         screen.blit(cutArea, (selectRect[0], selectRect[1]))

                         #Draws the nodes and their outline
                         draw.rect(screen, YELLOW, [xSelectStart-5, ySelectStart-5, 10, 10], 0)
                         draw.rect(screen, YELLOW, [xSelectStart-5, ySelectEnd-5, 10, 10], 0)
                         draw.rect(screen, YELLOW, [xSelectEnd-5, ySelectStart-5, 10, 10], 0)
                         draw.rect(screen, YELLOW, [xSelectEnd-5, ySelectEnd-5, 10, 10], 0)
                         draw.rect(screen, YELLOW, [xSelectStart-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5, 10, 10], 0)
                         draw.rect(screen, YELLOW, [xSelectEnd-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5, 10, 10], 0)
                         draw.rect(screen, YELLOW, [xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectStart-5, 10, 10], 0)
                         draw.rect(screen, YELLOW, [xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectEnd-5, 10, 10], 0)

                         draw.rect(screen, BLACK, [xSelectStart-5, ySelectStart-5, 10, 10], 1)
                         draw.rect(screen, BLACK, [xSelectStart-5, ySelectEnd-5, 10, 10], 1)
                         draw.rect(screen, BLACK, [xSelectEnd-5, ySelectStart-5, 10, 10], 1)
                         draw.rect(screen, BLACK, [xSelectEnd-5, ySelectEnd-5, 10, 10], 1)
                         draw.rect(screen, BLACK, [xSelectStart-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5, 10, 10], 1)
                         draw.rect(screen, BLACK, [xSelectEnd-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5, 10, 10], 1)
                         draw.rect(screen, BLACK, [xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectStart-5, 10, 10], 1)
                         draw.rect(screen, BLACK, [xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectEnd-5, 10, 10], 1)

                         #Draw background so cut doesnt overlap
                         screen.blit(screenLeftSelect, (0, 0))
                         screen.blit(screenBottomSelect, (width*0.3, height*0.7))
                         display.flip()

                         #Finds if any nodes are being clicked on to be selected
                         if leftHold:
                              if inRect((xSelectStart-5, ySelectStart-5, 10, 10), (mx, my)):
                                   selectRect1 = True
                              elif inRect((xSelectStart-5, ySelectEnd-5, 10, 10), (mx, my)):
                                   selectRect2 = True
                              elif inRect((xSelectEnd-5, ySelectStart-5, 10, 10), (mx, my)):
                                   selectRect3 = True
                              elif inRect((xSelectEnd-5, ySelectEnd-5, 10, 10), (mx, my)):
                                   selectRect4 = True
                              elif inRect((xSelectStart-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5, 10, 10), (mx, my)):
                                   selectRect5 = True
                              elif inRect((xSelectEnd-5, ySelectStart+(ySelectEnd-ySelectStart)//2-5,10, 10), (mx, my)):
                                   selectRect6 = True
                              elif inRect((xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectStart-5, 10, 10), (mx, my)):
                                   selectRect7 = True
                              elif inRect((xSelectStart+(xSelectEnd-xSelectStart)//2-5, ySelectEnd-5, 10, 10), (mx, my)):
                                   selectRect8 = True
                              elif inRect(selectRect, (mx, my)):
                                          dragRect = True
                         mxO, myO = mx, my #Old mouse position
                         myClock.tick(60) #Runs the clock so time data can be extrapolated
                         if release and not(selectRect1 or selectRect2 or selectRect3 or selectRect4 or selectRect5 or selectRect6 or selectRect7 or selectRect8 or dragRect):
                              if not inRect((selectRect[0]-5, selectRect[1]-5, selectRect[2]+10, selectRect[3]+10), (mx, my)):
                                   toolSelected = False
                                   screen.blit(paintScreen, (width*0.3, 0))
                                   screen.blit(cutArea, (selectRect[0], selectRect[1]))
          #################################################################################################### 
          #################################################################################################### 
                                   
          #Blits the background images onto the screen after draw so draw doesnt appear on the backgrounds
          screen.blit(paintScreenLeft, (0, 0))
          screen.blit(paintScreenBottom, (width*0.3, height*0.7))


          #Button for user to return to the homescreen
          screen.blit(homeButtonUnselected, (width*0.01, height*0.013))
          if inRect((width*0.01, height*0.013, width*0.08, height*0.05), (mx, my)):
               screen.blit(homeButtonSelected, (width*0.01, height*0.013))
               if click:
                    gameScreen = 0
                    continue
          #################################################################################################### 
          ####################################################################################################

               
          #Bar to change size
          screen.blit(sizeBar, (width*0.072, height*0.44))
          draw.rect(screen, WHITE, (width*0.072 + width*0.22*(size/500), height*0.44, width*0.005, height*0.06)) #Rect to show user how large size is
          if click and inRect((width*0.072, height*0.44, width*0.22, height*0.06), (mx, my)):
               size = int(500 * ((mx - width*0.072)/(width*0.22))) #Changes size when user clicks inside of size bar

          #Bar under the size bar that controls aspects of other tools
          #All have the same template as size bar               
          if drawState == "marker": #Changes the opacity of marker and highlighter
               screen.blit(sizeBar, (width*0.072, height*0.51))
               draw.rect(screen, WHITE, (width*0.072 + width*0.22*(transparency/9), height*0.51, width*0.005, height*0.06))
               if click and inRect((width*0.072, height*0.51, width*0.22, height*0.06), (mx, my)):
                    transparency = int(10 * ((mx - width*0.072)/(width*0.22)))
               screen.blit(OpacityTitle, (0, height*0.51))
               
          elif drawState == "pen": #Changes how often bleed occurs and how much bleed there is
               screen.blit(sizeBar, (width*0.072, height*0.51))
               draw.rect(screen, WHITE, (width*0.072 + width*0.22*(penBleed/500), height*0.51, width*0.005, height*0.06))
               if click and inRect((width*0.072, height*0.51, width*0.22, height*0.06), (mx, my)):
                    penBleed = int(500 * ((mx - width*0.072)/(width*0.22)))
               screen.blit(BleedTitle, (0, height*0.51))
               
          elif drawState == "spray": #Density of spray
               screen.blit(sizeBar, (width*0.072, height*0.51))
               draw.rect(screen, WHITE, (width*0.072 + width*0.22*(sprayDensity/2150), height*0.51, width*0.005, height*0.06))
               if click and inRect((width*0.072, height*0.51, width*0.22, height*0.06), (mx, my)):
                    sprayDensity = int(2150 * ((mx - width*0.072)/(width*0.22)))
               screen.blit(DensityTitle, (0, height*0.51))
               
          elif drawState == "pixelate": #How strong pixelate is
               screen.blit(sizeBar, (width*0.072, height*0.51))
               draw.rect(screen, WHITE, (width*0.072 + width*0.22*((pixelateStrength-2)/11), height*0.51, width*0.005, height*0.06))
               if click and inRect((width*0.072, height*0.51, width*0.22, height*0.06), (mx, my)):
                    pixelateStrength = int(12 * ((mx - width*0.072)/(width*0.22)))+2
               screen.blit(PixelTitle, (0, height*0.51))
               
          elif drawState == "shape" and shape != "line": #Whether or not shapes are filled
               screen.blit(filledUnselected, (width*0.03, height*0.51))
               if inRect((width*0.03, height*0.51, width*0.14, height*0.06), (mx, my)):
                    screen.blit(filledSelected, (width*0.03, height*0.51))
                    if click:
                         if fillShape:
                              fillShape = False
                         else:
                              fillShape = True
               if fillShape:
                    screen.blit(YesTitle, (width*0.18, height*0.51))
               else:
                    screen.blit(NoTitle, (width*0.18, height*0.51))

          

          
                    
          #Choosing the different types of lines
          elif drawState == "shape" and shape == "line":
               #Blit images of buttons
               screen.blit(LinesTitle, (width*0.01, height*0.51))
               screen.blit(lineStraight, (width*0.115, height*0.51))
               screen.blit(lineRounded, (width*0.15, height*0.51))
               screen.blit(lineDotted, (width*0.185, height*0.51))
               screen.blit(lineDashedOne, (width*0.22, height*0.51))
               screen.blit(lineDashedTwo, (width*0.255, height*0.51))
               #Code for the buttons to check if mouse in, and changes lineType
               if inRect((width*0.115, height*0.51, width*0.03, height*0.05), (mx, my)):
                    draw.rect(screen, YELLOW, (width*0.115, height*0.51, width*0.03, height*0.06), 3)
                    if click:
                         lineType = "straight"
               elif inRect((width*0.15, height*0.51, width*0.03, height*0.05), (mx, my)):
                    draw.rect(screen, YELLOW, (width*0.15, height*0.51, width*0.03, height*0.06), 3)
                    if click:
                         lineType = "rounded"
               elif inRect((width*0.185, height*0.51, width*0.03, height*0.05), (mx, my)):
                    draw.rect(screen, YELLOW, (width*0.185, height*0.51, width*0.03, height*0.06), 3)
                    if click:
                         lineType = "dotted"
               elif inRect((width*0.22, height*0.51, width*0.03, height*0.05), (mx, my)):
                    draw.rect(screen, YELLOW, (width*0.22, height*0.51, width*0.03, height*0.06), 3)
                    if click:
                         lineType = "dashedOne"
               elif inRect((width*0.255, height*0.51, width*0.03, height*0.05), (mx, my)):
                    draw.rect(screen, YELLOW, (width*0.255, height*0.51, width*0.03, height*0.06), 3)
                    if click:
                         lineType = "dashedTwo"

               #Yellow rect around line button mouse is over
               if lineType == "straight":
                    draw.rect(screen, YELLOW, (width*0.115, height*0.51, width*0.03, height*0.06), 3)
               elif lineType == "rounded":
                    draw.rect(screen, YELLOW, (width*0.15, height*0.51, width*0.03, height*0.06), 3)
               elif lineType == "dotted":
                    draw.rect(screen, YELLOW, (width*0.185, height*0.51, width*0.03, height*0.06), 3)
               elif lineType == "dashedOne":
                    draw.rect(screen, YELLOW, (width*0.22, height*0.51, width*0.03, height*0.06), 3)
               elif lineType == "dashedTwo":
                    draw.rect(screen, YELLOW, (width*0.255, height*0.51, width*0.03, height*0.06), 3)

          #Music volume bar with mute
          draw.line(screen, RED, (width*0.135, height*0.04), (width*0.18, height*0.04), 3)
          draw.rect(screen, RED, (width*0.125, height*0.025, width*0.01, height*0.03), 0)
          draw.rect(screen, RED, (width*0.18, height*0.025, width*0.01, height*0.03), 0)
          draw.rect(screen, WHITE, (width*0.125+width*0.05*volume, height*0.025, width*0.01, height*0.03), 0)
          screen.blit(soundButton, (width*0.097, height*0.024))
          if leftHold and inRect((width*0.135, height*0.025, width*0.05, height*0.03), (mx, my)):
               volume = (mx-width*0.135)/(width*0.05)
               mixer.music.set_volume(volume)
          if click and inRect((width*0.097, height*0.024, width*0.02, height*0.03), (mx, my)) and volume!=0:
               volume = 0
               mixer.music.set_volume(0)
          if volume == 0:
               draw.line(screen, RED, (width*0.097, height*0.024), (width*0.117, height*0.054), 2)
               draw.line(screen, RED, (width*0.097, height*0.054), (width*0.117, height*0.024), 2)
          
          #################################################################################################### 
          #################################################################################################### 
          
          #COLOUR SELECTION INCLUDING RAINBOW AND DROPPER
          screen.blit(colourUnselected, (width*0.03, height*0.755))
          if inRect((width*0.03, height*0.755, width*0.2, height*0.09), (mx, my)): 
               screen.blit(colourSelected, (width*0.03, height*0.755))
               if release: #Checks if mouse is released so colour choice prompt stays infront of screen
                    colTest = None #Var to see if user picked a colour
                    #Checks which colour is selected, to change colour one or two
                    if colourSelect == 1:
                         colTest = askcolor()[0] #colTest has rgb and hexa value, so only take first rgb value
                         #if colTest checks if colTest has a value, else itll stay as it was
                         if colTest: 
                              colourOne = colTest
                              colOneRainbow = False
                    elif colourSelect == 2:
                         colTest = askcolor()[0]
                         if colTest:
                              colourTwo = colTest
                              colTwoRainbow = False
          #Draws box to display colour which is chosen
          draw.rect(screen, colourOne, (width*0.04, height*0.87, width*0.07, height*0.1), 0)
          draw.rect(screen, YELLOW, (width*0.04, height*0.87, width*0.07, height*0.1), 2)
          draw.rect(screen, colourTwo, (width*0.19, height*0.87, width*0.07, height*0.1), 0)
          draw.rect(screen, YELLOW, (width*0.19, height*0.87, width*0.07, height*0.1), 2)

          screen.blit(whiteHeartCol, (width*0.05, height*0.88)) #0.05 0.08
          screen.blit(whiteHeartCol, (width*0.2, height*0.88))
          draw.rect(screen, YELLOW, (width*0.05, height*0.88, width*0.05, height*0.08), 2)
          draw.rect(screen, YELLOW, (width*0.2, height*0.88, width*0.05, height*0.08), 2)     

          #Allows user to change which colour is selected
          if inRect((width*0.04, height*0.87, width*0.07, height*0.1), (mx, my)) and click:
               colourSelect = 1
          if inRect((width*0.19, height*0.87, width*0.07, height*0.1), (mx, my)) and click:
               colourSelect = 2
          if colourSelect == 1:
               draw.rect(screen, ORANGE, (width*0.04, height*0.87, width*0.07, height*0.1), 4)
          else:
               draw.rect(screen, ORANGE, (width*0.19, height*0.87, width*0.07, height*0.1), 4)
          #Blitting images for rainbow and dropper buttons
          screen.blit(dropperUnselected, (width*0.24, height*0.755))
          screen.blit(rainbowUnselected, (width*0.24, height*0.805))
          #Dropper and rainbow buttons next to colour choosing colour
          if inRect((width*0.24, height*0.755, width*0.03, height*0.04), (mx, my)):
               screen.blit(dropperSelected, (width*0.24, height*0.755))
               if click:
                    drawState = "dropper"
          elif inRect((width*0.24, height*0.805, width*0.03, height*0.04), (mx, my)):
               screen.blit(rainbowSelected, (width*0.24, height*0.805))
               if click:
                    if colourSelect == 1:
                         colOneRainbow = True
                    if colourSelect == 2:
                         colTwoRainbow = True
          #Creates the rainbow colour, and sets chosen colour to be equal to rainbow
          #Red starts at 255, and as it goes down, green goes up. Once red reaches 0,
          #Green starts to go down, red stops, and blue goes up. This continues to cycle
          #around, even if nothing is being drawn.
          if colOneRainbow or colTwoRainbow:
               rainbowR+=rainbowRRate
               rainbowG+=rainbowGRate
               rainbowB+=rainbowBRate
               if rainbowR<0:
                    rainbowRRate = 0
                    rainbowGRate = -rainbowRate
                    rainbowBRate = rainbowRate
                    rainbowR = 0
                    rainbowG = 255
               if rainbowG<0:
                    rainbowGRate = 0
                    rainbowBRate = -rainbowRate
                    rainbowRRate = rainbowRate
                    rainbowG = 0
                    rainbowB = 255
               if rainbowB<0:
                    rainbowBRate = 0
                    rainbowRRate = -rainbowRate
                    rainbowGRate = rainbowRate
                    rainbowB = 0
                    rainbowR = 255
               if colOneRainbow:
                    colourOne = (rainbowR, rainbowG, rainbowB)
               if colTwoRainbow:
                    colourTwo = (rainbowR, rainbowG, rainbowB)
                    
          if drawState == "dropper" and inRect(canvasRect, (mx, my)): #Gets colour at certain position on the screen
               #Only changes colour which is selected
               if colourSelect == 1:
                    colourOne = screen.get_at((mx, my))
                    colOneRainbow = False
               elif colourSelect == 2:
                    colourTwo = screen.get_at((mx, my))
                    colTwoRainbow = False
               if release: #Changes tool to default pencil when colour is picked
                    drawState = "pencil"
                    dropperUsed = True
          
                    
               
          

          #Buttons for selecting shapes
          screen.blit(shapeButtonUnselected, (width*0.01, height*0.35))
          if drawState == "shape": 
               draw.rect(screen, BLACK, (width*0.1, height*0.351, width*0.195, height*0.078), 0) #Opens up shape choosing menu
               if inRect((width*0.281, height*0.35, width*0.015, height*0.08), (mx, my)):
                    screen.blit(openNextPageWhite, (width*0.281, height*0.35))
                    if click:
                         shapePage+=1
               else:
                    screen.blit(openNextPageGray, (width*0.281, height*0.35))
               draw.rect(screen, ORANGE, (width*0.1, height*0.351, width*0.195, height*0.078), 3)
               if shapePage%2 == 0:
                    shapeButton(screen, (width*0.125, height*0.363, width*0.04, height*0.05), "rectangle", rectButtonUnselected, rectButtonSelected, (mx, my), click)
                    shapeButton(screen, (width*0.175, height*0.363, width*0.04, height*0.05), "triangle", triangleButtonUnselected, triangleButtonSelected, (mx, my), click)
                    shapeButton(screen, (width*0.225, height*0.363, width*0.04, height*0.05), "ellipse", ellipseButtonUnselected, ellipseButtonSelected, (mx, my), click)
               elif shapePage%2 == 1:
                    shapeButton(screen, (width*0.125, height*0.363, width*0.04, height*0.05), "line", lineButtonUnselected, lineButtonSelected, (mx, my), click)
                    shapeButton(screen, (width*0.175, height*0.363, width*0.04, height*0.05), "hexagon", arcButtonUnselected, arcButtonSelected, (mx, my), click)
                    shapeButton(screen, (width*0.225, height*0.363, width*0.04, height*0.05), "polygon", polygonButtonUnselected, polygonButtonSelected, (mx, my), click)
          if inRect((width*0.01, height*0.35, width*0.11, height*0.08), (mx, my)) and drawState != "shape":
               screen.blit(shapeButtonUnselected, (width*0.01, height*0.35))
               if click:
                    drawState = "shape"
          elif inRect((width*0.01, height*0.35, width*0.11, height*0.08), (mx, my)) and drawState == "shape":
               screen.blit(shapeButtonSelected, (width*0.01, height*0.35))
               if click:
                    drawState = "pencil" #Changes tool to default pencil when you change away from shape
          elif drawState == "shape":
               screen.blit(shapeButtonUnselected, (width*0.01, height*0.35))


          #STAMP SELECTION
          if inRect((width*0.32, height*0.72, width*0.16, height*0.09), (mx, my)) and click:
               if drawState == "stamp": #If user unselects filter, tool switches to default pencil
                    drawState = "pencil"
               else:
                    drawState = "stamp"
          if drawState == "stamp":
               if inRect((width*0.32, height*0.94, width*0.16, height*0.04), (mx, my)):
                    screen.blit(pageDownWhite, (width*0.32, height*0.94))
                    if click:
                         stampPage+=1
                         stampPage%=(len(stampList)//2)
               else:
                    screen.blit(pageDownGray, (width*0.32, height*0.94))
               #Takes image from list so multiple lines for each page arent needed. Easier to customize
               stampButton(screen, (width*0.323, height*0.82, width*0.075, height*0.1), stampList[stampPage*2], (mx, my), click)
               stampButton(screen, (width*0.402, height*0.82, width*0.075, height*0.1), stampList[stampPage*2+1], (mx, my), click)
               draw.rect(screen, ORANGE, (width*0.32, height*0.72, width*0.16, height*0.26), 4)
          #Blits filter button depending on whether mouse is over the button
          if drawState != "stamp" or inRect((width*0.32, height*0.72, width*0.16, height*0.09), (mx, my)):
               screen.blit(stampsSelected, (width*0.32, height*0.72))
          else:
               screen.blit(stampsUnselected, (width*0.32, height*0.72))


          #BACKGROUND SELECTION
          if inRect((width*0.52, height*0.72, width*0.16, height*0.09), (mx, my)) and click:
               if drawState == "scene": #If user unselects filter, tool switches to default pencil
                    drawState = "pencil"
               else:
                    drawState = "scene"
          if drawState == "scene":
               if inRect((width*0.52, height*0.94, width*0.16, height*0.04), (mx, my)):
                    screen.blit(pageDownWhite, (width*0.52, height*0.94))
                    if click:
                         scenePage+=1
                         scenePage%=(len(sceneList)//2)
               else:
                    screen.blit(pageDownGray, (width*0.52, height*0.94))
               #Takes image from list so multiple lines for each page arent needed. Easier to customize
               sceneButton(screen, (width*0.523, height*0.82, width*0.075, height*0.1), sceneList[scenePage*2], (mx, my), release, width, height, scenePage*2)
               sceneButton(screen, (width*0.602, height*0.82, width*0.075, height*0.1), sceneList[scenePage*2+1], (mx, my), release, width, height, scenePage*2+1)
               draw.rect(screen, ORANGE, (width*0.52, height*0.72, width*0.16, height*0.26), 4)
          #Blits filter button depending on whether mouse is over the button
          if drawState != "scene" or inRect((width*0.52, height*0.72, width*0.16, height*0.09), (mx, my)):
               screen.blit(sceneSelected, (width*0.52, height*0.72))
          else:
               screen.blit(sceneUnselected, (width*0.52, height*0.72))


          #FILTER SELECTION
          if inRect((width*0.72, height*0.72, width*0.16, height*0.09), (mx, my)) and click:
               if drawState == "filter": #If user unselects filter, tool switches to default pencil
                    drawState = "pencil"
               else:
                    drawState = "filter"
          if drawState == "filter":
               if inRect((width*0.72, height*0.94, width*0.16, height*0.04), (mx, my)):
                    screen.blit(pageDownWhite, (width*0.72, height*0.94)) #Button to switch the page
                    if click:
                         filterPage+=1
               else:
                    screen.blit(pageDownGray, (width*0.72, height*0.94))    
               if filterPage%3 == 0: #No back button needed since modulo is used.
                    filterButton(screen, (width*0.72, height*0.82, width*0.075, height*0.1), (235, 235, 160), (mx, my), release, width, height, filterFormulae[0])
                    filterButton(screen, (width*0.804, height*0.82, width*0.075, height*0.1), (50, 50, 50), (mx, my), release, width, height, filterFormulae[1])
               elif filterPage%3 == 1:
                    filterButton(screen, (width*0.72, height*0.82, width*0.075, height*0.1), (100, 0, 0), (mx, my), release, width, height, filterFormulae[2])
                    filterButton(screen, (width*0.804, height*0.82, width*0.075, height*0.1), (100, 200, 0), (mx, my), release, width, height, filterFormulae[3])
               elif filterPage%3 == 2:
                    filterButton(screen, (width*0.72, height*0.82, width*0.075, height*0.1), (100, 100, 100), (mx, my), release, width, height, filterFormulae[4])
                    filterButton(screen, (width*0.804, height*0.82, width*0.075, height*0.1), (255, 255, 255), (mx, my), release, width, height, filterFormulae[5])
               draw.rect(screen, ORANGE, (width*0.72, height*0.72, width*0.16, height*0.26), 4)
          #Blits filter button depending on whether mouse is over the button
          if drawState != "filter" or inRect((width*0.72, height*0.72, width*0.16, height*0.09), (mx, my)):
               screen.blit(filtersUnselected, (width*0.72, height*0.72))
          else:
               screen.blit(filtersSelected, (width*0.72, height*0.72))

          
          #Buttons which allow user to choose a shape. Function description is above the game loop
          toolButton(screen, (width*0.03, height*0.1, width*0.1, height*0.05), "pencil", toolPencilButtonUnselected, toolPencilButtonSelected, heartSelect, (mx, my), click, width, height)
          toolButton(screen, (width*0.18, height*0.1, width*0.1, height*0.05), "eraser", toolEraserButtonUnselected, toolEraserButtonSelected, heartSelect, (mx, my), click, width, height)
          toolButton(screen, (width*0.03, height*0.16, width*0.1, height*0.05), "spray", toolSprayButtonUnselected, toolSprayButtonSelected, heartSelect, (mx, my), click, width, height)
          toolButton(screen, (width*0.18, height*0.16, width*0.1, height*0.05), "pen", toolPenButtonUnselected, toolPenButtonSelected, heartSelect, (mx, my), click, width, height)
          toolButton(screen, (width*0.03, height*0.22, width*0.1, height*0.05), "marker", toolMarkerButtonUnselected, toolMarkerButtonSelected, heartSelect, (mx, my), click, width, height)
          toolButton(screen, (width*0.18, height*0.22, width*0.1, height*0.05), "fill", toolFillButtonUnselected, toolFillButtonSelected, heartSelect, (mx, my), click, width, height)
          toolButton(screen, (width*0.03, height*0.28, width*0.1, height*0.05), "pixelate", toolPixelateButtonUnselected, toolPixelateButtonSelected, heartSelect, (mx, my), click, width, height)
          toolButton(screen, (width*0.18, height*0.28, width*0.1, height*0.05), "cut", toolBlurButtonUnselected, toolBlurButtonSelected, heartSelect, (mx, my), click, width, height)
          toolButton(screen, (width*0.12, height*0.6, width*0.06, height*0.05), "text", textButton, textButton, heartSelect,  (mx, my), click, width, height)
          
          #Bold and italicize
          #Regular buttons for selecting whether text will be bolded/italicized or not
          screen.blit(boldUnselected, (width*0.26, height*0.65)) 
          screen.blit(italicsUnselected, (width*0.26, height*0.7))
          if inRect((width*0.26, height*0.65, width*0.03, height*0.04), (mx, my)):
               screen.blit(boldSelected, (width*0.26, height*0.65))
               if click:
                    if bolded:
                         bolded = False
                    else:
                         bolded = True
          elif inRect((width*0.2601, height*0.7, width*0.03, height*0.04), (mx, my)):
               screen.blit(italicsSelected, (width*0.26, height*0.7))
               if click:
                    if italics:
                         italics = False
                    else:
                         italics = True
          #Shows user whether bold or italics are activated
          if bolded:
               screen.blit(boldSelected, (width*0.26, height*0.65))
          if italics:
               screen.blit(italicsSelected, (width*0.26, height*0.7))
          #Choosing different fonts
          screen.blit(fontsTitle, (width*0.01, height*0.665)) #fontButtonsList
          screen.blit(fontButtonsList[fontNumber%5], (width*0.1, height*0.665))
          if inRect((width*0.1, height*0.665, width*0.09, height*0.06), (mx, my)) and click:
               fontNumber+=1

          
          #Clear Screen Button
          #User will have to hold so they don't accidently clear the screen
          draw.rect(screen, RED, (width*0.2, height*0.01, width*0.08, height*0.06), 5)
          screen.blit(clearButton, (width*0.2, height*0.01))
          if leftHold and inRect((width*0.2, height*0.01, width*0.08, height*0.06), (mx, my)):
               clearCharge+=4 #Rate at which clear button works
               clearSurface = Surface((width*0.08, height*0.06), SRCALPHA) #Fades into white as held
               draw.rect(clearSurface, (255, 255, 255, 255*(clearCharge/100)), (0, 0, width*0.08, height*0.06), 0)
               screen.blit(clearSurface, (width*0.2, height*0.01))
               if clearCharge >= 100:
                    clearCharge = 0
                    canvasClear(screen, width, height) #Clears canvas
                    undoList.append(screen.subsurface(canvasRect).copy()) #Appends this white screen to the canvas
                    redoList = [] #Action has been performed, therefore redo must be emptied
          else:
               clearCharge = 0 #Clear stops charging if mouse is released or moved away
          

          #This section will include undo/redo, save, open
          screen.blit(undoUnselected, (width*0.893, height*0.73))
          screen.blit(redoUnselected, (width*0.947, height*0.73))
          if inRect((width*0.893, height*0.73, width*0.04, height*0.07), (mx, my)):
               screen.blit(undoSelected, (width*0.893, height*0.73))
               if click:
                    try:
                         redoList.append(undoList[-1])
                         del(undoList[-1])
                         screen.blit(undoList[-1], (width*0.3, 0))
                    except:
                         canvasClear(screen, width, height)
          elif inRect((width*0.947, height*0.73, width*0.04, height*0.07), (mx, my)):
               screen.blit(redoSelected, (width*0.947, height*0.73))
               if click:
                    try:
                         screen.blit(redoList[-1], (width*0.3, 0)) #Blits last item in redo onto canvas
                         undoList.append(redoList[-1]) #Appends this to undo
                         del(redoList[-1]) #Removes this item from redo
                    except:
                         pass

          #SAVE AND OPEN FUNCTIONS
          screen.blit(saveUnselected, (width*0.893, height*0.81))
          screen.blit(openUnselected, (width*0.893, height*0.89))
          #SAVE
          if inRect((width*0.893, height*0.81, width*0.094, height*0.07), (mx, my)):
               screen.blit(saveSelected, (width*0.893, height*0.81))
               if click:
                    try: #Try statement to prevent crashing from improper file or other difficulties with files
                         fname=filedialog.asksaveasfilename(defaultextension=".png")
                         image.save(screen.subsurface(canvasRect),fname)
                         saved = True
                    except:
                         pass
          #OPEN
          elif inRect((width*0.893, height*0.89, width*0.094, height*0.07), (mx, my)):
               screen.blit(openSelected, (width*0.893, height*0.89))
               if click:
                    try: #Try statement to prevent crashing from improper file or other difficulties with files
                         fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpg;*.jpeg;*.bmp")]) #Supported file types
                         openedImg = transform.scale(image.load(fname), (int(width*0.7), int(height*0.7))) #Resizes image to canvas size
                         screen.blit(openedImg, (width*0.3, 0)) #Blits image to canvas
                    except:
                         pass


          #APPENDING TO UNDO LIST
          if (drawState != "text" and release)and not(drawState == "shape" and shape == "polygon"): #Release and not having to copies of polygon
               #Checking if clicking filters and backgrounds
               if inRect(canvasRect, (mx, my)) or inRect((width*0.804, height*0.82, width*0.075, height*0.1), (mx, my)) or inRect((width*0.72, height*0.82, width*0.075, height*0.1), (mx, my)) or inRect((width*0.602, height*0.82, width*0.075, height*0.1), (mx, my)) or inRect((width*0.523, height*0.82, width*0.075, height*0.1), (mx, my)):
                    #Checking if release is not just stamp rotation or dropper
                    if (not rightClick or drawState != "stamp") and not dropperUsed and not helping:
                         #Saves an image of the canvas every time user releases the mouse
                         undoList.append(screen.subsurface(canvasRect).copy())
                         redoList = [] #Clear redo list
                         textScreen = screen.subsurface(canvasRect).copy()
                         currentText = ""
                         saved = False #Action has been made and program will now prompt user to save before quitting
                         textScreen = screen.subsurface(canvasRect).copy()
          #################################################################################################### 
          ####################################################################################################
          #HELP STATEMENTS TO ASSIST USER WITH TOOL INFORMATION
          if key.get_pressed()[K_h] and not hRelease:
               helping = True #Help screen popping up, therefore helping is True
                  
               if inRect((width*0.52, height*0.72, width*0.16, height*0.09), (mx, my)): #Background Help
                    screen.blit(helpList[0], (width*0.35, height*0.2)) #Blits help
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5) #Draws black border around help

               elif inRect((width*0.2, height*0.01, width*0.08, height*0.06), (mx, my)): #Clear button Help
                    screen.blit(helpList[1], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.03, height*0.755, width*0.2, height*0.09), (mx, my)): #Colour Choosing Help
                    screen.blit(helpList[2], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.18, height*0.28, width*0.1, height*0.05), (mx, my)): #Cut tool Help
                    screen.blit(helpList[3], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5) 

               elif inRect((width*0.24, height*0.755, width*0.03, height*0.04), (mx, my)): #Dropper Help
                    screen.blit(helpList[4], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)



               elif inRect((width*0.18, height*0.1, width*0.1, height*0.05), (mx, my)): #Eraser Help
                    screen.blit(helpList[6], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.18, height*0.22, width*0.1, height*0.05), (mx, my)): #Fill Help
                    screen.blit(helpList[7], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.72, height*0.72, width*0.16, height*0.09), (mx, my)): #Filters Help
                    screen.blit(helpList[8], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)





               elif inRect((width*0.03, height*0.22, width*0.1, height*0.05), (mx, my)): #Marker Help
                    screen.blit(helpList[11], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.893, height*0.89, width*0.094, height*0.07), (mx, my)): #Open Help
                    screen.blit(helpList[12], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.03, height*0.1, width*0.1, height*0.05), (mx, my)):#Pencil Help
                    screen.blit(helpList[13], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.18, height*0.16, width*0.1, height*0.05), (mx, my)): #Pen Help
                    screen.blit(helpList[14], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.03, height*0.28, width*0.1, height*0.05), (mx, my)): #Pixelate Help
                    screen.blit(helpList[15], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)



               elif inRect((width*0.24, height*0.805, width*0.03, height*0.04), (mx, my)): #Rainbow Help
                    screen.blit(helpList[17], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)



               elif inRect((width*0.947, height*0.73, width*0.04, height*0.07), (mx, my)): #Redo Help
                    screen.blit(helpList[19], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.893, height*0.81, width*0.094, height*0.07), (mx, my)): #Save Help
                    screen.blit(helpList[20], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.01, height*0.35, width*0.11, height*0.08), (mx, my)): #Shapes Help
                    screen.blit(helpList[21], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.072, height*0.44, width*0.22, height*0.06), (mx, my)): #Size Help
                    screen.blit(helpList[22], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.03, height*0.16, width*0.1, height*0.05), (mx, my)): #Spray Help
                    screen.blit(helpList[23], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.32, height*0.72, width*0.16, height*0.09), (mx, my)): #Stamps Help
                    screen.blit(helpList[24], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               elif inRect((width*0.12, height*0.6, width*0.06, height*0.05), (mx, my)): #Text Help
                    screen.blit(helpList[25], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)



               elif inRect((width*0.893, height*0.73, width*0.04, height*0.07), (mx, my)): #Undo Help
                    screen.blit(helpList[27], (width*0.35, height*0.2))
                    draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

               if drawState == "shape":
                    if shapePage%2 == 0:
                         
                         if inRect((width*0.125, height*0.363, width*0.04, height*0.05), (mx, my)): #Rectangle Help
                              screen.blit(helpList[18], (width*0.35, height*0.2))
                              draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)
                              
                         elif inRect((width*0.175, height*0.363, width*0.04, height*0.05), (mx, my)): #Triangle Help
                              screen.blit(helpList[26], (width*0.35, height*0.2))
                              draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

                         elif inRect((width*0.225, height*0.363, width*0.04, height*0.05), (mx, my)): #Ellipse Help
                              screen.blit(helpList[5], (width*0.35, height*0.2))
                              draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)
                         
                    else:
                         if inRect((width*0.225, height*0.363, width*0.04, height*0.05), (mx, my)): #Polygon Help
                              screen.blit(helpList[16], (width*0.35, height*0.2))
                              draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)
                              
                         elif inRect((width*0.175, height*0.363, width*0.04, height*0.05), (mx, my)): #Hexagon Help
                              screen.blit(helpList[9], (width*0.35, height*0.2))
                              draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)

                         elif inRect((width*0.125, height*0.363, width*0.04, height*0.05), (mx, my)): #Line Help
                              screen.blit(helpList[10], (width*0.35, height*0.2))
                              draw.rect(screen, BLACK, (width*0.35, height*0.2, width*0.4, height*0.3), 5)


          else:
               helping = False
               
          if hRelease: #When finished helping, blits canavs before help on top so help prompt disappears
               try:
                    screen.blit(undoList[-1], (width*0.3, 0))
               except:
                    canvasClear(screen, width, height)

          
                    
          #################################################################################################### 
          ####################################################################################################
                    
     elif gameScreen == 0: # The home screen

          screen.blit(homeScreen, (0,0)) #Background of the homescreen

          #Button to start paint
          screen.blit(paintButtonUnselected, (width*0.45, height*0.4))
          if inRect((width*0.45, height*0.4, width*0.1, height*0.05), (mx, my)):
               screen.blit(paintButtonSelected, (width*0.45, height*0.4))
               if release:
                    canvasClear(screen, width, height)
                    gameScreen = 1
                    continue



          #################################################################################################### 
          ####################################################################################################
    


     
     
     draw.rect(screen, BLACK, (0, 0, width, height), 1) #Creates a border around the screen to prevent 1 pixel white border on the outside
     
     display.flip() #Updates display
     mxO, myO = mx, my #Sets mxO, myO to be mouse position in previous frame
     myClock.tick(60) #Runs the clock so time data can be extrapolated
               
quit()

          
















