#Affection

init python:
    h_affection = 0
    e_affection = 0
    l_affection = 0
    p_affection = 0
    def addAffection(chr, amount, notif = ''):
        global h_affection
        global e_affection
        global l_affection
        global P_affection
        if chr == 'h' or chr == 'hina':
            h_affection = h_affection + amount
        elif chr == 'e' or chr == 'emi':
            e_affection = e_affection + amount
        elif chr == 'l' or chr == 'leah':
            l_affection = l_affection + amount
        elif chr == 'p' or chr == 'pika':
            p_affection = p_affection + amount
        else:
            print('Character inexistant. (Function addAffection)')
        
        renpy.notify(notif + ' ' + chr.capitalize() + ' has gained ' + str(amount) + ' affection points for you!')
        