import re

def solution(new_id):

    def enddot(new_id) : #4
        if new_id.endswith('.') :
            new_id = new_id[:-1]

        return new_id


    new_id = new_id.lower() #1

    new_id = re.sub('[^\w.-]', '', new_id) #2

    while '..' in new_id:
        new_id = new_id.replace('..', '.') #3

    if new_id.startswith('.'): #4
        new_id = new_id[1:]
    new_id = enddot(new_id)

    if not new_id : #5
        new_id = 'a'

    if len(str(new_id)) > 15 : #6
        new_id = new_id[:15]
        new_id = enddot(new_id)

    if len(str(new_id)) < 3 : #7
        s = new_id[-1]
        for i in range(3) :
            new_id = new_id + s
            if len(str(new_id)) == 3 :
                break

    return new_id
