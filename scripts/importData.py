import csv
from louisville_crime.models import *
def run():
    with open('/home/jtgiss01/Downloads/CData.csv', 'rb') as csvfile:
        cvr = csv.reader(csvfile, delimiter='\t')
        for row in cvr:
            i = Incident(incident_date = row[17],
                    date_reported = row[3],
                    time_reported = row[4],
                    case_number = row[1],
                    address = row[5],
                    city = row[13],
                    zip_code = row[6],
                    beat = row[10],
                    crime = row[2],
                    category = row[12],
                    division = row[7],
                    sector = row[9],
                    incident_beat = row[8]
                    )
            i.save()
