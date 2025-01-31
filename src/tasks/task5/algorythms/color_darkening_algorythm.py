def darkening_color(hex_color,amount):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

   
    darken_factor = 12

    r = max(r - int(darken_factor*(amount/1.5)), 0)
    g = max(g - int(darken_factor*(amount*1.5)), 0)
    b = max(b - int(darken_factor*amount), 0)

    return f'#{r:02X}{g:02X}{b:02X}'