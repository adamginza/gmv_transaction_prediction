# Gross Merchandise Value (GMV) Analysis and Forecasting

### Background
_ABC Co._ is a small payment processing company based in Japan that began operations
in 2019. The business team is interested in forecasting GMV (Gross Merchandise
Value), which is defined as the **sum of transaction amounts over a period of time**.

GMV can be defined as:
* per store (the seller),
* per user (the purchaser), or
* for _ABC Co._ as a whole (across all users and stores).

### Dataset
The business team has provided the following datasets (in CSV format):

**transactions** - contains all transactions for 2020 and 2021 
* user ID (user_id)
* store ID (store_id)
* the datetime of the transaction (event_occurance)
* the amount of the transaction in yen (amount)

**stores** - contains characteristics for each store
* the prefecture (nam)
* local administrative area (laa)
* category
* location in latitude (lat) and longitude (lon)

**users** - contains the characteristics for each user
* gender and age as of December 31, 2021

### Objectives
(1) Perform an exploratory data analysis to highlight patterns in the data.

(2) Forecast GMV for each user for the month of January 2022

(3) Forecast GMV for _ABC Co._ as a whole for each date in the month of January 2022

### Results
#### (1) Finding patterns in the data with EDA
