Notes on Ethereum NFT Metadata
===

###### 2022-08-11

[SO](https://ethereum.stackexchange.com/questions/107011/how-do-i-access-read-the-metadata-from-my-opensea-nft-purchase) has information
that indicates NFTs are too broad of a category and it's better to get OpenSea information directly from [their API](https://docs.opensea.io/reference/retrieving-a-single-asset).

Example:

```
curl --request GET \
  --url 'https://api.opensa.io/api/v1/asset/0x495f947276749ce646f68ac8c248420045cb7b5e
```

OpenSeak is requesting that I get an [API key](https://docs.opensea.io/reference/request-an-api-key).




