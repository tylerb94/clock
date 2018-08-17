import pygame
import time

def getTime():
    t = time.localtime()
    h = t[3]
    if h > 12: h -= 12
    h *= 5
    return [h, t[4], t[5]]

class HHand:
    def __init__(self, pos):
        self.location = pos
        self.pointList = [
            (0, -200),
            (21, -198),
            (42, -195),
            (62, -190),
            (82, -182),
            (100, -173),
            (118, -161),
            (134, -148),
            (149, -133),
            (162, -117),
            (174, -100),
            (183, -81),
            (191, -61),
            (196, -41),
            (199, -20),
            (200, 0),
            (199, 20),
            (196, 41),
            (191, 61),
            (183, 81),
            (174, 100),
            (162, 117),
            (149, 133),
            (134, 148),
            (118, 161),
            (100, 173),
            (82, 182),
            (62, 190),
            (42, 195),
            (21, 198),
            (0, 200),
            (-21, 198),
            (-42, 195),
            (-62, 190),
            (-82, 182),
            (-100, 173),
            (-118, 161),
            (-134, 148),
            (-149, 133),
            (-162, 117),
            (-174, 100),
            (-183, 81),
            (-191, 61),
            (-196, 41),
            (-199, 20),
            (-200, 0),
            (-199, -20),
            (-196, -41),
            (-191, -61),
            (-183, -81),
            (-174, -100),
            (-162, -117),
            (-149, -133),
            (-134, -148),
            (-118, -161),
            (-100, -173),
            (-82, -182),
            (-62, -190),
            (-42, -195),
            (-21, -198)
        ]
        self.startPoint = [250, 250]
        self.endPoint = self.pointList[0]
    def update(self, t):
        self.endPoint = self.pointList[t[0]] # Get end-point
        x = self.endPoint[0] * .5 + self.startPoint[0]
        y = self.endPoint[1] * .5 + self.startPoint[1]
        self.endPoint = (x, y)
    def draw(self):
        return self.startPoint, self.endPoint
class MHand:
    def __init__(self, pos):
        self.location = pos
        self.pointList = [
            (0, -200),
            (21, -198),
            (42, -195),
            (62, -190),
            (82, -182),
            (100, -173),
            (118, -161),
            (134, -148),
            (149, -133),
            (162, -117),
            (174, -100),
            (183, -81),
            (191, -61),
            (196, -41),
            (199, -20),
            (200, 0),
            (199, 20),
            (196, 41),
            (191, 61),
            (183, 81),
            (174, 100),
            (162, 117),
            (149, 133),
            (134, 148),
            (118, 161),
            (100, 173),
            (82, 182),
            (62, 190),
            (42, 195),
            (21, 198),
            (0, 200),
            (-21, 198),
            (-42, 195),
            (-62, 190),
            (-82, 182),
            (-100, 173),
            (-118, 161),
            (-134, 148),
            (-149, 133),
            (-162, 117),
            (-174, 100),
            (-183, 81),
            (-191, 61),
            (-196, 41),
            (-199, 20),
            (-200, 0),
            (-199, -20),
            (-196, -41),
            (-191, -61),
            (-183, -81),
            (-174, -100),
            (-162, -117),
            (-149, -133),
            (-134, -148),
            (-118, -161),
            (-100, -173),
            (-82, -182),
            (-62, -190),
            (-42, -195),
            (-21, -198)]
        self.startPoint = [250, 250]
        self.endPoint = self.pointList[0]
    def update(self, t):
        self.endPoint = self.pointList[t[1]] # Get end-point
        x = self.endPoint[0] * .85 + self.startPoint[0]
        y = self.endPoint[1] * .85 + self.startPoint[1]
        self.endPoint = (x, y)
    def draw(self):
        return self.startPoint, self.endPoint
class SHand:
    def __init__(self, pos):
        self.location = pos
        self.pointList = [
            (0, -200),
            (21, -198),
            (42, -195),
            (62, -190),
            (82, -182),
            (100, -173),
            (118, -161),
            (134, -148),
            (149, -133),
            (162, -117),
            (174, -100),
            (183, -81),
            (191, -61),
            (196, -41),
            (199, -20),
            (200, 0),
            (199, 20),
            (196, 41),
            (191, 61),
            (183, 81),
            (174, 100),
            (162, 117),
            (149, 133),
            (134, 148),
            (118, 161),
            (100, 173),
            (82, 182),
            (62, 190),
            (42, 195),
            (21, 198),
            (0, 200),
            (-21, 198),
            (-42, 195),
            (-62, 190),
            (-82, 182),
            (-100, 173),
            (-118, 161),
            (-134, 148),
            (-149, 133),
            (-162, 117),
            (-174, 100),
            (-183, 81),
            (-191, 61),
            (-196, 41),
            (-199, 20),
            (-200, 0),
            (-199, -20),
            (-196, -41),
            (-191, -61),
            (-183, -81),
            (-174, -100),
            (-162, -117),
            (-149, -133),
            (-134, -148),
            (-118, -161),
            (-100, -173),
            (-82, -182),
            (-62, -190),
            (-42, -195),
            (-21, -198)
        ]
        self.startPoint = [250, 250]
        self.endPoint = self.pointList[0]
    def update(self, t):
        self.endPoint = self.pointList[t[2]] # Get end-point
        x = self.endPoint[0] + self.startPoint[0]
        y = self.endPoint[1] + self.startPoint[1]
        self.endPoint = (x, y)
    def draw(self):
        return self.startPoint, self.endPoint
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pointList = [
            (0, -200), # 1
            (21, -198), # 2
            (42, -195), # 3
            (62, -190), # 4
            (82, -182), # 5 #
            (100, -173), # 6
            (118, -161), # 7
            (134, -148), # 8
            (149, -133), # 9
            (162, -117), # 10 #
            (174, -100), # 11
            (183, -81), # 12
            (191, -61), # 13
            (196, -41), # 14
            (199, -20), # 15 #
            (200, 0), # 16
            (199, 20), # 17
            (196, 41), # 18
            (191, 61), # 19
            (183, 81), # 20 #
            (174, 100), # 21
            (162, 117), # 22
            (149, 133), # 23
            (134, 148), # 24
            (118, 161), # 25 #
            (100, 173), # 26
            (82, 182), # 27
            (62, 190), # 28
            (42, 195), # 29
            (21, 198), # 30 #
            (0, 200), # 31
            (-21, 198), # 32
            (-42, 195), # 33
            (-62, 190), # 34
            (-82, 182), # 35 #
            (-100, 173), # 36
            (-118, 161), # 37
            (-134, 148), # 38
            (-149, 133), # 39
            (-162, 117), # 40 #
            (-174, 100), # 41
            (-183, 81), # 42
            (-191, 61), # 43
            (-196, 41), # 44
            (-199, 20), # 45 #
            (-200, 0), # 46
            (-199, -20), # 47
            (-196, -41), # 48
            (-191, -61), # 49
            (-183, -81), # 50 #
            (-174, -100), # 51
            (-162, -117), # 52
            (-149, -133), # 53
            (-134, -148), # 54
            (-118, -161), # 55 #
            (-100, -173), # 56
            (-82, -182), # 57
            (-62, -190), # 58
            (-42, -195), # 59
            (-21, -198) # 60 #
        ]
class Clock:

    def __init__(self, size):

        self.circle = Circle(size[0]/2); r = self.circle.radius
        self.size = size
        self.secondHand = SHand((r, r))
        self.minuteHand = MHand((r, r))
        self.hourHand = HHand((r, r))
        self.setButton = (500, 225, 15, 50)
        self.image = pygame.Surface((500, 500))

    def update(self, t):
        self.secondHand.update(t)
        self.hourHand.update(t)
        self.minuteHand.update(t)

    def draw(self):

        pygame.Surface.fill(self.image, (0, 0, 0))

        # Draw the hands
        s1, s2 = self.secondHand.draw()
        m1, m2 = self.minuteHand.draw()
        h1, h2 = self.hourHand.draw()

        # Draw the circle
        pygame.draw.circle(self.image, (0, 0, 255), s1, int(self.circle.radius), 1)


        pygame.draw.line(self.image, (0, 255, 255), h1, h2, 5)
        pygame.draw.line(self.image, (0, 0, 255), m1, m2, 3)
        pygame.draw.line(self.image, (255, 0, 0), s1, s2, 1)

        # Draw dots around clock
        for n in range(len(self.circle.pointList)):

            x = int(self.circle.pointList[n][0] * 1.15 + (self.size[0] / 2))
            y = int(self.circle.pointList[n][1] * 1.15 + (self.size[1] / 2))
            p = (x, y)

            # Increase the radius on 5, 10, 15...
            if n == 5 or n == 10 or n == 15 or n == 20 or n == 25 or n == 30 or n == 35 or n == 40 or n == 45 or n == 50 or n == 55 or n == 0:
                pygame.draw.circle(self.image, (255, 0, 0), p, 5)
            else:
                pygame.draw.circle(self.image, (0, 255, 255), p, 2)

        # Draw crown
        pygame.draw.rect(self.image, (255, 0, 0), self.setButton, 0)

        return self.image

    def event(self, event):
        pass

def main():

    pygame.init()
    window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    _clock = Clock((500, 500))
    pygame.mouse.set_visible(False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                quit()

            else:
                _clock.event(event)

        _clock.update(getTime())
        image = pygame.transform.scale(_clock.draw(), (1080, 1080))

        pygame.Surface.blit(window, image, (425, 0))
        pygame.display.update()


main()