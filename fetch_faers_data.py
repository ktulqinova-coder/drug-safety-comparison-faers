"""
Pulls adverse event reports for ibuprofen and acetaminophen from
openFDA (FAERS). Saves the results as CSVs in the data/ folder.

openFDA docs: https://open.fda.gov/apis/drug/event/
No API key needed, just don't hit it too fast (40/min limit).
"""

import requests
import pandas as pd
import time

BASE_URL = 'https://api.fda.gov/drug/event.json'

# openFDA uses uppercase generic names
# paracetamol is called ACETAMINOPHEN in the US data
DRUGS = {
    'ibuprofen': 'IBUPROFEN',
    'acetaminophen': 'ACETAMINOPHEN',
}


def fetch_count(search, count_field, limit=100):
    # uses openFDA's count query — returns aggregated stats directly,
    # so I don't have to download millions of raw reports
    params = {
        'search': search,
        'count': count_field,
        'limit': limit,
    }
    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    results = response.json()['results']
    return pd.DataFrame(results)


def main():
    for drug_key, drug_name in DRUGS.items():
        base_search = f'patient.drug.openfda.generic_name:"{drug_name}"'

        # top reactions
        df = fetch_count(base_search, 'patient.reaction.reactionmeddrapt.exact')
        df.to_csv(f'data/reactions_{drug_key}.csv', index=False)
        print(f'[{drug_key}] reactions saved:', len(df), 'rows')
        time.sleep(2)

        # sex distribution (1=male, 2=female, 0=unknown)
        df = fetch_count(base_search, 'patient.patientsex')
        df.to_csv(f'data/sex_{drug_key}.csv', index=False)
        print(f'[{drug_key}] sex saved')
        time.sleep(2)

        # reports over time (by date FDA received them)
        df = fetch_count(base_search, 'receivedate')
        df.to_csv(f'data/timeline_{drug_key}.csv', index=False)
        print(f'[{drug_key}] timeline saved:', len(df), 'rows')
        time.sleep(2)

        # same but only for serious reports (hospitalization, death, etc)
        serious_search = base_search + ' AND serious:1'
        df = fetch_count(serious_search, 'patient.reaction.reactionmeddrapt.exact')
        df.to_csv(f'data/serious_reactions_{drug_key}.csv', index=False)
        print(f'[{drug_key}] serious saved')
        time.sleep(2)

    print('\nDone, CSVs are in data/')


if __name__ == '__main__':
    main()
