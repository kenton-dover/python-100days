cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    stringToReturn = ''
    for counter, car in enumerate(cars['Jeep'], 1):
        if counter != len(cars['Jeep']):
            stringToReturn += car + ", "
        else:
            stringToReturn += car
    return stringToReturn


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    listToReturn = []
    for key in cars.keys():
        listToReturn.append(cars[key][0])
    return listToReturn


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    listToReturn = []
    for value in cars.values():
        for item in value:
            if grep.lower() in item.lower():
                listToReturn.append(item)
    return sorted(listToReturn)


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    dictToReturn = {}
    for key in sorted(cars.keys()):
        dictToReturn[key] = sorted(cars[key])
    return dictToReturn

def main():
    print(get_all_jeeps())
    print(get_first_model_each_manufacturer())
    print(get_all_matching_models('co'))
    print(sort_car_models())

if __name__ == '__main__':
    main()