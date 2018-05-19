#!/usr/bin/env python3
"""
Simulate and analyze a printing queue.

Find
-----------
    -   Average amount of time the students will wait for their task to be
        completed.

Assumptions
-----------
    -   There is 1 printer in the lab.
    -   The printer is older; capable of processing 10 pages of draft quality.
    -   Printer quality can be improved but at a processing cost.
    -   At any given hour, there are 10 students in the lab.
    -   Each student generally prints up to 2 times while they are in the lab.
    -   Print tasks range between 1 and 20 pages.
"""
import random

from queues import Queue


class Task:
    """
    Simulates a printing task.
    """
    def __init__(self, time):
        """
        Constructor.

        Variables
        ---------
        time, int
            Time at which the task was created.
        """
        self.created_at = time
        self.pages = random.randrange(1, 21)

    def get_pages(self):
        """Returns the number of pages."""
        return self.pages

    def get_timestamp(self):
        """Returns the time at which the task was created."""
        return self.created_at

    def wait_time(self, current_time):
        """Returns how long the task has been scheduled."""
        return current_time - self.created_at


class Printer:
    """Simulates a printer."""
    def __init__(self, pages_per_min):
        """
        Constructor.

        Variables
        ---------
        pages_per_min, int
            Number of pages the printer prints in one minute.
        """
        self.ppm = pages_per_min
        self.time_remaining = 0  # Time to complete the current task.
        self.current_task = None

    def is_busy(self):
        """Returns True is currently printing a task."""
        if self.current_task is not None:
            return True
        return False

    def add_task(self, new_task):
        """Assigns a new task to print."""
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.ppm

    def print_task(self):
        """Prints a task."""
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None


def simulation(pages_per_min, duration, repeat):
    """
    Simulates a printing queue.

    Variables
    ---------
    pages_per_min, int
        Number of pages that the printer can print in one minute.
    duration, int
        Number of seconds that the simulation will last.
    repeat, int
        NUmber of times to repeat the simulation.
    """
    lab_printer = Printer(pages_per_min)

    for trail_num in range(repeat):
        print_queue = Queue()
        length_of_tasks = []  # Will keep track of task wait time.
        for seconds in range(duration):

            # On average, a new task will be generated once every 180 seconds.
            if random.randrange(1, 181) == 180:
                print_queue.enqueue(Task(seconds))

            if not lab_printer.is_busy():
                try:
                    new_task = print_queue.dequeue()
                except IndexError:
                    # Printer is not busy and no new tasks have been created.
                    continue
                else:
                    lab_printer.add_task(new_task)
                    # Length of task: Time task has been in queue + duration
                    # that the job will take.
                    length_of_task = (new_task.wait_time(seconds)
                                      + lab_printer.time_remaining)
                    length_of_tasks.append(length_of_task)
            else:
                lab_printer.print_task()
        # Compute average task wait time and number of remaining tasks.
        average_task_wait_time = sum(length_of_tasks) / len(length_of_tasks)
        remaining_tasks = print_queue.size()

        print("Trial {}:\t".format(trail_num)
              + "Average wait time of {}".format(average_task_wait_time)
              + " seconds; {} tasks remaining".format(remaining_tasks))


if __name__ == "__main__":
    simulation(pages_per_min=10, duration=3600, repeat=10)
