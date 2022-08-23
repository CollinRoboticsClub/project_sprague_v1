from constants import schedule_consts
from util.ezmath import clamp

infinity = float("inf")

class PIDController:
    iErr = 0
    lastError = 0

    def __init__(self, kP=1.0, kI=0.0, kD=0.0, minOutput = infinity, maxOutput=-infinity, iZone=0, dt=schedule_consts.dt):
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.minOutput = minOutput
        self.maxOutput = maxOutput
        self.iZone = iZone
        self.dt = dt
    
    def calculate(self, setpoint: float, processVariable: float):
        error = setpoint - processVariable

        # integrate error
        self.iErr += error
        # apply iZone
        iTerm = (self.kI * self.iErr * self.dt) if (abs(error) < self.iZone) else 0


        # calculate dErr
        dErr = error - self.lastError
        self.lastError = error


        # output
        output = (self.kP * error
                + iTerm
                + self.kD * dErr / self.dt)
            
        # clamp between min and max
        output = clamp(output, self.minOutput, self.maxOutput)

        return output
    