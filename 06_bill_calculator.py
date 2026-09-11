video_title = input("Enter the title of the video: ").strip()

transport_cost = float(input("Enter the transport cost: ").strip())
drink_cost = float(input("Enter the drink cost: ").strip())
other_cost = float(input("Enter any other costs: ").strip())

usable_clips = int(input("Enter the number of usable clips: ").strip())

if len(video_title) == 0 or usable_clips <= 0:
    print("Error: Video title cannot be empty and usable clips must be greater than 0.")
else:
    total_cost = transport_cost + drink_cost + other_cost
    cost_per_clip = total_cost / usable_clips
    print(video_title.upper())
    print(round(total_cost, 2))
    print(round(cost_per_clip, 2))

    if usable_clips >= 8:
        print("You have a lot of usable clips!")
    else:
        print(8-usable_clips, "more clips needed to reach 8 usable clips.")


