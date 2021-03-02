def center_of_mass(data):
    """ Retorna uma tupla (cx, cy) que desenha o centro de data, que pode ser contorno ou matriz"""
    M = cv2.moments(data)
    # Usando a expressão do centróide definida em: https://en.wikipedia.org/wiki/Image_moment
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    return (int(cX), int(cY))
