import beautiful_date as bd

today = bd.BeautifulDate.fromisoformat("2026-09-08")

six_months_from_today = today + 6 * bd.months

print(today)
print(six_months_from_today)