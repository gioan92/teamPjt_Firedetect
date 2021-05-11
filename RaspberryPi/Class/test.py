import time;

abc = dict();

x = 10;
y = 100;
while True:
    abc["x"] = x;
    abc["y"] = y;
    print(abc);
    x += 1;
    y += 1;
    time.sleep(1);