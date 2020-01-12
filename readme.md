## eco-api fuzzer

It's written for python3. After checkout please run

```
pip3 install -r requirements.txt
```

Run with following options:

| Option | Description |
| ------ | ----------- |
| --uri  | base uri    |
| --port | port        |
| --rounds | number of rounds |

```
 python3 main.py --uri http://localhost --port 9000 --rounds 5
```


### configure fuzzer job
Simply add a json file in ./config folder and named it like you want. The file must end with .json and should contain valid json otherwise the fuzzer will give you notice a runtime. You can have multiple config files und multiple subfolder from ./config.

Example config file

```json
{
    "name": "fuzz_authentication",
    "jobs": [
        {
            "path": "api/v1/authenticate",
            "exit_codes": [401, 500],
            "timeout": 2,
            "method": "POST",
            "payload_type": "json",
            "fields": [
                {
                    "name": "email",
                    "type": "email"
                },
                {
                    "name": "password",
                    "type": "password"
                }
            ]
        },
        {
            "path": "api/v1/accounts/%id",
            "exit_codes": [200, 500],
            "timeout": 2,
            "method": "GET",
            "payload_type": "json",
            "headers": [
                {
                    "name": "content-type",
                    "value": "application/json"
                },
                {
                    "name": "Authorization",
                    "type": "jwt"
                }
            ]
        }
    ]
}
```

### configure job basic
The following properties needs to be configured for each job:

| Option | Description | Type | Example |
| ------ | ----------- | ---- | ------- |
| path   | path to the rest endpoint | String | ``` "path": "api/v1/authenticate" ``` |
| exit_codes | response http codes from the api that tell the fuzzer to end with error | Array<Number> | ``` "exit_codes": [401, 500] ``` |
| method    | http method  | GET, POST, PUT, DELETE | ``` "method": "GET" ``` |
| timeout | timout for resquest | value in seconds | ``` "timeout": 2 ``` |



### configure job payload
Add payload that should send to the api as json:

```json
 "fields": [
                {
                    "name": "email",
                    "type": "email"
                },
                {
                    "name": "password",
                    "type": "password"
                }
            ]
```

| Option | Description | Type |
| ------ | ----------- | ---- |
| name   | field name | String |
| type | type of randomness. fuzzer will generate, depending on your type, some random garbage for you. see available types for more details| String |



### configure job header
Add header the should send to the api:

```json
 "headers": [
                {
                    "name": "content-type",
                    "value": "application/json"
                },
                {
                    "name": "Authorization",
                    "type": "jwt"
                }
            ]
```

| Option | Description | Type |
| ------ | ----------- | ---- |
| name   | name of header | String |
| type | type of randomness. fuzzer will generate, depending on your type, some random garbage for you. see available types for more details| String |
| value | set a static value by your own. the fuzzer will not override this | Any |


### configure random values in uri
Add a replacement mark to the uri. For example %id to generate a random id in the uri string. Each random fuzzer type is available. You need only place a "%" as the first char. 

| Replacement mark |
| ---------------- |
| %email           |
| %password           |
| %string           |
| %string_with_digits          |
| %string_random           |
| %number           |
| %date           |
| %jwt           |
| %uuid           |
| %id           |


### available random fuzzer type
The following types are available to use in your json config file:

| Name of type | Description | Example |
| ------ | ----------- | ------------- | 
| email | random email addresses | ``` bjyfphcpknoguznxtobrrayzigbdjnauefailszkeefiqjnbcncatwoqopcdvjngxrcsrrcsl@ssslurwjeybgukyccu.org ```|
| password | random passwords | ``` 6/r7L?Zi~E ```
| string | random string | ``` olcrfltwybfwnunksvvtmwteiueqnzsehitr ```
| string_with_digits | random string with numbers | ``` olc86rfltwybfwnun23ksvvtm12wteiueqnzsehitr1sdasdq45 ```
| string_random | random string with numbers and punctuations | ```,iSW;Qu2BpqZJErf?VP6dUK&tnEXUrRX@Gn1zb ```
| number | random numbers | ``` 234 ```
| date | random date | ``` 2020-01-01 ```
| jwt | random json web token | ``` Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiJXblNuOXZ5VFNkeU96NVk2bjhnajAwSXoiLCJlbWFpbCI6Im9kY2lqa2ZtYXBqbW53YWZxdmlpYmxhbnhsc2Z4ZHpqZGRtZ25nbWxmdWJkbHBlZ25jb2tibmJpd2hwdmtxa21xZnNidnltY3poa3h3YWdzZnJ1ampkeUBjZ2t0aG9zeHltZ2xhanlmcGVoZWtieWxrbGNra2lpdGhoZXd0LmZyIiwicm9sZSI6InVzZXIiLCJpYXQiOjE1Nzg2NTI1NzAsImV4cCI6MTU3ODY1OTc3MH0.4LjkorF2Vk2dN_m3Ubhy0Itr1VCEjc2eHcrGmSKMrCk ```
| uuid | random uuid | ``` xtbytolm-xa43-zxr8-5e26-0i20nu0gb7n1```
| id | random  id|

### available payload types
The configure the type of payload that should send to the api you can simply choose one of the following:

| Name of type | Description | 
| ------ | ----------- | 
| json | send payload as json |
| application/x-www-form-urlencoded | send payload as application/x-www-form-urlencoded |
