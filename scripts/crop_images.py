from PIL import Image
import os

folder = r"c:\Users\Test\portfolio-site\images"

processed = []
for fname in os.listdir(folder):
    if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(folder, fname)
        try:
            im = Image.open(path)
            w, h = im.size
            side = min(w, h)
            left = (w - side) // 2
            top = (h - side) // 2
            cropped = im.crop((left, top, left + side, top + side))
            out_name = os.path.splitext(fname)[0] + "_cropped.jpg"
            out_path = os.path.join(folder, out_name)
            cropped.convert("RGB").save(out_path, quality=95)
            print(f"Saved: {out_path}")
            processed.append(out_path)
        except Exception as e:
            print(f"Failed to process {path}: {e}")

if not processed:
    print("No images processed.")
else:
    print(f"Processed {len(processed)} image(s).")
