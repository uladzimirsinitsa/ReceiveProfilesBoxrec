
i = 0
while i != 52350:
    item = 'https://boxrec.com/en/ratings?r%5Brole%5D=proboxer&r%5Bsex%5D=M&r%5Bdivision%5D=&r%5Bcountry%5D=&r%5Bstance%5D=&r%5Bstatus%5D=&r_go=&offset=' + str(i)
    with open('data/pages with links to profiles.csv', 'a') as file:
        file.write(item + '\n')
    i += 50
