import json

test_data_old = {
    "columns":
    ["CASES_ID",
     "CASE_NAME",
     "PROJECT_CODE",
     "CASE_LEVEL",
     "CASE_TYPE",
     "REMARKS",
     "INPUT_STRING",
     "EXPECTED_OUTPUT",
     "GH_PROPERTY",
     "PT_PROPERTY",
     "GS_PROPERTY",
     "KF_PROPERTY",
     "ZYX",
     "GM"
     ],

    "rows":
    [ ["3fba459b589b49ebb9a069e5931f2154",
      "\u8425\u8fd0-\u666e\u901a\u4fe1\u606f\u4fee\u6539-\u4e2a\u4eba\u5ba2\u6237-\u5de5\u4f5c\u5355\u4f4d\u4f20\u7a7a",
      "",
      "CASE_LEVEL_HIGH",
      "",
      "\u524d\u63d0\u6761\u4ef6\uff1a\n1.\u4e2a\u4eba\u5ba2\u6237\uff1b\n2.\u5de5\u4f5c\u5355\u4f4d\u4e3a\u7a7a\uff08cc_workplace\uff09\n\u6267\u884c\uff1a\n\u8c03\u7528121068\u529f\u80fd\u53f7\u6d4b\u8bd5;",
      "\u4fee\u6539\u6210\u529f,custoccinfo.cc_workplace\u4e3a\u7a7a;",
      "",
      "",
      "",
      "",
      "",
      "",
      ""],
    ["3fba459b589b49ebb9a069e5931f2154",
      "\u8425\u8fd0-\u666e\u901a\u4fe1\u606f\u4fee\u6539-\u4e2a\u4eba\u5ba2\u6237-\u5de5\u4f5c\u5355\u4f4d\u4f20\u7a7a",
      "",
      "CASE_LEVEL_HIGH",
      "",
      "\u524d\u63d0\u6761\u4ef6\uff1a\n1.\u4e2a\u4eba\u5ba2\u6237\uff1b\n2.\u5de5\u4f5c\u5355\u4f4d\u4e3a\u7a7a\uff08cc_workplace\uff09\n\u6267\u884c\uff1a\n\u8c03\u7528121068\u529f\u80fd\u53f7\u6d4b\u8bd5;",
      "\u4fee\u6539\u6210\u529f,custoccinfo.cc_workplace\u4e3a\u7a7a;",
      "",
      "",
      "",
      "",
      "",
      "",
      "",
      ""
     ]

    ]
}


test_data_old = json.dumps(test_data_old)


test_data_old = json.loads(test_data_old)
columns = test_data_old["columns"]
rows = test_data_old["rows"]
test_data = []

if "INPUT_STRING" in columns:
    input_index = columns.index("INPUT_STRING")
    columns[input_index] = "INPUT_STRING_SET"

if "EXPECTED_OUTPUT" in columns:
    output_index = columns.index("EXPECTED_OUTPUT")
    columns[output_index] = "EXPECTED_OUTPUT_SET"

for row in rows:
    new_row = {columns[index]: row[index] for index in range(len(columns))}
    test_data.append(new_row)


print(test_data)