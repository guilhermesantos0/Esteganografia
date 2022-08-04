from stegano import lsb
import sys

if sys.argv[1] == "-e":
    image = sys.argv[2]
    filename = sys.argv[3]
    message = ' '.join(sys.argv[4:])

    secret = lsb.hide(image, message)

    secret.save(filename)
elif sys.argv[1] == "-d":
    image = sys.argv[2]

    print(lsb.reveal(image))
else:
    print("tu ta me sacaneando ne?")