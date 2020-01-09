
# Movement

- A for left and D for right. W for activating the jetpack and jumping up. And some button for
    firing bullets at the enemies.
- You have to control the Mandalorian and move it up, forward and backward while collecting coins
    suspended in the air. When the Mandalorian moves upwards, the jet pack is activated as long as
    the ‘W’ key is pressed. When ‘W’ is released, the jetpack deactivates and gravity comes into play.
    There must be a gravity-like effect when the he moves up or down.

# Background and Scenery

- The scenery and the obstacles must change as you move in and out of the window. There must be
    a ground/platform and the sky, and the Mandalorian can’t go below the ground or above the sky.
- Lots of coins suspended which the Mandalorian can collect and increase his score.

# Obstacles 

- Fire Beams: Beam like structures should appear (like in the figure above) as obstacles. There
    must be three kinds of beams: horizontal, vertical and some at 45◦with the ground/platform. The
    Mandalorian must ensure to not collide with these beams, else he will lose a life. He can use his
    blaster to shoot at them and clear his way. 


- Magnet: A magnet should randomly appear on the way, which will influence the motion of the
    Mandalorian. So if he is in the range of the magnet, he would be continuously attracted towards
    the magnet. Assume that the magnet causes a constant attractive force in its direction. 

# The Boss Enemy!! 

- The boss enemy must appear in the end and once the Mandalorian defeats it, he can rescue Baby
    Yoda and complete the game. The boss enemy is Viserion, the flying dragon thatadjusts its
    position according to the player(with respect to the movement along the Y axis).It should
    throw ice ballsaimed at the Mandalorian, which he must dodge.
- The boss enemy will have multiple lives, which will decrease when the Mandalorian shoots bullets
    at it. Once the boss enemy is defeated, Baby Yoda can be rescued and the game is complete.
- Use your creativity and imagination for this one, this should be the most difficult obstacle to clear.
    The dragon need not look like an exact dragon :P But do look up ASCII arts online, some of them
    are beautiful :)

# Score and Lives

- Score must be displayed on the top. You can calculate it as you like, taking into account the
    number of coins collected. Have score increments for killing enemies and the boss enemy.
- Both time and the lives of the Mandalorian are limited. So the ’time remaining’ and ’lives remain-
    ing’ must be displayed on the top along the score. End the game when all lives are over, or if the
    user quits by pressing ’Q’.

# Power-Ups 

- Speed boost: The speed of the game will increase upon taking this power-up. 
- Shield: A shield should appear around the Mandalorian using which, he will not be affected by
    the enemies and obstacles. The shield will be activated using the ’Space’ key and will last for 10
    seconds. It will take 60 seconds for shield power-up to refill again after use.

# Bonus 
That’s a 100 points so far! Additionally, you could implement the following to be eligible for some bonus
marks.

- Drogon(15 marks):
    - Ultimate Dragon: We need a dragon on our side too :)
    - Drogon PowerUp will pop up once in the middle of the game and will be destroyed only on
       contact with an obstacle or enemy. Check this video out.
    - Marks are mainly for the wriggly effect; the dragon should move in a wave-like manner,
       continuously emitting flames. More marks for a handsome dragon :)


- Colour(10 marks): Have different colours for different objects in the scene. The colorama library
    is allowed for this. This should not be very difficult, easy 10 marks :P

