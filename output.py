def sen(fname):
    import pandas as pd
    fi = pd.read_excel(fname)
    print("outpput run "+fname)
    fin=fi.values.tolist()
    print(fin)
    subset_df = fi[fi["Unnamed: 2"] == 1]
    print(str(subset_df.count()))

    import openpyxl
    path = fname
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    fi = pd.read_excel(path)
    print("outpput run " + path)
    fin = fi.values.tolist()
    ro=len(fin)
    print(fin[0][0])

    fileout = open("C:/Users/admin/PycharmProjects/Amazon_review/templates/table.html", "w")

    table = "<table border=1>\n"

    table += "  <tr>\n"
    table += "<th>Name</th>\n"
    table += "<th>Rating</th>\n"
    table += "<th>Review</th>\n"
    table += "<th>Sentiment</th>\n"
    table += "<th>Class</th>\n"
    table += "  </tr>\n"

    for i in range(ro):
        table += "  <tr>\n"
        for j in range(5):
            table += "    <td>{0}</td>\n".format(fin[i][j])
        table += "  </tr>\n"

    table += "</table>"

    fileout.writelines(table)
    fileout.close()
    wb_obj.close()
    print("output file")
