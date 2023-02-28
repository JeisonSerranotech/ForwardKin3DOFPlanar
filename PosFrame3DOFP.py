import numpy as np
import math

def position(val1,val2,val3):
 #Definicion de constantes
 L1= float (25) #mm de distancia del primer link
 L2= float (50)#mm de distancia del segundo link
 L3= float (110.38) #mm de distancia del tercer link

 #Definicion de variables

 def cg(number):
  return (math.pi * number) / 180

 ThetaA=val1# en Degrees
 ThetaB=val2 # en Degrees
 ThetaC=val3 # en Degrees

 Theta1= cg(ThetaA) # Grados Rad
 Theta2= cg(ThetaB) # Grados Rad
 Theta3= cg(ThetaC) # Rad

 # Definicion de la funcion


 # Calculos

 A_1=L3*math.cos(Theta3)+L2
 A_2=L3*math.sin(Theta3)*-1*math.sin(Theta2)
 A_3=L3*math.sin(Theta3)*math.cos(Theta2)
 print(A_1*math.cos(Theta2)+A_2+L1)
 B=(A_1*math.cos(Theta2)+A_2+L1)*math.cos(Theta1)
 C=(A_1*math.sin(Theta2)+A_3)*-1*math.sin(Theta1)
 D=(A_1*math.cos(Theta2)+A_2+L1)*math.sin(Theta1)
 E=(A_1*math.sin(Theta2)+A_3)*math.cos(Theta1)
 P_base=np.array([[B+C],[E+D],[0],[1]])
 print(P_base)

 #Create the txt fyle




 file=open('3DOFPlanar.txt','w')
 if ThetaA >= 0:
  file.write('ThetaA=' + str(ThetaA))
 elif ThetaA<0:
  file.write('\nThetaA='+ str(360+ThetaA))

 if ThetaB>0:
  file.write('\nThetaB=' + str(360-ThetaB))
 else:
  file.write('\nThetaB='+str(-1*ThetaB))
 if ThetaC>0:
   file.write('\nThetaC=' + str(ThetaC))
 elif ThetaC<=0:
   file.write('\nThetaB=' + str(360 - ThetaB))

 file.write("\nL1="+str(L1))
 file.write("\nL2="+str(L2))
 file.write("\nL3="+str(L3))



 file.close()
 return P_base