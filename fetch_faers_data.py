"""
Fetch drug adverse event data from the openFDA API (FAERS database).

Project: Comparative safety profile analysis — Ibuprofen vs Acetaminophen
Author: <your name>

The script uses openFDA "count" queries, which return aggregated
statistics directly (no need to download millions of raw reports).
Results are saved as CSV files ready for analysis in pandas.

API docs: https://open.fda.gov/apis/drug/event/
No API key required (40 requests/minute limit).
"""

import requests
import pandas as pd
import time

BASE_URL = "https://api.fda.gov/drug/event.json"

# Drugs to compare (openFDA uses uppercase generic names;
# note: paracetamol is listed as ACETAMINOPHEN in the US data)
DRUGS = {
    "ibuprofen": "IBUPROFEN",
    "acetaminophen": "ACETAMINOPHEN",
}


def fetch_count(search: str, count_field: str, limit: int = 100) -> pd.DataFrame:
    """Run a single openFDA count query and return results as a DataFrame."""
    params = {
        "search": search,
        "count": count_field,
        "limit": limit,
    }
    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    results = response.json()["results"]
    return pd.DataFrame(results)


def main():
    for drug_key, drug_name in DRUGS.items():
        base_search = f'patient.drug.openfda.generic_name:"{drug_name}"'

        # 1. Top reported adverse reactions
        df = fetch_count(base_search, "patient.reaction.reactionmeddrapt.exact")
        df.to_csv(f"data/reactions_{drug_key}.csv", index=False)
        print(f"[{drug_key}] top reactions saved: {len(df)} rows")
        time.sleep(2)  # be polite to the API

        # 2. Distribution by patient sex (1=male, 2=female, 0=unknown)
        df = fetch_count(base_search, "patient.patientsex")
        df.to_csv(f"data/sex_{drug_key}.csv", index=False)
        print(f"[{drug_key}] sex distribution saved")
        time.sleep(2)

        # 3. Reports over time (by date FDA received the report)
        df = fetch_count(base_search, "receivedate")
        df.to_csv(f"data/timeline_{drug_key}.csv", index=False)
        print(f"[{drug_key}] timeline saved: {len(df)} rows")
        time.sleep(2)

        # 4. Top reactions among SERIOUS reports only
        serious_search = base_search + " AND serious:1"
        df = fetch_count(serious_search, "patient.reaction.reactionmeddrapt.exact")
        df.to_csv(f"data/serious_reactions_{drug_key}.csv", index=False)
        print(f"[{drug_key}] serious reactions saved")
        time.sleep(2)

    print("\nDone! All CSV files are in the data/ folder.")


if __name__ == "__main__":
    main()
