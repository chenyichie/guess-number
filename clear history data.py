from pickle import dump
data = []
with open('data.pkl', 'wb') as file:
    dump(data, file)
exit(0)
