EESchema Schematic File Version 2  date Tue Nov  5 00:50:38 2013
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:TS5A3154
LIBS:74HC4051
LIBS:SN754410
LIBS:driver-cache
EELAYER 25  0
EELAYER END
$Descr A4 11700 8267
encoding utf-8
Sheet 4 4
Title ""
Date "5 nov 2013"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text HLabel 1300 1950 2    60   Input ~ 0
B-
Text HLabel 1300 1750 2    60   Input ~ 0
B+
Text HLabel 1300 1550 2    60   Input ~ 0
A-
Text HLabel 1300 1350 2    60   Input ~ 0
A+
Text HLabel 3850 1450 2    60   Input ~ 0
ENABLE_B
Text HLabel 2550 1450 0    60   Input ~ 0
ENABLE_A
Text GLabel 3850 1550 2    60   Input ~ 0
PULSE+
Text GLabel 3850 1650 2    60   Input ~ 0
PULSE-
Text GLabel 2550 1650 0    60   Input ~ 0
PULSE-
Text GLabel 2550 1550 0    60   Input ~ 0
PULSE+
$Comp
L CONN_2 P201
U 1 1 52782F0B
P 950 1450
AR Path="/52783CA2/52782F0B" Ref="P201"  Part="1" 
AR Path="/52783C97/52782F0B" Ref="P301"  Part="1" 
AR Path="/52782E6C/52782F0B" Ref="P401"  Part="1" 
F 0 "P401" V 900 1450 40  0000 C CNN
F 1 "CONN_2" V 1000 1450 40  0000 C CNN
	1    950  1450
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR203
U 1 1 52782F0A
P 3350 2450
AR Path="/52783CA2/52782F0A" Ref="#PWR203"  Part="1" 
AR Path="/52783C97/52782F0A" Ref="#PWR303"  Part="1" 
AR Path="/52782E6C/52782F0A" Ref="#PWR403"  Part="1" 
F 0 "#PWR403" H 3350 2450 30  0001 C CNN
F 1 "GND" H 3350 2380 30  0001 C CNN
	1    3350 2450
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR201
U 1 1 52782F09
P 3150 900
AR Path="/52783CA2/52782F09" Ref="#PWR201"  Part="1" 
AR Path="/52783C97/52782F09" Ref="#PWR301"  Part="1" 
AR Path="/52782E6C/52782F09" Ref="#PWR401"  Part="1" 
F 0 "#PWR401" H 3150 990 20  0001 C CNN
F 1 "+5V" H 3150 990 30  0000 C CNN
	1    3150 900 
	1    0    0    -1  
$EndComp
Text Label 1300 1350 0    60   ~ 0
A+
Text Label 1300 1550 0    60   ~ 0
A-
Text Label 1300 1950 0    60   ~ 0
B-
Text Label 1300 1750 0    60   ~ 0
B+
$Comp
L CONN_2 P202
U 1 1 52782F08
P 950 1850
AR Path="/52783CA2/52782F08" Ref="P202"  Part="1" 
AR Path="/52783C97/52782F08" Ref="P302"  Part="1" 
AR Path="/52782E6C/52782F08" Ref="P402"  Part="1" 
F 0 "P402" V 900 1850 40  0000 C CNN
F 1 "CONN_2" V 1000 1850 40  0000 C CNN
	1    950  1850
	-1   0    0    1   
$EndComp
$Comp
L SN754410 IC?
U 1 1 52782F07
P 3150 1850
AR Path="/5278139E" Ref="IC?"  Part="1" 
AR Path="/52782E6C/52782F07" Ref="IC401"  Part="1" 
AR Path="/52783250/52782F07" Ref="IC?"  Part="1" 
AR Path="/52783CA2/52782F07" Ref="IC201"  Part="1" 
AR Path="/52783C97/52782F07" Ref="IC301"  Part="1" 
F 0 "IC401" H 2750 2550 50  0000 L BNN
F 1 "SN754410" H 3350 1450 50  0000 L BNN
F 2 "HBridge-DIP16" H 3150 2000 50  0001 C CNN
	1    3150 1850
	1    0    0    -1  
$EndComp
Text Label 2550 1950 2    60   ~ 0
A-
Text Label 2550 1850 2    60   ~ 0
A+
Text Label 3850 1850 0    60   ~ 0
B+
Text Label 3850 1950 0    60   ~ 0
B-
$Comp
L +12V #PWR202
U 1 1 52782F06
P 3250 900
AR Path="/52783CA2/52782F06" Ref="#PWR202"  Part="1" 
AR Path="/52783C97/52782F06" Ref="#PWR302"  Part="1" 
AR Path="/52782E6C/52782F06" Ref="#PWR402"  Part="1" 
F 0 "#PWR402" H 3250 850 20  0001 C CNN
F 1 "+12V" H 3250 1000 30  0000 C CNN
	1    3250 900 
	1    0    0    -1  
$EndComp
$Comp
L +12V #PWR204
U 1 1 52782F05
P 4950 1400
AR Path="/52783CA2/52782F05" Ref="#PWR204"  Part="1" 
AR Path="/52783C97/52782F05" Ref="#PWR304"  Part="1" 
AR Path="/52782E6C/52782F05" Ref="#PWR404"  Part="1" 
F 0 "#PWR404" H 4950 1350 20  0001 C CNN
F 1 "+12V" H 4950 1500 30  0000 C CNN
	1    4950 1400
	1    0    0    -1  
$EndComp
$Comp
L C C201
U 1 1 52782F04
P 4950 1700
AR Path="/52783CA2/52782F04" Ref="C201"  Part="1" 
AR Path="/52783C97/52782F04" Ref="C301"  Part="1" 
AR Path="/52782E6C/52782F04" Ref="C401"  Part="1" 
F 0 "C401" H 5000 1800 50  0000 L CNN
F 1 "10u" H 5000 1600 50  0000 L CNN
	1    4950 1700
	1    0    0    -1  
$EndComp
$Comp
L C C202
U 1 1 52782F03
P 5250 1700
AR Path="/52783CA2/52782F03" Ref="C202"  Part="1" 
AR Path="/52783C97/52782F03" Ref="C302"  Part="1" 
AR Path="/52782E6C/52782F03" Ref="C402"  Part="1" 
F 0 "C402" H 5300 1800 50  0000 L CNN
F 1 "1u" H 5300 1600 50  0000 L CNN
	1    5250 1700
	1    0    0    -1  
$EndComp
$Comp
L C C203
U 1 1 52782F02
P 5550 1700
AR Path="/52783CA2/52782F02" Ref="C203"  Part="1" 
AR Path="/52783C97/52782F02" Ref="C303"  Part="1" 
AR Path="/52782E6C/52782F02" Ref="C403"  Part="1" 
F 0 "C403" H 5600 1800 50  0000 L CNN
F 1 "0.1u" H 5600 1600 50  0000 L CNN
	1    5550 1700
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR205
U 1 1 52782F01
P 4950 2050
AR Path="/52783CA2/52782F01" Ref="#PWR205"  Part="1" 
AR Path="/52783C97/52782F01" Ref="#PWR305"  Part="1" 
AR Path="/52782E6C/52782F01" Ref="#PWR405"  Part="1" 
F 0 "#PWR405" H 4950 2050 30  0001 C CNN
F 1 "GND" H 4950 1980 30  0001 C CNN
	1    4950 2050
	1    0    0    -1  
$EndComp
Connection ~ 5250 1900
Wire Wire Line
	4950 1900 5550 1900
Wire Wire Line
	4950 1500 4950 1400
Wire Wire Line
	3150 950  3150 900 
Connection ~ 3150 2350
Connection ~ 3050 2350
Wire Wire Line
	3350 2350 2950 2350
Wire Wire Line
	3350 2450 3350 2350
Connection ~ 3250 2350
Wire Wire Line
	3250 950  3250 900 
Wire Wire Line
	5550 1500 4950 1500
Connection ~ 5250 1500
Wire Wire Line
	4950 2050 4950 1900
$EndSCHEMATC
