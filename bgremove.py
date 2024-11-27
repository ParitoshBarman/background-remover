# from rembg import remove
# import cv2

# input_path = 'confidentStudent.png'
# output_path = 'output.png'

# input = cv2.imread(input_path)
# output = remove(input)
# cv2.imwrite(output_path, output)



from rembg import remove

input_path = 'confidentStudent.png'
output_path = 'output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

# curl -s confidentStudent.png | rembg i > output.png
# rembg i confidentStudent.png output.png