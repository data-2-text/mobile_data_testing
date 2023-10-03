import phrazor
import json
phrazor.API_KEY = "2dc31051-60a7-42b2-8cab-46a017e267c2"
phrzr = phrazor.Phrazor()

phrzr.set_data({
  "Sales Person": [
    "John Doe",
    "Mike Johnson",
    "Sarah Brown",
    "John Doe",
    "Mike Johnson",
    "Sarah Brown",
    "John Doe",
    "Mike Johnson",
    "Sarah Brown"
  ],
  "Date": [
    "2023-01-01T10:00:00",
    "2023-01-01T10:15:00",
    "2023-01-01T10:30:00",
    "2023-02-01T11:00:00",
    "2023-02-01T11:15:00",
    "2023-02-01T11:30:00",
    "2023-03-01T12:00:00",
    "2023-03-01T12:15:00",
    "2023-03-01T12:30:00"
  ],
   "Amount": [
    500,
    300,
    100,
    1000,
    250,
    90,
    750,
    380,
    250
  ]
})

phrzr.set_column_meta(
  date_column="Date",
  metric_column="Amount",
  dimension_column="Sales Person"
)

insights = phrzr.get_insights('descriptor')

print(json.dumps(insights, indent=4))