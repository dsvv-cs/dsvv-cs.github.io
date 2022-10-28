from pathlib import Path
import subprocess

root = Path("assets/gallery")

other_formats_dir = Path(root.joinpath("other_formats"))
webp_dir = Path(root.joinpath("webp"))
webp_thumb_dir = Path(root.joinpath("webp/thumbnails"))

existing_webp_files = [i.name.split(".")[0]
                       for i in webp_dir.iterdir() if i.is_file()]
existing_webp_thumbnail_files = [
    i.name.split(".")[0] for i in webp_thumb_dir.iterdir() if i.is_file()]
existing_other_format_files = [
    i for i in other_formats_dir.iterdir() if i.is_file()]

for file in existing_other_format_files:
    f_name = file.name.split(".")[0]
    if f_name not in existing_webp_files:
        subprocess.run(
            F"cwebp {file.absolute()} -o assets/gallery/webp/{f_name}.webp")
    else:
        print(F"{f_name} already exists in webp root")
    if f_name not in existing_webp_thumbnail_files:
        subprocess.run(
            F"cwebp {file.absolute()} -q 1 -o assets/gallery/webp/thumbnails/{f_name}.webp")
    else:
        print(F"{f_name} already exists in thumbnails root")
