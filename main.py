import json
import sys
from pathlib import Path

from census import Census
from us import states

api_username = sys.argv[1:][0]  # account for USPS API access

zip_path = Path.cwd() / "zip.tsv"
out_path = Path.cwd() / "out.tsv"
in_path = Path.cwd() / "MKE-Call-Center-10-5-22.tsv"

#  Values from
#  https://api.census.gov/data/2020/acs/acs5/profile/variables.html

bachelor_or_higher_amt = "DP02_0068E"
bachelor_or_higher_pct = "DP02_0068PE"
mean_household_income = "DP03_0063E"
english_only_amt = "DP02_0113E"
english_only_pct = "DP02_0113PE"
non_english_amt = "DP02_0114E"
non_english_pct = "DP02_0114PE"
race_white_amt = "DP05_0037E"
race_white_pct = "DP05_0037PE"
race_black_amt = "DP05_0038E"
race_black_pct = "DP05_0038PE"
race_asian_amt = "DP05_0044E"
race_asian_pct = "DP05_0044PE"
hispanic_latino_amt = "DP05_0070E"
hispanic_latino_pct = "DP05_0070PE"

variables = [
    bachelor_or_higher_amt,
    bachelor_or_higher_pct,
    mean_household_income,
    english_only_amt,
    english_only_pct,
    non_english_amt,
    non_english_pct,
    race_white_amt,
    race_white_pct,
    race_black_amt,
    race_black_pct,
    race_asian_amt,
    race_asian_pct,
    hispanic_latino_amt,
    hispanic_latino_pct
]

output_header = [
    "line.number",
    "zip.code",
    "bachelor.or.higher.amt",
    "bachelor.or.higher.pct",
    "mean.household.income",
    "english.only.amt",
    "english.only.pct",
    "non.english.amt",
    "non.english.pct",
    "race.white.amt",
    "race.white.pct",
    "race.black.amt",
    "race.black.pct",
    "race.asian.amt",
    "race.asian.pct",
    "hispanic.latino.amt",
    "hispanic.latino.pct",
    "address",
    "creation.date",
    "closed.date",
    "title",
    "closure.reason"
]

stats_by_zip = {}

c = Census(api_username)

if __name__ == "__main__":
    with out_path.open(mode="w", encoding="utf-8") as out_file:
        out_file.write("\t".join(output_header) + "\n")
        with zip_path.open(mode="w", encoding='utf-8') as zip_file:
            with in_path.open(encoding='utf-8') as call_center_data:
                line_num = -1  # track last list number processed
                for line in call_center_data.readlines():
                    line_num += 1

                    if line_num == 0:
                        continue  # don't print old header line
                    #  if line_num > 5:  # only print a few lines for testing
                    #      break

                    #  Excel put quotes around stuff, grrr...
                    parts = [part.strip("\"")
                             for part in str.split(line.strip(), "\t")]

                    zip = parts[1]

                    if zip not in stats_by_zip:
                        #  response is a list where element 0 is a dictionary having keys of
                        #  the variable values (e.g., DP02_0068E) passed to the API
                        response = c.acs5dp.state_zipcode(variables, states.WI.fips, zip)

                        print(zip, "\t", json.dumps(response[0]))
                        zip_file.write(zip + "\t" + json.dumps(response[0]) + "\n")
                        stats_by_zip[zip] = response[0]

                    stats = stats_by_zip[zip]

                    new_line = [
                        str(line_num),
                        zip
                    ]

                    for variable in variables:
                        new_line.append(str(stats[variable]))

                    new_line.extend(parts[2:])
                    out_file.write("\t".join(new_line) + "\n")
