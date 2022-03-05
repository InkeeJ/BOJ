n = int(input())
end_game = [x for x in range(1,2666800) if '666' in str(x)]
print(end_game[:n])