def t3():
    import pandas as pd
    import os, os.path
    file_loc = "./data"
    txt_file = file_loc + '/Tmax_UK.txt'
    csv_file = file_loc + '/Tmax_UK.csv'
    if os.path.exists(csv_file):
        os.remove(csv_file)
    colspec= [(1,9),
                (9,15),
                (15,23),
                (23,29),
                (29,37),
                (37,43),
                (43,51),
                (51,57),
                (57,65),
                (65,71),
                (71,79),
                (79,85),
                (85,93),
                (93,99),
                (99,107),
                (107,113),
                (113,121),
                (121,127),
                (127,135),
                (135,141),
                (141,149),
                (149,155),
                (155,163),
                (163,169),
                (169,177),
                (177,183),
                (183,191),
                (191,197),
                (197,205),
                (205,211),
                (211,219),
                (219,225),
                (225,233),
                (233,239)
                ]
    cols = [
        'JAN', 'Year1', 
        'FEB', 'Year2', 
        'MAR', 'Year3',
        'APR', 'Year4', 
        'MAY', 'Year5', 
        'JUN', 'Year6', 'JUL', 'Year7', 'AUG', 'Year8', 'SEP', 'Year9',
        'OCT', 'Year10', 'NOV', 'Year11', 'DEC', 'Year12', 'WIN', 'Year13', 'SPR',
        'Year14', 'SUM', 'Year15', 'AUT', 'Year16', 'ANN', 'Year17'
    ]
    
    df = pd.read_fwf(txt_file, 
                     #names=cols, 
                     #widths= length,
                     colspecs = colspec,
                     #delim_whitespace = True,
                     #skipinitialspace = True,
                     #encoding = 'utf-8',
                     #skiprows = [0]
                     ).to_csv(csv_file)
    #print(df)

with open('some/path/to/file.csv') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)
    Foo.objects.bulk_create([Foo(first_name=row[0], last_name=row[1]) for row in reader])