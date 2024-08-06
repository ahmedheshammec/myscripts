import re
from datetime import timedelta

# Function to convert SRT time format to timedelta
def srt_time_to_timedelta(time_str):
    hours, minutes, seconds = time_str.split(':')
    seconds, milliseconds = seconds.split(',')
    return timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds), milliseconds=int(milliseconds))

# Read the SRT file
srt_file = '/Volumes/Samsung T5/Second Draft/captions.srt'
with open(srt_file, 'r', encoding='utf-8') as f:
    srt_content = f.read()

# Parse SRT content
subtitles = []
pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n((?:.+\n?)+)')
matches = pattern.findall(srt_content)

for match in matches:
    index, start_time, end_time, text = match
    start = srt_time_to_timedelta(start_time)
    end = srt_time_to_timedelta(end_time)
    subtitles.append((start, end, text.strip().replace('\n', '<br />')))

# Helper function to convert timedelta to the TTML format
def to_ttml_time(td):
    hours, remainder = divmod(td.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int((seconds - int(seconds)) * 1000)
    seconds = int(seconds)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{milliseconds:03}"

# Create ITT content
itt_content = '<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml">\n<body>\n<div>\n'
for start, end, text in subtitles:
    start = to_ttml_time(start)
    end = to_ttml_time(end)
    itt_content += f'<p begin="{start}" end="{end}">{text}</p>\n'
itt_content += '</div>\n</body>\n</tt>'

# Save ITT file
output_file = '/Volumes/Samsung T5/Second Draft/captions.itt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(itt_content)

print(f"ITT file saved as {output_file}")