
import csv
import sys

####################

def ExamTwo(file):
    data = []
    max_column_widths = [0]*5
    maxwidth= 0 

    with open(file,"r") as openfile:

        for line in openfile:
            line = line.strip()

            if not line:
                continue

            y = line.split(',')

            cleanrow = []

            for i, item in enumerate(y):
                cleanitem = item.strip()

                if i == 4:

                    cleanitem_val = float(cleanitem)
                    cleanrow.append(cleanitem_val)

                    formatted_price_len = len(f"${cleanitem_val:,.2f}")
                    if formatted_price_len > max_column_widths[i]:
                        max_column_widths[i] = formatted_price_len

                    if formatted_price_len > maxwidth:
                        maxwidth = formatted_price_len

                else:
                    cleanrow.append(cleanitem)

                    if len(cleanitem) > max_column_widths[i]:
                        max_column_widths[i] = len(cleanitem)

                    if len(cleanitem) > maxwidth:
                        maxwidth = len(cleanitem)

            data.append(cleanrow)

        align = [w + 2 for w in max_column_widths]

    zipcodes = []

    for property_row in data:
        zip_code = property_row[3]
        price = property_row[4]
        
        found = False
        for zipcode_row in zipcodes:
            if zip_code == zipcode_row[0]:
                zipcode_row[1] += 1
                zipcode_row[2] += price
                found = True
                break
        
        if not found:
            zipcodes.append([zip_code, 1, price])

    max_zip_width = len("Zipcode")
    max_count_width = len("count")
    max_avg_width = len("Average")

    for row in zipcodes:
        if len(row[0]) > max_zip_width:
            max_zip_width = len(row[0])

        avg_price = row[2] / row [1]
        formatted_avg = f"${avg_price:,.2f}"
        if len(formatted_avg) > max_avg_width:
            max_avg_width = len(formatted_avg)

    align_zip = max_zip_width +4
    align_count = max_count_width +4
    align_avg = max_avg_width +4

    print(f"{'Zipcode':>{align_zip}}{'count':>{align_count}}{'Average':>{align_avg}}")

    for row in zipcodes:
        zipcodes = row[0]
        count = row[1]
        sum_of_prices = row[2]

        average_price = sum_of_prices / count

        formatted_average = f"${average_price:,.2f}"

        print(f"{zip_code:>{align_zip}}{count:>{align_count}}{formatted_average:>{align_avg}}")

ExamTwo('Exam 2/Exam Two Properties.csv')