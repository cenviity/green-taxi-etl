if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    data = data[data["passenger_count"] != 0]
    data = data[data["trip_distance"] != 0]

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, "The output is undefined"


@test
def test_positive_passenger_count(output, *args) -> None:
    assert (output["passenger_count"] > 0).all(), "Non-positive value found in `passenger_count` column"


@test
def test_positive_trip_distance(output, *args) -> None:
    assert (output["trip_distance"] > 0).all(), "Non-positive value found in `trip_distance` column"
