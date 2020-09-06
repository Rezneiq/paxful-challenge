# README

This API provides basic functionality for managing users, BTC wallets and transactions between them.

## API Docs
* Users
  * URL

    ``` api/users```
  * Method

    ```POST```
  * Success Response
    
    The response is an object containing the user's username and a generated Token for authentication.
    ```
    {
      "user": {
        "username": "ryan"
      },
      "token": "a040afe62c075d30d42ae9efbff84cdab9d7b114"
    }´´´
* Wallets
  * URL

    ``` api/wallets```
  * Method

    ```GET```
  * Success Response GET method 
    
    The response for this method is a list of wallets from the authenticated user.
  ```
    {
        "id": 24,
        "address": "fl1fy75PEF0nM6i6477GX409LfY5WHxh",
        "amount": "1.00",
        "amount_usd": 10284.06,
        "owner": 1
    },
    {
        "id": 25,
        "address": "45HsHBwipqzFy9ZNk6FeSUHNaOms3Zft",
        "amount": "1.00",
        "amount_usd": 10284.06,
        "owner": 1
    },
    {
        "id": 26,
        "address": "Pdvv35llUSVLnG64z54P8dEG4lAE7eox",
        "amount": "1.00",
        "amount_usd": 10284.06,
        "owner": 1
    },
    {
        "id": 27,
        "address": "Vzav7rmiU5Wv4w8YslXv8GxuaphSeAug",
        "amount": "1.00",
        "amount_usd": 10284.06,
        "owner": 1
    }
´´´
  * URL

    ```api/wallets```
  * Method

    ```POST```
  
    Since the wallet address is generated automatically and the amount of the wallet has a default value of 1, the POST request needs no data

  * Success Response POST method
    
    The response from this method is the created wallet for the authenticated user. It will also return the converted amount of the wallet to USD.
  ```
{
    "id": 28,
    "address": "eYJqhWK1ZKEFI2lzgj23tHYuDCZhc3l0",
    "amount": "1.00",
    "amount_usd": 10206.21,
    "owner": 1
}
```

* Method

  ```GET```
* URL

  ```api/wallet/<address>```
