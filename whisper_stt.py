import whisper
from whisper.utils import WriteSRT
from datetime import timedelta

def format_timestamp(timestamp: float, always_include_hours: bool = False, decimal_marker: str = ".") -> str:
    """
    Formats a timestamp in seconds to SRT format (hours:minutes:seconds,milliseconds).
    """
    delta = timedelta(seconds=timestamp)
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int(delta.microseconds / 1000)
    if always_include_hours or hours > 0:
        return f"{hours:02}:{minutes:02}:{seconds:02}{decimal_marker}{milliseconds:03}"
    else:
        return f"{minutes:02}:{seconds:02}{decimal_marker}{milliseconds:03}"


def run(input_path: str, output_path: str) -> None:
    model = whisper.load_model("base")
    result = model.transcribe(input_path)

    with open(output_path, "w", encoding="utf-8") as srt_file:
        writer = WriteSRT(srt_file)
        for i, segment in enumerate(result["segments"], start=1):
            # split lines longer than 33 characters into multiple lines
            text = segment['text'].strip().replace('-->', '->')
            lines = [text[j:j+30] for j in range(0, len(text), 30)]
            text = '\n'.join(lines)
            # write srt lines
            print(
                f"{i}\n"
                f"{format_timestamp(segment['start'], always_include_hours=True, decimal_marker=',')} --> "
                f"{format_timestamp(segment['end'], always_include_hours=True, decimal_marker=',')}\n"
                f"{text}\n",
                file=srt_file,
                flush=True,
            )

    return print("subtitles created..")
