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

bool generating_pulses = false;
uint8_t remain_pulses;


void start_pulses(uint8_t pulses) {
  if (!generating_pulses) {
    generating_pulses = true;
    TCNT1 = 0;
    TCCR1B |= (1<<CS10); // no preescaling
    TIMSK1 |= 1<<OCIE1A; // interrupt on match
    OCR1A = 400;
    remain_pulses = 2*pulses;
    PORTD &= ~(1<<PD3);
  }
}


// pulse generation interrupt.
ISR(TIMER1_COMPA_vect) {
  PORTD ^=  (1<<PD3) | (1<<PD4);
  if (--remain_pulses == 0) {
    PORTD |= (1<<PD3) | (1<<PD4);
    TCCR1B &= ~(1<<CS10);
    TIMSK1 &= ~(1<<OCIE1A);
    generating_pulses = false;
  }
  OCR1A += 400;
}
