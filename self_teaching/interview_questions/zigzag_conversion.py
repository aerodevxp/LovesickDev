#The Zigzag Conversion
#
#I was watching a video on Youtube about someone's software engineering
#journey and there is a part of the video where he says he went to an
#interview and did not get the job because he couldn't solve the zig-
#-zag conversion interview question and that he still does not under-
#-stand it to this day even after years in the industry. I took it
#upon myself to try to solve it once I saw what the question was.
#...And I did it! With absolutely no help from any search engine or
#any type of module to help (as you can see, there are no imports).
#Video link: youtube.com/watch?v=fehAgOqTR44
#This took me around three hours max to make... which isn't very good
#Considering this is a potential interview question, but I feel proud
#Of myself for completing and understanding this problem by myself
#Without having gone to any coding school yet. To be fair, this was
#Mostly about mathematical thinking more than usual code and it was
#Not very fun to make as... honestly, I don't see why ANYONE would ever
#Want a zigzag string like this, but it did sharpen my problem-solving
#By forcing me to solve, all by myself, a problem I never even knew
#Anyone would need solved. I am sure this is not the most efficient way
#To go about this, but for a first time, I'm really happy I got it to
#Work without any external mathematical help from the Internet. This
#Program was extremely easy to code language wise, but creating (or
#more like discovering) the formulas and equations needed to pull
#Is what took most, if not all of my time.

#Started and finished on Feb. 23, 2023
#By Raphael B.

og_string = "PAYPALISHIRING"

def convert(txt, row_amount):
    og_txt = txt
    result = ''
    columns = []
    rows = []
    solo_columns = []

    normal_column_amount = len(txt)/row_amount
    solo_column_amount = 0
    for chr_index in range(len(txt)):
        if chr_index % (row_amount+1) == row_amount:
            #individual columns
            solo_columns.append([txt[chr_index]])
            solo_column_amount += 1
    group_column_amount = ((len(txt) - solo_column_amount)/row_amount).__round__()
    print(len(txt), solo_column_amount, group_column_amount)

    all_columns = []

    for group_column_index in range(group_column_amount):
        column = []
        base_string_index = group_column_index*(row_amount+1)
        column.append(txt[base_string_index:base_string_index+(row_amount)])
        columns.append(column)
        
    for column_index in range(group_column_amount):
        all_columns.append(columns[column_index])
        if len(solo_columns) > 0:
            all_columns.append(solo_columns[0])
            solo_columns.pop(0)

    columns = all_columns

    #And finally, adding to string (by row)
    rows = [''] * row_amount
    for column in columns:
        rowIndex = 0
        for chrs in column:
            if len(chrs) == 1:
                #Solo lane
                rows[((row_amount/2)).__round__() - 1]+=chrs[0]
            else:
                for chr in chrs:
                    rows[rowIndex] += chr
                    rowIndex += 1
                    print(chr)
        
    for row in rows:
        for chrs in row:
            for chr in chrs:
                result += chr
    
    print(columns)
    print(rows)

    return result

print(convert(og_string, 3))