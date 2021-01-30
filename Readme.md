# Closest Colors
A python script to compare a list of colors to a database of colors and store the closest color being searched for from the database in results.txt

# Instructions
1. Write the colors you want to search for in search.txt. Each color should be in hex code and each color should be on a new line. ',' or '.' are not needed
2. Write the database of colors you want to search from in pallete.txt. Each color should be in hex code and each color should be on a new line. ',' or '.' are not needed
3. Run main.py
4. The results will be stored in results.txt in serial order.

# Example Code

## search.txt
#ffffff
#000000
#aaaaaa

## pallete.txt
#fffffd
#fffff0
#fffff1
#fffffc
#000005
#000003
#00000d
#000001
#aaaaa2
#aaaaaa

## The results stored in search.txt:

#fffffd
#000001
#aaaaaa

## Explanation

1. The closest color for #ffffff in pallete.txt is #fffffd
1. The closest color for #000000 in pallete.txt is #000001
1. The closest color for #aaaaaa in pallete.txt is #aaaaaa

🤘 🚀 🤘   Hope this script helps you in your endeavours. 🤘 🚀 🤘
