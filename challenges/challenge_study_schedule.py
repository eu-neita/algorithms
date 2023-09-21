"""function study_schedule"""


def study_schedule(presence_period, target_time):
    """function content"""

    count = 0
    try:

        for start, stop in presence_period:

            if start <= target_time <= stop:
                count += 1

        return count

    except TypeError:
        return None
