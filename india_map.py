from turtle import *

hideturtle()
speed(0)

Screen().bgcolor('#f3f3fe')

def myposition(x, y):
    penup()
    goto(x - 300, (y * -1) + 365)
    pendown()


def positions():
    positions.upper_india = [(157, 473), (157, 469), (155, 464), (156, 461), (154, 457), (151, 452), (153, 449), (149, 445), (149, 440), (148, 434), (148, 428), (148, 424), (146, 420), (148, 416), (148, 410), (151, 406), (147, 395), (147, 391), (149, 389), (149, 385), (146, 383), (149, 379), (146, 378), (146, 375), (144, 378), (143, 383), (144, 388), (140, 394), (134, 398), (129, 399), (126, 402), (118, 402), (115, 404), (107, 399), (96, 388), (90, 381), (86, 376), (82, 372), (80, 366), (83, 363), (86, 363), (89, 366), (97, 365), (104, 362), (108, 359), (108, 356), (100, 358), (91, 361), (82, 356), (77, 352), (71, 343), (66, 341), (69, 339), (69, 332), (78, 333), (78, 327), (82, 325), (93, 329), (96, 327), (100, 332), (104, 332), (105, 329), (109, 328), (116, 326), (118, 330), (122, 326), (122, 321), (116, 309), (117, 305), (112, 305), (106, 295), (108, 286), (99, 282), (96, 276), (99, 270), (106, 266), (111, 259), (122, 255), (123, 263), (128, 260), (141, 259), (143, 255), (148, 252), (148, 247), (153, 241), (159, 241), (169, 228), (168, 224), (173, 219), (180, 216), (180, 210), (186, 205), (189, 198), (191, 190), (190, 185), (199, 178), (205, 178), (204, 173), (194, 170), (194, 165), (188, 165), (185, 162), (175, 158), (177, 150), (174, 141), (177, 136), (174, 132), (174, 127), (188, 118), (183, 117), (179, 113), (178, 109), (176, 111), (170, 103), (162, 103), (160, 95), (167, 92), (168, 87), (171, 84), (182, 84), (191, 80), (198, 78), (208, 79), (218, 90), (227, 95), (231, 98), (234, 104), (241, 106), (244, 111), (253, 109), (257, 105), (265, 101), (271, 103), (275, 99), (283, 104), (291, 110), (291, 116), (287, 121), (287, 127), (282, 127), (282, 131), (278, 131), (274, 141), (268, 139), (266, 142), (269, 144), (266, 153), (274, 156), (274, 161), (278, 169), (269, 172), (270, 176), (266, 176), (262, 169), (260, 175), (264, 182), (265, 189), (266, 196), (270, 191), (273, 195), (274, 199), (286, 203), (289, 210), (296, 211), (300, 217), (298, 222), (291, 230), (304, 251), (309, 257), (322, 262), (335, 266), (343, 270), (355, 267), (365, 270), (371, 278), (379, 281), (390, 282), (401, 285), (422, 287), (422, 277), (419, 271), (424, 261), (422, 255), (428, 255), (432, 251), (435, 257), (433, 263), (437, 267), (435, 270), (442, 276), (446, 273), (451, 278), (460, 273), (471, 274), (489, 270), (487, 262), (479, 260), (478, 253), (484, 255), (494, 252), (497, 250), (496, 246), (501, 241), (505, 242), (505, 235), (516, 233), (521, 228), (528, 220), (541, 223), (550, 214), (556, 218), (554, 224), (558, 222), (561, 228), (556, 235), (574, 237), (574, 241), (567, 251), (573, 260), (568, 260), (565, 256), (557, 259), (546, 273), (540, 275), (542, 285), (539, 295), (534, 301), (537, 303), (537, 311), (535, 316), (532, 328), (524, 329), (519, 329), (519, 348), (513, 351), (516, 367), (514, 374), (509, 372), (506, 375), (504, 372), (502, 360), (500, 352), (500, 346), (498, 343), (495, 337), (489, 353), (479, 350), (480, 343), (476, 336), (478, 329), (487, 324), (491, 320), (495, 315), (494, 309), (486, 310), (465, 310), (454, 310), (452, 306), (454, 300), (452, 298), (452, 292), (448, 295), (439, 290), (437, 293), (435, 294), (430, 289), (426, 297), (432, 301), (436, 301), (440, 304), (441, 310), (433, 313), (431, 318), (427, 319), (430, 326), (438, 326), (437, 336), (435, 338), (439, 342), (440, 347), (444, 350), (443, 362), (447, 370), (444, 377), (440, 361), (433, 346), (427, 336), (419, 325), (409, 315), (399, 307), (386, 300), (374, 294), (362, 290), (345, 287), (325, 287), (307, 291), (293, 295), (281, 302), (267, 311), (257, 320), (245, 333), (237, 347), (232, 360), (229, 367), (227, 378), (226, 389), (225, 404), (227, 416), (229, 426), (233, 437), (240, 449), (247, 462), (251, 468), (211, 471), (194, 473), (180, 474), (168, 475), (158, 475), (156, 473),]

    positions.lower_india = [(206, 590), (207, 596), (213, 605), (208, 602), (213, 615), (213, 622), (216, 628), (223, 634), (227, 635), (229, 639), (238, 643), (243, 639), (251, 636), (252, 627), (254, 623), (271, 620), (267, 614), (274, 604), (272, 602), (275, 599), (249, 595), (221, 592), (206, 590),]

    positions.upper_saff = [(291, 230), (301, 224), (317, 212), (328, 198), (333, 186), (333, 180), (332, 175), (328, 170), (346, 180), (353, 187), (356, 196), (354, 202), (351, 210), (343, 219), (338, 224), (325, 236), (305, 250), (300, 250), (296, 248), (294, 245), (292, 247), (286, 245), (288, 241), (290, 238), (290, 231), (301, 224),]

    positions.lower_saff = [(151, 406), (137, 416), (133, 424), (131, 432), (128, 447), (128, 453), (130, 461), (135, 468), (148, 473), (159, 475), (168, 475), (181, 475), (196, 473), (214, 471), (233, 469), (243, 469), (259, 468), (272, 468), (283, 469), (293, 469), (309, 473), (320, 475), (333, 481), (346, 488), (355, 497), (365, 507), (371, 518), (381, 543), (384, 553), (386, 563), (388, 579), (389, 598), (387, 609), (384, 619), (377, 632), (372, 640), (372, 623), (369, 597), (361, 569), (351, 549), (340, 535), (320, 519), (298, 510), (267, 504), (246, 503), (220, 505), (209, 506), (183, 507), (165, 507), (151, 506), (134, 504), (126, 501), (111, 496), (102, 487), (97, 471), (105, 451), (115, 438), (125, 427), (137, 416),]

    positions.green_area = [(133, 544), (162, 555), (204, 562), (249, 564), (282, 566), (313, 578), (331, 595), (343, 620), (346, 636), (346, 659), (339, 664), (333, 666), (315, 669), (296, 666), (307, 659), (314, 649), (314, 637), (306, 620), (297, 611), (286, 604), (270, 599), (255, 595), (236, 593), (218, 592), (206, 591), (187, 589), (177, 587), (162, 584), (151, 580), (142, 576), (134, 568), (133, 557), (134, 545), (-1, -1), (337, 269), (352, 256), (369, 237), (380, 218), (396, 240), (394, 247), (388, 257), (379, 267), (369, 276), (364, 269), (360, 269), (356, 267), (350, 269), (346, 269), (343, 270), (338, 270),]

    positions.red_shadow = [(321, 167), (320, 208), (327, 200), (332, 190), (331, 177), (329, 171), (322, 168), (-1, -1), (152, 406), (142, 411), (137, 417), (131, 434), (128, 446), (130, 460), (137, 469), (146, 472), (156, 474), (157, 469), (156, 465), (156, 460), (155, 456), (151, 451), (149, 446), (150, 440), (148, 434), (149, 430), (149, 426), (146, 420), (148, 416), (149, 410), (152, 407),]

    positions.between_spokes = [(260, 468), (259, 466), (263, 456), (258, 451), (249, 453), (243, 443), (251, 438), (245, 427), (237, 429), (234, 417), (243, 414), (244, 405), (232, 401), (232, 390), (240, 390), (245, 383), (239, 375), (235, 374), (239, 362), (246, 364), (252, 359), (251, 352), (244, 348), (250, 339), (255, 343), (262, 340), (264, 333), (259, 327), (266, 320), (271, 324), (280, 323), (282, 315), (279, 310), (288, 304), (291, 309), (300, 311), (305, 305), (303, 299), (313, 295), (316, 301), (322, 305), (329, 300), (329, 294), (341, 293), (341, 299), (346, 305), (355, 301), (356, 296), (366, 298), (365, 303), (369, 310), (378, 309), (382, 303), (390, 308), (388, 314), (390, 322), (399, 322), (404, 318), (411, 325), (407, 331), (408, 338), (416, 341), (421, 338), (428, 349), (422, 353), (422, 360), (428, 365), (435, 364), (438, 374), (429, 377), (426, 384), (413, 387), (414, 395), (414, 401), (408, 411), (401, 417), (390, 422), (380, 428), (372, 438), (367, 447), (357, 451), (350, 461), (342, 466), (335, 471), (334, 480), (319, 474), (305, 472), (295, 469), (280, 468), (260, 468),]

    positions.main_spokes = [(315, 473), (319, 446), (329, 414), (316, 444), (298, 469), (294, 469), (307, 440), (324, 412), (303, 438), (269, 465), (294, 434), (322, 408), (293, 428), (253, 446), (286, 421), (319, 404), (285, 416), (243, 421), (283, 407), (317, 400), (283, 402), (240, 395), (282, 393), (317, 394), (284, 386), (244, 367), (288, 378), (319, 390), (288, 375), (254, 347), (294, 367), (321, 386), (296, 364), (269, 327), (303, 356), (325, 382), (306, 352), (291, 312), (315, 347), (329, 380), (318, 347), (313, 305), (327, 345), (335, 378), (332, 345), (338, 301), (342, 344), (340, 379), (346, 345), (363, 304), (356, 347), (344, 380), (360, 351), (386, 316), (369, 354), (348, 383), (370, 356), (405, 331), (378, 364), (351, 386), (379, 367), (420, 350), (385, 375), (354, 390), (385, 379), (429, 372), (387, 389), (356, 395), (388, 392), (413, 395), (413, 400), (389, 401), (356, 400), (388, 405), (407, 412), (401, 417), (386, 414), (355, 404), (384, 419), (389, 423), (380, 428), (352, 408), (377, 430), (372, 437), (348, 411), (369, 441), (363, 449), (344, 415), (355, 446), (357, 452), (352, 461), (346, 449), (338, 416), (342, 449), (340, 466), (334, 480), (333, 471), (333, 449), (334, 416), (328, 449), (319, 474), (315, 474),]



def color_fill(coordinates, co = (0, 0, 0)):
    color(co)
    p_x, p_y = coordinates[0]
    myposition(p_x, p_y)
    fillcolor(co)
    begin_fill()
    t = 0
    for i in coordinates[1:]:
        x, y = i
        if t:
            myposition(x, y)
            t = 0
            begin_fill()
            continue

        if x == -1 and y == -1:
            t = 1
            end_fill()
            continue
        else:
            goto(x - 300, (y * -1) + 365)
    end_fill()


def draw(coordinates, mode = 1, co = (0, 0, 0), thickness = 1):
    co = (co[0] / 255, co[1] / 255, co[2] / 255)
    color(co)

    if mode:
        width(thickness)
        p_x, p_y = coordinates[0]
        myposition(p_x, p_y)
        t = 0
        for i in coordinates[1:]:
            x, y = i
            if t:
                myposition(x, y)
                t = 0
                continue

            if x == -1 and y == -1:
                t = 1
                continue
            else:
                goto(x - 300, (y * -1) + 365)
    else:
        color_fill(coordinates, co)


def files():
    positions()
    draw(positions.upper_india, co = (0, 0, 255), mode = 0)
    draw(positions.lower_india, co = (0, 0, 255), mode = 0)
    draw(positions.upper_saff, co = (255, 167, 31), mode = 0)
    draw(positions.lower_saff, co = (255, 167, 31), mode = 0)
    draw(positions.green_area, co = (1, 174, 59), mode = 0)
    draw(positions.red_shadow, co = (220, 79, 10), mode = 0)
    draw(positions.between_spokes, co = (0, 0, 255), mode = 0)
    draw(positions.main_spokes, co = (255, 255, 255), mode = 0)

files()
done()