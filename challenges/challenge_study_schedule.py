def study_schedule(permanence_period, target_time):
    try:
        for entry, exit in permanence_period:
            counter = 0
            if entry <= target_time <= exit:
                counter += 1
        return counter
    except TypeError:
        return None
