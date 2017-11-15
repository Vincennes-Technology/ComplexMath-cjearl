#!/usr/bin/python
#Chris Searl
#Series & Parallel

import math

pi = 3.141529


def complex_add(complex_a,complex_b):


    x1 = float(complex_a[0]) * math.cos(pi/180 * complex_a[1])

    x2 = float(complex_b[0]) * math.cos(pi/180 * complex_b[1])

    y1 = float(complex_a[0]) * math.sin(pi/180 * complex_a[1])

    y2 = float(complex_b[0]) * math.sin(pi/180 * complex_b[1])

    x_total = x1 + x2

    y_total = y1 + y2

    answer = rect_to_polar(x_total, y_total)

    return answer[0], answer[1]



def complex_division(complex_a, complex_b):

    real_answer = complex_a[0] / complex_b[0]

    imag_answer = complex_a[1] - complex_b[1]

    return real_answer, imag_answer



def complexAdd(a, b):
    realAnswer = a[0] + b[0] 
    imagAnswer = a[1] + b[1] 
    return (realAnswer, imagAnswer)


def complexSubtract(a, b):
    realAnswer = a[0] - b[0]
    imagAnswer = a[1] - b[1]
    return (realAnswer, imagAnswer)


def complexMultiply(a, b):
    realAnswer = a[0] * b[0]
    imagAnswer = a[1] * b[1]
    return (realAnswer, imagAnswer)


def complexDivide(a, b):
    realAnswer = a[0] / b[0]
    imagAnswer = a[1] / b[1]
    return (realAnswer, imagAnswer)

# Rectangular to Polar Conversion

def rect_to_polar(x, y):

    angle = math.atan((y/x))
    angle = angle * (180/pi)
    magnitude = (math.sqrt((x*x)+(y*y)))
    answer = magnitude, angle
    return answer

# Polar to Recatangular Conversion

def polar_to_rect(polar_num):

    y = polar_num[0] * (math.sin(polar_num[1] * pi/180))
    x = polar_num[0] * (math.cos(polar_num[1] * pi/180))
    rect = x, y
    return rect

# Magnitude

def magnitude(number):

    absolute = math.sqrt((number[0] * number[0]) + (number[1]* number[1]))
    return absolute

# Mode Select
mode_select = raw_input( 'Is this a Series or Parallel circuit?:')

#Series

if (mode_select == 'Series') or (mode_select == 'series'):
    
    
    frequency = input('\nWhat is the frequency of the source? (in Hz): ')
    
    voltage = input('\nWhat is the voltage of the source? (in RMS): ')
    
    resistor_value = input('\nWhat value of resistor is present? (in Ohms): ')

    inductor_value = input('\nWhat is the value of your inductor? (in Henrys): ')
    
    inductor_resistance = input('\nResistance of the wiring of the inductor? (in Ohms): ')

    capacitor_value = input('\nWhat is the value of your capacitor? (in Farads): ')


# Calculations

    total_resistance = inductor_resistance + resistor_value
    
    inductance = 2 * pi * frequency * inductor_value
    
    mag_inductance = (inductor_resistance, inductance)
    
    mag_inductance = magnitude(mag_inductance)
    
    capacitance = (1/(2 * pi * frequency * capacitor_value))
    
    impedance = total_resistance, (inductance + -capacitance)
    
    mag_impedance = magnitude(impedance)
    
    current = float(voltage) / float(mag_impedance)
    
    v_r = current * resistor_value
    
    v_l = current * inductance
    
    v_c = current * capacitance


# Phase angle calculations 

    if inductance > capacitance:
    
        argument_send = impedance[1] / impedance[0]
        
    if capacitance > inductance:
        
       argument_send = impedance[0] / impedance[1]
        
    if capacitance == inductance :

        argument_send = 0


    phase_radians = math.atan(argument_send)
    
    phase_angle = phase_radians * 180/pi

# Printing out the results

    if capacitance > inductance:
        print('Your phase angle is %f degrees ' % phase_angle)
    if inductance > capacitance:
        print('Your phase angle is -%f degrees ' % phase_angle)
        print('\nYour total impedance is: %.2f + %.2fj' % (impedance[0], impedance[1]))
        print('That means the magnitude of your impedance is: %.2f' % mag_impedance)
        print('Which then means your current is: %f A' % current)
        print('V(R) = %.2f, V(L) = %.2f, V(C) = %.2f' % (v_r, v_l, v_c))
    
#Parallel

if (mode_select == 'Parallel') or (mode_select == 'parallel'):

    print('If a value is not there, type 0')
    
    frequency = input('\nFrequency of the source? (in Hz): ')

    voltage = input('\nVoltage of the source? (in RMS): ')

    resistor_value = input('\nValue of your resistor? (in Ohms): ')

    inductor_value = input('\nValue of your inductor? (in Henrys): ')

    inductor_resistance = input('\nResistance of the wiring of the inductor? (in Ohms): ')

    capacitor_value = input('\nValue of your capacitor? (in Farads): ')



# basic calculations, using polar r, Theta

    polar_voltage = voltage, 0

    resistor_value = float(resistor_value)

    resistance = float(resistor_value), 0

    inductor_resistance = inductor_resistance, 0

    inductance = (2 * pi * frequency * inductor_value), 90

    capacitance = 1/(2 * pi * frequency*capacitor_value), -90

    inductor_branch = complex_add(inductor_resistance, inductance)

    one = 1, 0



# inverse of the impedances 

    inverse_resistance = complex_division(one, resistance)

    inverse_p_capacitance = complex_division(one, capacitance)

    inverse_p_inductance = complex_division(one, inductor_branch)



# Breaking the sum of the denominator in to variables for impedance calculations

# Using this formula 1 / ((1/Xl) + (1/R) + (1/Xc))

    denominator = complex_add(inverse_p_capacitance, inverse_p_inductance)

    denominator_f = complex_add(denominator, inverse_resistance)

    total_impedance = complex_division(one, denominator_f)



# Current calc. 

    total_current = voltage / total_impedance[0]

    inductor_branch_current = total_current * (total_impedance[0] / inductor_branch[0])

    cap_branch_current = total_current * (total_impedance[0] / capacitance[0])

    resistor_branch_current = total_current * (total_impedance[0] / resistance[0])



# Printing results

    print('The magnitude of your impedance is %f with a phase of %f degrees' % (total_impedance[0], total_impedance[1]))

    if total_impedance[1] > 0:

        print('Your current is lagging voltage by %f degrees' % total_impedance[1])

    if total_impedance[1] < 0:

        print('Your current is leading voltage by %f degrees' % total_impedance[1])

    if total_impedance[1] == 0:

        print('your voltage and current will be in phase')

    print('Your total current will be %f A' % total_current)
