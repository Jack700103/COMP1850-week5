"""
Task 3: Advent of Code Style Challenge
"""

import os
import re
import math
from collections import Counter, defaultdict
from pathlib import Path
from datetime import datetime

def create_challenge_input_files():
    """
    Create the input files for the Advent of Code challenges.
    These are typical AoC-style input files.
    """
    print("=" * 70)
    print("CREATING ADVENT OF CODE CHALLENGE INPUT FILES")
    print("=" * 70)

    challenges_dir = Path("aoc_challenges")
    challenges_dir.mkdir(exist_ok=True)

    calibration_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
two1nine
"""
    
    with open(challenges_dir / "day1_calibration.txt", "w") as f:
        f.write(calibration_input)
    print("Created: day1_calibration.txt")
    
    # Challenge 2: Navigation instructions (Day 2 style)
    navigation_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2
forward 10
down 20
up 5
down 1
forward 15
up 10"""
    
    with open(challenges_dir / "day2_navigation.txt", "w") as f:
        f.write(navigation_input)
    print("Created: day2_navigation.txt")

    expense_input = """1721
979
366
299
675
1456
1190
1344
1717
1062
1339
1580
902
1321
1481
670
1053
1108
1455
944
708
1128
1384
1438
1581
743
473
1346
584
771
1427
1472
1275
934
1933
1474
1067
1176
1345
897
896
1196
1199
1137
1234
629
1023
1088
791
1092
1360
1127
730
1166
1377
806
1186
527
1025
1039
1315
1329
859
1246
1072
1046
1396
1448
887
1007
1248
889
638
563
1197
591
1207
815
926
1082
1019
1167
546
506
1416
1278
646
813
797
1055
1302
743
1124
1283
757
1254
934
1332
711
1494
1036
1026
808
1112
1212
1265
967
1090
1056
1347
1098
1229
843
1291
1412
1184
1038
1289
1195
1083
1241
1552
1279
1350
1163
1222
1314
1133
1181
1178
1303
1420
1333
1075
943
1188
1335
1363
1233
1295
1369
1545
1138
1147
1018
1100
1044
1077
1146
1273
953
1162
1223
962
723
1277
1057
1105
1238
987
876
1005
1378
1011
1187
1306
1236
1192
1372
1391
1356
1136
1373
1037
1151
1446
1422
1022
1256
1272
1232
1013
1027
1040
1290
1131
1155
1334
1214
1250
1132
1177
1014
1198
1364
1358
1318
1086
1119
1031
1028
1068
1095
1204
1473
1526
1389
1262
1280
952
1029
1113
1160
1054
1263
1120
1231
1362
1417
1405
1225
1293
1174
1301
1140
1311
1021
1255
1235
1134
1209
1114
1061
1366
1337
1104
1096
1217
1063
994
1271
1143
1213
1175
1247
1125
1249
1118
1381
1084
1153
1141
1045
1073
1058
1288
1093
1268
1483
1165
1224
1286
1144
1193
1051
1226
1164
1205
1154
1130
1267
1179
1355
1253
1116
1242
1348
1219
1237
1091
1182
1340
1135
1342
1206
1319
1398
1071
1033
1173
1015
1070
1142
1243
1089
1050
1064
1117
1316
1287
1239
1126
1308
1066
1150
1383
1041
1079
1325
1365
1216
1159
1361
1257
1298
1284
1200
1109
1158
1189
1330
1094
1202
1111
1170
1349
1122
1139
1251
1244
1012
1081
1304
1059
1261
1259
1266
1065
1260
1276
1042
1157
1240
1322
1320"""
    
    with open(challenges_dir / "day1_expenses.txt", "w") as f:
        f.write(expense_input)
    print("Created: day1_expenses.txt")
    
    # Challenge 4: Password validation (Day 2 style)
    password_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
3-5 d: ddddd
1-4 e: eeee
5-7 f: fffffff
2-8 g: gggggggg
1-5 h: hhhhh
4-6 i: iiiiii
7-9 j: jjjjjjjjj
1-3 k: klm
2-4 l: llll
5-7 m: mmmmmmm
3-5 n: nnnnn
6-8 o: oooooooo
1-3 p: ppp
9-11 q: qqqqqqqqqqq
4-6 r: rrrrrr
2-4 s: ssss
7-9 t: ttttttttt
3-5 u: uuuuu
6-8 v: vvvvvvvv
2-4 w: wwww
5-7 x: xxxxxxx
3-5 y: yyyyy
6-8 z: zzzzzzzz"""
    
    with open(challenges_dir / "day2_passwords.txt", "w") as f:
        f.write(password_input)
    print("Created: day2_passwords.txt")
    
    # Challenge 5: Bingo boards (Day 4 style - simplified)
    bingo_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
    
    with open(challenges_dir / "day4_bingo.txt", "w") as f:
        f.write(bingo_input)
    print("Created: day4_bingo.txt")
    
    print(f"\nAll challenge input files created in: {challenges_dir}/")

def challenge_1_calibration():

    print("\n" + "=" * 70)
    print("CHALLENGE 1: Trebuchet Calibration (AoC Day 1 Style)")
    print("=" * 70)
    
    input_file = Path("aoc_challenges/day1_calibration.txt")
    
    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        return
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        total_sum = 0
        calibration_values = []
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue

            first_digit = None
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break

            last_digit = None
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break
            
            if first_digit and last_digit:
                calibration_value = int(first_digit + last_digit)
                calibration_values.append(calibration_value)
                total_sum += calibration_value

        output_file = Path("aoc_challenges/day1_calibration_result.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("CHALLENGE 1: Trebuchet Calibration Results\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Input file: {input_file}\n")
            f.write(f"Lines processed: {len(calibration_values)}\n\n")
            
            f.write("Calibration values by line:\n")
            for i, value in enumerate(calibration_values, 1):
                f.write(f"  Line {i:2}: {value}\n")
            
            f.write(f"\nTotal sum of calibration values: {total_sum}\n")
        
        print(f"✓ Challenge completed!")
        print(f"  Lines processed: {len(calibration_values)}")
        print(f"  Total sum: {total_sum}")
        print(f"  Results saved to: {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")

def challenge_2_navigation():
    print("\n" + "=" * 70)
    print("CHALLENGE 2: Submarine Navigation (AoC Day 2 Style)")
    print("=" * 70)
    
    input_file = Path("aoc_challenges/day2_navigation.txt")
    
    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        return
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        horizontal = 0
        depth = 0
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            command, value_str = line.split()
            value = int(value_str)
            
            if command == 'forward':
                horizontal += value
            elif command == 'down':
                depth += value
            elif command == 'up':
                depth -= value
        
        result = horizontal * depth

        output_file = Path("aoc_challenges/day2_navigation_result.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("CHALLENGE 2: Submarine Navigation Results\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Input file: {input_file}\n")
            f.write(f"Commands processed: {len(lines)}\n\n")
            
            f.write("Final position:\n")
            f.write(f"  Horizontal: {horizontal}\n")
            f.write(f"  Depth: {depth}\n")
            f.write(f"  Product (horizontal × depth): {result}\n")
        
        print(f"✓ Challenge completed!")
        print(f"  Final horizontal position: {horizontal}")
        print(f"  Final depth: {depth}")
        print(f"  Product: {result}")
        print(f"  Results saved to: {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")

def challenge_3_expense_report():
    print("\n" + "=" * 70)
    print("CHALLENGE 3: Expense Report (AoC Day 1 Style)")
    print("=" * 70)
    
    input_file = Path("aoc_challenges/day1_expenses.txt")
    
    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        return
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            numbers = [int(line.strip()) for line in f if line.strip()]

        found_part1 = False
        product_part1 = 0
        num1_part1 = 0
        num2_part1 = 0
        
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == 2020:
                    num1_part1, num2_part1 = numbers[i], numbers[j]
                    product_part1 = num1_part1 * num2_part1
                    found_part1 = True
                    break
            if found_part1:
                break

        found_part2 = False
        product_part2 = 0
        nums_part2 = (0, 0, 0)
        
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                for k in range(j + 1, len(numbers)):
                    if numbers[i] + numbers[j] + numbers[k] == 2020:
                        nums_part2 = (numbers[i], numbers[j], numbers[k])
                        product_part2 = numbers[i] * numbers[j] * numbers[k]
                        found_part2 = True
                        break
                if found_part2:
                    break
            if found_part2:
                break

        output_file = Path("aoc_challenges/day1_expenses_result.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("CHALLENGE 3: Expense Report Results\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Input file: {input_file}\n")
            f.write(f"Numbers processed: {len(numbers)}\n\n")
            
            f.write("PART 1: Find two numbers summing to 2020\n")
            if found_part1:
                f.write(f"  Found: {num1_part1} and {num2_part1}\n")
                f.write(f"  Product: {num1_part1} × {num2_part1} = {product_part1}\n")
            else:
                f.write("  No pair found summing to 2020\n")
            
            f.write("\nPART 2: Find three numbers summing to 2020\n")
            if found_part2:
                f.write(f"  Found: {nums_part2[0]}, {nums_part2[1]}, {nums_part2[2]}\n")
                f.write(f"  Product: {nums_part2[0]} × {nums_part2[1]} × {nums_part2[2]} = {product_part2}\n")
            else:
                f.write("  No triplet found summing to 2020\n")
        
        print(f"✓ Challenge completed!")
        print(f"  Numbers processed: {len(numbers)}")
        if found_part1:
            print(f"  Part 1: {num1_part1} × {num2_part1} = {product_part1}")
        if found_part2:
            print(f"  Part 2: {nums_part2[0]} × {nums_part2[1]} × {nums_part2[2]} = {product_part2}")
        print(f"  Results saved to: {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")

def challenge_4_password_validation():
    print("\n" + "=" * 70)
    print("CHALLENGE 4: Password Validation (AoC Day 2 Style)")
    print("=" * 70)
    
    input_file = Path("aoc_challenges/day2_passwords.txt")
    
    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        return
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        valid_part1 = 0
        valid_part2 = 0
        password_details = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            policy_part, password = line.split(': ')
            password = password.strip()
            
            range_part, letter = policy_part.split(' ')
            min_val, max_val = map(int, range_part.split('-'))
            
            count = password.count(letter)
            is_valid_part1 = min_val <= count <= max_val
            
            pos1_valid = password[min_val - 1] == letter
            pos2_valid = password[max_val - 1] == letter
            is_valid_part2 = (pos1_valid or pos2_valid) and not (pos1_valid and pos2_valid)
            
            if is_valid_part1:
                valid_part1 += 1
            if is_valid_part2:
                valid_part2 += 1
            
            password_details.append({
                'password': password,
                'letter': letter,
                'min': min_val,
                'max': max_val,
                'count': count,
                'valid_part1': is_valid_part1,
                'valid_part2': is_valid_part2
            })

        output_file = Path("aoc_challenges/day2_passwords_result.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("CHALLENGE 4: Password Validation Results\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Input file: {input_file}\n")
            f.write(f"Passwords processed: {len(password_details)}\n\n")
            
            f.write("PART 1: Letter count validation\n")
            f.write(f"  Valid passwords: {valid_part1} out of {len(password_details)}\n")
            f.write(f"  Invalid passwords: {len(password_details) - valid_part1}\n\n")
            
            f.write("PART 2: Position validation\n")
            f.write(f"  Valid passwords: {valid_part2} out of {len(password_details)}\n")
            f.write(f"  Invalid passwords: {len(password_details) - valid_part2}\n\n")
            
            f.write("Sample of password validations (first 10):\n")
            f.write("-" * 50 + "\n")
            for i, detail in enumerate(password_details[:10]):
                f.write(f"Password {i+1}: '{detail['password']}'\n")
                f.write(f"  Policy: {detail['min']}-{detail['max']} {detail['letter']}\n")
                f.write(f"  Count: {detail['count']} occurrences\n")
                f.write(f"  Part 1 valid: {'Yes' if detail['valid_part1'] else 'No'}\n")
                f.write(f"  Part 2 valid: {'Yes' if detail['valid_part2'] else 'No'}\n")
                f.write("\n")
        
        print(f"✓ Challenge completed!")
        print(f"  Passwords processed: {len(password_details)}")
        print(f"  Part 1 valid: {valid_part1}")
        print(f"  Part 2 valid: {valid_part2}")
        print(f"  Results saved to: {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")

def challenge_5_bingo():
    print("\n" + "=" * 70)
    print("CHALLENGE 5: Giant Squid Bingo (AoC Day 4 Style)")
    print("=" * 70)
    
    input_file = Path("aoc_challenges/day4_bingo.txt")
    
    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        return
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read().strip().split('\n\n')

        numbers = list(map(int, content[0].split(',')))

        boards = []
        for board_str in content[1:]:
            board = []
            for line in board_str.strip().split('\n'):
                row = list(map(int, line.split()))
                board.append(row)
            boards.append(board)

        marked_boards = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]

        winning_board = -1
        winning_number = -1
        winning_turn = -1
        
        for turn, number in enumerate(numbers):
            # Mark the number on all boards
            for b in range(len(boards)):
                for i in range(5):
                    for j in range(5):
                        if boards[b][i][j] == number:
                            marked_boards[b][i][j] = True

            for b in range(len(boards)):
                # Check rows
                for i in range(5):
                    if all(marked_boards[b][i][j] for j in range(5)):
                        winning_board = b
                        winning_number = number
                        winning_turn = turn
                        break

                for j in range(5):
                    if all(marked_boards[b][i][j] for i in range(5)):
                        winning_board = b
                        winning_number = number
                        winning_turn = turn
                        break
                
                if winning_board != -1:
                    break
            
            if winning_board != -1:
                break

        if winning_board != -1:
            unmarked_sum = 0
            for i in range(5):
                for j in range(5):
                    if not marked_boards[winning_board][i][j]:
                        unmarked_sum += boards[winning_board][i][j]
            
            final_score = unmarked_sum * winning_number

        output_file = Path("aoc_challenges/day4_bingo_result.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("CHALLENGE 5: Giant Squid Bingo Results\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Input file: {input_file}\n")
            f.write(f"Numbers to draw: {len(numbers)}\n")
            f.write(f"Bingo boards: {len(boards)}\n\n")
            
            if winning_board != -1:
                f.write("WINNING BOARD FOUND!\n")
                f.write("-" * 40 + "\n")
                f.write(f"Winning board: #{winning_board + 1}\n")
                f.write(f"Winning number: {winning_number}\n")
                f.write(f"Turn: {winning_turn + 1}\n\n")
                
                f.write("Winning board (X = marked):\n")
                for i in range(5):
                    row_str = ""
                    for j in range(5):
                        num = boards[winning_board][i][j]
                        marked = marked_boards[winning_board][i][j]
                        if marked:
                            row_str += f"X({num:2}) "
                        else:
                            row_str += f"{num:2}   "
                    f.write(f"  {row_str}\n")
                
                f.write(f"\nUnmarked sum: {unmarked_sum}\n")
                f.write(f"Final score: {unmarked_sum} × {winning_number} = {final_score}\n")
            else:
                f.write("No winning board found!\n")
        
        if winning_board != -1:
            print(f"✓ Challenge completed!")
            print(f"  Boards: {len(boards)}")
            print(f"  Winning board: #{winning_board + 1}")
            print(f"  Winning number: {winning_number}")
            print(f"  Final score: {final_score}")
            print(f"  Results saved to: {output_file}")
        else:
            print(f"✗ No winning board found!")
        
    except Exception as e:
        print(f"Error: {e}")

def create_custom_challenge():
    print("\n" + "=" * 70)
    print("CREATE YOUR OWN ADVENT OF CODE CHALLENGE")
    print("=" * 70)
    
    print("""
Template for creating your own challenge:

1. Think of a problem that can be solved with file I/O and data processing.
2. Create an input file with test data.
3. Write code to read the input file, process the data, and produce output.
4. Make sure your challenge has clear instructions and expected output.

Example challenge ideas:
- Count frequency of words in a text file
- Find the longest word in each line
- Calculate statistics from a dataset
- Parse log files and extract specific information
- Solve simple mathematical problems from input data
""")
    
    print("\nExample: Creating a word frequency challenge...")
    
    sample_text = """
hello world this is a test
advent of code challenges are fun
python programming is great for file handling
the quick brown fox is quick"""
    
    input_file = Path("aoc_challenges/custom_word_freq.txt")
    with open(input_file, 'w') as f:
        f.write(sample_text)
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    word_counts = Counter()
    for line in lines:
        words = line.lower().split()
        word_counts.update(words)
    
    top_words = word_counts.most_common(10)
    
    output_file = Path("aoc_challenges/custom_word_freq_result.txt")
    with open(output_file, 'w') as f:
        f.write("CUSTOM CHALLENGE: Word Frequency\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total unique words: {len(word_counts)}\n")
        f.write(f"Total words: {sum(word_counts.values())}\n\n")
        f.write("Top 10 most frequent words:\n")
        for word, count in top_words:
            f.write(f"  {word}: {count} times\n")
    
    print(f"✓ Example challenge created!")
    print(f"  Input file: {input_file}")
    print(f"  Output file: {output_file}")
    print("\nNow you can create your own challenges following this template!")

def main_menu():
    create_challenge_input_files()
    
    while True:
        print("\n" + "=" * 70)
        print("ADVENT OF CODE STYLE CHALLENGES - TASK 3")
        print("University of Leeds - COMP1850 Programming")
        print("=" * 70)
        print("1. Challenge 1: Trebuchet Calibration (Day 1 style)")
        print("2. Challenge 2: Submarine Navigation (Day 2 style)")
        print("3. Challenge 3: Expense Report (AoC 2019 Day 1)")
        print("4. Challenge 4: Password Validation (AoC 2020 Day 2)")
        print("5. Challenge 5: Giant Squid Bingo (AoC 2021 Day 4)")
        print("6. Create your own custom challenge")
        print("7. View README and instructions")
        print("8. Exit")
        print("-" * 40)
        
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            challenge_1_calibration()
        elif choice == "2":
            challenge_2_navigation()
        elif choice == "3":
            challenge_3_expense_report()
        elif choice == "4":
            challenge_4_password_validation()
        elif choice == "5":
            challenge_5_bingo()
        elif choice == "6":
            create_custom_challenge()
        elif choice == "7":
            display_readme()
        elif choice == "8":
            print("\nThank you for exploring Advent of Code challenges!")
            print("Remember to check out the actual Advent of Code website:")
            print("https://adventofcode.com")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")
        
        input("\nPress Enter to continue...")

def display_readme():
    print("\n" + "=" * 70)
    print("ADVENT OF CODE - INFORMATION")
    print("=" * 70)
    
    print("""
Why is it useful for learning?
==============================
1. It focuses on file I/O - most puzzles involve reading input from a file
2. It teaches problem-solving skills
3. It covers various data structures and algorithms
4. It's language-agnostic - you can use any programming language
5. The difficulty ramps up gradually

To access the real Advent of Code:
==================================
Visit: https://adventofcode.com
You can complete puzzles from previous years by clicking "Events" at the top.
""")

def run_all_challenges():
    """
    Run all challenges sequentially (for testing/demo).
    """
    print("=" * 70)
    print("RUNNING ALL ADVENT OF CODE CHALLENGES")
    print("=" * 70)
    
    create_challenge_input_files()
    
    challenges = [
        ("Trebuchet Calibration", challenge_1_calibration),
        ("Submarine Navigation", challenge_2_navigation),
        ("Expense Report", challenge_3_expense_report),
        ("Password Validation", challenge_4_password_validation),
        ("Giant Squid Bingo", challenge_5_bingo),
    ]
    
    for name, challenge_func in challenges:
        print(f"\n{'='*60}")
        print(f"Running: {name}")
        print(f"{'='*60}")
        challenge_func()

if __name__ == "__main__":
    print("Welcome to Advent of Code Style Challenges!")
    print("Task 3: Extension Activity - COMP1850 Programming")
    print("University of Leeds - School of Computer Science\n")

    main_menu()
