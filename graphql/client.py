import json

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


transport = AIOHTTPTransport(url="http://localhost:8000/graphql")
client = Client(transport=transport)

query = gql("""
    query {
        cosinesim(v1: 13, v2: 110) {
            value
        }
    }
""")

result = client.execute(query)
print(json.dumps(result, indent=2))
