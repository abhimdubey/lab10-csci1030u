# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.

def eval_rpn(tokens):
    # Outline (write your plan here first): define a stack to hold numbers. 
    # Iterate through each token in the input list.
    #   ...
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    stack = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Use int() to truncate towards zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]

def decode_string(s):
    # Outline: define a stack to hold characters and numbers. 
    # Iterate through each character in the input string.
    # 
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack = []
    current_num = 0
    current_str = ""
    answer = ""
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == "]":
            last_str, num = stack.pop()
            current_str = last_str + current_str * num
        else:
            current_str += char
    return current_str

def daily_temperatures(temps):
    # Outline: define a stack to hold indices of the temperatures. 
    # Check each temperature against the top of the stack to find warmer days.
    #   ...
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    n = len(temps)
    answer = [0] * n
    stack = []  # This will store indices of the temperatures
    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)
    return answer


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline: define a DFS function to explore the grid. Then iterate through each cell in the grid, 
    # and for each unvisited land cell, call DFS to mark all connected land cells as visited and 
    # increment the island count.
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    islands = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] == "0":
            return
        visited[r][c] = True
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:
                dfs(r, c)
                islands += 1

    return islands


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    print(eval_rpn(["2", "1", "+", "3", "*"]))    # returns 9    ((2 + 1) * 3)
    print(eval_rpn(["4", "13", "5", "/", "+"]))   # returns 6    (4 + 13 // 5)
    print(decode_string("3[a]2[bc]"))    # returns "aaabcbc"
    print(decode_string("3[a2[c]]"))     # returns "accaccacc"
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))   # returns [1, 1, 4, 2, 1, 1, 0, 0]
    print(num_islands(["11000", "11000", "00100", "00011"]))   # returns 3

if __name__ == "__main__":
    main()
