import cv2

# Resmi oku
image_path = "beyaz.jpg"
image = cv2.imread(image_path)
resized_image = cv2.resize(image, (240, 180))

# Dikdörtgenin koordinatları ve renk
rect_coordinates = [100.19007110595703, 4.141937255859375, 211.35031127929688, 178.08038330078125]
rect_color = (0, 255, 0) 
rect_thickness = 2

# Dikdörtgeni çiz
cv2.rectangle(resized_image, (int(rect_coordinates[0]), int(rect_coordinates[1])),
              (int(rect_coordinates[2]), int(rect_coordinates[3])), rect_color, rect_thickness)


# Dikdörtgenin merkez koordinatları
center_x = int((rect_coordinates[0] + rect_coordinates[2]) / 2)
center_y = int((rect_coordinates[1] + rect_coordinates[3]) / 2)
# Kare çizim için koordinatlar
square_size = 4
square_start_point = (center_x - square_size // 2, center_y - square_size // 2)
square_end_point = (center_x + square_size // 2, center_y + square_size // 2)
square_color = (0, 0, 255) 

# Kare çiz
cv2.rectangle(resized_image, square_start_point, square_end_point, square_color, rect_thickness)




# Sonucu göster
cv2.imshow('Resized Image with Rectangle', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()