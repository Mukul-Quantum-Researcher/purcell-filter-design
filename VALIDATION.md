# Validation

On 23 November 2026, scripts/analyse_exports.py completed and regenerated analysis/exported-sweeps.png and analysis/summary.json. Both original CSV exports contain 1,601 rows from 4 to 15 GHz. The middle transfer-impedance minimum is at 8.351875 GHz.

The Project14 plot marks a notch at 6.8256 GHz. No Project14 CSV is supplied, so that value is sourced to the original image. The CSV name and presentation disagree about the middle project number; the original names are retained.

The geometry notebook was statically inspected; its Qiskit Metal GUI workflow and HFSS projects were not rerun. Licensed HFSS and a compatible desktop geometry environment are required for that verification.
