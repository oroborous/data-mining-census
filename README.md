# Milwaukee OpenData Call Center Records

Processes the combined [historical call center records](https://data.milwaukee.gov/dataset/callcenterdatahistorical)
and [current call center records](https://data.milwaukee.gov/dataset/callcenterdatacurrent) from the Milwaukee OpenData portal. Current records were downloaded on October 5, 2022.

Enriches each line with demographic information from the [US Census American Community Survey 5-Year Data](https://www.census.gov/data/developers/data-sets/acs-5year.html) (Data Profiles).

The following [variables](https://api.census.gov/data/2020/acs/acs5/profile/variables.html) are queried by ZIP code:

- **DP02_0068E**:  Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!Mean household income (dollars)
- **DP02_0068PE**:  Percent!!EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor's degree or higher
- **DP03_0063E**:  Estimate!!INCOME AND BENEFITS (IN 2020 INFLATION-ADJUSTED DOLLARS)!!Total households!!Mean household income (dollars)
- **DP02_0113E**:  Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!English only
- **DP02_0113PE**:  Percent!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!English only
- **DP02_0114E**:  	Estimate!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Language other than English
- **DP02_0114PE**:  Percent!!LANGUAGE SPOKEN AT HOME!!Population 5 years and over!!Language other than English
- **DP05_0037E**:  Estimate!!RACE!!Total population!!One race!!White
- **DP05_0037PE**:  Percent!!RACE!!Total population!!One race!!White
- **DP05_0038E**:  Estimate!!RACE!!Total population!!One race!!Black or African American
- **DP05_0038PE**:  Percent!!RACE!!Total population!!One race!!Black or African American
- **DP05_0044E**:  Estimate!!RACE!!Total population!!One race!!Asian
- **DP05_0044PE**:  Percent!!RACE!!Total population!!One race!!Asian
- **DP05_0071E**:  Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)
- **DP05_0071PE**:  Percent!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)


## Usage instructions
Register for a free account at [Census.gov](https://api.census.gov/data/key_signup.html). You will receive a confirmation email containing your API key. 

Run `main.py APIKEY` where *APIKEY* is the API key provided in the registration confirmation email.

## Dependencies (see requirements.txt)
- census 0.8.19
- us 2.0.2

## Input data
Input data (Data  w 141 blank removed 10-25.txt) is tab-delimited, with the following columns. It contains a header row.

- line.number
- zip
- address
- creation.date
- closed.date
- title
- closure.reason

### Sample input data

<pre>
line.number	zip	address	creation.date	closed.date	title	closure.reason
2	53208	"1626 N 59TH ST, MILWAUKEE, WI, 53208-2146"	2022-09-27T00:00:00Z	2022-09-27T00:00:00Z	Broken Branch Down - Not Blocking	"Windstorm damage. Several large branches down. Stacked on boulevard in two piles, about 3 cu/yds"
3	53206	"3231 N 25TH ST, MILWAUKEE, WI, 53206-1235"	2022-09-27T00:00:00Z		Scattered Litter and Debris on Private Property	NEXT TO GARBAGE CARTS
4	53206	"3229 N 23RD ST, MILWAUKEE, WI, 53206-1728"	2022-09-27T00:00:00Z		Scattered Litter and Debris on Private Property	NEXT GARBAGFE CARTS
5	53207	"458 E BOLIVAR AV, MILWAUKEE, WI, 53207-5020"	2022-09-27T00:00:00Z		Weeds and Tall Grass Complaint	Rear
6	53206	"1720 W CLARKE ST, MILWAUKEE, WI, 53206-2030"	2022-09-27T00:00:00Z		Garbage Cart: No Cart	Single home. Always had 2 carts
</pre>


## Output data
Output data (out.tsv) is tab-delimited, with the following columns. The file includes a header line.

- line.number
- zip.code
- bachelor.or.higher.amt
- bachelor.or.higher.pct
- mean.household.income
- english.only.amt
- english.only.pct
- non.english.amt
- non.english.pct
- race.white.amt
- race.white.pct
- race.black.amt
- race.black.pct
- race.asian.amt
- race.asian.pct
- hispanic.latino.amt
- hispanic.latino.pct
- address
- creation.date
- closed.date
- title
- closure.reason

### Sample output data

<pre>
line.number	zip.code	bachelor.or.higher.amt	bachelor.or.higher.pct	mean.household.income	english.only.amt	english.only.pct	non.english.amt	non.english.pct	race.white.amt	race.white.pct	race.black.amt	race.black.pct	race.asian.amt	race.asian.pct	hispanic.latino.amt	hispanic.latino.pct	address	creation.date	closed.date	title	closure.reason
1	53208	5322.0	28.9	54100.0	21650.0	81.9	4799.0	18.1	10500.0	36.0	11978.0	41.0	3685.0	12.6	29205.0	29205.0	1626 N 59TH ST, MILWAUKEE, WI, 53208-2146	2022-09-27T00:00:00Z	2022-09-27T00:00:00Z	Broken Branch Down - Not Blocking	Windstorm damage. Several large branches down. Stacked on boulevard in two piles, about 3 cu/yds
2	53206	852.0	6.1	42126.0	19833.0	93.6	1366.0	6.4	526.0	2.2	22017.0	93.2	242.0	1.0	23612.0	23612.0	3231 N 25TH ST, MILWAUKEE, WI, 53206-1235	2022-09-27T00:00:00Z		Scattered Litter and Debris on Private Property	NEXT TO GARBAGE CARTS
3	53206	852.0	6.1	42126.0	19833.0	93.6	1366.0	6.4	526.0	2.2	22017.0	93.2	242.0	1.0	23612.0	23612.0	3229 N 23RD ST, MILWAUKEE, WI, 53206-1728	2022-09-27T00:00:00Z		Scattered Litter and Debris on Private Property	NEXT GARBAGFE CARTS
4	53207	11198.0	40.2	77172.0	30827.0	88.4	4044.0	11.6	31551.0	85.0	1140.0	3.1	401.0	1.1	37103.0	37103.0	458 E BOLIVAR AV, MILWAUKEE, WI, 53207-5020	2022-09-27T00:00:00Z		Weeds and Tall Grass Complaint	Rear
5	53206	852.0	6.1	42126.0	19833.0	93.6	1366.0	6.4	526.0	2.2	22017.0	93.2	242.0	1.0	23612.0	23612.0	1720 W CLARKE ST, MILWAUKEE, WI, 53206-2030	2022-09-27T00:00:00Z		Garbage Cart: No Cart	Single home. Always had 2 carts
</pre>

### Sample ZIP output data

ZIP code data from the API is also written to a separate file: `zip.tsv`.

<pre>
53208	{"DP02_0068E": 5322.0, "DP02_0068PE": 28.9, "DP03_0063E": 54100.0, "DP02_0113E": 21650.0, "DP02_0113PE": 81.9, "DP02_0114E": 4799.0, "DP02_0114PE": 18.1, "DP05_0037E": 10500.0, "DP05_0037PE": 36.0, "DP05_0038E": 11978.0, "DP05_0038PE": 41.0, "DP05_0044E": 3685.0, "DP05_0044PE": 12.6, "DP05_0070E": 29205.0, "DP05_0070PE": 29205.0, "zip code tabulation area": "53208"}
53206	{"DP02_0068E": 852.0, "DP02_0068PE": 6.1, "DP03_0063E": 42126.0, "DP02_0113E": 19833.0, "DP02_0113PE": 93.6, "DP02_0114E": 1366.0, "DP02_0114PE": 6.4, "DP05_0037E": 526.0, "DP05_0037PE": 2.2, "DP05_0038E": 22017.0, "DP05_0038PE": 93.2, "DP05_0044E": 242.0, "DP05_0044PE": 1.0, "DP05_0070E": 23612.0, "DP05_0070PE": 23612.0, "zip code tabulation area": "53206"}
53207	{"DP02_0068E": 11198.0, "DP02_0068PE": 40.2, "DP03_0063E": 77172.0, "DP02_0113E": 30827.0, "DP02_0113PE": 88.4, "DP02_0114E": 4044.0, "DP02_0114PE": 11.6, "DP05_0037E": 31551.0, "DP05_0037PE": 85.0, "DP05_0038E": 1140.0, "DP05_0038PE": 3.1, "DP05_0044E": 401.0, "DP05_0044PE": 1.1, "DP05_0070E": 37103.0, "DP05_0070PE": 37103.0, "zip code tabulation area": "53207"}
53221	{"DP02_0068E": 6717.0, "DP02_0068PE": 23.9, "DP03_0063E": 68176.0, "DP02_0113E": 25524.0, "DP02_0113PE": 69.5, "DP02_0114E": 11226.0, "DP02_0114PE": 30.5, "DP05_0037E": 28462.0, "DP05_0037PE": 71.9, "DP05_0038E": 2181.0, "DP05_0038PE": 5.5, "DP05_0044E": 2997.0, "DP05_0044PE": 7.6, "DP05_0070E": 39602.0, "DP05_0070PE": 39602.0, "zip code tabulation area": "53221"}
53216	{"DP02_0068E": 3306.0, "DP02_0068PE": 17.3, "DP03_0063E": 48263.0, "DP02_0113E": 26922.0, "DP02_0113PE": 92.0, "DP02_0114E": 2352.0, "DP02_0114PE": 8.0, "DP05_0037E": 3763.0, "DP05_0037PE": 12.0, "DP05_0038E": 25305.0, "DP05_0038PE": 80.4, "DP05_0044E": 811.0, "DP05_0044PE": 2.6, "DP05_0070E": 31476.0, "DP05_0070PE": 31476.0, "zip code tabulation area": "53216"}
</pre>

Run `zip.py` to ingest this file and create a new output file (zip.csv) that contains a summary of call counts per zip code.

### Sample call count summary output data

<pre>
zip,education,income,nonenglish,white,black,hispanic,calls
53208,28.9,54100,18.1,36,41,8.1,5690
53206,6.1,42126,6.4,2.2,93.2,1.8,7679
53207,40.2,77172,11.6,85,3.1,16.2,6999
</pre>