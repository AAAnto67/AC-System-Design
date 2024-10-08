#VER 1:
#Known Values
    MachNum = 0.77
    ByPassRatio = 6
    CruiseSpeed = 228.3
    NumEngines = 2
    LandingLength = 1210
    TakeoffLength = 1296
    CVClimbGradient = 0.024

#Mass Ratios:
    MassRatio = 0.95
    MassRatioLanding = 0.845

#Variables that have been set as an example, but are not real!!
    ClCruise = 0.65
    ClClimb = 1.2
    ClTakeoff = 2.1
    Clfl = 0.6
    ClMax = 2.5
    Cd0 = 0.02
    #Mass Ratio is Beta
    AspectRatio = 9
    OswaldFactor = 0.8
    StallSpeed = 70
    LandingAltitude = 1600
    LandingDensity = 1.04759
    RateOfClimb = 15
    Kt = 0.85

#Less important constants
    SeaLevelTemperature = 288.15
    #Cruise Altitude: FL35000
    TemperatureAtCruise = 218.81
    PressureAtCruise = 23835.918
    DensityAtCruise = 0.3796
    #Climb Rate Altitude: 7400
    PressureAtClimb = 38800
    TemperatureAtClimb = 240
    DensityAtClimb = 0.563
    #Climb Gradient Altitude:1600m
    PressureAtClimbGrad = 83523.5
    TemperatureAtClimbGrad = 240
    DensityAtClimbGrad = 0.563

    #Climb Grad Requirements taken from CS-25 Certification Specifications * a safety factor (1.5)
    Cl25119 = 1.27
    Cd25119 = 0.059
    Oswald25119 = 0.868
    ClimbReq25119 = 0.038
    Cl25121a = 1.01
    Cd25121a = 0.0395
    Oswald25121a = 0.829
    ClimbReq25121a = 0.045
    Cl25121b = 1.013
    Cd25121b = 0.0395
    Oswald25121b = 0.829
    ClimbReq25121b = 0.036
    Cl25121c = 0.704
    Cd25121c = 0.02
    Oswald25121c = 0.79
    ClimbReq25121c = 0.018
    Cl25121d = 1.268
    Cd25121d = 0.059
    Oswald25121d = 0.829
    ClimbReq25121d = 0.0315
    
    CS25SafetyMargin = 1.5

    PressureAtTakeoff = 101325
    TemperatureAtTakeoff = 288.15
    DensityAtTakeoff = 1.225
    Gamma = 1.4

#VER 2: T/W = 0.4077, Wing = 5210, ClCruise = 0.5266
#CHANGED Cd0 to an approximation which varied with thickness to chord ratio (from the adsee slides) --> 0.00548*2
