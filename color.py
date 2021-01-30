import cv2 
import numpy as np
from imageen import Imagen
redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)
redBajo2=np.array([175, 100, 20], np.uint8)
redAlto2=np.array([179, 255, 255], np.uint8)
azulBajo = np.array([100,100,20], np.uint8)
azulAlto = np.array([125,255,255], np.uint8)
amarilloBajo = np.array([15,100,20],np.uint8)
amarilloAlto = np.array([45,255,255],np.uint8)
verdeBajo = np.array([45,100,20],np.uint8)
verdeAlto = np.array([75,255,255],np.uint8)
violetaBajo = np.array([130,100,20],np.uint8)
violetaAlto = np.array([140,255,255],np.uint8)  
class Color:
   def __init__(self, nameBase,nameNoBase ,tipoForma):
     self.nameBase = nameBase 
     self.nameNoBase = nameNoBase 
     self.tipoForma = tipoForma    
   def colores(self):
     listaColores=[] 
     imaBase=cv2.imread(self.nameBase) 
     Base=Imagen(imaBase,"base",self.tipoForma,0,"",0)
     cv2.imshow("Base.jpg", imaBase )
     cv2.waitKey(0)
     cv2.destroyAllWindows()   
     Base.add()
     perimetro1=Base.perimetro
     image = cv2.imread(self.nameNoBase)       
     frameHSV = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)
     maskRed1 = cv2.inRange(frameHSV , redBajo1, redAlto1)
     maskRed2 = cv2.inRange(frameHSV , redBajo2, redAlto2)
     red = cv2.add(maskRed1, maskRed2)
     purple= cv2.inRange(frameHSV , violetaBajo, violetaAlto)
     blue=cv2.inRange(frameHSV , azulBajo, azulAlto)
     yelow=cv2.inRange(frameHSV , amarilloBajo, amarilloAlto)
     green=cv2.inRange(frameHSV , verdeBajo, verdeAlto)
     cv2.imshow("noBase.jpg",image)
     cv2.waitKey(0)
     cv2.destroyAllWindows()   
     listaColores.append(red)
     listaColores.append(purple)
     listaColores.append(blue)
     listaColores.append(yelow)
     listaColores.append(green)
     for colore in listaColores:
        if red is colore:            
           listaRed=Imagen(red,'no base',self.tipoForma,perimetro1, 'rojo',0) 
           listaRed.add()
        if purple is colore:
          listaPurple=Imagen(purple,'no base',self.tipoForma,perimetro1,'violeta',0) 
          listaPurple.add()       
        if blue is colore:
          listaBlue=Imagen(blue,'no base',self.tipoForma,perimetro1,'azul',0) 
          listaBlue.add()
        if yelow is colore:
          listaYelow=Imagen(yelow,'no base',self.tipoForma,perimetro1,'amarillo',0)
          listaYelow.add()
        if green is colore:
          listaGreen=Imagen(green,'no base',self.tipoForma,perimetro1,'verde',0)
          listaGreen.add()
        



       
