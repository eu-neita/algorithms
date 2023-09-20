def study_schedule(permanence_period, target_time):
    if target_time is None or not isinstance(target_time, int) or target_time < 0:
        return None

    student_count = 0

    for period in permanence_period:
        if not isinstance(period, tuple) or len(period) != 2 or not isinstance(period[0], int) or not isinstance(period[1], int) or period[0] < 0 or period[1] < 0:
            return None

        start, end = period

        if start <= target_time <= end:
            student_count += 1

    return student_count
