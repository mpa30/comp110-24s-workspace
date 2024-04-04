"""Some functions for my garden plan!"""


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Add plant under its kind."""
    if new_plant_kind in by_kind:  # if the kind is already in the dictionary ("flower" was in by_kind)
        by_kind[new_plant_kind].append(new_plant)

    else:  # if the kind is not in the dictionary.
        by_kind[new_plant_kind] = []
        by_kind[new_plant_kind].append(new_plant)


def add_by_date(garden_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plant under date to sow seeds."""
    if month in garden_by_date:
        garden_by_date[month].append(plant)
    else:
        garden_by_date[month] = []
        garden_by_date[month].append(plant)


def lookup_by_kind_and_date(plant_kind: dict[str, list[str]], date: dict[str, list[str]], kind: str, month: str) -> str:
    """Return string with list of plants of a specific kind of plant in a specific month."""
    assert kind in plant_kind
    assert month in date
    # Get a list of all plants od a specific kind input.
    kind_list: list[str] = plant_kind[kind]
    # Geta list of all plants planted in a specific month.
    month_list: list[str] = date[month]
    # Go through both list and find elements that appear in both.
    # Kind_list = ["marigold", "daisy"]
    # month_list = ["daisy", "rose"]
    combined_list: list[str] = []
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:  # plant is in both lists.
                combined_list.append(other_plant)  # does not matter what is appended bc they are the same.
    # "<kind>s to plant in <month>: <combined list>""
    if len(combined_list) > 0:
        f"{kind}s to plant in {month}: {combined_list}"
    else:  # "No <kind>s to plant in <month>."
        return f"No {kind}s to plant in {month}."
