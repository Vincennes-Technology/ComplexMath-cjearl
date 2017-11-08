#!/usr/bin/python
#Chris Searl
#Series & Parallel

import math

pi = 3.141529

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

if (mode_select == 'Series') or (mode_select == 'series'):
    print('For this particular experiment, I am only capable of Series calculations')
if (mode_select == 'Parallel') or (mode_select == 'parallel'):
    print('For this particular experiment, I will be performing Parallel Calculations')
frequency = input('\nWhat is the frequency of the source? (in Hz): ')
voltage = input('\nWhat is the voltage of the source? (in RMS): ')
resistor_value = input('\nWhat value of resistor is present? (in Ohms): ')
inductor_value = input('\nWhat is the value of your inductor? (in Henrys): ')
capacitor_value = input('\nWhat is the value of your capacitor? (in Farads): ')


# Calculations

omega = 2 * pi * frequency
total_resistance = inductor_resistance + resistor_value
inductance = omega * inductor_value
mag_inductance = (inductor_resistance, inductance)
mag_inductance = magnitude(mag_inductance)
capacitance = (1/(omega * capacitor_value))
impedance = total_resistance, (inductance + -capacitance)
mag_impedance = magnitude(impedance)
current = float(voltage) / float(mag_impedance)
v_r = current * resistor_value
v_l = current * inductance
v_c = current * capacitance


# Phase angle calculations 

if inductance > capacitance:
    argument_send = impedance[1] / impedance[0]
else:
    if capacitance > inductance:
        argument_send = impedance[0] / impedance[1]
    else:
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
