def update_lemmings(self):
        # When the lemming gets to the wall its direction will change
        if self.lemmings_x == 240 or self.lemmings_x == self.blocker.placed_x:
           self.lemmings.direction_left = False
        # I add 16 because is the other side of the blocker
        if self.lemmings_x == 1 or self.lemmings_x == self.blocker.placed_x + 16:
            self.lemmings.direction_left = True

        if self.lemmings.direction_left == True and self.lemmings.over_platform == True and Start_Screen.on == False:
            self.lemmings_x += 1
        if self.lemmings.direction_left == False and self.lemmings.over_platform == True and Start_Screen.on == False:
            self.lemmings_x -= 1

        if self.lemmings.over_platform == False and Umbrella.use == False:
            self.lemmings_y += 2
        if self.lemmings.over_platform == False and Umbrella.use == True:
            self.lemmings_y += 1
        if Stairs.use == True:
            self.lemmings_y -= 1

        return self.lemmings_x, self.lemmings_y