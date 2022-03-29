import face_recognition


knownimage = face_recognition.load_image_file("example.jpg")

unknownimage = face_recognition.load_image_file("example_2.jpg")

knownencoding = face_recognition.face_encodings(knownimage)[0]
unknownencoding = face_recognition.face_encodings(unknownimage)[0]

results = face_recognition.compare_faces([knownencoding],unknownencoding)

if results[0] == True:
    print("Image Matched")
else:
    print("No match")
