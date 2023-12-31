from pathlib import Path
from rembg import remove, new_session

session = new_session()

for file in Path('input').glob('*.jpg'):
    input_path = str(file)
    Path("output").mkdir(parents=True, exist_ok=True)
    output_path = str(Path('output') / (file.stem + ".png"))

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            print("Removing background from image: ", input_path)
            output = remove(input, session=session)
            o.write(output)
