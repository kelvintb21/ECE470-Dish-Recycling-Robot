# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:12:12 2020

@author: surface
"""
#stuff defined outside the infinite loop
#Define target speed, target space and PID coeeficient here. 
#These wil be optimized to proper value during simulation

target_speed = 20
target_space = 20
p0=2000
Kp0=100
Ki0=1/100
Kd0=5

Kp1=100
Ki1=1/100
Kd1=5
#initial integral(test)
I = 0
presentspeedcollect=[]
presentspacecollect=[]
Pcollect=[]
Icollect=[]
Dcollect=[]
PIDcollect=[]
error_speed_collect=[]
error_space_collect=[]
i = 0

#speed sensor
def SpeedSensor():
    present_speed=25
    return present_speed
presentspeedcollect.append(SpeedSensor())
present_speed=presentspeedcollect[i]

#Space sensor
def SpaceSensor():
    presentdis1=25#Front space
    presentdis2=25#Behind Space
    presentdis3=25#left space
    presentdis4=25#Right Space
    Present_space = [presentdis1,presentdis2,presentdis3,presentdis4]
    return Present_space
presentspacecollect.append(SpaceSensor())
present_space=presentspacecollect[i]

#Error Function
def Error_speed_Function(target_speed,presentspeed):
    error_speed=(target_speed-presentspeed)
    return error_speed

def Error_space_Function(target_spacing,presentspace):
    error_space=[target_space-presentspace[0],target_space-presentspace[1],target_space-presentspace[2],target_space-presentspace[3]]
    return error_space

#Collecting error in  a list
error_speed_collect.append(Error_speed_Function(target_speed,present_speed))
error_speed=error_speed_collect[i]

error_space_collect.append(Error_space_Function(target_space,present_space))
error_space=error_space_collect[i]

def DefineP(Kp0,Kp1,p0,error_speed,error_space):
   
    P=(Kp0*error_speed+Kp1*error_space[0]+Kp1*error_space[1])/3+p0
    #proportional clamp(not really needed,i put it just in case we set a too high proportional coefficient)
    #Define Proportioanl Limit, will be changed and optimized during simulation
    if P<500:
        P=500
        print("Maximum Speed achieved" )
    elif P>20000:
        P=20000
        print("Minimum Speed achieved")
    return P
 
#Collecting the proportional in a list
Pcollect.append(DefineP(Kp0,Kp1,p0,error_speed,error_space))
P=Pcollect[i]


#The integral
        
def DefineI(Ki0,Ki1,I,error_speed,error_space):
    # Define Integral limits
    if I<-1500:
        print("Integrator shutdown")
        I=0
    elif I>20000:
        print("Integrator shutdown")
        I=20000
    else:
        I=I+(error_speed*Ki0+error_space[0]*Ki1+error_space[1]*Ki1)/3 #This is what the integral actually looks like after integrating as it is from 0 to t.
    return I

Icollect.append(DefineI(Ki0,Ki1,I,error_speed,error_space))
I=Icollect[i]


#The derivative
prevspeed=presentspeedcollect[i-1]
prevspace=presentspacecollect[i-1]

def DefineD(presentspeed,presentspace,prevspeed,prevspace):
    D=(error_speed_collect[i]-error_speed_collect[i-1])*Kd0+(error_space_collect[i][0]-error_space_collect[i-1][0]+error_space_collect[i][1]-error_space_collect[i-1][1])/2*Kd1    
    return D

Dcollect.append(DefineD(present_speed,present_space,prevspeed,prevspace))
D=Dcollect[i]

#PID function

def PID(P,I,D):
    PID=P+I-D
    #Deine PID LIMIT
    if PID<500:
        PID=500
    if PID>20000:
        PID=20000
    return PID
PIDcollect.append(PID(P,I,D))
PID=PIDcollect[i]
print(PID)

#i ended up clamping saturation in all of them so not just on the integrator

i=i+1

