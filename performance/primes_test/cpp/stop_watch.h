/* stop_watch.h: A simple stop-watch implementation to measure time taken
 *               for a given activity in a C++ program.
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
 * within a C++ program. I created this library to measure time taken by
 * functions / code within a C++ program. The time measured is in wall-clock
 * time and not CPU usage time of the program. 
 * This function returns the duration in <seconds>.<nanoseconds> 
 * precision as a long double value.
 *
 * The functions are inlined to minimize function call overhead. 
 *
 * Author: Chandrashekar Babu <email@chandrashekar.info>
 *         https://www.chandrashekar.info/
 */


#include <time.h>

class StopWatch {
    private:
        long double start_time;
        long double stop_time;

        static inline auto timespec_to_sec(struct timespec ts)
        {
            return ts.tv_sec + ts.tv_nsec * 1.0e-9;
        }


    public:
        StopWatch()
        {
            this->start_time = 0.0;
            this->stop_time = 0.0;
        }

        auto duration()
        {
            return this->stop_time - this->start_time;
        }

        void start()
        {
            struct timespec ts;
            clock_gettime(CLOCK_REALTIME, &ts);
            this->start_time = timespec_to_sec(ts);
        }

        auto stop()
        {
            struct timespec ts;
            clock_gettime(CLOCK_REALTIME, &ts);
            this->stop_time = timespec_to_sec(ts);
            return this->duration();
        }

};
