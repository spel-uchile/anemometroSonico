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
 * PB0 => ADC select 0
 * PB1 => ADC select 1
 * PB2 => ADC select 2
 * PD2 => chip select
 * PD3 => pulse- signal
 * PD4 => pulse+ signal
 */

/* System State Machine.
 * The sistem state is evaluated in TIMER0 COMPARARTOR A interruption. The
 *following definitions control the state machine.
 */
// FSM states.
typedef enum {
  IDLE,
  DRIVE_NORTH,
  LISTEN_SOUTH,
  TRANSITION_NORTH_TO_SOUTH,
  DRIVE_SOUTH,
  LISTEN_NORTH
} state_t;
// FSM current state.
state_t state_;
// FSM next state.
state_t next_state_;
// wheter we are waiting for an event to happen (to avoid scheduling an event
// twice).
bool timer0_running_ = false;


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
    OCR1A = 400;
    remain_pulses = 2*pulses;
    PORTD &= ~(1<<PD3);
  }
}

// schedule to evaluate the event next_state in ticks ticks.
void setup_timer(uint8_t ticks, state_t next_state) {
  if (!timer0_running_) {
    timer0_running_ = true;
    next_state_ = next_state;
    TCNT0 = 0;
    TCCR0B |= (1<<CS02) | (1<<CS00); //1024 preescaling
    TIMSK0 |= 1<<OCIE0A;
    OCR0A = ticks;
  }
}

ISR (INT0_vect)
{
  // The first event is delayed so the ADC is already taking samples.
  setup_timer(20, DRIVE_NORTH);
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



ISR(TIMER0_COMPA_vect) {
  timer0_running_ = false;
  TCCR0B &= 0xF8; //disable counter
  TIMSK0 &= ~(1<<OCIE0A); // disable interrupt
  state_ = next_state_;
  switch (state_) {
  case IDLE:
    PORTB = 0x06; // Pulse -> ADC
    PORTC = 0x00;
    break;
  case DRIVE_NORTH:
    PORTB = 0x06; // Pulse -> ADC
    PORTC = 0xFE; // Enable North
    start_pulses(6);
    setup_timer(6, LISTEN_SOUTH);
    break;
  case LISTEN_SOUTH:
    PORTB = 0x01; // South -> ADC
    PORTC = 0xFF; // Disable All
    setup_timer(100, TRANSITION_NORTH_TO_SOUTH);
    break;
  case TRANSITION_NORTH_TO_SOUTH:
    PORTB = 0x06; // Pulse -> ADC
    PORTC = 0x00;
    setup_timer(10, DRIVE_SOUTH);
    break;
  case DRIVE_SOUTH:
    PORTB = 0x06; // Pulse -> ADC
    PORTC = 0xFD; // Enable South
    start_pulses(6);
    setup_timer(6, LISTEN_NORTH);
    break;
  case LISTEN_NORTH:
    PORTB = 0x00; // North -> ADC
    PORTC = 0xFF; // Disable All
    setup_timer(100, IDLE);
    break;
  }
}

int main() {
  // I/O set up
  DDRB = 0xFF;
  PORTB = 0x06; // Pulse -> ADC
  DDRC = 0xFF;
  PORTC = 0x00;
  DDRD |= (1<<PD3) | (1<<PD4);
  PORTD |= (1<<PD3) | (1<<PD4);

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

