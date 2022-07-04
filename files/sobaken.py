



distance = int(input("type distance: "))
first_friend_speed = int(input("type first friend speed: "))
second_friend_speed = int(input("type second friend speed: "))
dog_speed = int(input("type dog speed: "))
count = 0
friend = 2
if dog_speed > first_friend_speed:
  if dog_speed <= second_friend_speed:
    count = 1
  else:
    while (distance > 10):
      if friend == 1:
        time = distance / (first_friend_speed + dog_speed)
        friend = 2
      else:
         time = distance / (second_friend_speed + dog_speed)
         friend = 1
         distance = distance - (first_friend_speed + second_friend_speed) * time
         count = count + 1
else:
  count = 0
print ("собакен набегал", count, "раз")
repeat = input("type OK to repeat or any key to stop: ")
if repeat == "ok":
  while repeat == "ok":
    distance = int(input("type distance: "))
    first_friend_speed = int(input("type first friend speed: "))
    second_friend_speed = int(input("type second friend speed: "))
    dog_speed = int(input("type dog speed: "))
    count = 0
    friend = 2
    if dog_speed > first_friend_speed:
      if dog_speed <= second_friend_speed:
        count = 1
      else:
        while (distance > 10):
          if friend == 1:
            time = distance / (first_friend_speed + dog_speed)
            friend = 2
          else:
             time = distance / (second_friend_speed + dog_speed)
             friend = 1
             distance = distance - (first_friend_speed + second_friend_speed) * time
             count = count + 1
    else:
      count = 0
    print ("собакен набегал", count, "раз")
    repeat = input("type OK to repeat or any key to stop: ")
print ("Thank you, bye!")









