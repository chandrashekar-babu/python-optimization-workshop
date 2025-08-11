/* stop_watch.h: A simple stop-watch implementation to measure time taken
 *               for a given activity in a C program.
 * Copyright (C) 2014 Chandrashekar Babu.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 */

/* Description:
 * An simple stop-watch for measuring time elapsed between two probe-points
 * within a C program. I created this library to measure time taken by
 * functions / code within a C program. The time measured is in wall-clock
 * time and not CPU usage time of the program.
 * Usage is very simple. Just include this header file in your C program
 * and then start measurement by calling start_watch(&watch).
 * To stop measurement, simply call stop_watch(&watch). This function
 * returns the duration in <seconds>.<nanoseconds> precision as a
 * long double value.
 *
 * The functions are inlined to minimize function call overhead.
 *
 * Author: Chandrashekar Babu <email@chandrashekar.info>
 *         https://www.chandrashekar.info/
 */

#include <time.h>

typedef struct stop_watch_struct {
	long double start_time;
	long double stop_time;
} stop_watch_t;

static inline long double timespec_to_sec(struct timespec ts)
{
	return (long double) ts.tv_sec + (long double) ts.tv_nsec * 1.0e-9;
}

static inline long double duration(stop_watch_t *watch)
{
	return watch->stop_time - watch->start_time;
}

static inline void start_watch(stop_watch_t *watch)
{
	struct timespec ts;
	clock_gettime(CLOCK_REALTIME, &ts);
	watch->start_time = timespec_to_sec(ts);
}

static inline long double stop_watch(stop_watch_t *watch)
{
	struct timespec ts;
	clock_gettime(CLOCK_REALTIME, &ts);
	watch->stop_time = timespec_to_sec(ts);
	return duration(watch);
}
