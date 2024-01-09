def delay_srt_timing(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

        with open(output_file, 'w') as outfile:
            for line in lines:
                if '-->' in line:
                    start_time, end_time = line.strip().split(' --> ')
                    start_time_parts = start_time.split(':')
                    end_time_parts = end_time.split(':')

                    start_seconds = int(start_time_parts[0]) * 3600 + int(start_time_parts[1]) * 60 + float(start_time_parts[2].replace(',', '.'))
                    end_seconds = int(end_time_parts[0]) * 3600 + int(end_time_parts[1]) * 60 + float(end_time_parts[2].replace(',', '.'))

                    new_start_seconds = start_seconds + 10  # Delay timing by 10 seconds
                    new_end_seconds = end_seconds + 10  # Delay timing by 10 seconds

                    new_start_time = '{:02}:{:02}:{:.03f}'.format(
                        int(new_start_seconds // 3600),
                        int((new_start_seconds % 3600) // 60),
                        new_start_seconds % 60
                    )

                    new_end_time = '{:02}:{:02}:{:.03f}'.format(
                        int(new_end_seconds // 3600),
                        int((new_end_seconds % 3600) // 60),
                        new_end_seconds % 60
                    )

                    outfile.write("{0} --> {1}\n".format(new_start_time.replace('.', ','), new_end_time.replace('.', ',')))
                else:
                    outfile.write(line)

if __name__ == "__main__":
    input_file = "input.srt"  # Replace with your input SRT file
    output_file = "output.srt"  # Replace with the desired output file name
    delay_srt_timing(input_file, output_file)
    print("Subtitles delayed by 10 seconds. Modified subtitles saved to '{0}'".format(output_file))
