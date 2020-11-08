def read_data():
    data_file = open('data.txt', 'r')
    width, height = data_file.readline().strip().split(' ')
    raw_wind_data = data_file.readline().strip().split(' ')
    wind_data = []
    for node in raw_wind_data:
        strength, direction = node.split('/')
        wind_data.append({'strength': int(strength),
                          'direction': int(direction)})
    return {'width': int(width), 'height': int(height)}, wind_data


def main():
    dimensions, wind_data = read_data()
    print(dimensions, wind_data)


if __name__ == '__main__':
    main()
