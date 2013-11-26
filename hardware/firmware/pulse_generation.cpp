/*
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

#include "pulse_generation.h"

#include <avr/io.h>
#include <avr/interrupt.h>

#define PULSE_HALF_WIDTH 250
#define DISABLE_ALL 0x00

/* Pulse generation uses the COUNTER1, TIMER1 COMPARATOR A, and the folling
 * variables.
 */
// if we are generating pulses or not
bool generating_pulses;
// number of pulses remaining to be generated
uint8_t remain_pulses;

uint8_t next_portd;
uint8_t next_enable;



void start_pulses(uint8_t pulses, uint8_t enable_mask) {
  if (!generating_pulses) {
    generating_pulses = true;
    TCNT1 = 0;
    TCCR1B |= (1<<CS10); // no preescaling
    TIMSK1 |= (1<<OCIE1A) | (1<<OCIE1B); // interrupt on match A and B
    OCR1A = PULSE_HALF_WIDTH;
    OCR1B = pulses*2*PULSE_HALF_WIDTH - PULSE_HALF_WIDTH/2;

    next_enable = enable_mask;
    remain_pulses = 2*pulses;

    PORTC = next_enable;
    PIND = (1<<PD3) | (1<<PD4); // flip PD3 y PD4
  }
}


// pulse generation interrupt.
ISR(TIMER1_COMPA_vect) {
  PORTC = next_enable;
  PIND = (1<<PD3) | (1<<PD4); // flip PD3 y PD4
  if (--remain_pulses == 0) {
    PIND = (1<<PD3) | (1<<PD4); // flip again to keep polarity consitent
    TCCR1B &= ~(1<<CS10);
    TIMSK1 &= ~(1<<OCIE1A);
    TIMSK1 &= ~(1<<OCIE1B);
    generating_pulses = false;
  }
  OCR1A += PULSE_HALF_WIDTH;
}

ISR(TIMER1_COMPB_vect) {
  next_enable = DISABLE_ALL;
}
