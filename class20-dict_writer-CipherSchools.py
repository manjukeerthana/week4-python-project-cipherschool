from csv import DictWriter
with open("file.csv","w") as f:
          csv_writer = DictWriter(f,fieldness=["firstname","lastname","age"])
          csv_writer.writeheader()
          csv_writer.writerow({
                    "firstname" : "maju",
                    "lastname": "keerthaa",
                    "age": 500
          })
          csv_writer.writerow({
                    "firstname" : "manju",
                    "lastname": "keerthi",
                    "age": 500
          })
          # writerows([
          #           {"firstname": "manju","lastname": "keerthana","age": 500},
          #           {"firstname": "manju","lastname": "keerthana","age": 500},
          #           {"firstname": "manju","lastname": "keerthana","age": 500},
          # ])