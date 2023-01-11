from csv import writer
with open("class17-file.csv","w") as f:
          csv_writer=writer(f)
          csv_writer.writerow(["name","country"])
          csv_writer.writerow(["manju","INDIA"])
          csv_writer.writerow(["keerthi","INDIA"])

          # writerows([["name","country"],["manju","INDIA"],["keerthi","INDIA"]])