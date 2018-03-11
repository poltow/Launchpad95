from _Framework.ButtonElement import Color

class Blink(Color):

    def __init__(self, midi_value = 0, *a, **k):
        super(Blink, self).__init__(midi_value, *a, **k)

    def draw(self, interface):
        interface.send_value(0)
        interface.send_value(self.midi_value, channel=1)


class Pulse(Color):

    def __init__(self, midi_value = 0, *a, **k):
        super(Pulse, self).__init__(midi_value, *a, **k)

    def draw(self, interface):
        interface.send_value(0)
        interface.send_value(self.midi_value, channel=2)
        
    
class Rgb:
    BLACK = Color(0)
    DARK_GREY = Color(1)
    GREY = Color(2)
    WHITE = Color(3)
    RED = Color(5)
    RED_HALF = Color(6)
    RED_THIRD = Color(7)
    AMBER = Color(9)
    AMBER_HALF = Color(10)
    AMBER_THIRD = Color(11)
    GREEN = Color(21)
    GREEN_HALF = Color(22)
    GREEN_THIRD = Color(23)
    YELLOW = Color(13)
    YELLOW_HALF= Color(14)
    YELLOW_THIRD = Color(15)
    MINT = Color(29)
    MINT_HALF = Color(30)
    MINT_THIRD = Color(31)
    LIGHT_BLUE = Color(37)
    LIGHT_BLUE_HALF = Color(38)
    LIGHT_BLUE_THIRD = Color(39)
    BLUE = Color(45)
    BLUE_HALF = Color(46)
    BLUE_THIRD = Color(47)
    PINK = Color(53)
    PINK_HALF = Color(54)
    PINK_THIRD = Color(55)
    PURPLE = Color(48)
    PURPLE_HALF = Color(49)
    PURPLE_THIRD = Color(50)
    
    BLACK_BLINK = Blink(0)
    DARK_GREY_BLINK = Blink(1)
    GREY_BLINK = Blink(2)
    WHITE_BLINK = Blink(3)
    RED_BLINK = Blink(5)
    RED_HALF_BLINK = Blink(6)
    RED_THIRD_BLINK = Blink(7)
    AMBER_BLINK = Blink(9)
    AMBER_HALF_BLINK = Blink(10)
    AMBER_THIRD_BLINK = Blink(11)
    GREEN_BLINK = Blink(21)
    GREEN_HALF_BLINK = Blink(22)
    GREEN_THIRD_BLINK = Blink(23)
    YELLOW_BLINK = Blink(13)
    YELLOW_HALF_BLINK = Color(14)
    YELLOW_THIRD_BLINK = Blink(15)
    MINT_BLINK = Blink(29)
    MINT_HALF_BLINK = Blink(30)
    MINT_THIRD_BLINK = Blink(31)
    LIGHT_BLUE_BLINK = Blink(37)
    LIGHT_BLUE_HALF_BLINK = Blink(38)
    LIGHT_BLUE_THIRD_BLINK = Blink(39)
    BLUE_BLINK = Blink(45)
    BLUE_HALF_BLINK = Blink(46)
    BLUE_THIRD_BLINK = Blink(47)
    PINK_BLINK = Blink(53)
    PINK_HALF_BLINK = Blink(54)
    PINK_THIRD_BLINK = Blink(55)
    PURPLE_BLINK = Blink(48)
    PURPLE_HALF_BLINK = Blink(49)
    PURPLE_THIRD_BLINK = Blink(50)

    BLACK_PULSE = Pulse(0)
    DARK_GREY_PULSE = Pulse(1)
    GREY_PULSE = Pulse(2)
    WHITE_PULSE = Pulse(3)
    RED_PULSE = Pulse(5)
    RED_HALF_PULSE = Pulse(6)
    RED_THIRD_PULSE = Pulse(7)
    AMBER_PULSE = Pulse(9)
    AMBER_HALF_PULSE = Pulse(10)
    AMBER_THIRD_PULSE = Pulse(11)
    GREEN_PULSE = Pulse(21)
    GREEN_HALF_PULSE = Pulse(22)
    GREEN_THIRD_PULSE = Pulse(23)
    YELLOW_PULSE = Pulse(13)
    YELLOW_HALF_PULSE = Color(14)
    YELLOW_THIRD_PULSE = Pulse(15)
    MINT_PULSE = Pulse(29)
    MINT_HALF_PULSE = Pulse(30)
    MINT_THIRD_PULSE = Pulse(31)
    LIGHT_BLUE_PULSE = Pulse(37)
    LIGHT_BLUE_HALF_PULSE = Pulse(38)
    LIGHT_BLUE_THIRD_PULSE = Pulse(39)
    BLUE_PULSE = Pulse(45)
    BLUE_HALF_PULSE = Pulse(46)
    BLUE_THIRD_PULSE = Pulse(47)
    PINK_PULSE = Pulse(53)
    PINK_HALF_PULSE = Pulse(54)
    PINK_THIRD_PULSE = Pulse(55)
    PURPLE_PULSE = Pulse(48)
    PURPLE_HALF_PULSE = Pulse(49)
    PURPLE_THIRD_PULSE = Pulse(50)

CLIP_COLOR_TABLE = {
 15549221: 60,
 12411136: 61,
 11569920: 62,
 8754719: 63,
 5480241: 64,
 695438: 65,
 31421: 66,
 197631: 67,
 3101346: 68,
 6441901: 69,
 8092539: 70,
 3947580: 71,
 16712965: 72,
 12565097: 73,
 10927616: 74,
 8046132: 75,
 4047616: 76,
 49071: 77,
 1090798: 78,
 5538020: 79,
 8940772: 80,
 10701741: 81,
 12008809: 82,
 9852725: 83,
 16149507: 84,
 12581632: 85,
 8912743: 86,
 1769263: 87,
 2490280: 88,
 6094824: 89,
 1698303: 90,
 9160191: 91,
 9611263: 92,
 12094975: 93,
 14183652: 94,
 16726484: 95,
 16753961: 96,
 16773172: 97,
 14939139: 98,
 14402304: 99,
 12492131: 100,
 9024637: 101,
 8962746: 102,
 10204100: 103,
 8758722: 104,
 13011836: 105,
 15810688: 106,
 16749734: 107,
 16753524: 108,
 16772767: 109,
 13821080: 110,
 12243060: 111,
 11119017: 112,
 13958625: 113,
 13496824: 114,
 12173795: 115,
 13482980: 116,
 13684944: 117,
 14673637: 118,
 16777215: 119
}

RGB_COLOR_TABLE = (
 (0, 0),
 (1, 1973790),
 (2, 8355711),
 (3, 16777215),
 (4, 16731212),
 (5, 16711680),
 (6, 5832704),
 (7, 1638400),
 (8, 16760172),
 (9, 16733184),
 (10, 5840128),
 (11, 2562816),
 (12, 16777036),
 (13, 16776960),
 (14, 5855488),
 (15, 1644800),
 (16, 8978252),
 (17, 5570304),
 (18, 1923328),
 (19, 1321728),
 (20, 5046092),
 (21, 65280),
 (22, 22784),
 (23, 6400),
 (24, 5046110),
 (25, 65305),
 (26, 22797),
 (27, 6402),
 (28, 5046152),
 (29, 65365),
 (30, 22813),
 (31, 7954),
 (32, 5046199),
 (33, 65433),
 (34, 22837),
 (35, 6418),
 (36, 5030911),
 (37, 43519),
 (38, 16722),
 (39, 4121),
 (40, 5015807),
 (41, 22015),
 (42, 7513),
 (43, 2073),
 (44, 5000447),
 (45, 255),
 (46, 89),
 (47, 25),
 (48, 8867071),
 (49, 5505279),
 (50, 1638500),
 (51, 983088),
 (52, 16731391),
 (53, 16711935),
 (54, 5832793),
 (55, 1638425),
 (56, 16731271),
 (57, 16711764),
 (58, 5832733),
 (59, 2228243),
 (60, 16717056),
 (61, 10040576),
 (62, 7950592),
 (63, 4416512),
 (64, 211200),
 (65, 22325),
 (66, 21631),
 (67, 255),
 (68, 17743),
 (69, 2425036),
 (70, 8355711),
 (71, 2105376),
 (72, 16711680),
 (73, 12451629),
 (74, 11529478),
 (75, 6618889),
 (76, 1084160),
 (77, 65415),
 (78, 43519),
 (79, 11007),
 (80, 4129023),
 (81, 7995647),
 (82, 11672189),
 (83, 4202752),
 (84, 16730624),
 (85, 8970502),
 (86, 7536405),
 (87, 65280),
 (88, 3931942),
 (89, 5898097),
 (90, 3735500),
 (91, 5999359),
 (92, 3232198),
 (93, 8880105),
 (94, 13835775),
 (95, 16711773),
 (96, 16744192),
 (97, 12169216),
 (98, 9502464),
 (99, 8609031),
 (100, 3746560),
 (101, 1330192),
 (102, 872504),
 (103, 1381674),
 (104, 1450074),
 (105, 6896668),
 (106, 11010058),
 (107, 14569789),
 (108, 14182940),
 (109, 16769318),
 (110, 10412335),
 (111, 6796559),
 (112, 1973808),
 (113, 14483307),
 (114, 8454077),
 (115, 10131967),
 (116, 9332479),
 (117, 4210752),
 (118, 7697781),
 (119, 14745599),
 (120, 10485760),
 (121, 3473408),
 (122, 1757184),
 (123, 475648),
 (124, 12169216),
 (125, 4141312),
 (126, 11755264),
 (127, 4920578)
)