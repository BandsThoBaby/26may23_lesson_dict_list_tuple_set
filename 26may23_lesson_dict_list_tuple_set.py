#dictionary 

jordans_dictionary = {'used':['Yeezys1', 'Converses1', 'jordans1'], 'new':['Yeezys', 'Converses', 'jordans']
                      }

#print(jordans_dictionary)

jordans_dictionary['used']
#print(jordans_dictionary['used'])

for shoes in jordans_dictionary.values():
    print(shoes)
    for brands in shoes:
        print(brands)