Meta
===

This is source code focusing on analysis of projects on FXHash and related data.

Scraping Description
---

| Script | Description |
|---|---|
| `gentkid` | get information about a single generative token |
| `gentkid_actions` | get information about the actions associated with a generative token |
| `actions [start] [end-date]` | get all actions |

COMPLETED in actions list

Features (todo)
---

* Reserve list - show which user has a reserve on which token (reverse reserve lookup,
  filter on available/unavailable, default to available)
  - There should be a table in the db that has `seq_id,gentkid,json_reserves,date`
  - Table should be append only
  - When deciding to update an entry (append) all amounts should be considereded (in the `json_reserves` table)
  - `.data.generateiveToken.reserves`
* Filter on tag or keyword (in description)
  - Sort by gentk or artist 'popularity' (total sales in xtz?)
* Similarity/suggestion search
  - "find me pieces like this one"
  - "find me other pieces like this artist"
  - "find me other pieces like this collector"
  - "find me pieces like this set of pieces"
  - inception-v3? ([link](https://github.com/fchollet/deep-learning-models/blob/master/inception_v3.py))
  - some other ideas:
    + gabor filters
    + sift/kaze/brisk (akaze)
* 'admired' list
  - needs login
  - Table `seq_id,admire_id,user_id,json_info,active`



Analysis Ideas
---

* Time to fully mint
* project cap vs. percent minted
* gentk mint price vs. gentk minted

Resources
---

* [fxhashmonitor](https://fxhashmonitor.xyz/)
* [FXHash API Guide](https://api.fxhash.xyz/graphql)
* [Apollo GraphQL Explorer](https://studio.apollographql.com/sandbox/explorer)
* [FXHash Apollo GraphQL Exploerer](https://studio.apollographql.com/sandbox?endpoint=https%3A%2F%2Fapi.fxhash.xyz%2Fgraphql)
* [fxcollectors](https://fxcollectors.stroep.nl/?project=8486)
* [fxparty](https://fxparty.xyz/wallets/top)
* [Medium: A Data Analysts Perspective on the FXHash Beta](https://medium.com/@tgmeyer/a-data-analysts-perspective-on-the-fxhash-beta-52eb5c79e466)
* [fxhash user guide](https://gitbook.fxhash-userguide.xyz/view-and-analyse)
* [tzkt.io](https://tzkt.io/)
