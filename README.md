## ๐ฉโ๐ป Team
- **[์์์](https://github.com/tasddc1226)**
- **[๊ถ์๊ฒฝ](https://github.com/fore0919)**
- **[์ค์๋ฏผ](https://github.com/redtea89)**

`ํ๋ก์ ํธ ์งํ ๊ธฐ๊ฐ 2022.04.26 09:00 ~ 2022.04.29 18:00`

[`Team-A-notion`](https://pretty-marlin-13a.notion.site/Team-A-03cf51c7174847ce88a6302e6939ea2a)


## ๐  ๊ธฐ์  ์คํ
<img src="https://img.shields.io/badge/python-3776AB?style=plastic&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/django-092E20?style=plastic&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/mysql-C70D2C?style=plastic&logo=mysql&logoColor=white">
<img src="https://img.shields.io/badge/docker-2496ED?style=plastic&logo=docker&logoColor=white">


## ๐ฆ ์๋น์ค ๊ฐ์
- ๊ด๊ณ ์ฃผ๊ฐ ์ ๊ณตํ ํ์์ ํ๋ฉด๋ฐ์ดํฐ(ํด๋ฆญ ์, ํ๋ฉด์ ํ, ๊ด๊ณ ๋ธ์ถ์ ๋ฑ)๋ฅผ ์ด์ฉํ์ฌ ๊ด๊ณ ํจ๊ณผ๋ฅผ ์ ๋์ ์ผ๋ก ์ ๊ณตํ๋ค.

## ์ฌ์ฉ์ ์๊ตฌ์ฌํญ ์ ์
- ์ฃผ์ด์ง ๋ฐ์ดํฐ์์ ์๊ตฌ์ฌํญ๋๋ก ์๋นํ๊ธฐ์ํ ๋ฐ์ดํฐ๋ฒ ์ด์ค๋ฅผ ์ค๊ณ
    - [x] ์ฃผ์ด์ง ๋ฐ์ดํฐ csv๋ฅผ DB์ ์ ์ฌ
    - [x] ๋ฐ์ดํฐ์ ํ์ด๋ธ์ advertiser์ date, media๋์ธ๋ฑ์ฑ ๊ธฐ๋ฅ์ ํฌํจ
- ์๋ ๊ธฐ๋ฅ์ ์ ๊ณตํ๋ REST API ์๋ฒ๋ฅผ ๊ฐ๋ฐ
    - ๊ด๊ณ ์ฃผ ๋ฑ๋ก
        - [x] ๊ด๊ณ ์ฃผ์ด๋ฆ, ์ด๋ฉ์ผ, ํธ๋ํฐ๋ฒํธ ํ๋ ์ถ๊ฐ
        - [ ] ์๋์ผ๋ก ๊ด๊ณ ์ฃผ id ์์ฑ
    - ๊ด๊ณ ์ฃผ ์ ๋ณด ์์ 
        - [x] ๊ด๊ณ ์ฃผ์ด๋ฆ, ์ด๋ฉ์ผ, ํธ๋ํฐ๋ฒํธ๋ง ์์ ๊ฐ๋ฅ
    - ๊ด๊ณ ์ฃผ ์ญ์ 
        - [x] ๊ด๊ณ ์ฃผ๋ฅผ ์ญ์ ํ๋ฉด ๊ด๋ จ๋ ๊ด๊ณ ๋ฐ์ดํฐ ์ญ์ 
    - ๊ด๊ณ ์ฃผ ๋ชฉ๋ก ์กฐํ
        - [x] ๊ณ ์ id, ์ด๋ฆ, ์ด๋ฉ์ผ, ํธ๋ํฐ๋ฒํธ๊ฐ ๋ณด์ด๋๋ก
    - ๋ถ์๋ฐ์ดํฐ ์กฐํ
        - [x] ๊ด๊ณ ์ฃผ ๊ณ ์ ๋ฒํธ(adviser_id), ๊ธฐ๊ฐ(date)์ ์๋ ฅํ์ฌ ์กฐํ
            - ๊ธฐ๊ฐ์ start_date, end_date๋ก ์๋ ฅ
            - ๋ถ์๋ฐ์ดํฐ๋ ๋งค์ฒด(media)๋ณ๋ก ๊ทธ๋ฃน์ง์ด ๋ํ๋
            - ๋ถ์๊ฒฐ๊ณผ๋ ์๋์ ๊ฐ์ด ๋ํ๋ด๋ jsonํ์์ ๋ง๊ฒ ๋ฆฌํด
                - CTR = click * 100 / impression (๋ฐฑ๋ถ์จ %, ์์์  ๋์งธ๊น์ง์ถ๋ ฅ)
                - ROAS = cv * 100 / cost (๋ฐฑ๋ถ์จ %, ์์์  ๋์งธ๊น์ง์ถ๋ ฅ)
                - CPC = cost / click (์์์  ๋์งธ๊น์ง์ถ๋ ฅ)
                - CVR = conversion * 100 / click (๋ฐฑ๋ถ์จ %, ์์์  ๋์งธ๊น์ง์ถ๋ ฅ)
                - CPA = cost / conversion (์์์  ๋์งธ๊น์ง์ถ๋ ฅ)



## DB Modeling
![madup-db](https://user-images.githubusercontent.com/55699007/165890362-65309bbb-0e77-4396-bbcb-973b2dc94f3f.png)


---
## ๊ด๊ณ ์ฃผ CRUD
- `POST` `/api/v1/advertisers/signin`
  - ์์ฒญ Body
    ```json
      {
      "advertiser_id": "19971226",
      "name": "tasddc",
      "email": "tasddc@naver.com",
      "phone": "010-1234-1234"
      }
    ```
  - server ์๋ต
    ```json
      {
        "message": "SUCCESS"
      }
    ```
- `GET` `/api/v1/advertisers/<str:advertiser_id>`
  - ์์ฒญ Body : `None`
  - server ์๋ต
    ```json
      {
        "result": {
          "advertiser_id": "19971226",
          "name": "tasddc",
          "email": "tasddc@naver.com",
          "phone": "010-1234-1234"
        }
      }
    ```

- `PATCH` `/api/v1/advertisers/<str:advertiser_id>`
  - ์์ฒญ Body
    ```json
      {
        "email": "admin@admin.com",
        "name": "ํ๊ธธ๋",
        "phone": "010-9999-8888"
      }
    ```
  - server ์๋ต
    ```json
    {
      "message": "SUCCESS"
    }
    ```
  - ๋ณ๊ฒฝ ํ ์กฐํ ๊ฒฐ๊ณผ
    ```json
    {
      "result": {
        "advertiser_id": "19971226",
        "name": "ํ๊ธธ๋",
        "email": "admin@admin.com",
        "phone": "010-9999-8888"
      }
    }
    ```


- `DELETE` `/api/v1/advertisers/<str:advertiser_id>`
  - ์์ฒญ Body : `None`
  - server ์๋ต
    ```json
      {
        "message": "SUCCESS"
      }
    ```
  - ๊ด๊ณ ์ฃผ ์ญ์  ํ ์ฌ์ญ์  ์์ฒญ์ ๋ํ server ์์ฒญ
    ```json
      {
        "message": "ADVERTISER_DOES_NOT_EXIST"
      }
    ```

---
## ๊ธฐ๊ฐ ๋ด ๊ด๊ณ  ํจ์จ ๋ถ์ API

- `GET` `/api/v1/ads/analysis-detail`
  - ์์ฒญ ์ฟผ๋ฆฌ data set : `advertiser_id`, `start_date`, `end_date`

- ํน์  ๊ด๊ณ ์ฃผ์ ํน์  ๊ธฐ๊ฐ ๋ด์ ๊ด๊ณ  ํจ์จ ๋ฐ์ดํฐ๋ฅผ ๋ฐ์์ค๊ธฐ ์ํ ์์ ์์ฒญ
  - `/api/v1/ads/analysis-detail?advertiser_id=37445071&start_date=2022.04.01&end_date=2022.04.30`

- ์์ ์์ฒญ์ ๋ํ server ์๋ต
  ```json
    {
      "message": "SUCCESS",
      "analysis_datas": {
        "naver": {
          "ctr": 1.63,
          "roas": 514.28,
          "cpc": 47850.01,
          "cvr": 9.72,
          "cpa": 492212.26
        },
        "facebook": {
          "ctr": 1.51,
          "roas": 155.49,
          "cpc": 68889.16,
          "cvr": 35.08,
          "cpa": 196363.81
        },
        "google": {
          "ctr": 14.72,
          "roas": 545.5,
          "cpc": 22409.06,
          "cvr": 67.77,
          "cpa": 33065.92
        }
      }
    }
  ```
  
