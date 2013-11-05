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

#ifndef PULSE_GENERATION_H
#define PULSE_GENERATION_H

#include <stdint.h>

/* Pulse generation uses the COUNTER1, TIMER1 COMPARATOR A, and the folling
 * variables.
 */
// if we are generating pulses or not
extern bool generating_pulses;
// number of pulses remaining to be generated
extern uint8_t remain_pulses;

// Generate a fixed amount of pulses asyncronously.
// TODO: the first pulse is few micro-seconds larger than the rest
void start_pulses(uint8_t pulses);

#endif // PULSE_GENERATION_H
