from automon.integrations.neo4j import Neo4jWrapper


def http_header(headers):
    # [print(x) for x in auth.request_headers(request)]

    # token = helper_brain.hash_key(sorted([x for x in headers]))

    args = dict(
        blob=sorted(headers),
        label='Headers'
    )

    Neo4jWrapper._prepare_dict(**args)