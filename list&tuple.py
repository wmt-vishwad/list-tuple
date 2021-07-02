
def firstlast(sequence):
    return sequence[0] + sequence[-1]


t1 = ('a', 'b', 'c')
output1 = firstlast(t1)
print(output1)

t2 = (1, 2, 3, 4)
output2 = firstlast(t2)
print(output2)


def firstlast(sequence):
    return sequence[:1] + sequence[-1:]

print(firstlast('abcd'))



from operator import itemgetter
people = [('donald', 'trump', 7.85),
          ('viadimir', 'putin', 3.636),
          ('jinping', 'xi', 10.603)]

def format_sort_records(list_of_tuples):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for one_person in sorted(list_of_tuples, key=itemgetter(1, 0)):
        output.append(template.format(*one_person))
    return output

print('\n'.join (format_sort_records(people)))



words = ['this', 'is', 'an', 'elementary', 'example']

#from collections import counter
#def most_repeating_letter_count(words):
 #   return counter(words).most_common[1][0][2]

#def most_repeating_letter_count(words):
 #   return max(words, key=most_repeating_letter_count)
#most_repeating_letter_count(words)



peoples = [{'first' : 'abc', 'last': 'lerner',
           'email' :'abc@lerner.co.il'},
           {'first': 'xyz', 'last': 'len',
            'email': 'xyz@len.gov'},
           {'first' : 'pqr', 'last': 'putin',
           'email' :'president@pqr.ru'}]

def person_to_tuples(person_dict):
    return person_dict['last'], person_dict['first']
for one_person in peoples:
    print(person_to_tuples(one_person))

sorted(peoples, key=person_to_tuples)


from operator import itemgetter
person_to_tuples = itemgetter('last', 'first')
for one_person in peoples:
    print(person_to_tuples(one_person))

def alphabets_names(lists_of_dicts):
    return sorted(peoples, key=itemgetter('first', 'last'))
alphabets_names(peoples)


def mysum(*items):
    if not items:
        return items
    output = items[0]
    for one_item in items[1:]:
        output += one_item
    return output
print (mysum(10, 20, 30))
print(mysum(100, 200, 300, 400, 500))
