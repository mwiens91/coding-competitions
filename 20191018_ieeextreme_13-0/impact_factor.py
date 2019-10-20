#!/usr/bin/env python3

import json
import sys

ACCEPTED_YEARS = {"2018", "2017"}


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
raw_publications_list = json.loads(lines[1])
raw_citations_list = [json.loads(line) for line in lines[2:]]

# Keys are publication number, values is dictionary with keys "name" and
# "count"
publication_map = {}

for publication in raw_publications_list["publications"]:
    name = publication["publicationTitle"]
    number = publication["publicationNumber"]
    count = 0

    for article_count in publication["articleCounts"]:
        count += int(article_count["articleCount"])

    publication_map[number] = {"name": name, "count": count, "citations": 0}

for citation in raw_citations_list:
    for paper_citation in citation["paperCitations"]["ieee"]:
        if (
            paper_citation["publicationNumber"] in publication_map
            and paper_citation["year"] in ACCEPTED_YEARS
        ):
            publication_map[paper_citation["publicationNumber"]]["citations"] += 1

for _, publication in publication_map.items():
    publication["if"] = publication["citations"] / publication["count"]

ordered_idxs = sorted(
    publication_map,
    key=lambda idx: (-publication_map[idx]["if"], publication_map[idx]["name"]),
)

for idx in ordered_idxs:
    name = publication_map[idx]["name"]
    impact_factor = publication_map[idx]["if"]

    print("%s: %.2f" % (name, impact_factor))
