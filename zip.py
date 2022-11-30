import json
from pathlib import Path

bachelor_or_higher_pct = "DP02_0068PE"
mean_household_income = "DP03_0063E"
non_english_pct = "DP02_0114PE"
race_white_pct = "DP05_0037PE"
race_black_pct = "DP05_0038PE"
hispanic_latino_pct = "DP05_0071PE"

zip_path = Path.cwd() / "zip.tsv"
out_path = Path.cwd() / "zip.csv"
in_path = Path.cwd() / "call center zips.txt"

if __name__ == "__main__":
    zip_counts = {}

    # read in call center data logs
    with in_path.open(encoding='utf-8') as call_center_data:
        for line in call_center_data.readlines():
            zip_code = line.strip()
            # count the number of calls from each zip code
            if zip_code not in zip_counts:
                zip_counts[zip_code] = 1
            else:
                zip_counts[zip_code] += 1

    # write a CSV containing the zip code, demographics, and call count
    with out_path.open(mode="w", encoding="utf-8") as out_file:
        out_file.write("zip,education,income,nonenglish,white,black,hispanic,calls\n")

        # zip code data was stored as stringified JSON when originally retrieved from API
        # so must be parsed back into a JSON object
        with zip_path.open(encoding='utf-8') as zip_code_json:
            for line in zip_code_json.readlines():
                zip_code, json_str = str.split(line.strip(), "\t")

                json_obj = json.loads(json_str)
                if zip_code in zip_counts:
                    out_file.write(str.format("{},{},{},{},{},{},{},{}\n",
                                              zip_code,
                                              json_obj[bachelor_or_higher_pct],
                                              json_obj[mean_household_income],
                                              json_obj[non_english_pct],
                                              json_obj[race_white_pct],
                                              json_obj[race_black_pct],
                                              json_obj[hispanic_latino_pct],
                                              zip_counts[zip_code]))
                else:
                    print("No calls found for zip", zip_code)