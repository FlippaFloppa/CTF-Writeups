from PIL import Image

lemur = Image.open("lemur.png")
pixels_lemur = lemur.load() 
flag = Image.open("flag.png")
res = flag.load()

for i in range(lemur.size[0]): #cycle pixels
    for j in range(lemur.size[1]):
        l = pixels_lemur[i,j]
        f = res[i,j]

        # We only need one color to read the flag
        red = l[0] ^ f[0]

        # Save result
        res[i,j] = (red)

flag.save("lemur_xor_flag.png")