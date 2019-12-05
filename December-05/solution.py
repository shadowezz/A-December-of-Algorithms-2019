import csv
table_header = ""
table_body = ""
with open("../src/res/csv_to_html_res.csv", 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for row in reader:
        if (line == 0):
            table_header += "<tr>"
            for header in row:
                table_header += "<th>{}</th>".format(header)
            table_header += "</tr>"
            line += 1
        else:
            table_body += "<tr>"
            for item in row:
                table_body += "<td>{}</td>".format(item)
            table_body += "</tr>"

with open("table.html", "w") as html_file:
    html_file.write("<html><body><table>" + table_header + table_body + "</table></body></html>")
    
