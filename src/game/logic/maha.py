import math
from ..util import get_direction
from game.models import Board, GameObject, Properties

class Maha(object):
    def __init__(self):
        self.goal_position = None
        self.previous_position = (None, None)
        self.turn_direction = 1

    def next_move(self, board_bot: GameObject, board: Board):
        props = board_bot.properties

        teleporter = [obj for obj in board.game_objects if obj.type == "TeleportGameObject"]
        
        if props.diamonds == 5 or props.milliseconds_left == 5000 or props.milliseconds_left == 3000:
            base = props.base
            self.goal_position = base

        else:
            max_score = -1
            target = None
            for diamond in board.diamonds:
                if (board_bot.properties.diamonds + diamond.properties.points > 5):
                    continue
                xDist = abs(board_bot.position.x - diamond.position.x)
                yDist = abs(board_bot.position.y - diamond.position.y)
                distance = math.sqrt(xDist * xDist + yDist * yDist)
                score = diamond.properties.points / distance

                if (score > max_score):
                    max_score = score
                    target = diamond

            for other_bot in board.bots:
                if other_bot.id == board_bot.id:
                    continue

                # Menghitung jarak antara bot yang sedang diproses dengan bot lainnya
                xDist = abs(board_bot.position.x - other_bot.position.x)
                yDist = abs(board_bot.position.y - other_bot.position.y)
                distance = math.sqrt(xDist * xDist + yDist * yDist)
                # Mengecek apakah bot lain berada dalam jangkauan tertentu (1 <= distance <= 2)
                if distance == 1:
                    target = other_bot

            # Set goal_position ke posisi bot lain yang menjadi target
            if target is not None:
                self.goal_position = target.position


        if self.goal_position:
            current_position = board_bot.position
            cur_x = current_position.x
            cur_y = current_position.y
            delta_x, delta_y = get_direction(
                cur_x,
                cur_y,
                self.goal_position.x,
                self.goal_position.y,
            )

            if (cur_x, cur_y) == self.previous_position:
                if delta_x != 0:
                    delta_y = delta_x * self.turn_direction
                    delta_x = 0
                elif delta_y != 0:
                    delta_x = delta_y * self.turn_direction
                    delta_y = 0
                self.turn_direction = -self.turn_direction

            self.previous_position = (cur_x, cur_y)
            return delta_x, delta_y

        return 0, 0