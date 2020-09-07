# README

This API provides basic functionality for managing users, BTC wallets and transactions between them.

## Installation

In order to have the project up and running, clone the repo and on it's root path, run the following command:

```docker-compose up```

Disclaimer: Sometimes the containers are not correctly loaded due to the mysql server is not runnng yet. Please, run the command again and the migrations and django app should run without problems.


## API Docs
### Users
  * URL

    ``` api/users```
  * Method

    ```POST```
  * Data params
    ```
    username=[string]
    password=[string]  
  * Success Response
    
    The response is an object containing the user's username and a generated Token for authentication.
    ```
    {
      "user": {
        "username": "ryan"
      },
      "token": "a040afe62c075d30d42ae9efbff84cdab9d7b114"
    }
  * Error Response

    The request validates that a user uses a unique username and the password field is not blank.
    ```
    {
      "username": [
        "A user with that username already exists."
      ],
      "password": [
        "This field may not be blank."
      ]
    }
### Wallets
  * URL

    ``` api/wallets```
  * Method

    ```GET```
  * Success Response GET method 
    
    The response for this method is a list of wallets from the authenticated user.
    ```
    [
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
    ]
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
* URL params
  
  Required: 

  ```address=[alphanumeric]```
* Success Response
  
  This endpoint will return the wallet with the specified address on the URL parameter

  ```
  {
    "id": 24,
    "address": "fl1fy75PEF0nM6i6477GX409LfY5WHxh",
    "amount": "1.00",
    "amount_usd": 10211.2,
    "owner": 1
  }

* Error Response

  If no wallet matches the address url param, the reponse is a 404 wallet not found.

   ```
   {
    "error": "Wallet not found."
   }
* Method

  ```GET```
* URL

  ```api/wallet/<address>/transactions```
* URL params
  
  Required: 

  ```address=[alphanumeric]```
* Success Response
  
  This endpoint will return all the transactions made by the wallet specified on URL param

  ```
  [
    {
        "id": 11,
        "from_wallet": 12,
        "to_wallet": 4,
        "amount": "0.50",
        "user": 1
    },
    {
        "id": 12,
        "from_wallet": 12,
        "to_wallet": 4,
        "amount": "0.30",
        "user": 1
    }
  ]
* Error Response

  If no wallet matches the address url param, the reponse is a 404 wallet not found.

   ```
   {
    "error": "Wallet not found."
   }
### Transactions
  * Method

    ```GET```
  * URL

    ```api/transactions```
  * Success Response

    This endpoint returns all the transactions made by the auhenticated user.

    ```
    [
      {
        "id": 1,
        "from_wallet": 4,
        "to_wallet": 5,
        "amount": "0.50",
        "user": 1
      },
      {
        "id": 11,
        "from_wallet": 12,
        "to_wallet": 4,
        "amount": "0.50",
        "user": 1
      },
      { 
        "id": 12,
        "from_wallet": 12,
        "to_wallet": 4,
        "amount": "0.30",
        "user": 1
      }
    ]
  * Method
    
    ```POST```

  * URL
    
    ```api/transactions```
  * Data Params
    ```
     from_wallet=[wallet_address]
     to_wallet=[wallet_address]
     amount=[decimal_number]
  * Success Response

    The endpoint response returns an object with data of ```from_wallet```, ```to_wallet``` and ```amount```
    ```
    {
      "from_wallet": 6,
      "to_wallet": 4,
      "amount": "0.10"
    }
  * Error Response:

    The POST request validates that the wallet has enough money in order to do the transaction
    ```
    {
      "error": "The wallet dosn't have enought money."
    }
