/*
 * This file is part of the Ckelinar Project.
 *
 * Copyright (C) 2013  UNIVERSIDAD DE CHILE.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 * Authors: Luis Alberto Herrera <herrera.luis.alberto@gmail.com>
 */


/* This is the main program of the controller of the adquisition board.
 * 
 * The controller is connected to the chip_select of the ADC, the drivers of
 * the transductors and the analog multiplexer selecting the input of the ADC.
 * When a falling edge is detected in the chip_select signal the controller
 * sends a pulse into one transducer while selecting the oposite one to be
 * sampled by the ADC.
 */

#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

/* Pin allocation
 * PB0 => chip select
 * PC4 => pulse signal
 */

/* Pulse generation uses the COUNTER1, TIMER1 COMPARATOR A, and the folling
 * variables.
 */
// if we are generating pulses or not
bool generating_pulses = false;
// number of pulses remaining to be generated
uint8_t remain_pulses;
 
// Generate a fixed amount of pulses asyncronously.
// TODO: the first pulse is few micro-seconds larger than the rest
void start_pulses(uint8_t pulses) {
  if (!generating_pulses) {
    generating_pulses = true;
    TCNT1 = 0;
    TCCR1B |= (1<<CS10); // no preescaling
    TIMSK1 |= 1<<OCIE1A; // interrupt on match
    OCR1A = 313;
    remain_pulses = pulses;
    PORTC |= 1<<PC4;
  }
}

ISR (INT0_vect)
{
  start_pulses(6);
}

ISR(TIMER1_COMPA_vect) {
  if (PORTC & (1<<PC4)) {
    PORTC &= ~(1<<PC4);
  } else {
    if (--remain_pulses) {
      PORTC |= 1<<PC4;
    } else {
      TCCR1B &= ~(1<<CS10);
      TIMSK1 &= ~(1<<OCIE1A);
      generating_pulses = false;
    }
  }
  OCR1A += 314;
}

int main() {
  // I/O set up
  DDRB = 0xFF;
  PORTB = 0x00;
  DDRC |= 1<<PC4;
  PORTC &= ~(1<<PC4);

  // Set up interruption on falling edge of chip_select
  DDRD &= ~(1 << DDD2); // Set PD2 as input
  PORTD |= (1 << PORTD2); // turn on the pull-up on PD2
  EICRA |= (1 << ISC01); // set INT0 to trigger on falling edge
  EIMSK |= (1 << INT0);     // Turns on INT0_vect
  sei();
  
  while(1) {
    sleep_mode();
  }
  
  return 0;
}

