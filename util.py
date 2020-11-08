def read_wind_data():
    '''Reads wind data from file'''
    data_file = open('wind_data.txt', 'r')
    width, height = data_file.readline().strip().split(' ')
    raw_wind_data = data_file.readline().strip().split(' ')
    wind_data = []
    for node in raw_wind_data:
        strength, direction = node.split('/')
        wind_data.append({'strength': int(strength),
                          'direction': int(direction)})
    return {'width': int(width), 'height': int(height)}, wind_data
