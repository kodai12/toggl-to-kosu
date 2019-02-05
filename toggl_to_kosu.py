import csv


def main():
    with open('toggl_to_kosu.csv', 'r') as rf:
        reader = csv.reader(rf)
        next(reader)

        with open('output.csv', 'w', encoding='shift_jis') as wf:
            writer = csv.writer(wf, lineterminator='\n')
            for row in reader:
                description = row[5]
                date = row[7]
                duration = row[11]
                tag = row[-2]
                write_data_list = [
                        date,
                        description,
                        _duration_to_point(duration),
                        tag
                        ]
                writer.writerow(write_data_list)


def _duration_to_point(duration):
    (hour, minute, second) = str(duration).split(':')
    abs_minute = (int(hour) * 60) + int(minute)
    ratio = 1/(60/100)
    return "{0:.2f}".format((abs_minute * ratio)/100)


if __name__ == '__main__':
    main()
