def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for entry, exit in permanence_period:
            if entry <= target_time <= exit:
                counter += 1
        return counter
    except TypeError:
        return None
