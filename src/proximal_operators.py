import numpy as np


def proximal_update_admm(
    factor: np.ndarray[tuple[int, int], np.float64],
    dual_var: np.ndarray[tuple[int, int], np.float64],
    rho: float,
    constraint: str,
    hyperparams: dict,
) -> np.ndarray[tuple[int, int], np.float64]:
    """
    Performs the proximal update for the ADMM sub-problem.
    """
    if constraint == "None":
        return factor

    elif constraint == "nonnegative":
        return np.maximum(0, factor - dual_var)

    elif constraint == "L1":  # sparsity with L1 norm
        factor = factor - dual_var
        return np.sign(factor) * np.maximum(
            0, np.abs(factor) - hyperparams["l1_lambda"] / rho
        )

    elif constraint in [
        "NNL1",
        "nonnegative-l1sparsity-aoadmmasc",
        "nonnegative-l1sparsity-naiveasc",
    ]:
        factor = factor - dual_var
        return np.maximum(0, factor - hyperparams["l1_lambda"] / rho)

    else:
        raise ValueError("Invalid constraint")
