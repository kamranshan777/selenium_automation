import csv

from correct_answers import CorrectAnswer



# class WriteCSV(CorrectAnswer):

def creat_csv(abcd):
    try:
        mydict = abcd
       # mydict = self.correctans.select_final_correct_ans()
        with open('csv_file_kamran.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=mydict.keys())
            writer.writeheader()
            writer.writerows([mydict])
    except FileNotFoundError as e:
        print(e)


