"""
Part 1: Interval Scheduling

    Given a set of jobs, j, where sj is the start time of the job and fj is the finish time, we want to design a
    schedule with most non-overlapping, compatible, jobs.

     Solution:
        - We can achieve this using a greedy algorithm, where we select the next compatible job, with the earliest
        finish time.
        - We would sort the jobs by their finish times, and continuously pick the next compatible job until we have
        none left.

"""


def interval_schedule(jobs):
    """
    jobs: list of tuples (sj, fj)
    """
    schedule = []
    jobs.sort(lambda x: x[1])
    time = 0
    for job in jobs:
        if job[0] >= time:
            schedule.append(job)
            time = job[1]
    return schedule
