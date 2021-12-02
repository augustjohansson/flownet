import pandas as pd
import numpy as np


def write_well_paths(
    well_logs: pd.DataFrame,
    filename: str = None,
) -> None:
    """
    Write the well as a well path ascii file suitable for visualization in ResInsight.
    """

    _, indices = np.unique(well_logs["WELL_NAME"], return_index=True)
    indices = np.append(indices, len(well_logs))
    coords = well_logs[["X", "Y", "Z", "Z"]].to_numpy()

    with open(filename, "w") as f:
        for k in range(len(indices) - 1):
            f.write("Name: " + well_logs["WELL_NAME"][indices[k]] + "\n")
            np.savetxt(f, coords[indices[k] : indices[k+1], :])
            # for r in coords[indices[k] : indices[k+1]]:
            #     print(r)
            #     print(tuple(r))
            #     s = ' '.join(['%10.6f ']*r.size)
            #     print("10.6f 10.6f 10.6f 10.6f"%r)
            #     f.write("10.6f 10.6f 10.6f 10.6f"%tuple(r))

    f.close()
