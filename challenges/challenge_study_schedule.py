def study_schedule(presence_period, target_time):
    if target_time is None:
        return None

    current_count = 0

    for entry in presence_period:
        entry_start, entry_end = entry

        if (
            entry_start is None
            or entry_end is None
            or not isinstance(entry_start, (int, float))
            or not isinstance(entry_end, (int, float))
        ):
            return None

        if entry_start <= target_time <= entry_end:
            current_count += 1

    return current_count
