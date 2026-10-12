
def hardness_ratio(hard: float, soft: float) -> float:
    """Calculate hardness ratio from nonnegative band counts."""

    if hard < 0 or soft < 0:
        raise ValueError("Counts must be nonnegative.")

    total = hard + soft

    if total == 0:
        raise ValueError("Total counts must be greater than zero.")

    return (hard - soft) / total
