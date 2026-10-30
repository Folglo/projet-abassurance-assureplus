"""Démonstration du bug potentiel : une date de naissance mal formatée fait disparaître un doublon.

Version naïve : conversion `errors="coerce"` (les dates illisibles deviennent NaT sans message)
et rapprochement sur la seule date de naissance.
Version corrigée : le pipeline du projet (formats explicites, motifs de rejet, rapprochement par
email et téléphone en complément).

Lancement : python scripts/demo_silent_bug.py
"""

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from abassurance.duplicates import find_duplicates  # noqa: E402
from abassurance.extract import load_raw  # noqa: E402
from abassurance.pipeline import run_pipeline  # noqa: E402


def naive_birth_dates(raw):
    """Conversion naïve : tout ce qui n'est pas au format attendu devient NaT, sans alerte."""
    ab = pd.to_datetime(raw["ab_client"]["AB_DATE_NAISSANCE"], errors="coerce")
    ap = pd.to_datetime(raw["ap_users"]["AP_BIRTH_DATE"], errors="coerce")
    keys = ["AB-" + raw["ab_client"]["AB_CLIENT_ID"], "AP-" + raw["ap_users"]["AP_USER_ID"]]
    return pd.concat([ab.set_axis(keys[0]), ap.set_axis(keys[1])])


def main():
    raw = load_raw()
    result = run_pipeline()
    naive_dates = naive_birth_dates(raw)
    naive_customers = result.customers.copy()
    naive_customers["birth_date"] = naive_customers["customer_key"].map(
        naive_dates[~naive_dates.index.duplicated()]
    )
    naive_pairs = find_duplicates(naive_customers, identifiers=("birth_date",))

    print(f"Dates de naissance perdues en silence (NaT) : {int(naive_dates.isna().sum())}")
    print(f"Doublons trouvés par la version naïve     : {len(naive_pairs)}")
    print(f"Doublons trouvés par le pipeline corrigé  : {len(result.duplicates)}")
    missed = set(map(tuple, result.duplicates[["customer_a", "customer_b"]].to_numpy()))
    found = set(map(tuple, naive_pairs[["customer_a", "customer_b"]].to_numpy()))
    print(f"Doublons manqués par la version naïve     : {len(missed - found)}")


if __name__ == "__main__":
    main()
