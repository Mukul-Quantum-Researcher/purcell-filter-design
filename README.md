# MTL-coupled Purcell-filter design

Qiskit Metal geometry and Ansys HFSS simulations of a feedline, Purcell filter and readout resonator coupled through a multiconductor transmission-line section. The design study follows the intrinsic-notch approach discussed in Spring et al.; it is my simulation implementation, not an experimental replication of their performance.

## What the results show

Changing the shorted-end lengths moves the transfer-impedance notch: about 11.42 GHz in the initial result, 8.35 GHz in the middle iteration, and 6.8256 GHz in the supplied Project14 plot. No measured lifetime, readout fidelity or fabrication result is claimed.

![Project14 transfer-impedance notch](figures/low%20frequency%20impedence%206%20Ghz%20plot%20project%2014.png)

## Files

- `designs/`: Project11, Project13, Project14 and Project15 `.aedt` files. Results caches and meshes are excluded.
- `notebooks/purcell_geometry.ipynb`: selected geometry cells from the later Project15 variant, with old error outputs removed. This is **not** an exact regeneration of Project14.
- `data/`: original CSV exports, with their original filenames and column labels.
- `figures/`: selected original HFSS exports.
- `scripts/analyse_exports.py`: replot CSV data and locate minima without HFSS.

## Analyse the exported data

```shell
python -m pip install -r requirements-analysis.txt
python scripts/analyse_exports.py
```

The script writes a plot and numerical summary to `analysis/`. The middle-notch CSV contains 1,601 frequency points from 4 to 15 GHz; its minimum is at 8.351875 GHz. That export’s name says “project 12”, while the supplied presentation describes the corresponding middle stage as Project13. This mismatch has not been silently corrected. The CSV value is an HFSS `dB20(Z(...))` quantity, not a transmission coefficient in dB.

## Geometry and HFSS

The supplied logs reference Ansys Electronics Desktop 2024 R1. Open an `.aedt` file in a compatible licensed desktop installation and inspect its setup, materials and ports before solving. Solver results must be regenerated locally. The geometry notebook requires a desktop Qiskit Metal environment with its GUI dependencies; the notebook does not start HFSS or launch a solve.

There is no pinned geometry environment because it has not been reproduced in this workspace. The retained `.aedt` files and exports are the evidence for the historical design iterations. Changes between geometry iterations should not be interpreted as a single automated, validated sweep.

[Project explanation](https://mukul-quantum-researcher.github.io/projects/purcell-filter/) · [Portfolio](https://mukul-quantum-researcher.github.io)

