def calculate_new_weight(old_weight, savings ):
    """
    Calculate the new weight based on the old weight.
    
    Parameters:
    old_weight (float): The previous weight value.
    savings (float): The amount by which to reduce the weight.

    Returns:
    float: The new weight value.
    """
    
    new_weight = old_weight -savings
    return new_weight