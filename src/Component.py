class Component:
    def __init__(self, label, confidence, centerX, centerY, width, height):
        # Given data
        self.label = label
        self.confidence = confidence
        self.centerX = centerX
        self.centerY = centerY
        self.width = width
        self.height = height

        # Calculate corners
        self.x1 = centerX - (width / 2)
        self.x2 = self.x1 + width
        self.y1 = centerY - (height / 2)
        self.y2 = self.y1 + height

        # Calculate area
        self.area = width * height

    def overlaps(self, component, tresh=0.5):
        # Calculate overlaping x and y values
        dx = min(self.x2, component.x2) - max(self.x1, component.x1)
        dy = min(self.y2, component.y2) - max(self.y1, component.y1)

        # If any is 0 or less, components do not overlap at all
        if dx <= 0 or dy <= 0:
            return False

        # Calculate overlapping area
        overlappingArea = dx * dy

        # Check if area is less than the treshold (Based on the smallest component), if so, components do not overlap
        if overlappingArea < (min(self.area, component.area) * tresh):
            return False

        # Components Overlap
        return True

    def inLine(self, component, tresh=0.5):
        # Calculate overlapping y value
        dy = min(self.y2, component.y2) - max(self.y1, component.y1)

        # If it is 0 or less, components are not in line
        if dy <= 0:
            return False

        # Check if overlap is less than the treshold, if so, components are not in line
        if dy < (min(self.height, component.height) * tresh):
            return False

        # Components Overlap
        return True
