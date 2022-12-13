import dotenv
import os

from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import Query
import pandas as pd

# this file would create a csv would top 100,1000,5000,15000 cow trader base on their volumes.

dotenv.load_dotenv()
dune = DuneClient(os.environ["DUNE_API_KEY"])
dune_query_id = DuneClient(os.environ["QUERY_ID"])

query = Query(
    query_id=dune_query_id,

)
print("Results available at", query.url())


results = dune.refresh(query)
data = results.result.rows
df = pd.DataFrame(data=data)
df = df.sort_values('usd_volume_2022',ascending = False)

thresholds = [
    {"name": "cow_top_100","start":0, "end":100},
    {"name": "cow_top_1000","start":100, "end":1000},
    {"name": "cow_top_5000","start":1000, "end":5000},
    {"name": "cow_top_15000","start":5000, "end":15000},
    {"name": "cow_rest","start":15000, "end":df.shape[0]}
]
df = df.drop(['usd_volume_2022'], axis=1)
for t in thresholds:
    df.iloc[t["start"] : t["end"]].to_csv(f'{t["name"]}.csv', index=False, header=False, sep="\n")
