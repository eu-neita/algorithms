def validate_target_time(target_time):
    """Validate target_time."""
    if target_time is None:
        return False
    return True


def validate_period(period):
    """Validate period."""
    if not isinstance(period, tuple) or len(period) != 2:
        return False
    if not isinstance(period[0], int) or not isinstance(period[1], int):
        return False
    if period[0] < 0 or period[1] < 0:
        return False
    return True


def study_schedule(permanence_period, target_time):
    """
    Receives a list.
    """
    if not validate_target_time(target_time):
        return None

    student_count = 0

    for period in permanence_period:
        if not validate_period(period):
            return None

        start, end = period

        if start <= target_time <= end:
            student_count += 1

    return student_count
