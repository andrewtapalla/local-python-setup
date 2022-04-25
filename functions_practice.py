def hello():
    print('Hello World')

hello()

def pack():
    print(first_arguement, second_argument, third_arguement)
    return[first_arguement, second_argument, third_arguement]

print(pack)

def lunch(meal):
  if len(meal) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(meal)):
      if i == 0:
        print(f"First I eat {meal[0]}")
      else:
        print(f"Next I eat {meal[i]}")

print(lunch)
lunch(["ribs"])
lunch(["cake","cookie","thai food","pudding"])