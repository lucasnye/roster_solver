import gspread

gc = gspread.service_account(filename="credentials/worshiproster-b0c59a53310e.json")
sh = gc.open("Worship Roster")
eligibility = sh.worksheet("Blackouts")
print(eligibility.get_all_records())