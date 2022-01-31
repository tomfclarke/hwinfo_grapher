import argparse
import hwinfo_grapher as grapher

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file', type=str, help='CSV file generated from HWInfo logging.')
    parser.add_argument('keys', nargs='*', help='Keys to plot.')
    parser.add_argument('-l', '--list-keys', action='store_true', help='Lists available keys in the CSV file.')
    options = parser.parse_args()

    data = grapher.parse_csv(options.csv_file)

    if(options.list_keys):
        if(len(data) > 0):
            keys = list(data[0].keys())
            keys.remove("Date")
            keys.remove("Time")
            keys = ['\t' + key for key in keys]
            print('Available keys:')
            for key in keys:
                print(key)
            exit(0)
        else:
            print('No keys found in the provided CSV file!')
            exit(-1)
    elif options.keys:
        # print(options.keys)
        grapher.plot(data, options.keys)
    else:
        print('Please provide at least one key to plot.')
        exit(-1)
