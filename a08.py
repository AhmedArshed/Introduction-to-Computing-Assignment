## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(results):
    sum = 0
    list =[]
    m =()
    k =0
    for i in results:
        for j in range(2,len(i)):
            if results[k][j] == None:
                sum = sum + 0
            else:
                sum = sum + results[k][j]
        m = m+(results[k][0],)
        m = m+(results[k][1],)
        m =m+(sum,)
        list = list+[m]
        m=()
        sum = 0
        k=k+1
    return list
#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###

#### End OF MARKER





if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]

    print find_cumulative_marks(results)
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print find_top_student(results)
    # output: ('p101111', 'Ali Khayam')
